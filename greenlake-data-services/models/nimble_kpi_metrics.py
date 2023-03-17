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


class NimbleKpiMetrics(object):
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
        'read': 'NimbleperfData',
        'total': 'NimbleperfData',
        'write': 'NimbleperfData'
    }

    attribute_map = {
        'read': 'read',
        'total': 'total',
        'write': 'write'
    }

    def __init__(self, read=None, total=None, write=None):  # noqa: E501
        """NimbleKpiMetrics - a model defined in OpenAPI"""  # noqa: E501

        self._read = None
        self._total = None
        self._write = None
        self.discriminator = None

        if read is not None:
            self.read = read
        if total is not None:
            self.total = total
        if write is not None:
            self.write = write

    @property
    def read(self):
        """Gets the read of this NimbleKpiMetrics.  # noqa: E501


        :return: The read of this NimbleKpiMetrics.  # noqa: E501
        :rtype: NimbleperfData
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this NimbleKpiMetrics.


        :param read: The read of this NimbleKpiMetrics.  # noqa: E501
        :type: NimbleperfData
        """

        self._read = read

    @property
    def total(self):
        """Gets the total of this NimbleKpiMetrics.  # noqa: E501


        :return: The total of this NimbleKpiMetrics.  # noqa: E501
        :rtype: NimbleperfData
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this NimbleKpiMetrics.


        :param total: The total of this NimbleKpiMetrics.  # noqa: E501
        :type: NimbleperfData
        """

        self._total = total

    @property
    def write(self):
        """Gets the write of this NimbleKpiMetrics.  # noqa: E501


        :return: The write of this NimbleKpiMetrics.  # noqa: E501
        :rtype: NimbleperfData
        """
        return self._write

    @write.setter
    def write(self, write):
        """Sets the write of this NimbleKpiMetrics.


        :param write: The write of this NimbleKpiMetrics.  # noqa: E501
        :type: NimbleperfData
        """

        self._write = write

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
        if not isinstance(other, NimbleKpiMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
