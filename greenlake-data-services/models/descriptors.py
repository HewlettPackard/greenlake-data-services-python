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


class Descriptors(object):
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
        'comment': 'str',
        'contact': 'str',
        'location': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'comment': 'comment',
        'contact': 'contact',
        'location': 'location',
        'owner': 'owner'
    }

    def __init__(self, comment=None, contact=None, location=None, owner=None):  # noqa: E501
        """Descriptors - a model defined in OpenAPI"""  # noqa: E501

        self._comment = None
        self._contact = None
        self._location = None
        self._owner = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if contact is not None:
            self.contact = contact
        if location is not None:
            self.location = location
        if owner is not None:
            self.owner = owner

    @property
    def comment(self):
        """Gets the comment of this Descriptors.  # noqa: E501

        CommeUser-specified comment for the system  # noqa: E501

        :return: The comment of this Descriptors.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Descriptors.

        CommeUser-specified comment for the system  # noqa: E501

        :param comment: The comment of this Descriptors.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def contact(self):
        """Gets the contact of this Descriptors.  # noqa: E501

        User-specified contact for the system  # noqa: E501

        :return: The contact of this Descriptors.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Descriptors.

        User-specified contact for the system  # noqa: E501

        :param contact: The contact of this Descriptors.  # noqa: E501
        :type: str
        """

        self._contact = contact

    @property
    def location(self):
        """Gets the location of this Descriptors.  # noqa: E501

        User-specified location of the system  # noqa: E501

        :return: The location of this Descriptors.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Descriptors.

        User-specified location of the system  # noqa: E501

        :param location: The location of this Descriptors.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def owner(self):
        """Gets the owner of this Descriptors.  # noqa: E501

        User-specified owner for the system  # noqa: E501

        :return: The owner of this Descriptors.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Descriptors.

        User-specified owner for the system  # noqa: E501

        :param owner: The owner of this Descriptors.  # noqa: E501
        :type: str
        """

        self._owner = owner

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
        if not isinstance(other, Descriptors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other