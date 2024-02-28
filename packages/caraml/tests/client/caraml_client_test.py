
from client.caraml_client import CaraMLClient

import pytest


@pytest.fixture
def mock_url():
    return "http://console.ai"

CARAML_METHODS = {
    'get_project': "mlp",
    'list_projects': "mlp",
    'set_project': "mlp",
    'deploy': "models",
    'get_default_environment': "models",
    'get_environment': "models",
    'get_model': "models",
    'get_or_create_model': "models",
    'get_or_create_project': "models",
    'list_environment': "models",
    'list_project': "models",
    'new_model_version': "models",
    'standard_transformer_simulate': "models",
    'undeploy': "models", 
    'create_ensembler': "routers",
    'create_router': "routers",
    'create_router_version': "routers",
    'delete_ensembler': "routers",
    'delete_router': "routers",
    'delete_router_version': "routers",
    'deploy_router': "routers",
    'deploy_router_version': "routers",
    'get_ensembler': "routers",
    'get_ensembling_job': "routers",
    'get_project_by_name': "routers",
    'get_router': "routers",
    'get_router_events': "routers",
    'get_router_version': "routers",
    'list_ensemblers': "routers",
    'list_ensembling_jobs': "routers",
    'list_router_versions': "routers",
    'list_router_versions_with_filter': "routers",
    'list_routers': "routers",
    'submit_ensembling_job': "routers",
    'terminate_ensembling_job': "routers",
    'undeploy_router': "routers",
    'update_ensembler': "routers",
    'update_router': "routers"
}

@pytest.mark.unit
def test_caraml_client(mock_url):

    client = CaraMLClient(caraml_url=mock_url, use_google_oauth=False)

    client_methods = [method_name for method_name in dir(client)
                  if callable(getattr(client, method_name)) and not method_name.startswith('_')]
    
    assert len(client_methods) == len(CARAML_METHODS)
    lacks = CARAML_METHODS.keys() - set(client_methods)
    extra = set(client_methods) - CARAML_METHODS.keys()

    message = f"Actual list lacks methods {lacks} " if lacks else ''
    message += f"Extra methods in client {extra} not expected" if extra else ''
    assert not message