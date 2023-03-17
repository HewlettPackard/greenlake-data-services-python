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


class NimbleCreateSnapshotInput(object):
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
        'app_uuid': 'str',
        'description': 'str',
        'metadata': 'list[KeyValue]',
        'name': 'str',
        'online': 'bool',
        'writable': 'bool'
    }

    attribute_map = {
        'app_uuid': 'app_uuid',
        'description': 'description',
        'metadata': 'metadata',
        'name': 'name',
        'online': 'online',
        'writable': 'writable'
    }

    def __init__(self, app_uuid=None, description=None, metadata=None, name=None, online=None, writable=None):  # noqa: E501
        """NimbleCreateSnapshotInput - a model defined in OpenAPI"""  # noqa: E501

        self._app_uuid = None
        self._description = None
        self._metadata = None
        self._name = None
        self._online = None
        self._writable = None
        self.discriminator = None

        if app_uuid is not None:
            self.app_uuid = app_uuid
        if description is not None:
            self.description = description
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        if online is not None:
            self.online = online
        if writable is not None:
            self.writable = writable

    @property
    def app_uuid(self):
        """Gets the app_uuid of this NimbleCreateSnapshotInput.  # noqa: E501

        Application identifier of snapshots. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. Defaults to empty string.  # noqa: E501

        :return: The app_uuid of this NimbleCreateSnapshotInput.  # noqa: E501
        :rtype: str
        """
        return self._app_uuid

    @app_uuid.setter
    def app_uuid(self, app_uuid):
        """Sets the app_uuid of this NimbleCreateSnapshotInput.

        Application identifier of snapshots. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. Defaults to empty string.  # noqa: E501

        :param app_uuid: The app_uuid of this NimbleCreateSnapshotInput.  # noqa: E501
        :type: str
        """

        self._app_uuid = app_uuid

    @property
    def description(self):
        """Gets the description of this NimbleCreateSnapshotInput.  # noqa: E501

        Text description of snapshot. String of up to 255 printable ASCII characters. Defaults to the empty string.  # noqa: E501

        :return: The description of this NimbleCreateSnapshotInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NimbleCreateSnapshotInput.

        Text description of snapshot. String of up to 255 printable ASCII characters. Defaults to the empty string.  # noqa: E501

        :param description: The description of this NimbleCreateSnapshotInput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def metadata(self):
        """Gets the metadata of this NimbleCreateSnapshotInput.  # noqa: E501

        Key-value pairs that augment a volume's attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. Defaults to an empty array.  # noqa: E501

        :return: The metadata of this NimbleCreateSnapshotInput.  # noqa: E501
        :rtype: list[KeyValue]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NimbleCreateSnapshotInput.

        Key-value pairs that augment a volume's attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. Defaults to an empty array.  # noqa: E501

        :param metadata: The metadata of this NimbleCreateSnapshotInput.  # noqa: E501
        :type: list[KeyValue]
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this NimbleCreateSnapshotInput.  # noqa: E501

        Name of the snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints.  # noqa: E501

        :return: The name of this NimbleCreateSnapshotInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NimbleCreateSnapshotInput.

        Name of the snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints.  # noqa: E501

        :param name: The name of this NimbleCreateSnapshotInput.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def online(self):
        """Gets the online of this NimbleCreateSnapshotInput.  # noqa: E501

        Online state for a snapshot means it could be mounted for data restore. Defaults to 'false'.  # noqa: E501

        :return: The online of this NimbleCreateSnapshotInput.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this NimbleCreateSnapshotInput.

        Online state for a snapshot means it could be mounted for data restore. Defaults to 'false'.  # noqa: E501

        :param online: The online of this NimbleCreateSnapshotInput.  # noqa: E501
        :type: bool
        """

        self._online = online

    @property
    def writable(self):
        """Gets the writable of this NimbleCreateSnapshotInput.  # noqa: E501

        Allow snapshot to be writable. Mandatory and must be set to 'true' for VSS application synchronized snapshots. Defaults to 'false'.  # noqa: E501

        :return: The writable of this NimbleCreateSnapshotInput.  # noqa: E501
        :rtype: bool
        """
        return self._writable

    @writable.setter
    def writable(self, writable):
        """Sets the writable of this NimbleCreateSnapshotInput.

        Allow snapshot to be writable. Mandatory and must be set to 'true' for VSS application synchronized snapshots. Defaults to 'false'.  # noqa: E501

        :param writable: The writable of this NimbleCreateSnapshotInput.  # noqa: E501
        :type: bool
        """

        self._writable = writable

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
        if not isinstance(other, NimbleCreateSnapshotInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
