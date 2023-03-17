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


class RecommendationList(object):
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
        'capacity_info': 'CapacityInfoSolo',
        'id': 'str',
        'mgmt_ip': 'str',
        'name': 'str',
        'product_family': 'str',
        'state': 'str',
        'system_wwn': 'str'
    }

    attribute_map = {
        'capacity_info': 'capacityInfo',
        'id': 'id',
        'mgmt_ip': 'mgmtIp',
        'name': 'name',
        'product_family': 'productFamily',
        'state': 'state',
        'system_wwn': 'systemWWN'
    }

    def __init__(self, capacity_info=None, id=None, mgmt_ip=None, name=None, product_family=None, state=None, system_wwn=None):  # noqa: E501
        """RecommendationList - a model defined in OpenAPI"""  # noqa: E501

        self._capacity_info = None
        self._id = None
        self._mgmt_ip = None
        self._name = None
        self._product_family = None
        self._state = None
        self._system_wwn = None
        self.discriminator = None

        if capacity_info is not None:
            self.capacity_info = capacity_info
        if id is not None:
            self.id = id
        if mgmt_ip is not None:
            self.mgmt_ip = mgmt_ip
        if name is not None:
            self.name = name
        if product_family is not None:
            self.product_family = product_family
        if state is not None:
            self.state = state
        if system_wwn is not None:
            self.system_wwn = system_wwn

    @property
    def capacity_info(self):
        """Gets the capacity_info of this RecommendationList.  # noqa: E501


        :return: The capacity_info of this RecommendationList.  # noqa: E501
        :rtype: CapacityInfoSolo
        """
        return self._capacity_info

    @capacity_info.setter
    def capacity_info(self, capacity_info):
        """Sets the capacity_info of this RecommendationList.


        :param capacity_info: The capacity_info of this RecommendationList.  # noqa: E501
        :type: CapacityInfoSolo
        """

        self._capacity_info = capacity_info

    @property
    def id(self):
        """Gets the id of this RecommendationList.  # noqa: E501

        uid of the array  # noqa: E501

        :return: The id of this RecommendationList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecommendationList.

        uid of the array  # noqa: E501

        :param id: The id of this RecommendationList.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def mgmt_ip(self):
        """Gets the mgmt_ip of this RecommendationList.  # noqa: E501

        management Ip of the array  # noqa: E501

        :return: The mgmt_ip of this RecommendationList.  # noqa: E501
        :rtype: str
        """
        return self._mgmt_ip

    @mgmt_ip.setter
    def mgmt_ip(self, mgmt_ip):
        """Sets the mgmt_ip of this RecommendationList.

        management Ip of the array  # noqa: E501

        :param mgmt_ip: The mgmt_ip of this RecommendationList.  # noqa: E501
        :type: str
        """

        self._mgmt_ip = mgmt_ip

    @property
    def name(self):
        """Gets the name of this RecommendationList.  # noqa: E501

        name of the array  # noqa: E501

        :return: The name of this RecommendationList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecommendationList.

        name of the array  # noqa: E501

        :param name: The name of this RecommendationList.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def product_family(self):
        """Gets the product_family of this RecommendationList.  # noqa: E501

        Storage device type. Possible values: deviceType1 and deviceType2  # noqa: E501

        :return: The product_family of this RecommendationList.  # noqa: E501
        :rtype: str
        """
        return self._product_family

    @product_family.setter
    def product_family(self, product_family):
        """Sets the product_family of this RecommendationList.

        Storage device type. Possible values: deviceType1 and deviceType2  # noqa: E501

        :param product_family: The product_family of this RecommendationList.  # noqa: E501
        :type: str
        """

        self._product_family = product_family

    @property
    def state(self):
        """Gets the state of this RecommendationList.  # noqa: E501

        For deviceType1 State derived from ports, enclosure, disk and node state for deviceType2 state is state reported by deviceType2 array  # noqa: E501

        :return: The state of this RecommendationList.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RecommendationList.

        For deviceType1 State derived from ports, enclosure, disk and node state for deviceType2 state is state reported by deviceType2 array  # noqa: E501

        :param state: The state of this RecommendationList.  # noqa: E501
        :type: str
        """
        allowed_values = ["NORMAL", "DEGRADED", "null"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def system_wwn(self):
        """Gets the system_wwn of this RecommendationList.  # noqa: E501

        WWN of the array  # noqa: E501

        :return: The system_wwn of this RecommendationList.  # noqa: E501
        :rtype: str
        """
        return self._system_wwn

    @system_wwn.setter
    def system_wwn(self, system_wwn):
        """Sets the system_wwn of this RecommendationList.

        WWN of the array  # noqa: E501

        :param system_wwn: The system_wwn of this RecommendationList.  # noqa: E501
        :type: str
        """

        self._system_wwn = system_wwn

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
        if not isinstance(other, RecommendationList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
