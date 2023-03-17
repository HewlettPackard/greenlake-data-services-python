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


class VolumeSetHostGroupList(object):
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
        'customer_id': 'str',
        'generation': 'int',
        'host_group_name': 'str',
        'hosts': 'list[VolumeSetHostProximityInfo]',
        'system_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'customer_id': 'customerId',
        'generation': 'generation',
        'host_group_name': 'hostGroupName',
        'hosts': 'hosts',
        'system_id': 'systemId',
        'type': 'type'
    }

    def __init__(self, customer_id=None, generation=None, host_group_name=None, hosts=None, system_id=None, type=None):  # noqa: E501
        """VolumeSetHostGroupList - a model defined in OpenAPI"""  # noqa: E501

        self._customer_id = None
        self._generation = None
        self._host_group_name = None
        self._hosts = None
        self._system_id = None
        self._type = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if generation is not None:
            self.generation = generation
        if host_group_name is not None:
            self.host_group_name = host_group_name
        if hosts is not None:
            self.hosts = hosts
        if system_id is not None:
            self.system_id = system_id
        if type is not None:
            self.type = type

    @property
    def customer_id(self):
        """Gets the customer_id of this VolumeSetHostGroupList.  # noqa: E501

        customerId  # noqa: E501

        :return: The customer_id of this VolumeSetHostGroupList.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this VolumeSetHostGroupList.

        customerId  # noqa: E501

        :param customer_id: The customer_id of this VolumeSetHostGroupList.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def generation(self):
        """Gets the generation of this VolumeSetHostGroupList.  # noqa: E501

        generation  # noqa: E501

        :return: The generation of this VolumeSetHostGroupList.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this VolumeSetHostGroupList.

        generation  # noqa: E501

        :param generation: The generation of this VolumeSetHostGroupList.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def host_group_name(self):
        """Gets the host_group_name of this VolumeSetHostGroupList.  # noqa: E501

        Host group name  # noqa: E501

        :return: The host_group_name of this VolumeSetHostGroupList.  # noqa: E501
        :rtype: str
        """
        return self._host_group_name

    @host_group_name.setter
    def host_group_name(self, host_group_name):
        """Sets the host_group_name of this VolumeSetHostGroupList.

        Host group name  # noqa: E501

        :param host_group_name: The host_group_name of this VolumeSetHostGroupList.  # noqa: E501
        :type: str
        """

        self._host_group_name = host_group_name

    @property
    def hosts(self):
        """Gets the hosts of this VolumeSetHostGroupList.  # noqa: E501


        :return: The hosts of this VolumeSetHostGroupList.  # noqa: E501
        :rtype: list[VolumeSetHostProximityInfo]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this VolumeSetHostGroupList.


        :param hosts: The hosts of this VolumeSetHostGroupList.  # noqa: E501
        :type: list[VolumeSetHostProximityInfo]
        """

        self._hosts = hosts

    @property
    def system_id(self):
        """Gets the system_id of this VolumeSetHostGroupList.  # noqa: E501

        Unique ID or serial number of the system.  # noqa: E501

        :return: The system_id of this VolumeSetHostGroupList.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this VolumeSetHostGroupList.

        Unique ID or serial number of the system.  # noqa: E501

        :param system_id: The system_id of this VolumeSetHostGroupList.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def type(self):
        """Gets the type of this VolumeSetHostGroupList.  # noqa: E501

        type  # noqa: E501

        :return: The type of this VolumeSetHostGroupList.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VolumeSetHostGroupList.

        type  # noqa: E501

        :param type: The type of this VolumeSetHostGroupList.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, VolumeSetHostGroupList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
