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


class Applications(object):
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
        'application_set_type': 'str',
        'total_size_mi_b': 'float',
        'total_used_size_mi_b': 'float',
        'volumes_count': 'int'
    }

    attribute_map = {
        'application_set_type': 'applicationSetType',
        'total_size_mi_b': 'totalSizeMiB',
        'total_used_size_mi_b': 'totalUsedSizeMiB',
        'volumes_count': 'volumesCount'
    }

    def __init__(self, application_set_type=None, total_size_mi_b=None, total_used_size_mi_b=None, volumes_count=None):  # noqa: E501
        """Applications - a model defined in OpenAPI"""  # noqa: E501

        self._application_set_type = None
        self._total_size_mi_b = None
        self._total_used_size_mi_b = None
        self._volumes_count = None
        self.discriminator = None

        if application_set_type is not None:
            self.application_set_type = application_set_type
        if total_size_mi_b is not None:
            self.total_size_mi_b = total_size_mi_b
        if total_used_size_mi_b is not None:
            self.total_used_size_mi_b = total_used_size_mi_b
        if volumes_count is not None:
            self.volumes_count = volumes_count

    @property
    def application_set_type(self):
        """Gets the application_set_type of this Applications.  # noqa: E501

        Name of the application  # noqa: E501

        :return: The application_set_type of this Applications.  # noqa: E501
        :rtype: str
        """
        return self._application_set_type

    @application_set_type.setter
    def application_set_type(self, application_set_type):
        """Sets the application_set_type of this Applications.

        Name of the application  # noqa: E501

        :param application_set_type: The application_set_type of this Applications.  # noqa: E501
        :type: str
        """

        self._application_set_type = application_set_type

    @property
    def total_size_mi_b(self):
        """Gets the total_size_mi_b of this Applications.  # noqa: E501

        The total volume size in MiB of the application  # noqa: E501

        :return: The total_size_mi_b of this Applications.  # noqa: E501
        :rtype: float
        """
        return self._total_size_mi_b

    @total_size_mi_b.setter
    def total_size_mi_b(self, total_size_mi_b):
        """Sets the total_size_mi_b of this Applications.

        The total volume size in MiB of the application  # noqa: E501

        :param total_size_mi_b: The total_size_mi_b of this Applications.  # noqa: E501
        :type: float
        """

        self._total_size_mi_b = total_size_mi_b

    @property
    def total_used_size_mi_b(self):
        """Gets the total_used_size_mi_b of this Applications.  # noqa: E501

        The total used size in Mib of the application  # noqa: E501

        :return: The total_used_size_mi_b of this Applications.  # noqa: E501
        :rtype: float
        """
        return self._total_used_size_mi_b

    @total_used_size_mi_b.setter
    def total_used_size_mi_b(self, total_used_size_mi_b):
        """Sets the total_used_size_mi_b of this Applications.

        The total used size in Mib of the application  # noqa: E501

        :param total_used_size_mi_b: The total_used_size_mi_b of this Applications.  # noqa: E501
        :type: float
        """

        self._total_used_size_mi_b = total_used_size_mi_b

    @property
    def volumes_count(self):
        """Gets the volumes_count of this Applications.  # noqa: E501

        The number of volumes in an application  # noqa: E501

        :return: The volumes_count of this Applications.  # noqa: E501
        :rtype: int
        """
        return self._volumes_count

    @volumes_count.setter
    def volumes_count(self, volumes_count):
        """Sets the volumes_count of this Applications.

        The number of volumes in an application  # noqa: E501

        :param volumes_count: The volumes_count of this Applications.  # noqa: E501
        :type: int
        """

        self._volumes_count = volumes_count

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
        if not isinstance(other, Applications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other