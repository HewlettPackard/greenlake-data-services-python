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


class NimbleHostReview(object):
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
        'changes': 'NimbleChanges',
        'initiators': 'list[NimbleInitiatorReview]',
        'name': 'str'
    }

    attribute_map = {
        'changes': 'changes',
        'initiators': 'initiators',
        'name': 'name'
    }

    def __init__(self, changes=None, initiators=None, name=None):  # noqa: E501
        """NimbleHostReview - a model defined in OpenAPI"""  # noqa: E501

        self._changes = None
        self._initiators = None
        self._name = None
        self.discriminator = None

        if changes is not None:
            self.changes = changes
        if initiators is not None:
            self.initiators = initiators
        if name is not None:
            self.name = name

    @property
    def changes(self):
        """Gets the changes of this NimbleHostReview.  # noqa: E501


        :return: The changes of this NimbleHostReview.  # noqa: E501
        :rtype: NimbleChanges
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this NimbleHostReview.


        :param changes: The changes of this NimbleHostReview.  # noqa: E501
        :type: NimbleChanges
        """

        self._changes = changes

    @property
    def initiators(self):
        """Gets the initiators of this NimbleHostReview.  # noqa: E501

        list of initiator reviews  # noqa: E501

        :return: The initiators of this NimbleHostReview.  # noqa: E501
        :rtype: list[NimbleInitiatorReview]
        """
        return self._initiators

    @initiators.setter
    def initiators(self, initiators):
        """Sets the initiators of this NimbleHostReview.

        list of initiator reviews  # noqa: E501

        :param initiators: The initiators of this NimbleHostReview.  # noqa: E501
        :type: list[NimbleInitiatorReview]
        """

        self._initiators = initiators

    @property
    def name(self):
        """Gets the name of this NimbleHostReview.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this NimbleHostReview.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NimbleHostReview.

        Name  # noqa: E501

        :param name: The name of this NimbleHostReview.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, NimbleHostReview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other