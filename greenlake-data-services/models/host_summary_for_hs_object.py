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


class HostSummaryForHSObject(object):
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
        'initiators': 'list[InitiatorSummary]',
        'ip_address': 'str',
        'marked_for_delete': 'bool',
        'name': 'str',
        'systems': 'list[str]',
        'user_created': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'initiators': 'initiators',
        'ip_address': 'ipAddress',
        'marked_for_delete': 'markedForDelete',
        'name': 'name',
        'systems': 'systems',
        'user_created': 'userCreated'
    }

    def __init__(self, id=None, initiators=None, ip_address=None, marked_for_delete=None, name=None, systems=None, user_created=None):  # noqa: E501
        """HostSummaryForHSObject - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._initiators = None
        self._ip_address = None
        self._marked_for_delete = None
        self._name = None
        self._systems = None
        self._user_created = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if initiators is not None:
            self.initiators = initiators
        if ip_address is not None:
            self.ip_address = ip_address
        if marked_for_delete is not None:
            self.marked_for_delete = marked_for_delete
        if name is not None:
            self.name = name
        if systems is not None:
            self.systems = systems
        if user_created is not None:
            self.user_created = user_created

    @property
    def id(self):
        """Gets the id of this HostSummaryForHSObject.  # noqa: E501

        Identifier for host.  # noqa: E501

        :return: The id of this HostSummaryForHSObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostSummaryForHSObject.

        Identifier for host.  # noqa: E501

        :param id: The id of this HostSummaryForHSObject.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def initiators(self):
        """Gets the initiators of this HostSummaryForHSObject.  # noqa: E501

        Initiator to which the host belongs to.  # noqa: E501

        :return: The initiators of this HostSummaryForHSObject.  # noqa: E501
        :rtype: list[InitiatorSummary]
        """
        return self._initiators

    @initiators.setter
    def initiators(self, initiators):
        """Sets the initiators of this HostSummaryForHSObject.

        Initiator to which the host belongs to.  # noqa: E501

        :param initiators: The initiators of this HostSummaryForHSObject.  # noqa: E501
        :type: list[InitiatorSummary]
        """

        self._initiators = initiators

    @property
    def ip_address(self):
        """Gets the ip_address of this HostSummaryForHSObject.  # noqa: E501

        IP address of the host.  # noqa: E501

        :return: The ip_address of this HostSummaryForHSObject.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this HostSummaryForHSObject.

        IP address of the host.  # noqa: E501

        :param ip_address: The ip_address of this HostSummaryForHSObject.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def marked_for_delete(self):
        """Gets the marked_for_delete of this HostSummaryForHSObject.  # noqa: E501

        Indicates whether host is marked for deletion or not  # noqa: E501

        :return: The marked_for_delete of this HostSummaryForHSObject.  # noqa: E501
        :rtype: bool
        """
        return self._marked_for_delete

    @marked_for_delete.setter
    def marked_for_delete(self, marked_for_delete):
        """Sets the marked_for_delete of this HostSummaryForHSObject.

        Indicates whether host is marked for deletion or not  # noqa: E501

        :param marked_for_delete: The marked_for_delete of this HostSummaryForHSObject.  # noqa: E501
        :type: bool
        """

        self._marked_for_delete = marked_for_delete

    @property
    def name(self):
        """Gets the name of this HostSummaryForHSObject.  # noqa: E501

        Name of the host.  # noqa: E501

        :return: The name of this HostSummaryForHSObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostSummaryForHSObject.

        Name of the host.  # noqa: E501

        :param name: The name of this HostSummaryForHSObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def systems(self):
        """Gets the systems of this HostSummaryForHSObject.  # noqa: E501

        system IDs to which the host belongs to  # noqa: E501

        :return: The systems of this HostSummaryForHSObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """Sets the systems of this HostSummaryForHSObject.

        system IDs to which the host belongs to  # noqa: E501

        :param systems: The systems of this HostSummaryForHSObject.  # noqa: E501
        :type: list[str]
        """

        self._systems = systems

    @property
    def user_created(self):
        """Gets the user_created of this HostSummaryForHSObject.  # noqa: E501

        Indicates whether user created host or discovered host  # noqa: E501

        :return: The user_created of this HostSummaryForHSObject.  # noqa: E501
        :rtype: bool
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this HostSummaryForHSObject.

        Indicates whether user created host or discovered host  # noqa: E501

        :param user_created: The user_created of this HostSummaryForHSObject.  # noqa: E501
        :type: bool
        """

        self._user_created = user_created

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
        if not isinstance(other, HostSummaryForHSObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
