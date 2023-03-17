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


class NimbleProtectionTemplateFieldsWithoutSortKey(object):
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
        'app_cluster_name': 'str',
        'app_id': 'str',
        'app_server': 'str',
        'app_service_name': 'str',
        'app_sync': 'str',
        'creation_time': 'int',
        'id': 'str',
        'last_modified': 'int',
        'name': 'str',
        'vcenter_hostname': 'str'
    }

    attribute_map = {
        'agent_hostname': 'agent_hostname',
        'app_cluster_name': 'app_cluster_name',
        'app_id': 'app_id',
        'app_server': 'app_server',
        'app_service_name': 'app_service_name',
        'app_sync': 'app_sync',
        'creation_time': 'creation_time',
        'id': 'id',
        'last_modified': 'last_modified',
        'name': 'name',
        'vcenter_hostname': 'vcenter_hostname'
    }

    def __init__(self, agent_hostname=None, app_cluster_name=None, app_id=None, app_server=None, app_service_name=None, app_sync=None, creation_time=None, id=None, last_modified=None, name=None, vcenter_hostname=None):  # noqa: E501
        """NimbleProtectionTemplateFieldsWithoutSortKey - a model defined in OpenAPI"""  # noqa: E501

        self._agent_hostname = None
        self._app_cluster_name = None
        self._app_id = None
        self._app_server = None
        self._app_service_name = None
        self._app_sync = None
        self._creation_time = None
        self._id = None
        self._last_modified = None
        self._name = None
        self._vcenter_hostname = None
        self.discriminator = None

        if agent_hostname is not None:
            self.agent_hostname = agent_hostname
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
        if creation_time is not None:
            self.creation_time = creation_time
        if id is not None:
            self.id = id
        if last_modified is not None:
            self.last_modified = last_modified
        if name is not None:
            self.name = name
        if vcenter_hostname is not None:
            self.vcenter_hostname = vcenter_hostname

    @property
    def agent_hostname(self):
        """Gets the agent_hostname of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501

        Generic Backup agent hostname. Custom port number can be specified with agent hostname using \\\\\":\\\\\".  # noqa: E501

        :return: The agent_hostname of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._agent_hostname

    @agent_hostname.setter
    def agent_hostname(self, agent_hostname):
        """Sets the agent_hostname of this NimbleProtectionTemplateFieldsWithoutSortKey.

        Generic Backup agent hostname. Custom port number can be specified with agent hostname using \\\\\":\\\\\".  # noqa: E501

        :param agent_hostname: The agent_hostname of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._agent_hostname = agent_hostname

    @property
    def app_cluster_name(self):
        """Gets the app_cluster_name of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501

        If the application is running within a Windows cluster environment then this is the cluster name.  # noqa: E501

        :return: The app_cluster_name of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._app_cluster_name

    @app_cluster_name.setter
    def app_cluster_name(self, app_cluster_name):
        """Sets the app_cluster_name of this NimbleProtectionTemplateFieldsWithoutSortKey.

        If the application is running within a Windows cluster environment then this is the cluster name.  # noqa: E501

        :param app_cluster_name: The app_cluster_name of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._app_cluster_name = app_cluster_name

    @property
    def app_id(self):
        """Gets the app_id of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501

        Application ID running on the server. Application ID can only be specified if application synchronization is VSS.  Possible values:'exchange_dag', 'sql2012', 'sql2014', 'inval', 'sql2005', 'sql2016', 'exchange', 'sql2017', 'sql2018', 'hyperv'.  # noqa: E501

        :return: The app_id of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this NimbleProtectionTemplateFieldsWithoutSortKey.

        Application ID running on the server. Application ID can only be specified if application synchronization is VSS.  Possible values:'exchange_dag', 'sql2012', 'sql2014', 'inval', 'sql2005', 'sql2016', 'exchange', 'sql2017', 'sql2018', 'hyperv'.  # noqa: E501

        :param app_id: The app_id of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def app_server(self):
        """Gets the app_server of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501

        Application server hostname.  # noqa: E501

        :return: The app_server of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._app_server

    @app_server.setter
    def app_server(self, app_server):
        """Sets the app_server of this NimbleProtectionTemplateFieldsWithoutSortKey.

        Application server hostname.  # noqa: E501

        :param app_server: The app_server of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._app_server = app_server

    @property
    def app_service_name(self):
        """Gets the app_service_name of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501

        If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment.  # noqa: E501

        :return: The app_service_name of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._app_service_name

    @app_service_name.setter
    def app_service_name(self, app_service_name):
        """Sets the app_service_name of this NimbleProtectionTemplateFieldsWithoutSortKey.

        If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment.  # noqa: E501

        :param app_service_name: The app_service_name of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._app_service_name = app_service_name

    @property
    def app_sync(self):
        """Gets the app_sync of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501

        Application synchronization ({none|vss|vmware|generic}). Possible values:'vss', 'vmware', 'none', 'generic'.  # noqa: E501

        :return: The app_sync of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._app_sync

    @app_sync.setter
    def app_sync(self, app_sync):
        """Sets the app_sync of this NimbleProtectionTemplateFieldsWithoutSortKey.

        Application synchronization ({none|vss|vmware|generic}). Possible values:'vss', 'vmware', 'none', 'generic'.  # noqa: E501

        :param app_sync: The app_sync of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._app_sync = app_sync

    @property
    def creation_time(self):
        """Gets the creation_time of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501

        Time when this protection template was created.  # noqa: E501

        :return: The creation_time of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this NimbleProtectionTemplateFieldsWithoutSortKey.

        Time when this protection template was created.  # noqa: E501

        :param creation_time: The creation_time of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :type: int
        """

        self._creation_time = creation_time

    @property
    def id(self):
        """Gets the id of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501

        Identifier for protection template.  # noqa: E501

        :return: The id of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NimbleProtectionTemplateFieldsWithoutSortKey.

        Identifier for protection template.  # noqa: E501

        :param id: The id of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_modified(self):
        """Gets the last_modified of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501

        Time when this protection template was last modified.  # noqa: E501

        :return: The last_modified of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this NimbleProtectionTemplateFieldsWithoutSortKey.

        Time when this protection template was last modified.  # noqa: E501

        :param last_modified: The last_modified of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :type: int
        """

        self._last_modified = last_modified

    @property
    def name(self):
        """Gets the name of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501

        Fully qualified name of protection template.  # noqa: E501

        :return: The name of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NimbleProtectionTemplateFieldsWithoutSortKey.

        Fully qualified name of protection template.  # noqa: E501

        :param name: The name of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def vcenter_hostname(self):
        """Gets the vcenter_hostname of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501

        VMware vCenter hostname. Custom port number can be specified with vCenter hostname.  # noqa: E501

        :return: The vcenter_hostname of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._vcenter_hostname

    @vcenter_hostname.setter
    def vcenter_hostname(self, vcenter_hostname):
        """Sets the vcenter_hostname of this NimbleProtectionTemplateFieldsWithoutSortKey.

        VMware vCenter hostname. Custom port number can be specified with vCenter hostname.  # noqa: E501

        :param vcenter_hostname: The vcenter_hostname of this NimbleProtectionTemplateFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._vcenter_hostname = vcenter_hostname

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
        if not isinstance(other, NimbleProtectionTemplateFieldsWithoutSortKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
