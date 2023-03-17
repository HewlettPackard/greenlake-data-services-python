# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    OpenAPI spec version: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class NimbleFCConfigsList(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'items': 'list[NimbleFibreChannelConfigsWithSortKey]',
        'page_limit': 'int',
        'page_offset': 'int',
        'request_uri': 'str',
        'total': 'int'
    }

    attribute_map = {
        'items': 'items',
        'page_limit': 'pageLimit',
        'page_offset': 'pageOffset',
        'request_uri': 'requestUri',
        'total': 'total'
    }

    def __init__(self, items=None, page_limit=None, page_offset=None, request_uri=None, total=None):  # noqa: E501
        """NimbleFCConfigsList - a model defined in OpenAPI"""  # noqa: E501

        self._items = None
        self._page_limit = None
        self._page_offset = None
        self._request_uri = None
        self._total = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if page_limit is not None:
            self.page_limit = page_limit
        if page_offset is not None:
            self.page_offset = page_offset
        if request_uri is not None:
            self.request_uri = request_uri
        if total is not None:
            self.total = total

    @property
    def items(self):
        """Gets the items of this NimbleFCConfigsList.  # noqa: E501


        :return: The items of this NimbleFCConfigsList.  # noqa: E501
        :rtype: list[NimbleFibreChannelConfigsWithSortKey]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this NimbleFCConfigsList.


        :param items: The items of this NimbleFCConfigsList.  # noqa: E501
        :type: list[NimbleFibreChannelConfigsWithSortKey]
        """

        self._items = items

    @property
    def page_limit(self):
        """Gets the page_limit of this NimbleFCConfigsList.  # noqa: E501

        page limit  # noqa: E501

        :return: The page_limit of this NimbleFCConfigsList.  # noqa: E501
        :rtype: int
        """
        return self._page_limit

    @page_limit.setter
    def page_limit(self, page_limit):
        """Sets the page_limit of this NimbleFCConfigsList.

        page limit  # noqa: E501

        :param page_limit: The page_limit of this NimbleFCConfigsList.  # noqa: E501
        :type: int
        """

        self._page_limit = page_limit

    @property
    def page_offset(self):
        """Gets the page_offset of this NimbleFCConfigsList.  # noqa: E501

        page offset  # noqa: E501

        :return: The page_offset of this NimbleFCConfigsList.  # noqa: E501
        :rtype: int
        """
        return self._page_offset

    @page_offset.setter
    def page_offset(self, page_offset):
        """Sets the page_offset of this NimbleFCConfigsList.

        page offset  # noqa: E501

        :param page_offset: The page_offset of this NimbleFCConfigsList.  # noqa: E501
        :type: int
        """

        self._page_offset = page_offset

    @property
    def request_uri(self):
        """Gets the request_uri of this NimbleFCConfigsList.  # noqa: E501

        requestUri for  Fibre Channel Configs  # noqa: E501

        :return: The request_uri of this NimbleFCConfigsList.  # noqa: E501
        :rtype: str
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri):
        """Sets the request_uri of this NimbleFCConfigsList.

        requestUri for  Fibre Channel Configs  # noqa: E501

        :param request_uri: The request_uri of this NimbleFCConfigsList.  # noqa: E501
        :type: str
        """

        self._request_uri = request_uri

    @property
    def total(self):
        """Gets the total of this NimbleFCConfigsList.  # noqa: E501

        Total number of Fibre Channel Configs.  # noqa: E501

        :return: The total of this NimbleFCConfigsList.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this NimbleFCConfigsList.

        Total number of Fibre Channel Configs.  # noqa: E501

        :param total: The total of this NimbleFCConfigsList.  # noqa: E501
        :type: int
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NimbleFCConfigsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
