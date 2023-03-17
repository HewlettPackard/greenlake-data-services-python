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


class NimbleShelfFieldsWithSortKey(object):
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
        'id': 'str',
        'model': 'str',
        'serial': 'str'
    }

    attribute_map = {
        'array_id': 'array_id',
        'array_name': 'array_name',
        'id': 'id',
        'model': 'model',
        'serial': 'serial'
    }

    def __init__(self, array_id=None, array_name=None, id=None, model=None, serial=None):  # noqa: E501
        """NimbleShelfFieldsWithSortKey - a model defined in OpenAPI"""  # noqa: E501

        self._array_id = None
        self._array_name = None
        self._id = None
        self._model = None
        self._serial = None
        self.discriminator = None

        if array_id is not None:
            self.array_id = array_id
        if array_name is not None:
            self.array_name = array_name
        if id is not None:
            self.id = id
        if model is not None:
            self.model = model
        if serial is not None:
            self.serial = serial

    @property
    def array_id(self):
        """Gets the array_id of this NimbleShelfFieldsWithSortKey.  # noqa: E501

        ID of array the shelf belongs to. `Filter, Sort`  # noqa: E501

        :return: The array_id of this NimbleShelfFieldsWithSortKey.  # noqa: E501
        :rtype: str
        """
        return self._array_id

    @array_id.setter
    def array_id(self, array_id):
        """Sets the array_id of this NimbleShelfFieldsWithSortKey.

        ID of array the shelf belongs to. `Filter, Sort`  # noqa: E501

        :param array_id: The array_id of this NimbleShelfFieldsWithSortKey.  # noqa: E501
        :type: str
        """

        self._array_id = array_id

    @property
    def array_name(self):
        """Gets the array_name of this NimbleShelfFieldsWithSortKey.  # noqa: E501

        Name of array the shelf belongs to. `Filter, Sort`  # noqa: E501

        :return: The array_name of this NimbleShelfFieldsWithSortKey.  # noqa: E501
        :rtype: str
        """
        return self._array_name

    @array_name.setter
    def array_name(self, array_name):
        """Sets the array_name of this NimbleShelfFieldsWithSortKey.

        Name of array the shelf belongs to. `Filter, Sort`  # noqa: E501

        :param array_name: The array_name of this NimbleShelfFieldsWithSortKey.  # noqa: E501
        :type: str
        """

        self._array_name = array_name

    @property
    def id(self):
        """Gets the id of this NimbleShelfFieldsWithSortKey.  # noqa: E501

        Identifier of the shelf. `Filter`  # noqa: E501

        :return: The id of this NimbleShelfFieldsWithSortKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NimbleShelfFieldsWithSortKey.

        Identifier of the shelf. `Filter`  # noqa: E501

        :param id: The id of this NimbleShelfFieldsWithSortKey.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def model(self):
        """Gets the model of this NimbleShelfFieldsWithSortKey.  # noqa: E501

        Model of the shelf or head unit. `Filter, Sort`  # noqa: E501

        :return: The model of this NimbleShelfFieldsWithSortKey.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this NimbleShelfFieldsWithSortKey.

        Model of the shelf or head unit. `Filter, Sort`  # noqa: E501

        :param model: The model of this NimbleShelfFieldsWithSortKey.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def serial(self):
        """Gets the serial of this NimbleShelfFieldsWithSortKey.  # noqa: E501

        The serial number of the chassis. `Filter, Sort`  # noqa: E501

        :return: The serial of this NimbleShelfFieldsWithSortKey.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this NimbleShelfFieldsWithSortKey.

        The serial number of the chassis. `Filter, Sort`  # noqa: E501

        :param serial: The serial of this NimbleShelfFieldsWithSortKey.  # noqa: E501
        :type: str
        """

        self._serial = serial

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
        if not isinstance(other, NimbleShelfFieldsWithSortKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other