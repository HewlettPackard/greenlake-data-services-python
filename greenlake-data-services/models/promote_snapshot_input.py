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


class PromoteSnapshotInput(object):
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
        'pri': 'Priority',
        'target': 'str'
    }

    attribute_map = {
        'pri': 'pri',
        'target': 'target'
    }

    def __init__(self, pri=None, target=None):  # noqa: E501
        """PromoteSnapshotInput - a model defined in OpenAPI"""  # noqa: E501

        self._pri = None
        self._target = None
        self.discriminator = None

        if pri is not None:
            self.pri = pri
        if target is not None:
            self.target = target

    @property
    def pri(self):
        """Gets the pri of this PromoteSnapshotInput.  # noqa: E501


        :return: The pri of this PromoteSnapshotInput.  # noqa: E501
        :rtype: Priority
        """
        return self._pri

    @pri.setter
    def pri(self, pri):
        """Sets the pri of this PromoteSnapshotInput.


        :param pri: The pri of this PromoteSnapshotInput.  # noqa: E501
        :type: Priority
        """

        self._pri = pri

    @property
    def target(self):
        """Gets the target of this PromoteSnapshotInput.  # noqa: E501

        Target volume name to which the snapshot need to be promoted. If not specified it will be promoted to its base volume.  # noqa: E501

        :return: The target of this PromoteSnapshotInput.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this PromoteSnapshotInput.

        Target volume name to which the snapshot need to be promoted. If not specified it will be promoted to its base volume.  # noqa: E501

        :param target: The target of this PromoteSnapshotInput.  # noqa: E501
        :type: str
        """

        self._target = target

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
        if not isinstance(other, PromoteSnapshotInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other