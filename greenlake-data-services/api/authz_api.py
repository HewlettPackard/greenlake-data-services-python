# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    OpenAPI spec version: 1.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from greenlake-data-services.api_client import ApiClient


class AuthzApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_access_controls(self, **kwargs):  # noqa: E501
        """Get User Accessible Resources  # noqa: E501

        Retun a list of user permissions.  The returned list of permissions will be based upon the supplied filter.  If no filter was supplied, all user permissions will be returned. It is also possible to request all resource type with certain permission type (ex. ALL.read)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_access_controls(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] permission: List of permissions, each of which, has the form \"resource type.permission\" (ex. volume.read,volume.write). The word \"ANY\" can be used as a wild card for the resource type (ex. ANY.read). Omitting the permission parameters is equivalent to asking for all user permissions.
        :return: AccessControlsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_access_controls_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_access_controls_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_access_controls_with_http_info(self, **kwargs):  # noqa: E501
        """Get User Accessible Resources  # noqa: E501

        Retun a list of user permissions.  The returned list of permissions will be based upon the supplied filter.  If no filter was supplied, all user permissions will be returned. It is also possible to request all resource type with certain permission type (ex. ALL.read)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_access_controls_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] permission: List of permissions, each of which, has the form \"resource type.permission\" (ex. volume.read,volume.write). The word \"ANY\" can be used as a wild card for the resource type (ex. ANY.read). Omitting the permission parameters is equivalent to asking for all user permissions.
        :return: AccessControlsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['permission']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_access_controls" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'permission' in params:
            query_params.append(('permission', params['permission']))  # noqa: E501
            collection_formats['permission'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWTAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/access-controls', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessControlsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_resource_types(self, **kwargs):  # noqa: E501
        """Get resource types with read permissions  # noqa: E501

        Return resource types on which the user has a read permission.  The returned list will be based upon the supplied filter.  If no filter was provided, all resource types for which the user has a read permission on will be returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_resource_types(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ResourceTypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_resource_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_resource_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_resource_types_with_http_info(self, **kwargs):  # noqa: E501
        """Get resource types with read permissions  # noqa: E501

        Return resource types on which the user has a read permission.  The returned list will be based upon the supplied filter.  If no filter was provided, all resource types for which the user has a read permission on will be returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_resource_types_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ResourceTypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource_types" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWTAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/resource-types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceTypesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
