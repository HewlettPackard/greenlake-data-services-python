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


class SystemSettingsDetails(object):
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
        'associated_links': 'list[AssociatedLinksInner]',
        'auth_mode': 'str',
        'console_uri': 'str',
        'customer_id': 'str',
        'generation': 'int',
        'installationsites': 'SystemSettingsDetailsInstallationsites',
        'is_fips_enabled': 'bool',
        'name': 'str',
        'ntp_server': 'str',
        'remote_syslog_settings': 'object',
        'srinfo': 'object',
        'supportcontact': 'ContactsDetails',
        'system_date': 'int',
        'system_id': 'str',
        'system_parameters': 'object',
        'timezone': 'str',
        'type': 'str'
    }

    attribute_map = {
        'associated_links': 'associatedLinks',
        'auth_mode': 'authMode',
        'console_uri': 'consoleUri',
        'customer_id': 'customerId',
        'generation': 'generation',
        'installationsites': 'installationsites',
        'is_fips_enabled': 'isFIPSEnabled',
        'name': 'name',
        'ntp_server': 'ntpServer',
        'remote_syslog_settings': 'remoteSyslogSettings',
        'srinfo': 'srinfo',
        'supportcontact': 'supportcontact',
        'system_date': 'systemDate',
        'system_id': 'systemId',
        'system_parameters': 'systemParameters',
        'timezone': 'timezone',
        'type': 'type'
    }

    def __init__(self, associated_links=None, auth_mode=None, console_uri=None, customer_id=None, generation=None, installationsites=None, is_fips_enabled=None, name=None, ntp_server=None, remote_syslog_settings=None, srinfo=None, supportcontact=None, system_date=None, system_id=None, system_parameters=None, timezone=None, type=None):  # noqa: E501
        """SystemSettingsDetails - a model defined in OpenAPI"""  # noqa: E501

        self._associated_links = None
        self._auth_mode = None
        self._console_uri = None
        self._customer_id = None
        self._generation = None
        self._installationsites = None
        self._is_fips_enabled = None
        self._name = None
        self._ntp_server = None
        self._remote_syslog_settings = None
        self._srinfo = None
        self._supportcontact = None
        self._system_date = None
        self._system_id = None
        self._system_parameters = None
        self._timezone = None
        self._type = None
        self.discriminator = None

        if associated_links is not None:
            self.associated_links = associated_links
        if auth_mode is not None:
            self.auth_mode = auth_mode
        if console_uri is not None:
            self.console_uri = console_uri
        if customer_id is not None:
            self.customer_id = customer_id
        if generation is not None:
            self.generation = generation
        if installationsites is not None:
            self.installationsites = installationsites
        if is_fips_enabled is not None:
            self.is_fips_enabled = is_fips_enabled
        if name is not None:
            self.name = name
        if ntp_server is not None:
            self.ntp_server = ntp_server
        if remote_syslog_settings is not None:
            self.remote_syslog_settings = remote_syslog_settings
        if srinfo is not None:
            self.srinfo = srinfo
        if supportcontact is not None:
            self.supportcontact = supportcontact
        if system_date is not None:
            self.system_date = system_date
        if system_id is not None:
            self.system_id = system_id
        if system_parameters is not None:
            self.system_parameters = system_parameters
        if timezone is not None:
            self.timezone = timezone
        if type is not None:
            self.type = type

    @property
    def associated_links(self):
        """Gets the associated_links of this SystemSettingsDetails.  # noqa: E501

        Associated Links Details  # noqa: E501

        :return: The associated_links of this SystemSettingsDetails.  # noqa: E501
        :rtype: list[AssociatedLinksInner]
        """
        return self._associated_links

    @associated_links.setter
    def associated_links(self, associated_links):
        """Sets the associated_links of this SystemSettingsDetails.

        Associated Links Details  # noqa: E501

        :param associated_links: The associated_links of this SystemSettingsDetails.  # noqa: E501
        :type: list[AssociatedLinksInner]
        """

        self._associated_links = associated_links

    @property
    def auth_mode(self):
        """Gets the auth_mode of this SystemSettingsDetails.  # noqa: E501

        Password Authentication Mode  # noqa: E501

        :return: The auth_mode of this SystemSettingsDetails.  # noqa: E501
        :rtype: str
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        """Sets the auth_mode of this SystemSettingsDetails.

        Password Authentication Mode  # noqa: E501

        :param auth_mode: The auth_mode of this SystemSettingsDetails.  # noqa: E501
        :type: str
        """

        self._auth_mode = auth_mode

    @property
    def console_uri(self):
        """Gets the console_uri of this SystemSettingsDetails.  # noqa: E501

        consoleUri for detailed storage object   # noqa: E501

        :return: The console_uri of this SystemSettingsDetails.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this SystemSettingsDetails.

        consoleUri for detailed storage object   # noqa: E501

        :param console_uri: The console_uri of this SystemSettingsDetails.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def customer_id(self):
        """Gets the customer_id of this SystemSettingsDetails.  # noqa: E501

        The customer application identifier  # noqa: E501

        :return: The customer_id of this SystemSettingsDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this SystemSettingsDetails.

        The customer application identifier  # noqa: E501

        :param customer_id: The customer_id of this SystemSettingsDetails.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def generation(self):
        """Gets the generation of this SystemSettingsDetails.  # noqa: E501

        A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.  # noqa: E501

        :return: The generation of this SystemSettingsDetails.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this SystemSettingsDetails.

        A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.  # noqa: E501

        :param generation: The generation of this SystemSettingsDetails.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def installationsites(self):
        """Gets the installationsites of this SystemSettingsDetails.  # noqa: E501


        :return: The installationsites of this SystemSettingsDetails.  # noqa: E501
        :rtype: SystemSettingsDetailsInstallationsites
        """
        return self._installationsites

    @installationsites.setter
    def installationsites(self, installationsites):
        """Sets the installationsites of this SystemSettingsDetails.


        :param installationsites: The installationsites of this SystemSettingsDetails.  # noqa: E501
        :type: SystemSettingsDetailsInstallationsites
        """

        self._installationsites = installationsites

    @property
    def is_fips_enabled(self):
        """Gets the is_fips_enabled of this SystemSettingsDetails.  # noqa: E501

        Apply FIPS Standard  # noqa: E501

        :return: The is_fips_enabled of this SystemSettingsDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_fips_enabled

    @is_fips_enabled.setter
    def is_fips_enabled(self, is_fips_enabled):
        """Sets the is_fips_enabled of this SystemSettingsDetails.

        Apply FIPS Standard  # noqa: E501

        :param is_fips_enabled: The is_fips_enabled of this SystemSettingsDetails.  # noqa: E501
        :type: bool
        """

        self._is_fips_enabled = is_fips_enabled

    @property
    def name(self):
        """Gets the name of this SystemSettingsDetails.  # noqa: E501

        system name  # noqa: E501

        :return: The name of this SystemSettingsDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemSettingsDetails.

        system name  # noqa: E501

        :param name: The name of this SystemSettingsDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ntp_server(self):
        """Gets the ntp_server of this SystemSettingsDetails.  # noqa: E501

        ntp server  # noqa: E501

        :return: The ntp_server of this SystemSettingsDetails.  # noqa: E501
        :rtype: str
        """
        return self._ntp_server

    @ntp_server.setter
    def ntp_server(self, ntp_server):
        """Sets the ntp_server of this SystemSettingsDetails.

        ntp server  # noqa: E501

        :param ntp_server: The ntp_server of this SystemSettingsDetails.  # noqa: E501
        :type: str
        """

        self._ntp_server = ntp_server

    @property
    def remote_syslog_settings(self):
        """Gets the remote_syslog_settings of this SystemSettingsDetails.  # noqa: E501


        :return: The remote_syslog_settings of this SystemSettingsDetails.  # noqa: E501
        :rtype: object
        """
        return self._remote_syslog_settings

    @remote_syslog_settings.setter
    def remote_syslog_settings(self, remote_syslog_settings):
        """Sets the remote_syslog_settings of this SystemSettingsDetails.


        :param remote_syslog_settings: The remote_syslog_settings of this SystemSettingsDetails.  # noqa: E501
        :type: object
        """

        self._remote_syslog_settings = remote_syslog_settings

    @property
    def srinfo(self):
        """Gets the srinfo of this SystemSettingsDetails.  # noqa: E501


        :return: The srinfo of this SystemSettingsDetails.  # noqa: E501
        :rtype: object
        """
        return self._srinfo

    @srinfo.setter
    def srinfo(self, srinfo):
        """Sets the srinfo of this SystemSettingsDetails.


        :param srinfo: The srinfo of this SystemSettingsDetails.  # noqa: E501
        :type: object
        """

        self._srinfo = srinfo

    @property
    def supportcontact(self):
        """Gets the supportcontact of this SystemSettingsDetails.  # noqa: E501


        :return: The supportcontact of this SystemSettingsDetails.  # noqa: E501
        :rtype: ContactsDetails
        """
        return self._supportcontact

    @supportcontact.setter
    def supportcontact(self, supportcontact):
        """Sets the supportcontact of this SystemSettingsDetails.


        :param supportcontact: The supportcontact of this SystemSettingsDetails.  # noqa: E501
        :type: ContactsDetails
        """

        self._supportcontact = supportcontact

    @property
    def system_date(self):
        """Gets the system_date of this SystemSettingsDetails.  # noqa: E501

        system date time  # noqa: E501

        :return: The system_date of this SystemSettingsDetails.  # noqa: E501
        :rtype: int
        """
        return self._system_date

    @system_date.setter
    def system_date(self, system_date):
        """Sets the system_date of this SystemSettingsDetails.

        system date time  # noqa: E501

        :param system_date: The system_date of this SystemSettingsDetails.  # noqa: E501
        :type: int
        """

        self._system_date = system_date

    @property
    def system_id(self):
        """Gets the system_id of this SystemSettingsDetails.  # noqa: E501

        SystemId/serialNumber of the array.  # noqa: E501

        :return: The system_id of this SystemSettingsDetails.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemSettingsDetails.

        SystemId/serialNumber of the array.  # noqa: E501

        :param system_id: The system_id of this SystemSettingsDetails.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def system_parameters(self):
        """Gets the system_parameters of this SystemSettingsDetails.  # noqa: E501


        :return: The system_parameters of this SystemSettingsDetails.  # noqa: E501
        :rtype: object
        """
        return self._system_parameters

    @system_parameters.setter
    def system_parameters(self, system_parameters):
        """Sets the system_parameters of this SystemSettingsDetails.


        :param system_parameters: The system_parameters of this SystemSettingsDetails.  # noqa: E501
        :type: object
        """

        self._system_parameters = system_parameters

    @property
    def timezone(self):
        """Gets the timezone of this SystemSettingsDetails.  # noqa: E501

        system time zone  # noqa: E501

        :return: The timezone of this SystemSettingsDetails.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this SystemSettingsDetails.

        system time zone  # noqa: E501

        :param timezone: The timezone of this SystemSettingsDetails.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def type(self):
        """Gets the type of this SystemSettingsDetails.  # noqa: E501

        The type of resource.  # noqa: E501

        :return: The type of this SystemSettingsDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemSettingsDetails.

        The type of resource.  # noqa: E501

        :param type: The type of this SystemSettingsDetails.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, SystemSettingsDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
