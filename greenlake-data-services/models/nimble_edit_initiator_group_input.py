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


class NimbleEditInitiatorGroupInput(object):
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
        'fc_initiators': 'list[NimbleFCInitiator]',
        'fc_tdz_ports': 'list[NimbleFCTdzPorts]',
        'host_type': 'str',
        'iscsi_initiators': 'list[NimbleISCSIInitiator]',
        'metadata': 'list[NimbleMetadata]',
        'name': 'str',
        'target_subnets': 'list[NimbleTargetSubnets]'
    }

    attribute_map = {
        'app_uuid': 'app_uuid',
        'description': 'description',
        'fc_initiators': 'fc_initiators',
        'fc_tdz_ports': 'fc_tdz_ports',
        'host_type': 'host_type',
        'iscsi_initiators': 'iscsi_initiators',
        'metadata': 'metadata',
        'name': 'name',
        'target_subnets': 'target_subnets'
    }

    def __init__(self, app_uuid=None, description=None, fc_initiators=None, fc_tdz_ports=None, host_type=None, iscsi_initiators=None, metadata=None, name=None, target_subnets=None):  # noqa: E501
        """NimbleEditInitiatorGroupInput - a model defined in OpenAPI"""  # noqa: E501

        self._app_uuid = None
        self._description = None
        self._fc_initiators = None
        self._fc_tdz_ports = None
        self._host_type = None
        self._iscsi_initiators = None
        self._metadata = None
        self._name = None
        self._target_subnets = None
        self.discriminator = None

        if app_uuid is not None:
            self.app_uuid = app_uuid
        if description is not None:
            self.description = description
        if fc_initiators is not None:
            self.fc_initiators = fc_initiators
        if fc_tdz_ports is not None:
            self.fc_tdz_ports = fc_tdz_ports
        if host_type is not None:
            self.host_type = host_type
        if iscsi_initiators is not None:
            self.iscsi_initiators = iscsi_initiators
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if target_subnets is not None:
            self.target_subnets = target_subnets

    @property
    def app_uuid(self):
        """Gets the app_uuid of this NimbleEditInitiatorGroupInput.  # noqa: E501

        Application identifier of initiator group. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed.  # noqa: E501

        :return: The app_uuid of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :rtype: str
        """
        return self._app_uuid

    @app_uuid.setter
    def app_uuid(self, app_uuid):
        """Sets the app_uuid of this NimbleEditInitiatorGroupInput.

        Application identifier of initiator group. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed.  # noqa: E501

        :param app_uuid: The app_uuid of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :type: str
        """

        self._app_uuid = app_uuid

    @property
    def description(self):
        """Gets the description of this NimbleEditInitiatorGroupInput.  # noqa: E501

        Text description of initiator group. String of up to 255 printable ASCII characters.  # noqa: E501

        :return: The description of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NimbleEditInitiatorGroupInput.

        Text description of initiator group. String of up to 255 printable ASCII characters.  # noqa: E501

        :param description: The description of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def fc_initiators(self):
        """Gets the fc_initiators of this NimbleEditInitiatorGroupInput.  # noqa: E501

        List of FC initiators. When create/update fc_initiators, wwpn is required. List of Fibre Channel initiators.  # noqa: E501

        :return: The fc_initiators of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :rtype: list[NimbleFCInitiator]
        """
        return self._fc_initiators

    @fc_initiators.setter
    def fc_initiators(self, fc_initiators):
        """Sets the fc_initiators of this NimbleEditInitiatorGroupInput.

        List of FC initiators. When create/update fc_initiators, wwpn is required. List of Fibre Channel initiators.  # noqa: E501

        :param fc_initiators: The fc_initiators of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :type: list[NimbleFCInitiator]
        """

        self._fc_initiators = fc_initiators

    @property
    def fc_tdz_ports(self):
        """Gets the fc_tdz_ports of this NimbleEditInitiatorGroupInput.  # noqa: E501

        List of target Fibre Channel ports with Target Driven Zoning configured on this initiator group. List of target ports.  # noqa: E501

        :return: The fc_tdz_ports of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :rtype: list[NimbleFCTdzPorts]
        """
        return self._fc_tdz_ports

    @fc_tdz_ports.setter
    def fc_tdz_ports(self, fc_tdz_ports):
        """Sets the fc_tdz_ports of this NimbleEditInitiatorGroupInput.

        List of target Fibre Channel ports with Target Driven Zoning configured on this initiator group. List of target ports.  # noqa: E501

        :param fc_tdz_ports: The fc_tdz_ports of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :type: list[NimbleFCTdzPorts]
        """

        self._fc_tdz_ports = fc_tdz_ports

    @property
    def host_type(self):
        """Gets the host_type of this NimbleEditInitiatorGroupInput.  # noqa: E501

        Initiator group host type. Available options are auto and hpux. The default option is auto. This attribute will be applied to all the initiators in the initiator group. Initiators with different host OSes should not be kept in the same initiator group having a non-default host type attribute. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The host_type of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this NimbleEditInitiatorGroupInput.

        Initiator group host type. Available options are auto and hpux. The default option is auto. This attribute will be applied to all the initiators in the initiator group. Initiators with different host OSes should not be kept in the same initiator group having a non-default host type attribute. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param host_type: The host_type of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :type: str
        """

        self._host_type = host_type

    @property
    def iscsi_initiators(self):
        """Gets the iscsi_initiators of this NimbleEditInitiatorGroupInput.  # noqa: E501

        List of iSCSI initiators. When create/update iscsi_initiators, either iqn or ip_address is always required with label.  # noqa: E501

        :return: The iscsi_initiators of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :rtype: list[NimbleISCSIInitiator]
        """
        return self._iscsi_initiators

    @iscsi_initiators.setter
    def iscsi_initiators(self, iscsi_initiators):
        """Sets the iscsi_initiators of this NimbleEditInitiatorGroupInput.

        List of iSCSI initiators. When create/update iscsi_initiators, either iqn or ip_address is always required with label.  # noqa: E501

        :param iscsi_initiators: The iscsi_initiators of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :type: list[NimbleISCSIInitiator]
        """

        self._iscsi_initiators = iscsi_initiators

    @property
    def metadata(self):
        """Gets the metadata of this NimbleEditInitiatorGroupInput.  # noqa: E501

        Key-value pairs that augment an initiator group's attributes.  # noqa: E501

        :return: The metadata of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :rtype: list[NimbleMetadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NimbleEditInitiatorGroupInput.

        Key-value pairs that augment an initiator group's attributes.  # noqa: E501

        :param metadata: The metadata of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :type: list[NimbleMetadata]
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this NimbleEditInitiatorGroupInput.  # noqa: E501

        Name of initiator group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The name of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NimbleEditInitiatorGroupInput.

        Name of initiator group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param name: The name of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def target_subnets(self):
        """Gets the target_subnets of this NimbleEditInitiatorGroupInput.  # noqa: E501

        List of target subnet labels. If specified, discovery and access to volumes will be restricted to to the specified subnets. List of target subnet tables.  # noqa: E501

        :return: The target_subnets of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :rtype: list[NimbleTargetSubnets]
        """
        return self._target_subnets

    @target_subnets.setter
    def target_subnets(self, target_subnets):
        """Sets the target_subnets of this NimbleEditInitiatorGroupInput.

        List of target subnet labels. If specified, discovery and access to volumes will be restricted to to the specified subnets. List of target subnet tables.  # noqa: E501

        :param target_subnets: The target_subnets of this NimbleEditInitiatorGroupInput.  # noqa: E501
        :type: list[NimbleTargetSubnets]
        """

        self._target_subnets = target_subnets

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
        if not isinstance(other, NimbleEditInitiatorGroupInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
