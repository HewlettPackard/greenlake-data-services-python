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


class SnapshotFromVolume(object):
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
        'name': 'str',
        'snap_id': 'str',
        'snap_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'snap_id': 'snap_id',
        'snap_name': 'snap_name'
    }

    def __init__(self, id=None, name=None, snap_id=None, snap_name=None):  # noqa: E501
        """SnapshotFromVolume - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._snap_id = None
        self._snap_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if snap_id is not None:
            self.snap_id = snap_id
        if snap_name is not None:
            self.snap_name = snap_name

    @property
    def id(self):
        """Gets the id of this SnapshotFromVolume.  # noqa: E501

        ID of snapshot.  # noqa: E501

        :return: The id of this SnapshotFromVolume.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotFromVolume.

        ID of snapshot.  # noqa: E501

        :param id: The id of this SnapshotFromVolume.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SnapshotFromVolume.  # noqa: E501

        Snapshot name.  # noqa: E501

        :return: The name of this SnapshotFromVolume.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotFromVolume.

        Snapshot name.  # noqa: E501

        :param name: The name of this SnapshotFromVolume.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def snap_id(self):
        """Gets the snap_id of this SnapshotFromVolume.  # noqa: E501

        ID of snapshot.  # noqa: E501

        :return: The snap_id of this SnapshotFromVolume.  # noqa: E501
        :rtype: str
        """
        return self._snap_id

    @snap_id.setter
    def snap_id(self, snap_id):
        """Sets the snap_id of this SnapshotFromVolume.

        ID of snapshot.  # noqa: E501

        :param snap_id: The snap_id of this SnapshotFromVolume.  # noqa: E501
        :type: str
        """

        self._snap_id = snap_id

    @property
    def snap_name(self):
        """Gets the snap_name of this SnapshotFromVolume.  # noqa: E501

        Snapshot name.  # noqa: E501

        :return: The snap_name of this SnapshotFromVolume.  # noqa: E501
        :rtype: str
        """
        return self._snap_name

    @snap_name.setter
    def snap_name(self, snap_name):
        """Sets the snap_name of this SnapshotFromVolume.

        Snapshot name.  # noqa: E501

        :param snap_name: The snap_name of this SnapshotFromVolume.  # noqa: E501
        :type: str
        """

        self._snap_name = snap_name

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
        if not isinstance(other, SnapshotFromVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other