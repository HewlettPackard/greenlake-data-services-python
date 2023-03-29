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
from greenlake_data_services.model.primera_host_list import PrimeraHostList
from greenlake_data_services.model.primera_hosts import PrimeraHosts


class HostsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.device_type1_get_all_hosts_endpoint = _Endpoint(
            settings={
                'response_type': (PrimeraHostList,),
                'auth': [
                    'JWTAuth'
                ],
                'endpoint_path': '/api/v1/storage-systems/device-type1/{systemId}/hosts',
                'operation_id': 'device_type1_get_all_hosts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'system_id',
                    'limit',
                    'offset',
                    'filter',
                    'sort',
                    'select',
                ],
                'required': [
                    'system_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_minimum': 0,
                    },
                    ('offset',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'system_id':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'filter':
                        (str,),
                    'sort':
                        (str,),
                    'select':
                        (str,),
                },
                'attribute_map': {
                    'system_id': 'systemId',
                    'limit': 'limit',
                    'offset': 'offset',
                    'filter': 'filter',
                    'sort': 'sort',
                    'select': 'select',
                },
                'location_map': {
                    'system_id': 'path',
                    'limit': 'query',
                    'offset': 'query',
                    'filter': 'query',
                    'sort': 'query',
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
        self.device_type1_get_host_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (PrimeraHosts,),
                'auth': [
                    'JWTAuth'
                ],
                'endpoint_path': '/api/v1/storage-systems/device-type1/{systemId}/hosts/{hostId}',
                'operation_id': 'device_type1_get_host_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'system_id',
                    'host_id',
                    'select',
                ],
                'required': [
                    'system_id',
                    'host_id',
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
                    'host_id':
                        (str,),
                    'select':
                        (str,),
                },
                'attribute_map': {
                    'system_id': 'systemId',
                    'host_id': 'hostId',
                    'select': 'select',
                },
                'location_map': {
                    'system_id': 'path',
                    'host_id': 'path',
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

    def device_type1_get_all_hosts(
        self,
        system_id,
        **kwargs
    ):
        """Get details of Primera / Alletra 9K Hosts  # noqa: E501

        Get details of Primera / Alletra 9K Hosts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.device_type1_get_all_hosts(system_id, async_req=True)
        >>> result = thread.get()

        Args:
            system_id (str): systemId of the device-type1 storage system

        Keyword Args:
            limit (int): Number of items to return at a time. [optional]
            offset (int): The offset of the first item in the collection to return. [optional]
            filter (str): Lucene query to filter host by Key.. [optional]
            sort (str): oData query to sort host resource by Key.. [optional]
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
            PrimeraHostList
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
        return self.device_type1_get_all_hosts_endpoint.call_with_http_info(**kwargs)

    def device_type1_get_host_by_id(
        self,
        system_id,
        host_id,
        **kwargs
    ):
        """Get details of Primera / Alletra 9K Host identified by {HostId}  # noqa: E501

        Get details of Primera / Alletra 9K Host identified by {HostId}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.device_type1_get_host_by_id(system_id, host_id, async_req=True)
        >>> result = thread.get()

        Args:
            system_id (str): systemId of the device-type1 storage system
            host_id (str): ID of the primera Host Set. A 42 digit hexadecimal number.

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
            PrimeraHosts
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
        kwargs['host_id'] = \
            host_id
        return self.device_type1_get_host_by_id_endpoint.call_with_http_info(**kwargs)
