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


class NodeDriveDetails(object):
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
        'console_uri': 'str',
        'customer_id': 'str',
        'displayname': 'str',
        'domain': 'str',
        'fw_version': 'str',
        'generation': 'int',
        'id': 'str',
        'manufacturing': 'ManufacturingSingle',
        'max_lba': 'str',
        'name': 'str',
        'node_device_id': 'int',
        'node_drive_id': 'int',
        'node_drive_type': 'str',
        'node_id': 'str',
        'request_uri': 'str',
        'resource_uri': 'str',
        'sed_state': 'str',
        'size_mi_b': 'int',
        'system_id': 'str',
        'type': 'str',
        'wwn': 'str'
    }

    attribute_map = {
        'associated_links': 'associatedLinks',
        'console_uri': 'consoleUri',
        'customer_id': 'customerId',
        'displayname': 'displayname',
        'domain': 'domain',
        'fw_version': 'fwVersion',
        'generation': 'generation',
        'id': 'id',
        'manufacturing': 'manufacturing',
        'max_lba': 'maxLBA',
        'name': 'name',
        'node_device_id': 'nodeDeviceId',
        'node_drive_id': 'nodeDriveId',
        'node_drive_type': 'nodeDriveType',
        'node_id': 'nodeId',
        'request_uri': 'requestUri',
        'resource_uri': 'resourceUri',
        'sed_state': 'sedState',
        'size_mi_b': 'sizeMiB',
        'system_id': 'systemId',
        'type': 'type',
        'wwn': 'wwn'
    }

    def __init__(self, associated_links=None, console_uri=None, customer_id=None, displayname=None, domain=None, fw_version=None, generation=None, id=None, manufacturing=None, max_lba=None, name=None, node_device_id=None, node_drive_id=None, node_drive_type=None, node_id=None, request_uri=None, resource_uri=None, sed_state=None, size_mi_b=None, system_id=None, type=None, wwn=None):  # noqa: E501
        """NodeDriveDetails - a model defined in OpenAPI"""  # noqa: E501

        self._associated_links = None
        self._console_uri = None
        self._customer_id = None
        self._displayname = None
        self._domain = None
        self._fw_version = None
        self._generation = None
        self._id = None
        self._manufacturing = None
        self._max_lba = None
        self._name = None
        self._node_device_id = None
        self._node_drive_id = None
        self._node_drive_type = None
        self._node_id = None
        self._request_uri = None
        self._resource_uri = None
        self._sed_state = None
        self._size_mi_b = None
        self._system_id = None
        self._type = None
        self._wwn = None
        self.discriminator = None

        if associated_links is not None:
            self.associated_links = associated_links
        if console_uri is not None:
            self.console_uri = console_uri
        if customer_id is not None:
            self.customer_id = customer_id
        if displayname is not None:
            self.displayname = displayname
        if domain is not None:
            self.domain = domain
        if fw_version is not None:
            self.fw_version = fw_version
        if generation is not None:
            self.generation = generation
        if id is not None:
            self.id = id
        if manufacturing is not None:
            self.manufacturing = manufacturing
        if max_lba is not None:
            self.max_lba = max_lba
        if name is not None:
            self.name = name
        if node_device_id is not None:
            self.node_device_id = node_device_id
        if node_drive_id is not None:
            self.node_drive_id = node_drive_id
        if node_drive_type is not None:
            self.node_drive_type = node_drive_type
        if node_id is not None:
            self.node_id = node_id
        if request_uri is not None:
            self.request_uri = request_uri
        if resource_uri is not None:
            self.resource_uri = resource_uri
        if sed_state is not None:
            self.sed_state = sed_state
        if size_mi_b is not None:
            self.size_mi_b = size_mi_b
        if system_id is not None:
            self.system_id = system_id
        if type is not None:
            self.type = type
        if wwn is not None:
            self.wwn = wwn

    @property
    def associated_links(self):
        """Gets the associated_links of this NodeDriveDetails.  # noqa: E501

        Associated Links Details  # noqa: E501

        :return: The associated_links of this NodeDriveDetails.  # noqa: E501
        :rtype: list[AssociatedLinksInner]
        """
        return self._associated_links

    @associated_links.setter
    def associated_links(self, associated_links):
        """Sets the associated_links of this NodeDriveDetails.

        Associated Links Details  # noqa: E501

        :param associated_links: The associated_links of this NodeDriveDetails.  # noqa: E501
        :type: list[AssociatedLinksInner]
        """

        self._associated_links = associated_links

    @property
    def console_uri(self):
        """Gets the console_uri of this NodeDriveDetails.  # noqa: E501

        consoleUri for detailed storage object  # noqa: E501

        :return: The console_uri of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this NodeDriveDetails.

        consoleUri for detailed storage object  # noqa: E501

        :param console_uri: The console_uri of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def customer_id(self):
        """Gets the customer_id of this NodeDriveDetails.  # noqa: E501

        customerId  # noqa: E501

        :return: The customer_id of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this NodeDriveDetails.

        customerId  # noqa: E501

        :param customer_id: The customer_id of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def displayname(self):
        """Gets the displayname of this NodeDriveDetails.  # noqa: E501

        Name to be used for display purposes  # noqa: E501

        :return: The displayname of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._displayname

    @displayname.setter
    def displayname(self, displayname):
        """Sets the displayname of this NodeDriveDetails.

        Name to be used for display purposes  # noqa: E501

        :param displayname: The displayname of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._displayname = displayname

    @property
    def domain(self):
        """Gets the domain of this NodeDriveDetails.  # noqa: E501

        Domain that the resource belongs to  # noqa: E501

        :return: The domain of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this NodeDriveDetails.

        Domain that the resource belongs to  # noqa: E501

        :param domain: The domain of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def fw_version(self):
        """Gets the fw_version of this NodeDriveDetails.  # noqa: E501

        Firmware version  # noqa: E501

        :return: The fw_version of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._fw_version

    @fw_version.setter
    def fw_version(self, fw_version):
        """Sets the fw_version of this NodeDriveDetails.

        Firmware version  # noqa: E501

        :param fw_version: The fw_version of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._fw_version = fw_version

    @property
    def generation(self):
        """Gets the generation of this NodeDriveDetails.  # noqa: E501

        generation  # noqa: E501

        :return: The generation of this NodeDriveDetails.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this NodeDriveDetails.

        generation  # noqa: E501

        :param generation: The generation of this NodeDriveDetails.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def id(self):
        """Gets the id of this NodeDriveDetails.  # noqa: E501

        Unique Identifier of the resource.  # noqa: E501

        :return: The id of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeDriveDetails.

        Unique Identifier of the resource.  # noqa: E501

        :param id: The id of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def manufacturing(self):
        """Gets the manufacturing of this NodeDriveDetails.  # noqa: E501


        :return: The manufacturing of this NodeDriveDetails.  # noqa: E501
        :rtype: ManufacturingSingle
        """
        return self._manufacturing

    @manufacturing.setter
    def manufacturing(self, manufacturing):
        """Sets the manufacturing of this NodeDriveDetails.


        :param manufacturing: The manufacturing of this NodeDriveDetails.  # noqa: E501
        :type: ManufacturingSingle
        """

        self._manufacturing = manufacturing

    @property
    def max_lba(self):
        """Gets the max_lba of this NodeDriveDetails.  # noqa: E501

        Max Logical Block Address  # noqa: E501

        :return: The max_lba of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._max_lba

    @max_lba.setter
    def max_lba(self, max_lba):
        """Sets the max_lba of this NodeDriveDetails.

        Max Logical Block Address  # noqa: E501

        :param max_lba: The max_lba of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._max_lba = max_lba

    @property
    def name(self):
        """Gets the name of this NodeDriveDetails.  # noqa: E501

        Name of the resource.  # noqa: E501

        :return: The name of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeDriveDetails.

        Name of the resource.  # noqa: E501

        :param name: The name of this NodeDriveDetails.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def node_device_id(self):
        """Gets the node_device_id of this NodeDriveDetails.  # noqa: E501

        ID of the node  # noqa: E501

        :return: The node_device_id of this NodeDriveDetails.  # noqa: E501
        :rtype: int
        """
        return self._node_device_id

    @node_device_id.setter
    def node_device_id(self, node_device_id):
        """Sets the node_device_id of this NodeDriveDetails.

        ID of the node  # noqa: E501

        :param node_device_id: The node_device_id of this NodeDriveDetails.  # noqa: E501
        :type: int
        """

        self._node_device_id = node_device_id

    @property
    def node_drive_id(self):
        """Gets the node_drive_id of this NodeDriveDetails.  # noqa: E501

        Numeric ID of the resource  # noqa: E501

        :return: The node_drive_id of this NodeDriveDetails.  # noqa: E501
        :rtype: int
        """
        return self._node_drive_id

    @node_drive_id.setter
    def node_drive_id(self, node_drive_id):
        """Sets the node_drive_id of this NodeDriveDetails.

        Numeric ID of the resource  # noqa: E501

        :param node_drive_id: The node_drive_id of this NodeDriveDetails.  # noqa: E501
        :type: int
        """

        self._node_drive_id = node_drive_id

    @property
    def node_drive_type(self):
        """Gets the node_drive_type of this NodeDriveDetails.  # noqa: E501

        Node type  # noqa: E501

        :return: The node_drive_type of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._node_drive_type

    @node_drive_type.setter
    def node_drive_type(self, node_drive_type):
        """Sets the node_drive_type of this NodeDriveDetails.

        Node type  # noqa: E501

        :param node_drive_type: The node_drive_type of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._node_drive_type = node_drive_type

    @property
    def node_id(self):
        """Gets the node_id of this NodeDriveDetails.  # noqa: E501

        Unique Identifier of the node.  # noqa: E501

        :return: The node_id of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this NodeDriveDetails.

        Unique Identifier of the node.  # noqa: E501

        :param node_id: The node_id of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def request_uri(self):
        """Gets the request_uri of this NodeDriveDetails.  # noqa: E501

        requestUri for detailed node object  # noqa: E501

        :return: The request_uri of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri):
        """Sets the request_uri of this NodeDriveDetails.

        requestUri for detailed node object  # noqa: E501

        :param request_uri: The request_uri of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._request_uri = request_uri

    @property
    def resource_uri(self):
        """Gets the resource_uri of this NodeDriveDetails.  # noqa: E501

        resourceUri for detailed node object  # noqa: E501

        :return: The resource_uri of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this NodeDriveDetails.

        resourceUri for detailed node object  # noqa: E501

        :param resource_uri: The resource_uri of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

    @property
    def sed_state(self):
        """Gets the sed_state of this NodeDriveDetails.  # noqa: E501

        SED state  # noqa: E501

        :return: The sed_state of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._sed_state

    @sed_state.setter
    def sed_state(self, sed_state):
        """Sets the sed_state of this NodeDriveDetails.

        SED state  # noqa: E501

        :param sed_state: The sed_state of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._sed_state = sed_state

    @property
    def size_mi_b(self):
        """Gets the size_mi_b of this NodeDriveDetails.  # noqa: E501

        Size in MiB.  # noqa: E501

        :return: The size_mi_b of this NodeDriveDetails.  # noqa: E501
        :rtype: int
        """
        return self._size_mi_b

    @size_mi_b.setter
    def size_mi_b(self, size_mi_b):
        """Sets the size_mi_b of this NodeDriveDetails.

        Size in MiB.  # noqa: E501

        :param size_mi_b: The size_mi_b of this NodeDriveDetails.  # noqa: E501
        :type: int
        """

        self._size_mi_b = size_mi_b

    @property
    def system_id(self):
        """Gets the system_id of this NodeDriveDetails.  # noqa: E501

        SystemId/Serial Number  of the array.  # noqa: E501

        :return: The system_id of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this NodeDriveDetails.

        SystemId/Serial Number  of the array.  # noqa: E501

        :param system_id: The system_id of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def type(self):
        """Gets the type of this NodeDriveDetails.  # noqa: E501

        type  # noqa: E501

        :return: The type of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodeDriveDetails.

        type  # noqa: E501

        :param type: The type of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def wwn(self):
        """Gets the wwn of this NodeDriveDetails.  # noqa: E501

        Unique World Wide Name  # noqa: E501

        :return: The wwn of this NodeDriveDetails.  # noqa: E501
        :rtype: str
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """Sets the wwn of this NodeDriveDetails.

        Unique World Wide Name  # noqa: E501

        :param wwn: The wwn of this NodeDriveDetails.  # noqa: E501
        :type: str
        """

        self._wwn = wwn

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
        if not isinstance(other, NodeDriveDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other