# Copyright 2020 The Merlin Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import warnings
from tests.models.utils import undeploy_all_version

import joblib
import numpy as np
import pytest
import xgboost as xgb
from models.model import ModelType, PyFuncModel, PyFuncV3Model
from models.pyfunc import ModelInput, ModelOutput, Values
from models.resource_request import ResourceRequest
from sklearn.datasets import load_iris

import models as merlin

warnings.filterwarnings("ignore")

request_json = {"instances": [[2.8, 1.0, 6.8, 0.4], [3.1, 1.4, 4.5, 1.6]]}

XGB_PATH = os.path.join("test/pyfunc/", "model_1.bst")
SKLEARN_PATH = os.path.join("test/pyfunc/", "model_2.joblib")


class EnsembleModel(PyFuncModel):
    def initialize(self, artifacts):
        self._model_1 = xgb.Booster(model_file=artifacts["xgb_model"])
        self._model_2 = joblib.load(artifacts["sklearn_model"])

    def infer(self, model_input):
        inputs = np.array(model_input["instances"])
        dmatrix = xgb.DMatrix(model_input["instances"])
        result_1 = self._model_1.predict(dmatrix)
        result_2 = self._model_2.predict_proba(inputs)
        return {"predictions": ((result_1 + result_2) / 2).tolist()}


class EnvVarModel(PyFuncModel):
    def initialize(self, artifacts):
        self.env_var = {}
        self.env_var["workers"] = os.environ.get("WORKERS")
        self.env_var["env_var_1"] = os.environ.get("ENV_VAR_1")
        self.env_var["env_var_2"] = os.environ.get("ENV_VAR_2")

    def infer(self, model_input):
        return self.env_var


class ModelObservabilityModel(PyFuncV3Model):
    def initialize(self, artifacts):
        self._feature_names = [
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
        ]
        self._target_names = ["setosa", "versicolor", "virginica"]
        self._model = xgb.Booster(model_file=artifacts["xgb_model"])

    def preprocess(self, request: dict, **kwargs) -> ModelInput:
        features_data = request["instances"]
        return ModelInput(
            prediction_ids=["prediction_1", "prediction_2"],
            features=Values(columns=self._feature_names, data=features_data),
        )

    def infer(self, model_input: ModelInput) -> ModelOutput:
        dmatrix = xgb.DMatrix(model_input.features.data)
        outputs = self._model.predict(dmatrix).tolist()
        return ModelOutput(
            prediction_ids=model_input.prediction_ids,
            predictions=Values(columns=self._target_names, data=outputs),
        )

    def postprocess(self, model_output: ModelOutput, request: dict) -> dict:
        return {"predictions": model_output.predictions.data}


def train_xgboost_model(X, y):
    model_1_dir = "test/pyfunc/"
    BST_FILE = "model_1.bst"
    dtrain = xgb.DMatrix(X, label=y)
    param = {
        "max_depth": 6,
        "eta": 0.1,
        "silent": 1,
        "nthread": 4,
        "num_class": 3,
        "objective": "multi:softprob",
    }
    xgb_model = xgb.train(params=param, dtrain=dtrain)
    model_1_path = os.path.join(model_1_dir, BST_FILE)
    xgb_model.save_model(model_1_path)
    return model_1_path


def train_sklearn_model(X, y):
    model_2_dir = "test/pyfunc/"
    MODEL_FILE = "model_2.joblib"
    model_2_path = os.path.join(model_2_dir, MODEL_FILE)

    clf = svm.SVC(gamma="scale", probability=True)
    clf.fit(X, y)
    joblib.dump(clf, model_2_path)
    return model_2_path


@pytest.mark.pyfunc
@pytest.mark.integration
@pytest.mark.dependency()
def test_pyfunc(integration_test_url, project_name, use_google_oauth, requests):
    merlin.set_url(integration_test_url, use_google_oauth=use_google_oauth)
    merlin.set_project(project_name)
    merlin.set_model("pyfunc-sample", ModelType.PYFUNC)

    undeploy_all_version()
    with merlin.new_model_version() as v:
        iris = load_iris()
        y = iris["target"]
        X = iris["data"]
        xgb_path = train_xgboost_model(X, y)
        sklearn_path = train_sklearn_model(X, y)
        v.log_pyfunc_model(
            model_instance=EnsembleModel(),
            conda_env="test/pyfunc/env.yaml",
            code_dir=["test"],
            artifacts={"xgb_model": xgb_path, "sklearn_model": sklearn_path},
        )

    endpoint = merlin.deploy(v)

    resp = requests.post(f"{endpoint.url}", json=request_json)

    assert resp.status_code == 200
    assert resp.json() is not None
    assert len(resp.json()["predictions"]) == len(request_json["instances"])

    merlin.undeploy(v)


