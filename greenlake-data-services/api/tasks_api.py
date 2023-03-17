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


class TasksApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_task(self, id, **kwargs):  # noqa: E501
        """Returns details of a specific task  # noqa: E501

        Returns the task with the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_task(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The UUID of the object (required)
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_task_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_task_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_task_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns details of a specific task  # noqa: E501

        Returns the task with the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_task_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The UUID of the object (required)
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/api/v1/tasks/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Task',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_tasks(self, **kwargs):  # noqa: E501
        """Returns a list of tasks accessible by the user  # noqa: E501

        Returns a list of tasks that are visible to the user. The response can be paged by using the limit and offset query parameters and filtered, sorted and ordered by using the filter, sortby and orderby query parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_tasks(async=True)
        >>> result = thread.get()

        :param async bool
        :param int offset: The offset query parameter should be used in conjunction with limit for paging, e.g.: offset=30&&limit=10. The offset is the number of items from the beginning of the result set to the first item included in the response. 
        :param int limit: The limit query parameter should be used in conjunction with offset for paging, e.g.: offset=30&&limit=10. The limit is the maximum number of items to include in the response. 
        :param str filter: The expression to filter responses.
        :return: TaskList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_tasks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_tasks_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_tasks_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list of tasks accessible by the user  # noqa: E501

        Returns a list of tasks that are visible to the user. The response can be paged by using the limit and offset query parameters and filtered, sorted and ordered by using the filter, sortby and orderby query parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_tasks_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int offset: The offset query parameter should be used in conjunction with limit for paging, e.g.: offset=30&&limit=10. The offset is the number of items from the beginning of the result set to the first item included in the response. 
        :param int limit: The limit query parameter should be used in conjunction with offset for paging, e.g.: offset=30&&limit=10. The limit is the maximum number of items to include in the response. 
        :param str filter: The expression to filter responses.
        :return: TaskList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'filter']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_tasks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

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
            '/api/v1/tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)