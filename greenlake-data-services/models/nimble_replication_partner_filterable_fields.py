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


class NimbleReplicationPartnerFilterableFields(object):
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
        'array_serial': 'str',
        'cfg_sync_status': 'str',
        'creation_time': 'int',
        'folder_id': 'str',
        'folder_name': 'str',
        'hostname': 'str',
        'id': 'str',
        'is_alive': 'bool',
        'name': 'str',
        'partner_type': 'str',
        'paused': 'bool',
        'pool_id': 'str',
        'pool_name': 'str',
        'repl_hostname': 'str',
        'subnet_label': 'str',
        'subnet_netmask': 'str',
        'subnet_network': 'str',
        'subnet_type': 'str',
        'system_id': 'str',
        'version': 'int',
        'volume_collection_list_count': 'int'
    }

    attribute_map = {
        'array_serial': 'array_serial',
        'cfg_sync_status': 'cfg_sync_status',
        'creation_time': 'creation_time',
        'folder_id': 'folder_id',
        'folder_name': 'folder_name',
        'hostname': 'hostname',
        'id': 'id',
        'is_alive': 'is_alive',
        'name': 'name',
        'partner_type': 'partner_type',
        'paused': 'paused',
        'pool_id': 'pool_id',
        'pool_name': 'pool_name',
        'repl_hostname': 'repl_hostname',
        'subnet_label': 'subnet_label',
        'subnet_netmask': 'subnet_netmask',
        'subnet_network': 'subnet_network',
        'subnet_type': 'subnet_type',
        'system_id': 'systemId',
        'version': 'version',
        'volume_collection_list_count': 'volume_collection_list_count'
    }

    def __init__(self, array_serial=None, cfg_sync_status=None, creation_time=None, folder_id=None, folder_name=None, hostname=None, id=None, is_alive=None, name=None, partner_type=None, paused=None, pool_id=None, pool_name=None, repl_hostname=None, subnet_label=None, subnet_netmask=None, subnet_network=None, subnet_type=None, system_id=None, version=None, volume_collection_list_count=None):  # noqa: E501
        """NimbleReplicationPartnerFilterableFields - a model defined in OpenAPI"""  # noqa: E501

        self._array_serial = None
        self._cfg_sync_status = None
        self._creation_time = None
        self._folder_id = None
        self._folder_name = None
        self._hostname = None
        self._id = None
        self._is_alive = None
        self._name = None
        self._partner_type = None
        self._paused = None
        self._pool_id = None
        self._pool_name = None
        self._repl_hostname = None
        self._subnet_label = None
        self._subnet_netmask = None
        self._subnet_network = None
        self._subnet_type = None
        self._system_id = None
        self._version = None
        self._volume_collection_list_count = None
        self.discriminator = None

        if array_serial is not None:
            self.array_serial = array_serial
        if cfg_sync_status is not None:
            self.cfg_sync_status = cfg_sync_status
        if creation_time is not None:
            self.creation_time = creation_time
        if folder_id is not None:
            self.folder_id = folder_id
        if folder_name is not None:
            self.folder_name = folder_name
        if hostname is not None:
            self.hostname = hostname
        if id is not None:
            self.id = id
        if is_alive is not None:
            self.is_alive = is_alive
        if name is not None:
            self.name = name
        if partner_type is not None:
            self.partner_type = partner_type
        if paused is not None:
            self.paused = paused
        if pool_id is not None:
            self.pool_id = pool_id
        if pool_name is not None:
            self.pool_name = pool_name
        if repl_hostname is not None:
            self.repl_hostname = repl_hostname
        if subnet_label is not None:
            self.subnet_label = subnet_label
        if subnet_netmask is not None:
            self.subnet_netmask = subnet_netmask
        if subnet_network is not None:
            self.subnet_network = subnet_network
        if subnet_type is not None:
            self.subnet_type = subnet_type
        if system_id is not None:
            self.system_id = system_id
        if version is not None:
            self.version = version
        if volume_collection_list_count is not None:
            self.volume_collection_list_count = volume_collection_list_count

    @property
    def array_serial(self):
        """Gets the array_serial of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Serial number of group leader array of the partner. Plain string. `Filter, Sort`  # noqa: E501

        :return: The array_serial of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._array_serial

    @array_serial.setter
    def array_serial(self, array_serial):
        """Sets the array_serial of this NimbleReplicationPartnerFilterableFields.

        Serial number of group leader array of the partner. Plain string. `Filter, Sort`  # noqa: E501

        :param array_serial: The array_serial of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._array_serial = array_serial

    @property
    def cfg_sync_status(self):
        """Gets the cfg_sync_status of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Indicates whether all volumes and volume collections have been synced to the partner. Possible values: N/A, Yes, No `Filter, Sort`  # noqa: E501

        :return: The cfg_sync_status of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._cfg_sync_status

    @cfg_sync_status.setter
    def cfg_sync_status(self, cfg_sync_status):
        """Sets the cfg_sync_status of this NimbleReplicationPartnerFilterableFields.

        Indicates whether all volumes and volume collections have been synced to the partner. Possible values: N/A, Yes, No `Filter, Sort`  # noqa: E501

        :param cfg_sync_status: The cfg_sync_status of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._cfg_sync_status = cfg_sync_status

    @property
    def creation_time(self):
        """Gets the creation_time of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Time when this replication partner was created. Seconds since last epoch i.e. 00:00 January 1, 1970. `Filter, Sort`  # noqa: E501

        :return: The creation_time of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this NimbleReplicationPartnerFilterableFields.

        Time when this replication partner was created. Seconds since last epoch i.e. 00:00 January 1, 1970. `Filter, Sort`  # noqa: E501

        :param creation_time: The creation_time of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: int
        """

        self._creation_time = creation_time

    @property
    def folder_id(self):
        """Gets the folder_id of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        The Folder ID within the pool where volumes replicated from this partner will be created. This is not supported for pool partners. A 42 digit hexadecimal number. `Filter, Sort`  # noqa: E501

        :return: The folder_id of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this NimbleReplicationPartnerFilterableFields.

        The Folder ID within the pool where volumes replicated from this partner will be created. This is not supported for pool partners. A 42 digit hexadecimal number. `Filter, Sort`  # noqa: E501

        :param folder_id: The folder_id of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def folder_name(self):
        """Gets the folder_name of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        The Folder name within the pool where volumes replicated from this partner will be created. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. `Filter, Sort`  # noqa: E501

        :return: The folder_name of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this NimbleReplicationPartnerFilterableFields.

        The Folder name within the pool where volumes replicated from this partner will be created. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. `Filter, Sort`  # noqa: E501

        :param folder_name: The folder_name of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._folder_name = folder_name

    @property
    def hostname(self):
        """Gets the hostname of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        IP address or hostname of partner interface. This must be the partners Group Management IP address. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. `Filter, Sort`  # noqa: E501

        :return: The hostname of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this NimbleReplicationPartnerFilterableFields.

        IP address or hostname of partner interface. This must be the partners Group Management IP address. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. `Filter, Sort`  # noqa: E501

        :param hostname: The hostname of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def id(self):
        """Gets the id of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Identifier for a replication partner. A 42 digit hexadecimal number. `Filter`  # noqa: E501

        :return: The id of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NimbleReplicationPartnerFilterableFields.

        Identifier for a replication partner. A 42 digit hexadecimal number. `Filter`  # noqa: E501

        :param id: The id of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_alive(self):
        """Gets the is_alive of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Whether the partner is available, and responding to pings. Possible values: true, false `Filter, Sort`  # noqa: E501

        :return: The is_alive of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: bool
        """
        return self._is_alive

    @is_alive.setter
    def is_alive(self, is_alive):
        """Sets the is_alive of this NimbleReplicationPartnerFilterableFields.

        Whether the partner is available, and responding to pings. Possible values: true, false `Filter, Sort`  # noqa: E501

        :param is_alive: The is_alive of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: bool
        """

        self._is_alive = is_alive

    @property
    def name(self):
        """Gets the name of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Name of replication partner. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.`Filter, Sort`  # noqa: E501

        :return: The name of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NimbleReplicationPartnerFilterableFields.

        Name of replication partner. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.`Filter, Sort`  # noqa: E501

        :param name: The name of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def partner_type(self):
        """Gets the partner_type of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Type of the partner, Possible values: 'group' or 'pool'.`Filter, Sort`  # noqa: E501

        :return: The partner_type of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._partner_type

    @partner_type.setter
    def partner_type(self, partner_type):
        """Sets the partner_type of this NimbleReplicationPartnerFilterableFields.

        Type of the partner, Possible values: 'group' or 'pool'.`Filter, Sort`  # noqa: E501

        :param partner_type: The partner_type of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._partner_type = partner_type

    @property
    def paused(self):
        """Gets the paused of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Indicates whether replication traffic from/to this partner has been halted. Possible values: true, false `Filter, Sort`  # noqa: E501

        :return: The paused of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this NimbleReplicationPartnerFilterableFields.

        Indicates whether replication traffic from/to this partner has been halted. Possible values: true, false `Filter, Sort`  # noqa: E501

        :param paused: The paused of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: bool
        """

        self._paused = paused

    @property
    def pool_id(self):
        """Gets the pool_id of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        The pool ID where volumes replicated from this partner will be created. Replica volumes created as clones ignore this parameter and are always created in the same pool as their parent volume. A 42 digit hexadecimal number. `Filter, Sort`  # noqa: E501

        :return: The pool_id of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this NimbleReplicationPartnerFilterableFields.

        The pool ID where volumes replicated from this partner will be created. Replica volumes created as clones ignore this parameter and are always created in the same pool as their parent volume. A 42 digit hexadecimal number. `Filter, Sort`  # noqa: E501

        :param pool_id: The pool_id of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._pool_id = pool_id

    @property
    def pool_name(self):
        """Gets the pool_name of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        The pool name where volumes replicated from this partner will be created. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. `Filter, Sort`  # noqa: E501

        :return: The pool_name of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        """Sets the pool_name of this NimbleReplicationPartnerFilterableFields.

        The pool name where volumes replicated from this partner will be created. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. `Filter, Sort`  # noqa: E501

        :param pool_name: The pool_name of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._pool_name = pool_name

    @property
    def repl_hostname(self):
        """Gets the repl_hostname of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        IP address or hostname of partner data interface. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. `Filter, Sort`  # noqa: E501

        :return: The repl_hostname of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._repl_hostname

    @repl_hostname.setter
    def repl_hostname(self, repl_hostname):
        """Sets the repl_hostname of this NimbleReplicationPartnerFilterableFields.

        IP address or hostname of partner data interface. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. `Filter, Sort`  # noqa: E501

        :param repl_hostname: The repl_hostname of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._repl_hostname = repl_hostname

    @property
    def subnet_label(self):
        """Gets the subnet_label of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Label of the subnet used to replicate to this partner. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. `Filter, Sort`  # noqa: E501

        :return: The subnet_label of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._subnet_label

    @subnet_label.setter
    def subnet_label(self, subnet_label):
        """Sets the subnet_label of this NimbleReplicationPartnerFilterableFields.

        Label of the subnet used to replicate to this partner. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. `Filter, Sort`  # noqa: E501

        :param subnet_label: The subnet_label of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._subnet_label = subnet_label

    @property
    def subnet_netmask(self):
        """Gets the subnet_netmask of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Subnet mask used to replicate to this partner. A netmask expressed as a 32 bit binary value must have the highest bit set (2^31) and the lowest bit clear (2^0) with the first zero followed by only zeros. `Filter, Sort`  # noqa: E501

        :return: The subnet_netmask of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._subnet_netmask

    @subnet_netmask.setter
    def subnet_netmask(self, subnet_netmask):
        """Sets the subnet_netmask of this NimbleReplicationPartnerFilterableFields.

        Subnet mask used to replicate to this partner. A netmask expressed as a 32 bit binary value must have the highest bit set (2^31) and the lowest bit clear (2^0) with the first zero followed by only zeros. `Filter, Sort`  # noqa: E501

        :param subnet_netmask: The subnet_netmask of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._subnet_netmask = subnet_netmask

    @property
    def subnet_network(self):
        """Gets the subnet_network of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Subnet used to replicate to this partner. Four numbers in the range [0,255] separated by periods. `Filter, Sort`  # noqa: E501

        :return: The subnet_network of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._subnet_network

    @subnet_network.setter
    def subnet_network(self, subnet_network):
        """Sets the subnet_network of this NimbleReplicationPartnerFilterableFields.

        Subnet used to replicate to this partner. Four numbers in the range [0,255] separated by periods. `Filter, Sort`  # noqa: E501

        :param subnet_network: The subnet_network of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._subnet_network = subnet_network

    @property
    def subnet_type(self):
        """Gets the subnet_type of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Type of the subnet used to replicate to this partner. Possible values: invalid, unconfigured, mgmt, data, mgmt_data `Filter, Sort`  # noqa: E501

        :return: The subnet_type of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._subnet_type

    @subnet_type.setter
    def subnet_type(self, subnet_type):
        """Sets the subnet_type of this NimbleReplicationPartnerFilterableFields.

        Type of the subnet used to replicate to this partner. Possible values: invalid, unconfigured, mgmt, data, mgmt_data `Filter, Sort`  # noqa: E501

        :param subnet_type: The subnet_type of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._subnet_type = subnet_type

    @property
    def system_id(self):
        """Gets the system_id of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Identifier for a system or array. A 42 digit hexadecimal number. `Filter`  # noqa: E501

        :return: The system_id of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this NimbleReplicationPartnerFilterableFields.

        Identifier for a system or array. A 42 digit hexadecimal number. `Filter`  # noqa: E501

        :param system_id: The system_id of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def version(self):
        """Gets the version of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Replication version of the partner. Signed 64-bit integer. `Filter, Sort`  # noqa: E501

        :return: The version of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NimbleReplicationPartnerFilterableFields.

        Replication version of the partner. Signed 64-bit integer. `Filter, Sort`  # noqa: E501

        :param version: The version of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def volume_collection_list_count(self):
        """Gets the volume_collection_list_count of this NimbleReplicationPartnerFilterableFields.  # noqa: E501

        Count of volume collections that are replicating from/to this partner. Unsigned 64-bit integer. `Filter, Sort`  # noqa: E501

        :return: The volume_collection_list_count of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :rtype: int
        """
        return self._volume_collection_list_count

    @volume_collection_list_count.setter
    def volume_collection_list_count(self, volume_collection_list_count):
        """Sets the volume_collection_list_count of this NimbleReplicationPartnerFilterableFields.

        Count of volume collections that are replicating from/to this partner. Unsigned 64-bit integer. `Filter, Sort`  # noqa: E501

        :param volume_collection_list_count: The volume_collection_list_count of this NimbleReplicationPartnerFilterableFields.  # noqa: E501
        :type: int
        """

        self._volume_collection_list_count = volume_collection_list_count

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
        if not isinstance(other, NimbleReplicationPartnerFilterableFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
