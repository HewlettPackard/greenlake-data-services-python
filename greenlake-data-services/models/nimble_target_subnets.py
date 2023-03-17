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


class NimbleTargetSubnets(object):
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
        'id': 'str',
        'label': 'str'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label'
    }

    def __init__(self, id=None, label=None):  # noqa: E501
        """NimbleTargetSubnets - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._label = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if label is not None:
            self.label = label

    @property
    def id(self):
        """Gets the id of this NimbleTargetSubnets.  # noqa: E501

        Subnet ID.  # noqa: E501

        :return: The id of this NimbleTargetSubnets.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NimbleTargetSubnets.

        Subnet ID.  # noqa: E501

        :param id: The id of this NimbleTargetSubnets.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this NimbleTargetSubnets.  # noqa: E501

        Subnet label.  # noqa: E501

        :return: The label of this NimbleTargetSubnets.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this NimbleTargetSubnets.

        Subnet label.  # noqa: E501

        :param label: The label of this NimbleTargetSubnets.  # noqa: E501
        :type: str
        """

        self._label = label

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
        if not isinstance(other, NimbleTargetSubnets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
