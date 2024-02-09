# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities  # noqa: E501

    OpenAPI spec version: 0.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from models.client.api_client import ApiClient


class EndpointApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def models_model_id_versions_version_id_endpoint_endpoint_id_containers_get(self, model_id, version_id, endpoint_id, **kwargs):  # noqa: E501
        """Get all container belong to a version endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_versions_version_id_endpoint_endpoint_id_containers_get(model_id, version_id, endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param int version_id: (required)
        :param str endpoint_id: (required)
        :return: Container
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.models_model_id_versions_version_id_endpoint_endpoint_id_containers_get_with_http_info(model_id, version_id, endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.models_model_id_versions_version_id_endpoint_endpoint_id_containers_get_with_http_info(model_id, version_id, endpoint_id, **kwargs)  # noqa: E501
            return data

    def models_model_id_versions_version_id_endpoint_endpoint_id_containers_get_with_http_info(self, model_id, version_id, endpoint_id, **kwargs):  # noqa: E501
        """Get all container belong to a version endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_versions_version_id_endpoint_endpoint_id_containers_get_with_http_info(model_id, version_id, endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param int version_id: (required)
        :param str endpoint_id: (required)
        :return: Container
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_id', 'version_id', 'endpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method models_model_id_versions_version_id_endpoint_endpoint_id_containers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params or
                params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `models_model_id_versions_version_id_endpoint_endpoint_id_containers_get`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `models_model_id_versions_version_id_endpoint_endpoint_id_containers_get`")  # noqa: E501
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `models_model_id_versions_version_id_endpoint_endpoint_id_containers_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in params:
            path_params['model_id'] = params['model_id']  # noqa: E501
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']  # noqa: E501
        if 'endpoint_id' in params:
            path_params['endpoint_id'] = params['endpoint_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/models/{model_id}/versions/{version_id}/endpoint/{endpoint_id}/containers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Container',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def models_model_id_versions_version_id_endpoint_endpoint_id_delete(self, model_id, version_id, endpoint_id, **kwargs):  # noqa: E501
        """Undeploy the specified model version deployment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_versions_version_id_endpoint_endpoint_id_delete(model_id, version_id, endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param int version_id: (required)
        :param str endpoint_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.models_model_id_versions_version_id_endpoint_endpoint_id_delete_with_http_info(model_id, version_id, endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.models_model_id_versions_version_id_endpoint_endpoint_id_delete_with_http_info(model_id, version_id, endpoint_id, **kwargs)  # noqa: E501
            return data

    def models_model_id_versions_version_id_endpoint_endpoint_id_delete_with_http_info(self, model_id, version_id, endpoint_id, **kwargs):  # noqa: E501
        """Undeploy the specified model version deployment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_versions_version_id_endpoint_endpoint_id_delete_with_http_info(model_id, version_id, endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param int version_id: (required)
        :param str endpoint_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_id', 'version_id', 'endpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method models_model_id_versions_version_id_endpoint_endpoint_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params or
                params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `models_model_id_versions_version_id_endpoint_endpoint_id_delete`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `models_model_id_versions_version_id_endpoint_endpoint_id_delete`")  # noqa: E501
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `models_model_id_versions_version_id_endpoint_endpoint_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in params:
            path_params['model_id'] = params['model_id']  # noqa: E501
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']  # noqa: E501
        if 'endpoint_id' in params:
            path_params['endpoint_id'] = params['endpoint_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/models/{model_id}/versions/{version_id}/endpoint/{endpoint_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def models_model_id_versions_version_id_endpoint_endpoint_id_get(self, model_id, version_id, endpoint_id, **kwargs):  # noqa: E501
        """Get version endpoint resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_versions_version_id_endpoint_endpoint_id_get(model_id, version_id, endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param int version_id: (required)
        :param str endpoint_id: (required)
        :return: VersionEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.models_model_id_versions_version_id_endpoint_endpoint_id_get_with_http_info(model_id, version_id, endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.models_model_id_versions_version_id_endpoint_endpoint_id_get_with_http_info(model_id, version_id, endpoint_id, **kwargs)  # noqa: E501
            return data

    def models_model_id_versions_version_id_endpoint_endpoint_id_get_with_http_info(self, model_id, version_id, endpoint_id, **kwargs):  # noqa: E501
        """Get version endpoint resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_versions_version_id_endpoint_endpoint_id_get_with_http_info(model_id, version_id, endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param int version_id: (required)
        :param str endpoint_id: (required)
        :return: VersionEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_id', 'version_id', 'endpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method models_model_id_versions_version_id_endpoint_endpoint_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params or
                params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `models_model_id_versions_version_id_endpoint_endpoint_id_get`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `models_model_id_versions_version_id_endpoint_endpoint_id_get`")  # noqa: E501
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `models_model_id_versions_version_id_endpoint_endpoint_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in params:
            path_params['model_id'] = params['model_id']  # noqa: E501
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']  # noqa: E501
        if 'endpoint_id' in params:
            path_params['endpoint_id'] = params['endpoint_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/models/{model_id}/versions/{version_id}/endpoint/{endpoint_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VersionEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def models_model_id_versions_version_id_endpoint_endpoint_id_put(self, model_id, version_id, endpoint_id, **kwargs):  # noqa: E501
        """Modify version endpoint, this API will redeploy the associated deployment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_versions_version_id_endpoint_endpoint_id_put(model_id, version_id, endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param int version_id: (required)
        :param str endpoint_id: (required)
        :param VersionEndpoint body:
        :return: VersionEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.models_model_id_versions_version_id_endpoint_endpoint_id_put_with_http_info(model_id, version_id, endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.models_model_id_versions_version_id_endpoint_endpoint_id_put_with_http_info(model_id, version_id, endpoint_id, **kwargs)  # noqa: E501
            return data

    def models_model_id_versions_version_id_endpoint_endpoint_id_put_with_http_info(self, model_id, version_id, endpoint_id, **kwargs):  # noqa: E501
        """Modify version endpoint, this API will redeploy the associated deployment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_versions_version_id_endpoint_endpoint_id_put_with_http_info(model_id, version_id, endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param int version_id: (required)
        :param str endpoint_id: (required)
        :param VersionEndpoint body:
        :return: VersionEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_id', 'version_id', 'endpoint_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method models_model_id_versions_version_id_endpoint_endpoint_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params or
                params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `models_model_id_versions_version_id_endpoint_endpoint_id_put`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `models_model_id_versions_version_id_endpoint_endpoint_id_put`")  # noqa: E501
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `models_model_id_versions_version_id_endpoint_endpoint_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in params:
            path_params['model_id'] = params['model_id']  # noqa: E501
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']  # noqa: E501
        if 'endpoint_id' in params:
            path_params['endpoint_id'] = params['endpoint_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/models/{model_id}/versions/{version_id}/endpoint/{endpoint_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VersionEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def models_model_id_versions_version_id_endpoint_get(self, model_id, version_id, **kwargs):  # noqa: E501
        """List all endpoint of a model version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_versions_version_id_endpoint_get(model_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param int version_id: (required)
        :return: list[VersionEndpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.models_model_id_versions_version_id_endpoint_get_with_http_info(model_id, version_id, **kwargs)  # noqa: E501
        else:
            (data) = self.models_model_id_versions_version_id_endpoint_get_with_http_info(model_id, version_id, **kwargs)  # noqa: E501
            return data

    def models_model_id_versions_version_id_endpoint_get_with_http_info(self, model_id, version_id, **kwargs):  # noqa: E501
        """List all endpoint of a model version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_versions_version_id_endpoint_get_with_http_info(model_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param int version_id: (required)
        :return: list[VersionEndpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_id', 'version_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method models_model_id_versions_version_id_endpoint_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params or
                params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `models_model_id_versions_version_id_endpoint_get`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `models_model_id_versions_version_id_endpoint_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in params:
            path_params['model_id'] = params['model_id']  # noqa: E501
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/models/{model_id}/versions/{version_id}/endpoint', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[VersionEndpoint]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def models_model_id_versions_version_id_endpoint_post(self, model_id, version_id, **kwargs):  # noqa: E501
        """Deploy specific version of the models  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_versions_version_id_endpoint_post(model_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param int version_id: (required)
        :param VersionEndpoint body:
        :return: VersionEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.models_model_id_versions_version_id_endpoint_post_with_http_info(model_id, version_id, **kwargs)  # noqa: E501
        else:
            (data) = self.models_model_id_versions_version_id_endpoint_post_with_http_info(model_id, version_id, **kwargs)  # noqa: E501
            return data

    def models_model_id_versions_version_id_endpoint_post_with_http_info(self, model_id, version_id, **kwargs):  # noqa: E501
        """Deploy specific version of the models  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_versions_version_id_endpoint_post_with_http_info(model_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param int version_id: (required)
        :param VersionEndpoint body:
        :return: VersionEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_id', 'version_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method models_model_id_versions_version_id_endpoint_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params or
                params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `models_model_id_versions_version_id_endpoint_post`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `models_model_id_versions_version_id_endpoint_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in params:
            path_params['model_id'] = params['model_id']  # noqa: E501
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/models/{model_id}/versions/{version_id}/endpoint', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VersionEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
