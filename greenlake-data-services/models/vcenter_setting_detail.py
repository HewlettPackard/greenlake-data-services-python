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


class VcenterSettingDetail(object):
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
        'console_uri': 'str',
        'customer_id': 'str',
        'description': 'str',
        'friendly_cert': 'FriendlyCert',
        'generation': 'int',
        'id': 'str',
        'inetaddress': 'str',
        'name': 'str',
        'port': 'int',
        'request_uri': 'str',
        'resource_uri': 'str',
        'status': 'VcenterStatus',
        'system_id': 'str',
        'type': 'str',
        'username': 'str',
        'vm_manager_type': 'str'
    }

    attribute_map = {
        'console_uri': 'consoleUri',
        'customer_id': 'customerId',
        'description': 'description',
        'friendly_cert': 'friendlyCert',
        'generation': 'generation',
        'id': 'id',
        'inetaddress': 'inetaddress',
        'name': 'name',
        'port': 'port',
        'request_uri': 'requestUri',
        'resource_uri': 'resourceUri',
        'status': 'status',
        'system_id': 'systemId',
        'type': 'type',
        'username': 'username',
        'vm_manager_type': 'vmManagerType'
    }

    def __init__(self, console_uri=None, customer_id=None, description=None, friendly_cert=None, generation=None, id=None, inetaddress=None, name=None, port=None, request_uri=None, resource_uri=None, status=None, system_id=None, type=None, username=None, vm_manager_type=None):  # noqa: E501
        """VcenterSettingDetail - a model defined in OpenAPI"""  # noqa: E501

        self._console_uri = None
        self._customer_id = None
        self._description = None
        self._friendly_cert = None
        self._generation = None
        self._id = None
        self._inetaddress = None
        self._name = None
        self._port = None
        self._request_uri = None
        self._resource_uri = None
        self._status = None
        self._system_id = None
        self._type = None
        self._username = None
        self._vm_manager_type = None
        self.discriminator = None

        if console_uri is not None:
            self.console_uri = console_uri
        if customer_id is not None:
            self.customer_id = customer_id
        if description is not None:
            self.description = description
        if friendly_cert is not None:
            self.friendly_cert = friendly_cert
        if generation is not None:
            self.generation = generation
        if id is not None:
            self.id = id
        if inetaddress is not None:
            self.inetaddress = inetaddress
        if name is not None:
            self.name = name
        if port is not None:
            self.port = port
        if request_uri is not None:
            self.request_uri = request_uri
        if resource_uri is not None:
            self.resource_uri = resource_uri
        if status is not None:
            self.status = status
        if system_id is not None:
            self.system_id = system_id
        if type is not None:
            self.type = type
        if username is not None:
            self.username = username
        if vm_manager_type is not None:
            self.vm_manager_type = vm_manager_type

    @property
    def console_uri(self):
        """Gets the console_uri of this VcenterSettingDetail.  # noqa: E501

        consoleUri for detailed storage object  # noqa: E501

        :return: The console_uri of this VcenterSettingDetail.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this VcenterSettingDetail.

        consoleUri for detailed storage object  # noqa: E501

        :param console_uri: The console_uri of this VcenterSettingDetail.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def customer_id(self):
        """Gets the customer_id of this VcenterSettingDetail.  # noqa: E501

        The customer application identifier  # noqa: E501

        :return: The customer_id of this VcenterSettingDetail.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this VcenterSettingDetail.

        The customer application identifier  # noqa: E501

        :param customer_id: The customer_id of this VcenterSettingDetail.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def description(self):
        """Gets the description of this VcenterSettingDetail.  # noqa: E501

        Vcenter description  # noqa: E501

        :return: The description of this VcenterSettingDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VcenterSettingDetail.

        Vcenter description  # noqa: E501

        :param description: The description of this VcenterSettingDetail.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def friendly_cert(self):
        """Gets the friendly_cert of this VcenterSettingDetail.  # noqa: E501


        :return: The friendly_cert of this VcenterSettingDetail.  # noqa: E501
        :rtype: FriendlyCert
        """
        return self._friendly_cert

    @friendly_cert.setter
    def friendly_cert(self, friendly_cert):
        """Sets the friendly_cert of this VcenterSettingDetail.


        :param friendly_cert: The friendly_cert of this VcenterSettingDetail.  # noqa: E501
        :type: FriendlyCert
        """

        self._friendly_cert = friendly_cert

    @property
    def generation(self):
        """Gets the generation of this VcenterSettingDetail.  # noqa: E501

        A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.  # noqa: E501

        :return: The generation of this VcenterSettingDetail.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this VcenterSettingDetail.

        A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.  # noqa: E501

        :param generation: The generation of this VcenterSettingDetail.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def id(self):
        """Gets the id of this VcenterSettingDetail.  # noqa: E501

        Unique identifier of the vcenter settings.  # noqa: E501

        :return: The id of this VcenterSettingDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VcenterSettingDetail.

        Unique identifier of the vcenter settings.  # noqa: E501

        :param id: The id of this VcenterSettingDetail.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inetaddress(self):
        """Gets the inetaddress of this VcenterSettingDetail.  # noqa: E501

        Address of the vcenter.  # noqa: E501

        :return: The inetaddress of this VcenterSettingDetail.  # noqa: E501
        :rtype: str
        """
        return self._inetaddress

    @inetaddress.setter
    def inetaddress(self, inetaddress):
        """Sets the inetaddress of this VcenterSettingDetail.

        Address of the vcenter.  # noqa: E501

        :param inetaddress: The inetaddress of this VcenterSettingDetail.  # noqa: E501
        :type: str
        """

        self._inetaddress = inetaddress

    @property
    def name(self):
        """Gets the name of this VcenterSettingDetail.  # noqa: E501

        Name of vcenter.  # noqa: E501

        :return: The name of this VcenterSettingDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VcenterSettingDetail.

        Name of vcenter.  # noqa: E501

        :param name: The name of this VcenterSettingDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port(self):
        """Gets the port of this VcenterSettingDetail.  # noqa: E501

        port number of vcenter.  # noqa: E501

        :return: The port of this VcenterSettingDetail.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this VcenterSettingDetail.

        port number of vcenter.  # noqa: E501

        :param port: The port of this VcenterSettingDetail.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def request_uri(self):
        """Gets the request_uri of this VcenterSettingDetail.  # noqa: E501

        requestUri for vcenter setting details per system   # noqa: E501

        :return: The request_uri of this VcenterSettingDetail.  # noqa: E501
        :rtype: str
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri):
        """Sets the request_uri of this VcenterSettingDetail.

        requestUri for vcenter setting details per system   # noqa: E501

        :param request_uri: The request_uri of this VcenterSettingDetail.  # noqa: E501
        :type: str
        """

        self._request_uri = request_uri

    @property
    def resource_uri(self):
        """Gets the resource_uri of this VcenterSettingDetail.  # noqa: E501

        resourceUri for detailed vcenter setting object  # noqa: E501

        :return: The resource_uri of this VcenterSettingDetail.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this VcenterSettingDetail.

        resourceUri for detailed vcenter setting object  # noqa: E501

        :param resource_uri: The resource_uri of this VcenterSettingDetail.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

    @property
    def status(self):
        """Gets the status of this VcenterSettingDetail.  # noqa: E501


        :return: The status of this VcenterSettingDetail.  # noqa: E501
        :rtype: VcenterStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VcenterSettingDetail.


        :param status: The status of this VcenterSettingDetail.  # noqa: E501
        :type: VcenterStatus
        """

        self._status = status

    @property
    def system_id(self):
        """Gets the system_id of this VcenterSettingDetail.  # noqa: E501

        SystemID of the array  # noqa: E501

        :return: The system_id of this VcenterSettingDetail.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this VcenterSettingDetail.

        SystemID of the array  # noqa: E501

        :param system_id: The system_id of this VcenterSettingDetail.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def type(self):
        """Gets the type of this VcenterSettingDetail.  # noqa: E501

        The type of resource.  # noqa: E501

        :return: The type of this VcenterSettingDetail.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VcenterSettingDetail.

        The type of resource.  # noqa: E501

        :param type: The type of this VcenterSettingDetail.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def username(self):
        """Gets the username of this VcenterSettingDetail.  # noqa: E501

        User of the vcenter configured.  # noqa: E501

        :return: The username of this VcenterSettingDetail.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this VcenterSettingDetail.

        User of the vcenter configured.  # noqa: E501

        :param username: The username of this VcenterSettingDetail.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def vm_manager_type(self):
        """Gets the vm_manager_type of this VcenterSettingDetail.  # noqa: E501

        Type of the vmmanager settings.  # noqa: E501

        :return: The vm_manager_type of this VcenterSettingDetail.  # noqa: E501
        :rtype: str
        """
        return self._vm_manager_type

    @vm_manager_type.setter
    def vm_manager_type(self, vm_manager_type):
        """Sets the vm_manager_type of this VcenterSettingDetail.

        Type of the vmmanager settings.  # noqa: E501

        :param vm_manager_type: The vm_manager_type of this VcenterSettingDetail.  # noqa: E501
        :type: str
        """

        self._vm_manager_type = vm_manager_type

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
        if not isinstance(other, VcenterSettingDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