@pytest.mark.pyfunc
@pytest.mark.integration
@pytest.mark.dependency()
def test_pyfunc_image_builder_resource_request(
    integration_test_url, project_name, use_google_oauth, requests
):
    merlin.set_url(integration_test_url, use_google_oauth=use_google_oauth)
    merlin.set_project(project_name)
    merlin.set_model("pyfunc-image-builder", ModelType.PYFUNC)

    undeploy_all_version()
    with merlin.new_model_version() as v:
        iris = load_iris()
        y = iris["target"]
        X = iris["data"]
        xgb_path = train_xgboost_model(X, y)
        sklearn_path = train_sklearn_model(X, y)
        v.log_pyfunc_model(
            model_instance=EnsembleModel(),
            conda_env="test/pyfunc/env.yaml",
            code_dir=["test"],
            artifacts={"xgb_model": xgb_path, "sklearn_model": sklearn_path},
        )

    image_builder_resource_request = ResourceRequest(
        cpu_request="2", memory_request="4Gi"
    )
    endpoint = merlin.deploy(
        v, image_builder_resource_request=image_builder_resource_request
    )

    resp = requests.post(f"{endpoint.url}", json=request_json)

    assert resp.status_code == 200
    assert resp.json() is not None
    assert len(resp.json()["predictions"]) == len(request_json["instances"])

    merlin.undeploy(v)


@pytest.mark.pyfunc
@pytest.mark.integration
def test_pyfunc_env_vars(
    integration_test_url, project_name, use_google_oauth, requests
):
    merlin.set_url(integration_test_url, use_google_oauth=use_google_oauth)
    merlin.set_project(project_name)
    merlin.set_model("pyfunc-env-vars-sample", ModelType.PYFUNC)

    undeploy_all_version()
    with merlin.new_model_version() as v:
        v.log_pyfunc_model(
            model_instance=EnvVarModel(),
            conda_env="test/pyfunc/env.yaml",
            code_dir=["test"],
            artifacts={},
        )

    env_vars = {"WORKERS": "8", "ENV_VAR_1": "1", "ENV_VAR_2": "2"}
    endpoint = merlin.deploy(v, env_vars=env_vars)
    resp = requests.post(f"{endpoint.url}", json=request_json)

    assert resp.status_code == 200
    assert resp.json() is not None
    assert resp.json()["workers"] == "8"
    assert resp.json()["env_var_1"] == "1"
    assert resp.json()["env_var_2"] == "2"
    assert env_vars.items() <= endpoint.env_vars.items()

    merlin.undeploy(v)


@pytest.mark.pyfunc
@pytest.mark.integration
@pytest.mark.dependency()
def test_pyfunc_model_observability(
    integration_test_url, project_name, use_google_oauth, requests
):
    merlin.set_url(integration_test_url, use_google_oauth=use_google_oauth)
    merlin.set_project(project_name)
    merlin.set_model("pyfunc-mlobs", ModelType.PYFUNC_V3)

    undeploy_all_version()
    with merlin.new_model_version() as v:
        iris = load_iris()
        y = iris["target"]
        X = iris["data"]
        xgb_path = train_xgboost_model(X, y)

        v.log_pyfunc_model(
            model_instance=ModelObservabilityModel(),
            conda_env="test/pyfunc/env.yaml",
            code_dir=["test"],
            artifacts={"xgb_model": xgb_path},
        )

    endpoint = merlin.deploy(v, enable_model_observability=True)

    resp = requests.post(f"{endpoint.url}", json=request_json)

    assert resp.status_code == 200
    assert resp.json() is not None
    assert len(resp.json()["predictions"]) == len(request_json["instances"])

    merlin.undeploy(v)


# This implementation of PyFuncModel uses the old infer method (no keyword arguments).
# The keywords arguments for infer() method introduced in Merlin 0.5.2.
class OldInferModel(PyFuncModel):
    def initialize(self, artifacts):
        pass

    def infer(self, model_input):
        return model_input


@pytest.mark.pyfunc
@pytest.mark.integration
def test_pyfunc_old_infer(
    integration_test_url, project_name, use_google_oauth, requests
):
    merlin.set_url(integration_test_url, use_google_oauth=use_google_oauth)
    merlin.set_project(project_name)
    merlin.set_model("pyfunc-old-infer-sample", ModelType.PYFUNC)

    undeploy_all_version()
    with merlin.new_model_version() as v:
        v.log_pyfunc_model(
            model_instance=OldInferModel(),
            conda_env="test/pyfunc/env.yaml",
            code_dir=["test"],
            artifacts={},
        )

    endpoint = merlin.deploy(v)
    resp = requests.post(f"{endpoint.url}", json=request_json)

    assert resp.status_code == 200
    assert resp.json()["instances"] == request_json["instances"]

    merlin.undeploy(v)
