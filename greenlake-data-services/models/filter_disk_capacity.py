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


class FilterDiskCapacity(object):
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
        'allocated_mi_b': 'int',
        'failed_mi_b': 'int',
        'free_mi_b': 'int',
        'total_mi_b': 'int',
        'unavailable_mi_b': 'int'
    }

    attribute_map = {
        'allocated_mi_b': 'allocatedMiB',
        'failed_mi_b': 'failedMiB',
        'free_mi_b': 'freeMiB',
        'total_mi_b': 'totalMiB',
        'unavailable_mi_b': 'unavailableMiB'
    }

    def __init__(self, allocated_mi_b=None, failed_mi_b=None, free_mi_b=None, total_mi_b=None, unavailable_mi_b=None):  # noqa: E501
        """FilterDiskCapacity - a model defined in OpenAPI"""  # noqa: E501

        self._allocated_mi_b = None
        self._failed_mi_b = None
        self._free_mi_b = None
        self._total_mi_b = None
        self._unavailable_mi_b = None
        self.discriminator = None

        if allocated_mi_b is not None:
            self.allocated_mi_b = allocated_mi_b
        if failed_mi_b is not None:
            self.failed_mi_b = failed_mi_b
        if free_mi_b is not None:
            self.free_mi_b = free_mi_b
        if total_mi_b is not None:
            self.total_mi_b = total_mi_b
        if unavailable_mi_b is not None:
            self.unavailable_mi_b = unavailable_mi_b

    @property
    def allocated_mi_b(self):
        """Gets the allocated_mi_b of this FilterDiskCapacity.  # noqa: E501

        allocated Size in MiB  # noqa: E501

        :return: The allocated_mi_b of this FilterDiskCapacity.  # noqa: E501
        :rtype: int
        """
        return self._allocated_mi_b

    @allocated_mi_b.setter
    def allocated_mi_b(self, allocated_mi_b):
        """Sets the allocated_mi_b of this FilterDiskCapacity.

        allocated Size in MiB  # noqa: E501

        :param allocated_mi_b: The allocated_mi_b of this FilterDiskCapacity.  # noqa: E501
        :type: int
        """

        self._allocated_mi_b = allocated_mi_b

    @property
    def failed_mi_b(self):
        """Gets the failed_mi_b of this FilterDiskCapacity.  # noqa: E501

        failed Size in MiB  # noqa: E501

        :return: The failed_mi_b of this FilterDiskCapacity.  # noqa: E501
        :rtype: int
        """
        return self._failed_mi_b

    @failed_mi_b.setter
    def failed_mi_b(self, failed_mi_b):
        """Sets the failed_mi_b of this FilterDiskCapacity.

        failed Size in MiB  # noqa: E501

        :param failed_mi_b: The failed_mi_b of this FilterDiskCapacity.  # noqa: E501
        :type: int
        """

        self._failed_mi_b = failed_mi_b

    @property
    def free_mi_b(self):
        """Gets the free_mi_b of this FilterDiskCapacity.  # noqa: E501

        free Size in MiB  # noqa: E501

        :return: The free_mi_b of this FilterDiskCapacity.  # noqa: E501
        :rtype: int
        """
        return self._free_mi_b

    @free_mi_b.setter
    def free_mi_b(self, free_mi_b):
        """Sets the free_mi_b of this FilterDiskCapacity.

        free Size in MiB  # noqa: E501

        :param free_mi_b: The free_mi_b of this FilterDiskCapacity.  # noqa: E501
        :type: int
        """

        self._free_mi_b = free_mi_b

    @property
    def total_mi_b(self):
        """Gets the total_mi_b of this FilterDiskCapacity.  # noqa: E501

        total Size in MiB. `Filter, Sort`  # noqa: E501

        :return: The total_mi_b of this FilterDiskCapacity.  # noqa: E501
        :rtype: int
        """
        return self._total_mi_b

    @total_mi_b.setter
    def total_mi_b(self, total_mi_b):
        """Sets the total_mi_b of this FilterDiskCapacity.

        total Size in MiB. `Filter, Sort`  # noqa: E501

        :param total_mi_b: The total_mi_b of this FilterDiskCapacity.  # noqa: E501
        :type: int
        """

        self._total_mi_b = total_mi_b

    @property
    def unavailable_mi_b(self):
        """Gets the unavailable_mi_b of this FilterDiskCapacity.  # noqa: E501

        unavailable Size in MiB  # noqa: E501

        :return: The unavailable_mi_b of this FilterDiskCapacity.  # noqa: E501
        :rtype: int
        """
        return self._unavailable_mi_b

    @unavailable_mi_b.setter
    def unavailable_mi_b(self, unavailable_mi_b):
        """Sets the unavailable_mi_b of this FilterDiskCapacity.

        unavailable Size in MiB  # noqa: E501

        :param unavailable_mi_b: The unavailable_mi_b of this FilterDiskCapacity.  # noqa: E501
        :type: int
        """

        self._unavailable_mi_b = unavailable_mi_b

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
        if not isinstance(other, FilterDiskCapacity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other