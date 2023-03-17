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


class Cim(object):
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
        'cim_policy': 'str',
        'cim_state': 'str',
        'cim_version': 'str',
        'console_uri': 'str',
        'customer_id': 'str',
        'generation': 'int',
        'http_port': 'int',
        'http_state': 'bool',
        'https_port': 'int',
        'https_state': 'bool',
        'id': 'str',
        'pg_version': 'str',
        'service_state': 'bool',
        'slp_port': 'int',
        'slp_state': 'bool',
        'system_id': 'str',
        'system_wwn': 'str',
        'type': 'str'
    }

    attribute_map = {
        'cim_policy': 'cimPolicy',
        'cim_state': 'cimState',
        'cim_version': 'cimVersion',
        'console_uri': 'consoleUri',
        'customer_id': 'customerId',
        'generation': 'generation',
        'http_port': 'httpPort',
        'http_state': 'httpState',
        'https_port': 'httpsPort',
        'https_state': 'httpsState',
        'id': 'id',
        'pg_version': 'pgVersion',
        'service_state': 'serviceState',
        'slp_port': 'slpPort',
        'slp_state': 'slpState',
        'system_id': 'systemId',
        'system_wwn': 'systemWWN',
        'type': 'type'
    }

    def __init__(self, cim_policy=None, cim_state=None, cim_version=None, console_uri=None, customer_id=None, generation=None, http_port=None, http_state=None, https_port=None, https_state=None, id=None, pg_version=None, service_state=None, slp_port=None, slp_state=None, system_id=None, system_wwn=None, type=None):  # noqa: E501
        """Cim - a model defined in OpenAPI"""  # noqa: E501

        self._cim_policy = None
        self._cim_state = None
        self._cim_version = None
        self._console_uri = None
        self._customer_id = None
        self._generation = None
        self._http_port = None
        self._http_state = None
        self._https_port = None
        self._https_state = None
        self._id = None
        self._pg_version = None
        self._service_state = None
        self._slp_port = None
        self._slp_state = None
        self._system_id = None
        self._system_wwn = None
        self._type = None
        self.discriminator = None

        if cim_policy is not None:
            self.cim_policy = cim_policy
        if cim_state is not None:
            self.cim_state = cim_state
        if cim_version is not None:
            self.cim_version = cim_version
        if console_uri is not None:
            self.console_uri = console_uri
        if customer_id is not None:
            self.customer_id = customer_id
        if generation is not None:
            self.generation = generation
        if http_port is not None:
            self.http_port = http_port
        if http_state is not None:
            self.http_state = http_state
        if https_port is not None:
            self.https_port = https_port
        if https_state is not None:
            self.https_state = https_state
        if id is not None:
            self.id = id
        if pg_version is not None:
            self.pg_version = pg_version
        if service_state is not None:
            self.service_state = service_state
        if slp_port is not None:
            self.slp_port = slp_port
        if slp_state is not None:
            self.slp_state = slp_state
        if system_id is not None:
            self.system_id = system_id
        if system_wwn is not None:
            self.system_wwn = system_wwn
        if type is not None:
            self.type = type

    @property
    def cim_policy(self):
        """Gets the cim_policy of this Cim.  # noqa: E501

        Specifies the CIM Policy of CIM server  # noqa: E501

        :return: The cim_policy of this Cim.  # noqa: E501
        :rtype: str
        """
        return self._cim_policy

    @cim_policy.setter
    def cim_policy(self, cim_policy):
        """Sets the cim_policy of this Cim.

        Specifies the CIM Policy of CIM server  # noqa: E501

        :param cim_policy: The cim_policy of this Cim.  # noqa: E501
        :type: str
        """

        self._cim_policy = cim_policy

    @property
    def cim_state(self):
        """Gets the cim_state of this Cim.  # noqa: E501

        Specifies whether CIM state is active or inactive  # noqa: E501

        :return: The cim_state of this Cim.  # noqa: E501
        :rtype: str
        """
        return self._cim_state

    @cim_state.setter
    def cim_state(self, cim_state):
        """Sets the cim_state of this Cim.

        Specifies whether CIM state is active or inactive  # noqa: E501

        :param cim_state: The cim_state of this Cim.  # noqa: E501
        :type: str
        """

        self._cim_state = cim_state

    @property
    def cim_version(self):
        """Gets the cim_version of this Cim.  # noqa: E501

        CIM version information  # noqa: E501

        :return: The cim_version of this Cim.  # noqa: E501
        :rtype: str
        """
        return self._cim_version

    @cim_version.setter
    def cim_version(self, cim_version):
        """Sets the cim_version of this Cim.

        CIM version information  # noqa: E501

        :param cim_version: The cim_version of this Cim.  # noqa: E501
        :type: str
        """

        self._cim_version = cim_version

    @property
    def console_uri(self):
        """Gets the console_uri of this Cim.  # noqa: E501

        consoleUri for detailed storage object  # noqa: E501

        :return: The console_uri of this Cim.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this Cim.

        consoleUri for detailed storage object  # noqa: E501

        :param console_uri: The console_uri of this Cim.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def customer_id(self):
        """Gets the customer_id of this Cim.  # noqa: E501

        The customer application identifier  # noqa: E501

        :return: The customer_id of this Cim.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Cim.

        The customer application identifier  # noqa: E501

        :param customer_id: The customer_id of this Cim.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def generation(self):
        """Gets the generation of this Cim.  # noqa: E501

        A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.  # noqa: E501

        :return: The generation of this Cim.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this Cim.

        A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.  # noqa: E501

        :param generation: The generation of this Cim.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def http_port(self):
        """Gets the http_port of this Cim.  # noqa: E501

        HTTP port number  # noqa: E501

        :return: The http_port of this Cim.  # noqa: E501
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """Sets the http_port of this Cim.

        HTTP port number  # noqa: E501

        :param http_port: The http_port of this Cim.  # noqa: E501
        :type: int
        """

        self._http_port = http_port

    @property
    def http_state(self):
        """Gets the http_state of this Cim.  # noqa: E501

        Specifies whether HTTPState is enabled or disabled for CIM Server  # noqa: E501

        :return: The http_state of this Cim.  # noqa: E501
        :rtype: bool
        """
        return self._http_state

    @http_state.setter
    def http_state(self, http_state):
        """Sets the http_state of this Cim.

        Specifies whether HTTPState is enabled or disabled for CIM Server  # noqa: E501

        :param http_state: The http_state of this Cim.  # noqa: E501
        :type: bool
        """

        self._http_state = http_state

    @property
    def https_port(self):
        """Gets the https_port of this Cim.  # noqa: E501

        Specifies HTTPS port number  # noqa: E501

        :return: The https_port of this Cim.  # noqa: E501
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this Cim.

        Specifies HTTPS port number  # noqa: E501

        :param https_port: The https_port of this Cim.  # noqa: E501
        :type: int
        """

        self._https_port = https_port

    @property
    def https_state(self):
        """Gets the https_state of this Cim.  # noqa: E501

        Specifies whether HTTPS state is enabled or disabled for cim server  # noqa: E501

        :return: The https_state of this Cim.  # noqa: E501
        :rtype: bool
        """
        return self._https_state

    @https_state.setter
    def https_state(self, https_state):
        """Sets the https_state of this Cim.

        Specifies whether HTTPS state is enabled or disabled for cim server  # noqa: E501

        :param https_state: The https_state of this Cim.  # noqa: E501
        :type: bool
        """

        self._https_state = https_state

    @property
    def id(self):
        """Gets the id of this Cim.  # noqa: E501

        Unique Identifier of the resource  # noqa: E501

        :return: The id of this Cim.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Cim.

        Unique Identifier of the resource  # noqa: E501

        :param id: The id of this Cim.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def pg_version(self):
        """Gets the pg_version of this Cim.  # noqa: E501

        Information about PGVersion of CIM server  # noqa: E501

        :return: The pg_version of this Cim.  # noqa: E501
        :rtype: str
        """
        return self._pg_version

    @pg_version.setter
    def pg_version(self, pg_version):
        """Sets the pg_version of this Cim.

        Information about PGVersion of CIM server  # noqa: E501

        :param pg_version: The pg_version of this Cim.  # noqa: E501
        :type: str
        """

        self._pg_version = pg_version

    @property
    def service_state(self):
        """Gets the service_state of this Cim.  # noqa: E501

        Specifies whether service state is enabled or disabled  # noqa: E501

        :return: The service_state of this Cim.  # noqa: E501
        :rtype: bool
        """
        return self._service_state

    @service_state.setter
    def service_state(self, service_state):
        """Sets the service_state of this Cim.

        Specifies whether service state is enabled or disabled  # noqa: E501

        :param service_state: The service_state of this Cim.  # noqa: E501
        :type: bool
        """

        self._service_state = service_state

    @property
    def slp_port(self):
        """Gets the slp_port of this Cim.  # noqa: E501

        SLPport specification  # noqa: E501

        :return: The slp_port of this Cim.  # noqa: E501
        :rtype: int
        """
        return self._slp_port

    @slp_port.setter
    def slp_port(self, slp_port):
        """Sets the slp_port of this Cim.

        SLPport specification  # noqa: E501

        :param slp_port: The slp_port of this Cim.  # noqa: E501
        :type: int
        """

        self._slp_port = slp_port

    @property
    def slp_state(self):
        """Gets the slp_state of this Cim.  # noqa: E501

        whether slpstate is enabled or disabled  # noqa: E501

        :return: The slp_state of this Cim.  # noqa: E501
        :rtype: bool
        """
        return self._slp_state

    @slp_state.setter
    def slp_state(self, slp_state):
        """Sets the slp_state of this Cim.

        whether slpstate is enabled or disabled  # noqa: E501

        :param slp_state: The slp_state of this Cim.  # noqa: E501
        :type: bool
        """

        self._slp_state = slp_state

    @property
    def system_id(self):
        """Gets the system_id of this Cim.  # noqa: E501

        SystemId of the storage system  # noqa: E501

        :return: The system_id of this Cim.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this Cim.

        SystemId of the storage system  # noqa: E501

        :param system_id: The system_id of this Cim.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def system_wwn(self):
        """Gets the system_wwn of this Cim.  # noqa: E501

        WWN of the array  # noqa: E501

        :return: The system_wwn of this Cim.  # noqa: E501
        :rtype: str
        """
        return self._system_wwn

    @system_wwn.setter
    def system_wwn(self, system_wwn):
        """Sets the system_wwn of this Cim.

        WWN of the array  # noqa: E501

        :param system_wwn: The system_wwn of this Cim.  # noqa: E501
        :type: str
        """

        self._system_wwn = system_wwn

    @property
    def type(self):
        """Gets the type of this Cim.  # noqa: E501

        The type of resource.  # noqa: E501

        :return: The type of this Cim.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Cim.

        The type of resource.  # noqa: E501

        :param type: The type of this Cim.  # noqa: E501
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
        if not isinstance(other, Cim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other