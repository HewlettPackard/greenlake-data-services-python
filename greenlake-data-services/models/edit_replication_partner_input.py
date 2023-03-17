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


class EditReplicationPartnerInput(object):
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
        'add_rc_links': 'AddRemoteCopyLinks',
        'remove_rc_links': 'RemoveRemoteCopyLinksInput'
    }

    attribute_map = {
        'add_rc_links': 'addRcLinks',
        'remove_rc_links': 'removeRcLinks'
    }

    def __init__(self, add_rc_links=None, remove_rc_links=None):  # noqa: E501
        """EditReplicationPartnerInput - a model defined in OpenAPI"""  # noqa: E501

        self._add_rc_links = None
        self._remove_rc_links = None
        self.discriminator = None

        if add_rc_links is not None:
            self.add_rc_links = add_rc_links
        if remove_rc_links is not None:
            self.remove_rc_links = remove_rc_links

    @property
    def add_rc_links(self):
        """Gets the add_rc_links of this EditReplicationPartnerInput.  # noqa: E501


        :return: The add_rc_links of this EditReplicationPartnerInput.  # noqa: E501
        :rtype: AddRemoteCopyLinks
        """
        return self._add_rc_links

    @add_rc_links.setter
    def add_rc_links(self, add_rc_links):
        """Sets the add_rc_links of this EditReplicationPartnerInput.


        :param add_rc_links: The add_rc_links of this EditReplicationPartnerInput.  # noqa: E501
        :type: AddRemoteCopyLinks
        """

        self._add_rc_links = add_rc_links

    @property
    def remove_rc_links(self):
        """Gets the remove_rc_links of this EditReplicationPartnerInput.  # noqa: E501


        :return: The remove_rc_links of this EditReplicationPartnerInput.  # noqa: E501
        :rtype: RemoveRemoteCopyLinksInput
        """
        return self._remove_rc_links

    @remove_rc_links.setter
    def remove_rc_links(self, remove_rc_links):
        """Sets the remove_rc_links of this EditReplicationPartnerInput.


        :param remove_rc_links: The remove_rc_links of this EditReplicationPartnerInput.  # noqa: E501
        :type: RemoveRemoteCopyLinksInput
        """

        self._remove_rc_links = remove_rc_links

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
        if not isinstance(other, EditReplicationPartnerInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
