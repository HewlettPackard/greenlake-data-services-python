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


class OfflineClone(object):
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
        'create_volume': 'list[CreateVolume]',
        'enable_resync': 'bool',
        'use_existing_volume': 'bool'
    }

    attribute_map = {
        'create_volume': 'createVolume',
        'enable_resync': 'enableResync',
        'use_existing_volume': 'useExistingVolume'
    }

    def __init__(self, create_volume=None, enable_resync=None, use_existing_volume=None):  # noqa: E501
        """OfflineClone - a model defined in OpenAPI"""  # noqa: E501

        self._create_volume = None
        self._enable_resync = None
        self._use_existing_volume = None
        self.discriminator = None

        if create_volume is not None:
            self.create_volume = create_volume
        if enable_resync is not None:
            self.enable_resync = enable_resync
        if use_existing_volume is not None:
            self.use_existing_volume = use_existing_volume

    @property
    def create_volume(self):
        """Gets the create_volume of this OfflineClone.  # noqa: E501

        Create a new volume for clone.  # noqa: E501

        :return: The create_volume of this OfflineClone.  # noqa: E501
        :rtype: list[CreateVolume]
        """
        return self._create_volume

    @create_volume.setter
    def create_volume(self, create_volume):
        """Sets the create_volume of this OfflineClone.

        Create a new volume for clone.  # noqa: E501

        :param create_volume: The create_volume of this OfflineClone.  # noqa: E501
        :type: list[CreateVolume]
        """

        self._create_volume = create_volume

    @property
    def enable_resync(self):
        """Gets the enable_resync of this OfflineClone.  # noqa: E501

        Secify to save a snapshot for fast resynchronization.  # noqa: E501

        :return: The enable_resync of this OfflineClone.  # noqa: E501
        :rtype: bool
        """
        return self._enable_resync

    @enable_resync.setter
    def enable_resync(self, enable_resync):
        """Sets the enable_resync of this OfflineClone.

        Secify to save a snapshot for fast resynchronization.  # noqa: E501

        :param enable_resync: The enable_resync of this OfflineClone.  # noqa: E501
        :type: bool
        """

        self._enable_resync = enable_resync

    @property
    def use_existing_volume(self):
        """Gets the use_existing_volume of this OfflineClone.  # noqa: E501

        Secify to use existing volume or create a new volume for clone.  # noqa: E501

        :return: The use_existing_volume of this OfflineClone.  # noqa: E501
        :rtype: bool
        """
        return self._use_existing_volume

    @use_existing_volume.setter
    def use_existing_volume(self, use_existing_volume):
        """Sets the use_existing_volume of this OfflineClone.

        Secify to use existing volume or create a new volume for clone.  # noqa: E501

        :param use_existing_volume: The use_existing_volume of this OfflineClone.  # noqa: E501
        :type: bool
        """

        self._use_existing_volume = use_existing_volume

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
        if not isinstance(other, OfflineClone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other