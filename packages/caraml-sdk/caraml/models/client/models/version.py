# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities

    The version of the OpenAPI document: 0.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictInt, StrictStr
from caraml.models.client.models.custom_predictor import CustomPredictor
from caraml.models.client.models.model_schema import ModelSchema
from caraml.models.client.models.version_endpoint import VersionEndpoint

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Version(BaseModel):
    """
    Version
    """  # noqa: E501

    id: Optional[StrictInt] = None
    model_id: Optional[StrictInt] = None
    mlflow_run_id: Optional[StrictStr] = None
    mlflow_url: Optional[StrictStr] = None
    artifact_uri: Optional[StrictStr] = None
    endpoints: Optional[List[VersionEndpoint]] = None
    properties: Optional[Union[str, Any]] = None
    labels: Optional[Dict[str, StrictStr]] = None
    custom_predictor: Optional[CustomPredictor] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    python_version: Optional[StrictStr] = None
    model_schema: Optional[ModelSchema] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "model_id",
        "mlflow_run_id",
        "mlflow_url",
        "artifact_uri",
        "endpoints",
        "properties",
        "labels",
        "custom_predictor",
        "created_at",
        "updated_at",
        "python_version",
        "model_schema",
    ]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Version from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in endpoints (list)
        _items = []
        if self.endpoints:
            for _item in self.endpoints:
                if _item:
                    _items.append(_item.to_dict())
            _dict["endpoints"] = _items
        # override the default output from pydantic by calling `to_dict()` of custom_predictor
        if self.custom_predictor:
            _dict["custom_predictor"] = self.custom_predictor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_schema
        if self.model_schema:
            _dict["model_schema"] = self.model_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Version from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "model_id": obj.get("model_id"),
                "mlflow_run_id": obj.get("mlflow_run_id"),
                "mlflow_url": obj.get("mlflow_url"),
                "artifact_uri": obj.get("artifact_uri"),
                "endpoints": [
                    VersionEndpoint.from_dict(_item) for _item in obj.get("endpoints")
                ]
                if obj.get("endpoints") is not None
                else None,
                "properties": obj.get("properties"),
                "labels": obj.get("labels"),
                "custom_predictor": CustomPredictor.from_dict(
                    obj.get("custom_predictor")
                )
                if obj.get("custom_predictor") is not None
                else None,
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "python_version": obj.get("python_version"),
                "model_schema": ModelSchema.from_dict(obj.get("model_schema"))
                if obj.get("model_schema") is not None
                else None,
            }
        )
        return _obj
