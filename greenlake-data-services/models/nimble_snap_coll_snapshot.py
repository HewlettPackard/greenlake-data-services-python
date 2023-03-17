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


class NimbleSnapCollSnapshot(object):
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
        'expiry_time': 'int',
        'id': 'str',
        'name': 'str',
        'schedule_id': 'str',
        'schedule_name': 'str',
        'snap_collection_id': 'str',
        'snap_collection_name': 'str',
        'vol_id': 'str',
        'vol_name': 'str'
    }

    attribute_map = {
        'expiry_time': 'expiry_time',
        'id': 'id',
        'name': 'name',
        'schedule_id': 'schedule_id',
        'schedule_name': 'schedule_name',
        'snap_collection_id': 'snap_collection_id',
        'snap_collection_name': 'snap_collection_name',
        'vol_id': 'vol_id',
        'vol_name': 'vol_name'
    }

    def __init__(self, expiry_time=None, id=None, name=None, schedule_id=None, schedule_name=None, snap_collection_id=None, snap_collection_name=None, vol_id=None, vol_name=None):  # noqa: E501
        """NimbleSnapCollSnapshot - a model defined in OpenAPI"""  # noqa: E501

        self._expiry_time = None
        self._id = None
        self._name = None
        self._schedule_id = None
        self._schedule_name = None
        self._snap_collection_id = None
        self._snap_collection_name = None
        self._vol_id = None
        self._vol_name = None
        self.discriminator = None

        if expiry_time is not None:
            self.expiry_time = expiry_time
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if schedule_id is not None:
            self.schedule_id = schedule_id
        if schedule_name is not None:
            self.schedule_name = schedule_name
        if snap_collection_id is not None:
            self.snap_collection_id = snap_collection_id
        if snap_collection_name is not None:
            self.snap_collection_name = snap_collection_name
        if vol_id is not None:
            self.vol_id = vol_id
        if vol_name is not None:
            self.vol_name = vol_name

    @property
    def expiry_time(self):
        """Gets the expiry_time of this NimbleSnapCollSnapshot.  # noqa: E501

        Unix timestamp indicating that the snapshot is considered expired by Snapshot Time-to-live(TTL). A value of 0 indicates that snapshot never expires. Seconds since last epoch i.e. 00:00 January 1, 1970.  # noqa: E501

        :return: The expiry_time of this NimbleSnapCollSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, expiry_time):
        """Sets the expiry_time of this NimbleSnapCollSnapshot.

        Unix timestamp indicating that the snapshot is considered expired by Snapshot Time-to-live(TTL). A value of 0 indicates that snapshot never expires. Seconds since last epoch i.e. 00:00 January 1, 1970.  # noqa: E501

        :param expiry_time: The expiry_time of this NimbleSnapCollSnapshot.  # noqa: E501
        :type: int
        """

        self._expiry_time = expiry_time

    @property
    def id(self):
        """Gets the id of this NimbleSnapCollSnapshot.  # noqa: E501

        Identifier for the snapshot. A 42 digit hexadecimal number.  # noqa: E501

        :return: The id of this NimbleSnapCollSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NimbleSnapCollSnapshot.

        Identifier for the snapshot. A 42 digit hexadecimal number.  # noqa: E501

        :param id: The id of this NimbleSnapCollSnapshot.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NimbleSnapCollSnapshot.  # noqa: E501

        Name of snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period.  # noqa: E501

        :return: The name of this NimbleSnapCollSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NimbleSnapCollSnapshot.

        Name of snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period.  # noqa: E501

        :param name: The name of this NimbleSnapCollSnapshot.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def schedule_id(self):
        """Gets the schedule_id of this NimbleSnapCollSnapshot.  # noqa: E501

        Identifier of protection schedule. A 42 digit hexadecimal number.  # noqa: E501

        :return: The schedule_id of this NimbleSnapCollSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """Sets the schedule_id of this NimbleSnapCollSnapshot.

        Identifier of protection schedule. A 42 digit hexadecimal number.  # noqa: E501

        :param schedule_id: The schedule_id of this NimbleSnapCollSnapshot.  # noqa: E501
        :type: str
        """

        self._schedule_id = schedule_id

    @property
    def schedule_name(self):
        """Gets the schedule_name of this NimbleSnapCollSnapshot.  # noqa: E501

        Name of protection schedule. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The schedule_name of this NimbleSnapCollSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._schedule_name

    @schedule_name.setter
    def schedule_name(self, schedule_name):
        """Sets the schedule_name of this NimbleSnapCollSnapshot.

        Name of protection schedule. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param schedule_name: The schedule_name of this NimbleSnapCollSnapshot.  # noqa: E501
        :type: str
        """

        self._schedule_name = schedule_name

    @property
    def snap_collection_id(self):
        """Gets the snap_collection_id of this NimbleSnapCollSnapshot.  # noqa: E501

        Identifier of snapshot collection. A 42 digit hexadecimal number.  # noqa: E501

        :return: The snap_collection_id of this NimbleSnapCollSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._snap_collection_id

    @snap_collection_id.setter
    def snap_collection_id(self, snap_collection_id):
        """Sets the snap_collection_id of this NimbleSnapCollSnapshot.

        Identifier of snapshot collection. A 42 digit hexadecimal number.  # noqa: E501

        :param snap_collection_id: The snap_collection_id of this NimbleSnapCollSnapshot.  # noqa: E501
        :type: str
        """

        self._snap_collection_id = snap_collection_id

    @property
    def snap_collection_name(self):
        """Gets the snap_collection_name of this NimbleSnapCollSnapshot.  # noqa: E501

        Name of snapshot collection. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints.  # noqa: E501

        :return: The snap_collection_name of this NimbleSnapCollSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._snap_collection_name

    @snap_collection_name.setter
    def snap_collection_name(self, snap_collection_name):
        """Sets the snap_collection_name of this NimbleSnapCollSnapshot.

        Name of snapshot collection. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints.  # noqa: E501

        :param snap_collection_name: The snap_collection_name of this NimbleSnapCollSnapshot.  # noqa: E501
        :type: str
        """

        self._snap_collection_name = snap_collection_name

    @property
    def vol_id(self):
        """Gets the vol_id of this NimbleSnapCollSnapshot.  # noqa: E501

        Parent volume ID. A 42 digit hexadecimal number.  # noqa: E501

        :return: The vol_id of this NimbleSnapCollSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._vol_id

    @vol_id.setter
    def vol_id(self, vol_id):
        """Sets the vol_id of this NimbleSnapCollSnapshot.

        Parent volume ID. A 42 digit hexadecimal number.  # noqa: E501

        :param vol_id: The vol_id of this NimbleSnapCollSnapshot.  # noqa: E501
        :type: str
        """

        self._vol_id = vol_id

    @property
    def vol_name(self):
        """Gets the vol_name of this NimbleSnapCollSnapshot.  # noqa: E501

        Name of the parent volume in which the snapshot belongs to. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints.  # noqa: E501

        :return: The vol_name of this NimbleSnapCollSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._vol_name

    @vol_name.setter
    def vol_name(self, vol_name):
        """Sets the vol_name of this NimbleSnapCollSnapshot.

        Name of the parent volume in which the snapshot belongs to. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints.  # noqa: E501

        :param vol_name: The vol_name of this NimbleSnapCollSnapshot.  # noqa: E501
        :type: str
        """

        self._vol_name = vol_name

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
        if not isinstance(other, NimbleSnapCollSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other