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


class NimbleRemoveVolumeFromVolumeCollectionInput(object):
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
        'volume_ids': 'list[str]'
    }

    attribute_map = {
        'volume_ids': 'volume_ids'
    }

    def __init__(self, volume_ids=None):  # noqa: E501
        """NimbleRemoveVolumeFromVolumeCollectionInput - a model defined in OpenAPI"""  # noqa: E501

        self._volume_ids = None
        self.discriminator = None

        if volume_ids is not None:
            self.volume_ids = volume_ids

    @property
    def volume_ids(self):
        """Gets the volume_ids of this NimbleRemoveVolumeFromVolumeCollectionInput.  # noqa: E501

        Volume ids that need to be remove from volume collections.  # noqa: E501

        :return: The volume_ids of this NimbleRemoveVolumeFromVolumeCollectionInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        """Sets the volume_ids of this NimbleRemoveVolumeFromVolumeCollectionInput.

        Volume ids that need to be remove from volume collections.  # noqa: E501

        :param volume_ids: The volume_ids of this NimbleRemoveVolumeFromVolumeCollectionInput.  # noqa: E501
        :type: list[str]
        """

        self._volume_ids = volume_ids

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
        if not isinstance(other, NimbleRemoveVolumeFromVolumeCollectionInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
