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


class Allocation(object):
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
        'ha': 'AllocationHA',
        'raid_type': 'str',
        'chunklet_pos_pref': 'str',
        'device_speed': 'AllocationDeviceSpeed',
        'device_type': 'str',
        'disk_filter': 'str',
        'requested_ha': 'AllocationHA',
        'set_size': 'str',
        'step_size': 'float'
    }

    attribute_map = {
        'ha': 'HA',
        'raid_type': 'RAIDType',
        'chunklet_pos_pref': 'chunkletPosPref',
        'device_speed': 'deviceSpeed',
        'device_type': 'deviceType',
        'disk_filter': 'diskFilter',
        'requested_ha': 'requestedHA',
        'set_size': 'setSize',
        'step_size': 'stepSize'
    }

    def __init__(self, ha=None, raid_type=None, chunklet_pos_pref=None, device_speed=None, device_type=None, disk_filter=None, requested_ha=None, set_size=None, step_size=None):  # noqa: E501
        """Allocation - a model defined in OpenAPI"""  # noqa: E501

        self._ha = None
        self._raid_type = None
        self._chunklet_pos_pref = None
        self._device_speed = None
        self._device_type = None
        self._disk_filter = None
        self._requested_ha = None
        self._set_size = None
        self._step_size = None
        self.discriminator = None

        if ha is not None:
            self.ha = ha
        if raid_type is not None:
            self.raid_type = raid_type
        if chunklet_pos_pref is not None:
            self.chunklet_pos_pref = chunklet_pos_pref
        if device_speed is not None:
            self.device_speed = device_speed
        if device_type is not None:
            self.device_type = device_type
        if disk_filter is not None:
            self.disk_filter = disk_filter
        if requested_ha is not None:
            self.requested_ha = requested_ha
        if set_size is not None:
            self.set_size = set_size
        if step_size is not None:
            self.step_size = step_size

    @property
    def ha(self):
        """Gets the ha of this Allocation.  # noqa: E501


        :return: The ha of this Allocation.  # noqa: E501
        :rtype: AllocationHA
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this Allocation.


        :param ha: The ha of this Allocation.  # noqa: E501
        :type: AllocationHA
        """

        self._ha = ha

    @property
    def raid_type(self):
        """Gets the raid_type of this Allocation.  # noqa: E501

        RAID type  # noqa: E501

        :return: The raid_type of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._raid_type

    @raid_type.setter
    def raid_type(self, raid_type):
        """Sets the raid_type of this Allocation.

        RAID type  # noqa: E501

        :param raid_type: The raid_type of this Allocation.  # noqa: E501
        :type: str
        """

        self._raid_type = raid_type

    @property
    def chunklet_pos_pref(self):
        """Gets the chunklet_pos_pref of this Allocation.  # noqa: E501

        Chunklets position  # noqa: E501

        :return: The chunklet_pos_pref of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._chunklet_pos_pref

    @chunklet_pos_pref.setter
    def chunklet_pos_pref(self, chunklet_pos_pref):
        """Sets the chunklet_pos_pref of this Allocation.

        Chunklets position  # noqa: E501

        :param chunklet_pos_pref: The chunklet_pos_pref of this Allocation.  # noqa: E501
        :type: str
        """

        self._chunklet_pos_pref = chunklet_pos_pref

    @property
    def device_speed(self):
        """Gets the device_speed of this Allocation.  # noqa: E501


        :return: The device_speed of this Allocation.  # noqa: E501
        :rtype: AllocationDeviceSpeed
        """
        return self._device_speed

    @device_speed.setter
    def device_speed(self, device_speed):
        """Sets the device_speed of this Allocation.


        :param device_speed: The device_speed of this Allocation.  # noqa: E501
        :type: AllocationDeviceSpeed
        """

        self._device_speed = device_speed

    @property
    def device_type(self):
        """Gets the device_type of this Allocation.  # noqa: E501

        Device type  # noqa: E501

        :return: The device_type of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this Allocation.

        Device type  # noqa: E501

        :param device_type: The device_type of this Allocation.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def disk_filter(self):
        """Gets the disk_filter of this Allocation.  # noqa: E501

        Disk filter  # noqa: E501

        :return: The disk_filter of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._disk_filter

    @disk_filter.setter
    def disk_filter(self, disk_filter):
        """Sets the disk_filter of this Allocation.

        Disk filter  # noqa: E501

        :param disk_filter: The disk_filter of this Allocation.  # noqa: E501
        :type: str
        """

        self._disk_filter = disk_filter

    @property
    def requested_ha(self):
        """Gets the requested_ha of this Allocation.  # noqa: E501


        :return: The requested_ha of this Allocation.  # noqa: E501
        :rtype: AllocationHA
        """
        return self._requested_ha

    @requested_ha.setter
    def requested_ha(self, requested_ha):
        """Sets the requested_ha of this Allocation.


        :param requested_ha: The requested_ha of this Allocation.  # noqa: E501
        :type: AllocationHA
        """

        self._requested_ha = requested_ha

    @property
    def set_size(self):
        """Gets the set_size of this Allocation.  # noqa: E501

        Set size  # noqa: E501

        :return: The set_size of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._set_size

    @set_size.setter
    def set_size(self, set_size):
        """Sets the set_size of this Allocation.

        Set size  # noqa: E501

        :param set_size: The set_size of this Allocation.  # noqa: E501
        :type: str
        """

        self._set_size = set_size

    @property
    def step_size(self):
        """Gets the step_size of this Allocation.  # noqa: E501

        Step size  # noqa: E501

        :return: The step_size of this Allocation.  # noqa: E501
        :rtype: float
        """
        return self._step_size

    @step_size.setter
    def step_size(self, step_size):
        """Sets the step_size of this Allocation.

        Step size  # noqa: E501

        :param step_size: The step_size of this Allocation.  # noqa: E501
        :type: float
        """

        self._step_size = step_size

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
        if not isinstance(other, Allocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
