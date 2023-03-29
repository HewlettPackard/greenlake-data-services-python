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
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.issue_details import IssueDetails
from greenlake_data_services.model.issues_list import IssuesList


class IssuesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_issue_endpoint = _Endpoint(
            settings={
                'response_type': (IssueDetails,),
                'auth': [
                    'JWTAuth'
                ],
                'endpoint_path': '/api/v1/issues/{id}',
                'operation_id': 'get_issue',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'select',
                ],
                'required': [
                    'id',
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
                    'id':
                        (str,),
                    'select':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'select': 'select',
                },
                'location_map': {
                    'id': 'path',
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
        self.list_issues_endpoint = _Endpoint(
            settings={
                'response_type': (IssuesList,),
                'auth': [
                    'JWTAuth'
                ],
                'endpoint_path': '/api/v1/issues',
                'operation_id': 'list_issues',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'offset',
                    'limit',
                    'filter',
                    'sort',
                    'select',
                ],
                'required': [],
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
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                    'filter':
                        (str,),
                    'sort':
                        (str,),
                    'select':
                        (str,),
                },
                'attribute_map': {
                    'offset': 'offset',
                    'limit': 'limit',
                    'filter': 'filter',
                    'sort': 'sort',
                    'select': 'select',
                },
                'location_map': {
                    'offset': 'query',
                    'limit': 'query',
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

    def get_issue(
        self,
        id,
        **kwargs
    ):
        """Returns the active issue with the given Id  # noqa: E501

        Returns the active issue (state=\"CREATED\") associated with the account (retrieved from the request headers) and with given Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_issue(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): The UUID of the issue

        Keyword Args:
            select (str): The select query parameter is used to limit the properties returned with a resource or collection-level GET. Multiple properties can be listed to be returned. The server must only return the set of properties requested by the client. The property “select” is the name of the select query parameter; its value is the list of properties to return separated by commas. . [optional]
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
            IssueDetails
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
        kwargs['id'] = \
            id
        return self.get_issue_endpoint.call_with_http_info(**kwargs)

    def list_issues(
        self,
        **kwargs
    ):
        """Returns a list of active issues associated with the account, scoped by the user's permissions  # noqa: E501

        Returns the active (state=\"CREATED\") issues for the account, which are associated with the resource-types for which the user has access. The user should also have the permission to view issues. Eg: if there are issues associated with 50 resources (of different resource-types) for a customer (obtained from the request header), and the user (obtained from the request headers), who has correct permissions to view the issues but has acceess to only 20 of those resources (ie access to their resource types), this API will return only the issues associated with those 20 resources. The grouped issues are places next to each other. The client will have to process them for any desired grouping   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_issues(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            offset (int): The number of items to skip before starting to collect the result set. [optional]
            limit (int): The numbers of items to return. [optional]
            filter (str): The filter query parameter is used to filter the set of resources returned in the response. The returned set of resources must match the criteria in the filter query parameter A comparision compares a property name to a literal. The comparisons supported are the following: “eq” : Is a property equal to value. Valid for number, boolean and string properties. “gt” : Is a property greater than a value. Valid for number or string timestamp properties. “lt” : Is a property less than a value. Valid for number or string timestamp properties “in” : Is a value in a property (that is an array of strings) Syntax:  “eq” : filter=<property> eq <value> {host:port}/api/v1/issues?filter=<property> eq <value> “gt” : filter=<property> gt <value> {host:port}/api/v1/issues?filter=<property> gt <value> “lt” : filter=<property> lt <value> {host:port}/api/v1/issues?filter=<property> lt <value> “in” : filter=<property> in <value> {host:port}/api/v1/issues?filter=<property> in <value> * Can use and to add more filter inputs {host:port}/api/v1/issues?filter=<property1> eq <value1> and <property2> lt <value2>  * To filter multiple values on one property e.g. filter=severity in ('CRITICAL','WARNING') {host:port}/api/v1/issues?filter=severity%20in%20CRITICAL%2CWARNING Examples: GET /api/v1/issues?filter=issueType eq 'ISSUE' GET /api/v1/issues?filter=issueType eq 'ISSUE' and state eq 'CREATED' GET /api/v1/issues?filter=relatedObjectType in ('NIMBLE-VOLUME') Filters are supported on following attributes: issueType, severity, category, state, relatedObject (relatedObject.resourceUri), relatedObjectType (relatedObject.type), relatedObjectOwner (relatedObjectOwner.resourceUri), relatedObjectOwnerType (relatedObjectOwner.type), ruleId, createdAt . [optional]
            sort (str): resource property to sort, with an order appended Order may only be either “asc” (ascending) or “desc” (descending) . [optional]
            select (str): The select query parameter is used to limit the properties returned with a resource or collection-level GET. Multiple properties can be listed to be returned. The server must only return the set of properties requested by the client. The property “select” is the name of the select query parameter; its value is the list of properties to return separated by commas. . [optional]
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
            IssuesList
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
        return self.list_issues_endpoint.call_with_http_info(**kwargs)
