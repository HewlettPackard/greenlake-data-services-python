"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from greenlake_data_services.api_client import ApiClient, Endpoint as _Endpoint
from greenlake_data_services.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.nimble_create_folder_input import NimbleCreateFolderInput
from greenlake_data_services.model.nimble_edit_folder_input import NimbleEditFolderInput
from greenlake_data_services.model.nimble_folder_details_with_request_uri import NimbleFolderDetailsWithRequestUri
from greenlake_data_services.model.task_response import TaskResponse


class FoldersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.device_type2_folder_create_endpoint = _Endpoint(
            settings={
                'response_type': (TaskResponse,),
                'auth': [
                    'JWTAuth'
                ],
                'endpoint_path': '/api/v1/storage-systems/device-type2/{systemId}/folders',
                'operation_id': 'device_type2_folder_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'system_id',
                    'nimble_create_folder_input',
                ],
                'required': [
                    'system_id',
                    'nimble_create_folder_input',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'system_id':
                        (str,),
                    'nimble_create_folder_input':
                        (NimbleCreateFolderInput,),
                },
                'attribute_map': {
                    'system_id': 'systemId',
                },
                'location_map': {
                    'system_id': 'path',
                    'nimble_create_folder_input': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.device_type2_folder_edit_endpoint = _Endpoint(
            settings={
                'response_type': (TaskResponse,),
                'auth': [
                    'JWTAuth'
                ],
                'endpoint_path': '/api/v1/storage-systems/device-type2/{systemId}/folders/{folderId}',
                'operation_id': 'device_type2_folder_edit',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'system_id',
                    'folder_id',
                    'nimble_edit_folder_input',
                ],
                'required': [
                    'system_id',
                    'folder_id',
                    'nimble_edit_folder_input',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'system_id':
                        (str,),
                    'folder_id':
                        (str,),
                    'nimble_edit_folder_input':
                        (NimbleEditFolderInput,),
                },
                'attribute_map': {
                    'system_id': 'systemId',
                    'folder_id': 'folderId',
                },
                'location_map': {
                    'system_id': 'path',
                    'folder_id': 'path',
                    'nimble_edit_folder_input': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.device_type2_get_folder_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (NimbleFolderDetailsWithRequestUri,),
                'auth': [
                    'JWTAuth'
                ],
                'endpoint_path': '/api/v1/storage-systems/device-type2/{systemId}/folders/{folderId}',
                'operation_id': 'device_type2_get_folder_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'system_id',
                    'folder_id',
                    'select',
                ],
                'required': [
                    'system_id',
                    'folder_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'system_id':
                        (str,),
                    'folder_id':
                        (str,),
                    'select':
                        (str,),
                },
                'attribute_map': {
                    'system_id': 'systemId',
                    'folder_id': 'folderId',
                    'select': 'select',
                },
                'location_map': {
                    'system_id': 'path',
                    'folder_id': 'path',
                    'select': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.device_type2_remove_folder_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (TaskResponse,),
                'auth': [
                    'JWTAuth'
                ],
                'endpoint_path': '/api/v1/storage-systems/device-type2/{systemId}/folders/{folderId}',
                'operation_id': 'device_type2_remove_folder_by_id',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'system_id',
                    'folder_id',
                ],
                'required': [
                    'system_id',
                    'folder_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'system_id':
                        (str,),
                    'folder_id':
                        (str,),
                },
                'attribute_map': {
                    'system_id': 'systemId',
                    'folder_id': 'folderId',
                },
                'location_map': {
                    'system_id': 'path',
                    'folder_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def device_type2_folder_create(
        self,
        system_id,
        nimble_create_folder_input,
        **kwargs
    ):
        """Create Nimble / Alletra 6K folder in system identified by {systemId}  # noqa: E501

        Create Nimble / Alletra 6K folder in system identified by {systemId}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.device_type2_folder_create(system_id, nimble_create_folder_input, async_req=True)
        >>> result = thread.get()

        Args:
            system_id (str): ID of the storage system
            nimble_create_folder_input (NimbleCreateFolderInput):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            TaskResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['system_id'] = \
            system_id
        kwargs['nimble_create_folder_input'] = \
            nimble_create_folder_input
        return self.device_type2_folder_create_endpoint.call_with_http_info(**kwargs)

    def device_type2_folder_edit(
        self,
        system_id,
        folder_id,
        nimble_edit_folder_input,
        **kwargs
    ):
        """Edit details of Nimble / Alletra 6K folder identified by {folderId}  # noqa: E501

        Edit details of Nimble / Alletra 6K folder identified by {folderId}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.device_type2_folder_edit(system_id, folder_id, nimble_edit_folder_input, async_req=True)
        >>> result = thread.get()

        Args:
            system_id (str): ID of the storage system
            folder_id (str): ID of the folder. A 42 digit hexadecimal number.
            nimble_edit_folder_input (NimbleEditFolderInput):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            TaskResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['system_id'] = \
            system_id
        kwargs['folder_id'] = \
            folder_id
        kwargs['nimble_edit_folder_input'] = \
            nimble_edit_folder_input
        return self.device_type2_folder_edit_endpoint.call_with_http_info(**kwargs)

    def device_type2_get_folder_by_id(
        self,
        system_id,
        folder_id,
        **kwargs
    ):
        """Get details of Nimble / Alletra 6K Folders identified by {folderId}  # noqa: E501

        Get details of Nimble / Alletra 6K Folders identified by {folderId}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.device_type2_get_folder_by_id(system_id, folder_id, async_req=True)
        >>> result = thread.get()

        Args:
            system_id (str): ID of the storage system
            folder_id (str): ID of the folder. A 42 digit hexadecimal number.

        Keyword Args:
            select (str): Query to select only the required parameters, separated by . if nested. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            NimbleFolderDetailsWithRequestUri
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['system_id'] = \
            system_id
        kwargs['folder_id'] = \
            folder_id
        return self.device_type2_get_folder_by_id_endpoint.call_with_http_info(**kwargs)

    def device_type2_remove_folder_by_id(
        self,
        system_id,
        folder_id,
        **kwargs
    ):
        """Remove Nimble / Alletra 6K folder identified by {folderId}  # noqa: E501

        Remove Nimble / Alletra 6K folder identified by {folderId}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.device_type2_remove_folder_by_id(system_id, folder_id, async_req=True)
        >>> result = thread.get()

        Args:
            system_id (str): ID of the storage system
            folder_id (str): ID of the folder. A 42 digit hexadecimal number.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            TaskResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['system_id'] = \
            system_id
        kwargs['folder_id'] = \
            folder_id
        return self.device_type2_remove_folder_by_id_endpoint.call_with_http_info(**kwargs)

