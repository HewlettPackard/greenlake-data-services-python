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


class NimbleArrayFieldsWithoutSortKey(object):
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
        'model': 'str',
        'name': 'str',
        'pool_id': 'str',
        'serial': 'str'
    }

    attribute_map = {
        'id': 'id',
        'model': 'model',
        'name': 'name',
        'pool_id': 'pool_id',
        'serial': 'serial'
    }

    def __init__(self, id=None, model=None, name=None, pool_id=None, serial=None):  # noqa: E501
        """NimbleArrayFieldsWithoutSortKey - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._model = None
        self._name = None
        self._pool_id = None
        self._serial = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if model is not None:
            self.model = model
        if name is not None:
            self.name = name
        if pool_id is not None:
            self.pool_id = pool_id
        if serial is not None:
            self.serial = serial

    @property
    def id(self):
        """Gets the id of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501

        Identifier for array. A 42 digit hexadecimal number.  # noqa: E501

        :return: The id of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NimbleArrayFieldsWithoutSortKey.

        Identifier for array. A 42 digit hexadecimal number.  # noqa: E501

        :param id: The id of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def model(self):
        """Gets the model of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501

        Array model. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The model of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this NimbleArrayFieldsWithoutSortKey.

        Array model. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param model: The model of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def name(self):
        """Gets the name of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501

        The user provided name of the array. It is also the array's hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen.  # noqa: E501

        :return: The name of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NimbleArrayFieldsWithoutSortKey.

        The user provided name of the array. It is also the array's hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen.  # noqa: E501

        :param name: The name of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pool_id(self):
        """Gets the pool_id of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501

        ID of pool to which this is a member. A 42 digit hexadecimal number.  # noqa: E501

        :return: The pool_id of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this NimbleArrayFieldsWithoutSortKey.

        ID of pool to which this is a member. A 42 digit hexadecimal number.  # noqa: E501

        :param pool_id: The pool_id of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._pool_id = pool_id

    @property
    def serial(self):
        """Gets the serial of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501

        Serial number of the array.  # noqa: E501

        :return: The serial of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this NimbleArrayFieldsWithoutSortKey.

        Serial number of the array.  # noqa: E501

        :param serial: The serial of this NimbleArrayFieldsWithoutSortKey.  # noqa: E501
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
        if not isinstance(other, NimbleArrayFieldsWithoutSortKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
