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


class ReplicationPartnerCommonFieldsPolicies(object):
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
        'mirror_config': 'bool'
    }

    attribute_map = {
        'mirror_config': 'mirrorConfig'
    }

    def __init__(self, mirror_config=None):  # noqa: E501
        """ReplicationPartnerCommonFieldsPolicies - a model defined in OpenAPI"""  # noqa: E501

        self._mirror_config = None
        self.discriminator = None

        if mirror_config is not None:
            self.mirror_config = mirror_config

    @property
    def mirror_config(self):
        """Gets the mirror_config of this ReplicationPartnerCommonFieldsPolicies.  # noqa: E501

        Duplication of all configurations involving the specified partner.  # noqa: E501

        :return: The mirror_config of this ReplicationPartnerCommonFieldsPolicies.  # noqa: E501
        :rtype: bool
        """
        return self._mirror_config

    @mirror_config.setter
    def mirror_config(self, mirror_config):
        """Sets the mirror_config of this ReplicationPartnerCommonFieldsPolicies.

        Duplication of all configurations involving the specified partner.  # noqa: E501

        :param mirror_config: The mirror_config of this ReplicationPartnerCommonFieldsPolicies.  # noqa: E501
        :type: bool
        """

        self._mirror_config = mirror_config

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
        if not isinstance(other, ReplicationPartnerCommonFieldsPolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other