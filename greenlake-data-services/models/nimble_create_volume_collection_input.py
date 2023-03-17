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


class NimbleCreateVolumeCollectionInput(object):
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
        'agent_hostname': 'str',
        'agent_username': 'str',
        'app_cluster_name': 'str',
        'app_id': 'str',
        'app_server': 'str',
        'app_service_name': 'str',
        'app_sync': 'str',
        'description': 'str',
        'is_standalone_volcoll': 'bool',
        'metadata': 'list[KeyValue]',
        'name': 'str',
        'prottmpl_id': 'str',
        'replication_type': 'str',
        'vcenter_hostname': 'str',
        'vcenter_username': 'str',
        'volume_list': 'list[str]'
    }

    attribute_map = {
        'agent_hostname': 'agent_hostname',
        'agent_username': 'agent_username',
        'app_cluster_name': 'app_cluster_name',
        'app_id': 'app_id',
        'app_server': 'app_server',
        'app_service_name': 'app_service_name',
        'app_sync': 'app_sync',
        'description': 'description',
        'is_standalone_volcoll': 'is_standalone_volcoll',
        'metadata': 'metadata',
        'name': 'name',
        'prottmpl_id': 'prottmpl_id',
        'replication_type': 'replication_type',
        'vcenter_hostname': 'vcenter_hostname',
        'vcenter_username': 'vcenter_username',
        'volume_list': 'volume_list'
    }

    def __init__(self, agent_hostname=None, agent_username=None, app_cluster_name=None, app_id=None, app_server=None, app_service_name=None, app_sync=None, description=None, is_standalone_volcoll=None, metadata=None, name=None, prottmpl_id=None, replication_type=None, vcenter_hostname=None, vcenter_username=None, volume_list=None):  # noqa: E501
        """NimbleCreateVolumeCollectionInput - a model defined in OpenAPI"""  # noqa: E501

        self._agent_hostname = None
        self._agent_username = None
        self._app_cluster_name = None
        self._app_id = None
        self._app_server = None
        self._app_service_name = None
        self._app_sync = None
        self._description = None
        self._is_standalone_volcoll = None
        self._metadata = None
        self._name = None
        self._prottmpl_id = None
        self._replication_type = None
        self._vcenter_hostname = None
        self._vcenter_username = None
        self._volume_list = None
        self.discriminator = None

        if agent_hostname is not None:
            self.agent_hostname = agent_hostname
        if agent_username is not None:
            self.agent_username = agent_username
        if app_cluster_name is not None:
            self.app_cluster_name = app_cluster_name
        if app_id is not None:
            self.app_id = app_id
        if app_server is not None:
            self.app_server = app_server
        if app_service_name is not None:
            self.app_service_name = app_service_name
        if app_sync is not None:
            self.app_sync = app_sync
        if description is not None:
            self.description = description
        if is_standalone_volcoll is not None:
            self.is_standalone_volcoll = is_standalone_volcoll
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        if prottmpl_id is not None:
            self.prottmpl_id = prottmpl_id
        if replication_type is not None:
            self.replication_type = replication_type
        if vcenter_hostname is not None:
            self.vcenter_hostname = vcenter_hostname
        if vcenter_username is not None:
            self.vcenter_username = vcenter_username
        if volume_list is not None:
            self.volume_list = volume_list

    @property
    def agent_hostname(self):
        """Gets the agent_hostname of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        Generic backup agent hostname. Custom port number can be specified with agent hostname using \\\\\":\\\\\". String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The agent_hostname of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._agent_hostname

    @agent_hostname.setter
    def agent_hostname(self, agent_hostname):
        """Sets the agent_hostname of this NimbleCreateVolumeCollectionInput.

        Generic backup agent hostname. Custom port number can be specified with agent hostname using \\\\\":\\\\\". String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param agent_hostname: The agent_hostname of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """

        self._agent_hostname = agent_hostname

    @property
    def agent_username(self):
        """Gets the agent_username of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        Generic backup agent username. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The agent_username of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._agent_username

    @agent_username.setter
    def agent_username(self, agent_username):
        """Sets the agent_username of this NimbleCreateVolumeCollectionInput.

        Generic backup agent username. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param agent_username: The agent_username of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """

        self._agent_username = agent_username

    @property
    def app_cluster_name(self):
        """Gets the app_cluster_name of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        If the application is running within a Windows cluster environment, this is the cluster name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The app_cluster_name of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._app_cluster_name

    @app_cluster_name.setter
    def app_cluster_name(self, app_cluster_name):
        """Sets the app_cluster_name of this NimbleCreateVolumeCollectionInput.

        If the application is running within a Windows cluster environment, this is the cluster name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param app_cluster_name: The app_cluster_name of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """

        self._app_cluster_name = app_cluster_name

    @property
    def app_id(self):
        """Gets the app_id of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        Application ID running on the server. Application ID can only be specified if application synchronization is \\\\\"vss\\\\\". Possible values: 'inval', 'exchange', 'exchange_dag', 'hyperv', 'sql2005', 'sql2008', 'sql2012', 'sql2014', 'sql2016', 'sql2017'.  # noqa: E501

        :return: The app_id of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this NimbleCreateVolumeCollectionInput.

        Application ID running on the server. Application ID can only be specified if application synchronization is \\\\\"vss\\\\\". Possible values: 'inval', 'exchange', 'exchange_dag', 'hyperv', 'sql2005', 'sql2008', 'sql2012', 'sql2014', 'sql2016', 'sql2017'.  # noqa: E501

        :param app_id: The app_id of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def app_server(self):
        """Gets the app_server of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        Application server hostname. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The app_server of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._app_server

    @app_server.setter
    def app_server(self, app_server):
        """Sets the app_server of this NimbleCreateVolumeCollectionInput.

        Application server hostname. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param app_server: The app_server of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """

        self._app_server = app_server

    @property
    def app_service_name(self):
        """Gets the app_service_name of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The app_service_name of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._app_service_name

    @app_service_name.setter
    def app_service_name(self, app_service_name):
        """Sets the app_service_name of this NimbleCreateVolumeCollectionInput.

        If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param app_service_name: The app_service_name of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """

        self._app_service_name = app_service_name

    @property
    def app_sync(self):
        """Gets the app_sync of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        Application Synchronization. Possible values: 'none', 'vss', 'vmware', 'generic'.  # noqa: E501

        :return: The app_sync of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._app_sync

    @app_sync.setter
    def app_sync(self, app_sync):
        """Sets the app_sync of this NimbleCreateVolumeCollectionInput.

        Application Synchronization. Possible values: 'none', 'vss', 'vmware', 'generic'.  # noqa: E501

        :param app_sync: The app_sync of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """

        self._app_sync = app_sync

    @property
    def description(self):
        """Gets the description of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        Text description of volume collection. String of up to 255 printable ASCII characters.  # noqa: E501

        :return: The description of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NimbleCreateVolumeCollectionInput.

        Text description of volume collection. String of up to 255 printable ASCII characters.  # noqa: E501

        :param description: The description of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_standalone_volcoll(self):
        """Gets the is_standalone_volcoll of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        Indicates whether this is a standalone volume collection. Possible values: 'true', 'false'.  # noqa: E501

        :return: The is_standalone_volcoll of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_standalone_volcoll

    @is_standalone_volcoll.setter
    def is_standalone_volcoll(self, is_standalone_volcoll):
        """Sets the is_standalone_volcoll of this NimbleCreateVolumeCollectionInput.

        Indicates whether this is a standalone volume collection. Possible values: 'true', 'false'.  # noqa: E501

        :param is_standalone_volcoll: The is_standalone_volcoll of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: bool
        """

        self._is_standalone_volcoll = is_standalone_volcoll

    @property
    def metadata(self):
        """Gets the metadata of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        Key-value pairs that augment a volume collection's attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed.  # noqa: E501

        :return: The metadata of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: list[KeyValue]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NimbleCreateVolumeCollectionInput.

        Key-value pairs that augment a volume collection's attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed.  # noqa: E501

        :param metadata: The metadata of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: list[KeyValue]
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        Name of volume collection. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The name of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NimbleCreateVolumeCollectionInput.

        Name of volume collection. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param name: The name of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def prottmpl_id(self):
        """Gets the prottmpl_id of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        Identifier of the protection template whose attributes will be used to create this volume collection. This attribute is only used for input when creating a volume collection and is not outputed. A 42 digit hexadecimal number.  # noqa: E501

        :return: The prottmpl_id of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._prottmpl_id

    @prottmpl_id.setter
    def prottmpl_id(self, prottmpl_id):
        """Sets the prottmpl_id of this NimbleCreateVolumeCollectionInput.

        Identifier of the protection template whose attributes will be used to create this volume collection. This attribute is only used for input when creating a volume collection and is not outputed. A 42 digit hexadecimal number.  # noqa: E501

        :param prottmpl_id: The prottmpl_id of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """

        self._prottmpl_id = prottmpl_id

    @property
    def replication_type(self):
        """Gets the replication_type of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        Type of replication configured for the volume collection. Possible values are periodic snapshot and synchronous. Default value is periodic_snapshot.  # noqa: E501

        :return: The replication_type of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._replication_type

    @replication_type.setter
    def replication_type(self, replication_type):
        """Sets the replication_type of this NimbleCreateVolumeCollectionInput.

        Type of replication configured for the volume collection. Possible values are periodic snapshot and synchronous. Default value is periodic_snapshot.  # noqa: E501

        :param replication_type: The replication_type of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """

        self._replication_type = replication_type

    @property
    def vcenter_hostname(self):
        """Gets the vcenter_hostname of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\\\\":\\\\\". String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The vcenter_hostname of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._vcenter_hostname

    @vcenter_hostname.setter
    def vcenter_hostname(self, vcenter_hostname):
        """Sets the vcenter_hostname of this NimbleCreateVolumeCollectionInput.

        VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\\\\":\\\\\". String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param vcenter_hostname: The vcenter_hostname of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """

        self._vcenter_hostname = vcenter_hostname

    @property
    def vcenter_username(self):
        """Gets the vcenter_username of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        Application VMware vCenter username. String of up to 80 alphanumeric characters, beginning with a letter. It can include ampersand (@), backslash (\\), dash (-), period (.), and underscore (_).  # noqa: E501

        :return: The vcenter_username of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: str
        """
        return self._vcenter_username

    @vcenter_username.setter
    def vcenter_username(self, vcenter_username):
        """Sets the vcenter_username of this NimbleCreateVolumeCollectionInput.

        Application VMware vCenter username. String of up to 80 alphanumeric characters, beginning with a letter. It can include ampersand (@), backslash (\\), dash (-), period (.), and underscore (_).  # noqa: E501

        :param vcenter_username: The vcenter_username of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: str
        """

        self._vcenter_username = vcenter_username

    @property
    def volume_list(self):
        """Gets the volume_list of this NimbleCreateVolumeCollectionInput.  # noqa: E501

        List of volume id's that need to be added to the volume collection.  # noqa: E501

        :return: The volume_list of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume_list

    @volume_list.setter
    def volume_list(self, volume_list):
        """Sets the volume_list of this NimbleCreateVolumeCollectionInput.

        List of volume id's that need to be added to the volume collection.  # noqa: E501

        :param volume_list: The volume_list of this NimbleCreateVolumeCollectionInput.  # noqa: E501
        :type: list[str]
        """

        self._volume_list = volume_list

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
        if not isinstance(other, NimbleCreateVolumeCollectionInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other