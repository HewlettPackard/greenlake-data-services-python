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


class NimbleDiskSmartAttributes(object):
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
        'cur_value': 'int',
        'flags': 'int',
        'last_updated_epoch_secs': 'int',
        'name': 'str',
        'raw_value': 'int',
        'smart_id': 'int',
        'threshold': 'int',
        'worst_value': 'int'
    }

    attribute_map = {
        'cur_value': 'cur_value',
        'flags': 'flags',
        'last_updated_epoch_secs': 'last_updated_epoch_secs',
        'name': 'name',
        'raw_value': 'raw_value',
        'smart_id': 'smart_id',
        'threshold': 'threshold',
        'worst_value': 'worst_value'
    }

    def __init__(self, cur_value=None, flags=None, last_updated_epoch_secs=None, name=None, raw_value=None, smart_id=None, threshold=None, worst_value=None):  # noqa: E501
        """NimbleDiskSmartAttributes - a model defined in OpenAPI"""  # noqa: E501

        self._cur_value = None
        self._flags = None
        self._last_updated_epoch_secs = None
        self._name = None
        self._raw_value = None
        self._smart_id = None
        self._threshold = None
        self._worst_value = None
        self.discriminator = None

        if cur_value is not None:
            self.cur_value = cur_value
        if flags is not None:
            self.flags = flags
        if last_updated_epoch_secs is not None:
            self.last_updated_epoch_secs = last_updated_epoch_secs
        if name is not None:
            self.name = name
        if raw_value is not None:
            self.raw_value = raw_value
        if smart_id is not None:
            self.smart_id = smart_id
        if threshold is not None:
            self.threshold = threshold
        if worst_value is not None:
            self.worst_value = worst_value

    @property
    def cur_value(self):
        """Gets the cur_value of this NimbleDiskSmartAttributes.  # noqa: E501

        Current value.  # noqa: E501

        :return: The cur_value of this NimbleDiskSmartAttributes.  # noqa: E501
        :rtype: int
        """
        return self._cur_value

    @cur_value.setter
    def cur_value(self, cur_value):
        """Sets the cur_value of this NimbleDiskSmartAttributes.

        Current value.  # noqa: E501

        :param cur_value: The cur_value of this NimbleDiskSmartAttributes.  # noqa: E501
        :type: int
        """

        self._cur_value = cur_value

    @property
    def flags(self):
        """Gets the flags of this NimbleDiskSmartAttributes.  # noqa: E501

        Smart flags.  # noqa: E501

        :return: The flags of this NimbleDiskSmartAttributes.  # noqa: E501
        :rtype: int
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this NimbleDiskSmartAttributes.

        Smart flags.  # noqa: E501

        :param flags: The flags of this NimbleDiskSmartAttributes.  # noqa: E501
        :type: int
        """

        self._flags = flags

    @property
    def last_updated_epoch_secs(self):
        """Gets the last_updated_epoch_secs of this NimbleDiskSmartAttributes.  # noqa: E501

        Last update time in epoch seconds.  # noqa: E501

        :return: The last_updated_epoch_secs of this NimbleDiskSmartAttributes.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_epoch_secs

    @last_updated_epoch_secs.setter
    def last_updated_epoch_secs(self, last_updated_epoch_secs):
        """Sets the last_updated_epoch_secs of this NimbleDiskSmartAttributes.

        Last update time in epoch seconds.  # noqa: E501

        :param last_updated_epoch_secs: The last_updated_epoch_secs of this NimbleDiskSmartAttributes.  # noqa: E501
        :type: int
        """

        self._last_updated_epoch_secs = last_updated_epoch_secs

    @property
    def name(self):
        """Gets the name of this NimbleDiskSmartAttributes.  # noqa: E501

        Name of the Smart attribute.  # noqa: E501

        :return: The name of this NimbleDiskSmartAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NimbleDiskSmartAttributes.

        Name of the Smart attribute.  # noqa: E501

        :param name: The name of this NimbleDiskSmartAttributes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def raw_value(self):
        """Gets the raw_value of this NimbleDiskSmartAttributes.  # noqa: E501

        Raw value.  # noqa: E501

        :return: The raw_value of this NimbleDiskSmartAttributes.  # noqa: E501
        :rtype: int
        """
        return self._raw_value

    @raw_value.setter
    def raw_value(self, raw_value):
        """Sets the raw_value of this NimbleDiskSmartAttributes.

        Raw value.  # noqa: E501

        :param raw_value: The raw_value of this NimbleDiskSmartAttributes.  # noqa: E501
        :type: int
        """

        self._raw_value = raw_value

    @property
    def smart_id(self):
        """Gets the smart_id of this NimbleDiskSmartAttributes.  # noqa: E501

        Smart attribute ID.  # noqa: E501

        :return: The smart_id of this NimbleDiskSmartAttributes.  # noqa: E501
        :rtype: int
        """
        return self._smart_id

    @smart_id.setter
    def smart_id(self, smart_id):
        """Sets the smart_id of this NimbleDiskSmartAttributes.

        Smart attribute ID.  # noqa: E501

        :param smart_id: The smart_id of this NimbleDiskSmartAttributes.  # noqa: E501
        :type: int
        """

        self._smart_id = smart_id

    @property
    def threshold(self):
        """Gets the threshold of this NimbleDiskSmartAttributes.  # noqa: E501

        Smart threshold.  # noqa: E501

        :return: The threshold of this NimbleDiskSmartAttributes.  # noqa: E501
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this NimbleDiskSmartAttributes.

        Smart threshold.  # noqa: E501

        :param threshold: The threshold of this NimbleDiskSmartAttributes.  # noqa: E501
        :type: int
        """

        self._threshold = threshold

    @property
    def worst_value(self):
        """Gets the worst_value of this NimbleDiskSmartAttributes.  # noqa: E501

        Worst value.  # noqa: E501

        :return: The worst_value of this NimbleDiskSmartAttributes.  # noqa: E501
        :rtype: int
        """
        return self._worst_value

    @worst_value.setter
    def worst_value(self, worst_value):
        """Sets the worst_value of this NimbleDiskSmartAttributes.

        Worst value.  # noqa: E501

        :param worst_value: The worst_value of this NimbleDiskSmartAttributes.  # noqa: E501
        :type: int
        """

        self._worst_value = worst_value

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
        if not isinstance(other, NimbleDiskSmartAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other