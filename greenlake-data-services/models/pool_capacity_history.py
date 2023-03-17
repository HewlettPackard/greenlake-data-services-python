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


class PoolCapacityHistory(object):
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
        'count': 'int',
        'request_uri': 'str',
        'series_data': 'list[NimblecapacitySeriesData]'
    }

    attribute_map = {
        'count': 'count',
        'request_uri': 'requestURI',
        'series_data': 'series_data'
    }

    def __init__(self, count=None, request_uri=None, series_data=None):  # noqa: E501
        """PoolCapacityHistory - a model defined in OpenAPI"""  # noqa: E501

        self._count = None
        self._request_uri = None
        self._series_data = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if request_uri is not None:
            self.request_uri = request_uri
        if series_data is not None:
            self.series_data = series_data

    @property
    def count(self):
        """Gets the count of this PoolCapacityHistory.  # noqa: E501

        count of series data  # noqa: E501

        :return: The count of this PoolCapacityHistory.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PoolCapacityHistory.

        count of series data  # noqa: E501

        :param count: The count of this PoolCapacityHistory.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def request_uri(self):
        """Gets the request_uri of this PoolCapacityHistory.  # noqa: E501

        requestUri for detailed storage object  # noqa: E501

        :return: The request_uri of this PoolCapacityHistory.  # noqa: E501
        :rtype: str
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri):
        """Sets the request_uri of this PoolCapacityHistory.

        requestUri for detailed storage object  # noqa: E501

        :param request_uri: The request_uri of this PoolCapacityHistory.  # noqa: E501
        :type: str
        """

        self._request_uri = request_uri

    @property
    def series_data(self):
        """Gets the series_data of this PoolCapacityHistory.  # noqa: E501


        :return: The series_data of this PoolCapacityHistory.  # noqa: E501
        :rtype: list[NimblecapacitySeriesData]
        """
        return self._series_data

    @series_data.setter
    def series_data(self, series_data):
        """Sets the series_data of this PoolCapacityHistory.


        :param series_data: The series_data of this PoolCapacityHistory.  # noqa: E501
        :type: list[NimblecapacitySeriesData]
        """

        self._series_data = series_data

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
        if not isinstance(other, PoolCapacityHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
