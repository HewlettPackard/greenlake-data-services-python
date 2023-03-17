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


class DiskFilterableFieldsWithoutFilter(object):
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
        'array_id': 'str',
        'array_name': 'str',
        'disk_type': 'str',
        'id': 'str',
        'model': 'str',
        'serial': 'str',
        'shelf_id': 'str',
        'shelf_serial': 'str',
        'state': 'str'
    }

    attribute_map = {
        'array_id': 'array_id',
        'array_name': 'array_name',
        'disk_type': 'disk_type',
        'id': 'id',
        'model': 'model',
        'serial': 'serial',
        'shelf_id': 'shelf_id',
        'shelf_serial': 'shelf_serial',
        'state': 'state'
    }

    def __init__(self, array_id=None, array_name=None, disk_type=None, id=None, model=None, serial=None, shelf_id=None, shelf_serial=None, state=None):  # noqa: E501
        """DiskFilterableFieldsWithoutFilter - a model defined in OpenAPI"""  # noqa: E501

        self._array_id = None
        self._array_name = None
        self._disk_type = None
        self._id = None
        self._model = None
        self._serial = None
        self._shelf_id = None
        self._shelf_serial = None
        self._state = None
        self.discriminator = None

        if array_id is not None:
            self.array_id = array_id
        if array_name is not None:
            self.array_name = array_name
        if disk_type is not None:
            self.disk_type = disk_type
        if id is not None:
            self.id = id
        if model is not None:
            self.model = model
        if serial is not None:
            self.serial = serial
        if shelf_id is not None:
            self.shelf_id = shelf_id
        if shelf_serial is not None:
            self.shelf_serial = shelf_serial
        if state is not None:
            self.state = state

    @property
    def array_id(self):
        """Gets the array_id of this DiskFilterableFieldsWithoutFilter.  # noqa: E501

        ID of array the disk belongs to. A 42 digit hexadecimal number.  # noqa: E501

        :return: The array_id of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :rtype: str
        """
        return self._array_id

    @array_id.setter
    def array_id(self, array_id):
        """Sets the array_id of this DiskFilterableFieldsWithoutFilter.

        ID of array the disk belongs to. A 42 digit hexadecimal number.  # noqa: E501

        :param array_id: The array_id of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :type: str
        """

        self._array_id = array_id

    @property
    def array_name(self):
        """Gets the array_name of this DiskFilterableFieldsWithoutFilter.  # noqa: E501

        Name of array the disk belongs to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The array_name of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :rtype: str
        """
        return self._array_name

    @array_name.setter
    def array_name(self, array_name):
        """Sets the array_name of this DiskFilterableFieldsWithoutFilter.

        Name of array the disk belongs to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param array_name: The array_name of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :type: str
        """

        self._array_name = array_name

    @property
    def disk_type(self):
        """Gets the disk_type of this DiskFilterableFieldsWithoutFilter.  # noqa: E501

        Type of disk (HDD, SSD, N/A). Disk type. Possible values: 'hdd', 'ssd'.  # noqa: E501

        :return: The disk_type of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        """Sets the disk_type of this DiskFilterableFieldsWithoutFilter.

        Type of disk (HDD, SSD, N/A). Disk type. Possible values: 'hdd', 'ssd'.  # noqa: E501

        :param disk_type: The disk_type of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :type: str
        """

        self._disk_type = disk_type

    @property
    def id(self):
        """Gets the id of this DiskFilterableFieldsWithoutFilter.  # noqa: E501

        Identifier of disk. A 42 digit hexadecimal number.  # noqa: E501

        :return: The id of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DiskFilterableFieldsWithoutFilter.

        Identifier of disk. A 42 digit hexadecimal number.  # noqa: E501

        :param id: The id of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def model(self):
        """Gets the model of this DiskFilterableFieldsWithoutFilter.  # noqa: E501

        Disk model name.  # noqa: E501

        :return: The model of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DiskFilterableFieldsWithoutFilter.

        Disk model name.  # noqa: E501

        :param model: The model of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def serial(self):
        """Gets the serial of this DiskFilterableFieldsWithoutFilter.  # noqa: E501

        Disk serial number(N/A if empty).  # noqa: E501

        :return: The serial of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this DiskFilterableFieldsWithoutFilter.

        Disk serial number(N/A if empty).  # noqa: E501

        :param serial: The serial of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def shelf_id(self):
        """Gets the shelf_id of this DiskFilterableFieldsWithoutFilter.  # noqa: E501

        Identifies the physical shelf the disk belongs to. A 42 digit hexadecimal number.  # noqa: E501

        :return: The shelf_id of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :rtype: str
        """
        return self._shelf_id

    @shelf_id.setter
    def shelf_id(self, shelf_id):
        """Sets the shelf_id of this DiskFilterableFieldsWithoutFilter.

        Identifies the physical shelf the disk belongs to. A 42 digit hexadecimal number.  # noqa: E501

        :param shelf_id: The shelf_id of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :type: str
        """

        self._shelf_id = shelf_id

    @property
    def shelf_serial(self):
        """Gets the shelf_serial of this DiskFilterableFieldsWithoutFilter.  # noqa: E501

        Serial number of the shelf the disk is attached to.  # noqa: E501

        :return: The shelf_serial of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :rtype: str
        """
        return self._shelf_serial

    @shelf_serial.setter
    def shelf_serial(self, shelf_serial):
        """Sets the shelf_serial of this DiskFilterableFieldsWithoutFilter.

        Serial number of the shelf the disk is attached to.  # noqa: E501

        :param shelf_serial: The shelf_serial of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :type: str
        """

        self._shelf_serial = shelf_serial

    @property
    def state(self):
        """Gets the state of this DiskFilterableFieldsWithoutFilter.  # noqa: E501

        Disk hardware state. Disk state. Possible values: 'valid', 'in use', 'failed', absent', 'removed', 'void', 't_fail', 'foreign'.  # noqa: E501

        :return: The state of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DiskFilterableFieldsWithoutFilter.

        Disk hardware state. Disk state. Possible values: 'valid', 'in use', 'failed', absent', 'removed', 'void', 't_fail', 'foreign'.  # noqa: E501

        :param state: The state of this DiskFilterableFieldsWithoutFilter.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if not isinstance(other, DiskFilterableFieldsWithoutFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
