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


class NodePowerSupplyDetails(object):
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
        'fanspeed': 'str',
        'fanstate': 'STATE',
        'generation': 'int',
        'id': 'str',
        'locate_enabled': 'bool',
        'manufacturing': 'ManufacturingSingle',
        'name': 'str',
        'node_power_id': 'int',
        'primary_node_id': 'int',
        'request_uri': 'str',
        'resource_uri': 'str',
        'safe_to_remove': 'bool',
        'secondary_node_id': 'int',
        'service_led': 'LED',
        'state': 'STATE',
        'system_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'associated_links': 'associatedLinks',
        'console_uri': 'consoleUri',
        'customer_id': 'customerId',
        'displayname': 'displayname',
        'domain': 'domain',
        'fanspeed': 'fanspeed',
        'fanstate': 'fanstate',
        'generation': 'generation',
        'id': 'id',
        'locate_enabled': 'locateEnabled',
        'manufacturing': 'manufacturing',
        'name': 'name',
        'node_power_id': 'nodePowerId',
        'primary_node_id': 'primaryNodeId',
        'request_uri': 'requestUri',
        'resource_uri': 'resourceUri',
        'safe_to_remove': 'safeToRemove',
        'secondary_node_id': 'secondaryNodeId',
        'service_led': 'serviceLED',
        'state': 'state',
        'system_id': 'systemId',
        'type': 'type'
    }

    def __init__(self, associated_links=None, console_uri=None, customer_id=None, displayname=None, domain=None, fanspeed=None, fanstate=None, generation=None, id=None, locate_enabled=None, manufacturing=None, name=None, node_power_id=None, primary_node_id=None, request_uri=None, resource_uri=None, safe_to_remove=None, secondary_node_id=None, service_led=None, state=None, system_id=None, type=None):  # noqa: E501
        """NodePowerSupplyDetails - a model defined in OpenAPI"""  # noqa: E501

        self._associated_links = None
        self._console_uri = None
        self._customer_id = None
        self._displayname = None
        self._domain = None
        self._fanspeed = None
        self._fanstate = None
        self._generation = None
        self._id = None
        self._locate_enabled = None
        self._manufacturing = None
        self._name = None
        self._node_power_id = None
        self._primary_node_id = None
        self._request_uri = None
        self._resource_uri = None
        self._safe_to_remove = None
        self._secondary_node_id = None
        self._service_led = None
        self._state = None
        self._system_id = None
        self._type = None
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
        if fanspeed is not None:
            self.fanspeed = fanspeed
        if fanstate is not None:
            self.fanstate = fanstate
        if generation is not None:
            self.generation = generation
        if id is not None:
            self.id = id
        if locate_enabled is not None:
            self.locate_enabled = locate_enabled
        if manufacturing is not None:
            self.manufacturing = manufacturing
        if name is not None:
            self.name = name
        if node_power_id is not None:
            self.node_power_id = node_power_id
        if primary_node_id is not None:
            self.primary_node_id = primary_node_id
        if request_uri is not None:
            self.request_uri = request_uri
        if resource_uri is not None:
            self.resource_uri = resource_uri
        if safe_to_remove is not None:
            self.safe_to_remove = safe_to_remove
        if secondary_node_id is not None:
            self.secondary_node_id = secondary_node_id
        if service_led is not None:
            self.service_led = service_led
        if state is not None:
            self.state = state
        if system_id is not None:
            self.system_id = system_id
        if type is not None:
            self.type = type

    @property
    def associated_links(self):
        """Gets the associated_links of this NodePowerSupplyDetails.  # noqa: E501

        Associated Links Details  # noqa: E501

        :return: The associated_links of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: list[AssociatedLinksInner]
        """
        return self._associated_links

    @associated_links.setter
    def associated_links(self, associated_links):
        """Sets the associated_links of this NodePowerSupplyDetails.

        Associated Links Details  # noqa: E501

        :param associated_links: The associated_links of this NodePowerSupplyDetails.  # noqa: E501
        :type: list[AssociatedLinksInner]
        """

        self._associated_links = associated_links

    @property
    def console_uri(self):
        """Gets the console_uri of this NodePowerSupplyDetails.  # noqa: E501

        consoleUri for detailed storage object  # noqa: E501

        :return: The console_uri of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this NodePowerSupplyDetails.

        consoleUri for detailed storage object  # noqa: E501

        :param console_uri: The console_uri of this NodePowerSupplyDetails.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def customer_id(self):
        """Gets the customer_id of this NodePowerSupplyDetails.  # noqa: E501

        customerId  # noqa: E501

        :return: The customer_id of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this NodePowerSupplyDetails.

        customerId  # noqa: E501

        :param customer_id: The customer_id of this NodePowerSupplyDetails.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def displayname(self):
        """Gets the displayname of this NodePowerSupplyDetails.  # noqa: E501

        Name to be used for display purposes  # noqa: E501

        :return: The displayname of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: str
        """
        return self._displayname

    @displayname.setter
    def displayname(self, displayname):
        """Sets the displayname of this NodePowerSupplyDetails.

        Name to be used for display purposes  # noqa: E501

        :param displayname: The displayname of this NodePowerSupplyDetails.  # noqa: E501
        :type: str
        """

        self._displayname = displayname

    @property
    def domain(self):
        """Gets the domain of this NodePowerSupplyDetails.  # noqa: E501

        Domain that the resource belongs to  # noqa: E501

        :return: The domain of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this NodePowerSupplyDetails.

        Domain that the resource belongs to  # noqa: E501

        :param domain: The domain of this NodePowerSupplyDetails.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def fanspeed(self):
        """Gets the fanspeed of this NodePowerSupplyDetails.  # noqa: E501

        Fan speed of the node power supply  # noqa: E501

        :return: The fanspeed of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: str
        """
        return self._fanspeed

    @fanspeed.setter
    def fanspeed(self, fanspeed):
        """Sets the fanspeed of this NodePowerSupplyDetails.

        Fan speed of the node power supply  # noqa: E501

        :param fanspeed: The fanspeed of this NodePowerSupplyDetails.  # noqa: E501
        :type: str
        """

        self._fanspeed = fanspeed

    @property
    def fanstate(self):
        """Gets the fanstate of this NodePowerSupplyDetails.  # noqa: E501


        :return: The fanstate of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: STATE
        """
        return self._fanstate

    @fanstate.setter
    def fanstate(self, fanstate):
        """Sets the fanstate of this NodePowerSupplyDetails.


        :param fanstate: The fanstate of this NodePowerSupplyDetails.  # noqa: E501
        :type: STATE
        """

        self._fanstate = fanstate

    @property
    def generation(self):
        """Gets the generation of this NodePowerSupplyDetails.  # noqa: E501

        generation  # noqa: E501

        :return: The generation of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this NodePowerSupplyDetails.

        generation  # noqa: E501

        :param generation: The generation of this NodePowerSupplyDetails.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def id(self):
        """Gets the id of this NodePowerSupplyDetails.  # noqa: E501

        Unique Identifier of the resource.  # noqa: E501

        :return: The id of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodePowerSupplyDetails.

        Unique Identifier of the resource.  # noqa: E501

        :param id: The id of this NodePowerSupplyDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def locate_enabled(self):
        """Gets the locate_enabled of this NodePowerSupplyDetails.  # noqa: E501

        Indicates if the locate beacon is enabled or not  # noqa: E501

        :return: The locate_enabled of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._locate_enabled

    @locate_enabled.setter
    def locate_enabled(self, locate_enabled):
        """Sets the locate_enabled of this NodePowerSupplyDetails.

        Indicates if the locate beacon is enabled or not  # noqa: E501

        :param locate_enabled: The locate_enabled of this NodePowerSupplyDetails.  # noqa: E501
        :type: bool
        """

        self._locate_enabled = locate_enabled

    @property
    def manufacturing(self):
        """Gets the manufacturing of this NodePowerSupplyDetails.  # noqa: E501


        :return: The manufacturing of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: ManufacturingSingle
        """
        return self._manufacturing

    @manufacturing.setter
    def manufacturing(self, manufacturing):
        """Sets the manufacturing of this NodePowerSupplyDetails.


        :param manufacturing: The manufacturing of this NodePowerSupplyDetails.  # noqa: E501
        :type: ManufacturingSingle
        """

        self._manufacturing = manufacturing

    @property
    def name(self):
        """Gets the name of this NodePowerSupplyDetails.  # noqa: E501

        Name of the resource.  # noqa: E501

        :return: The name of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodePowerSupplyDetails.

        Name of the resource.  # noqa: E501

        :param name: The name of this NodePowerSupplyDetails.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def node_power_id(self):
        """Gets the node_power_id of this NodePowerSupplyDetails.  # noqa: E501

        Numeric ID of the resource  # noqa: E501

        :return: The node_power_id of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: int
        """
        return self._node_power_id

    @node_power_id.setter
    def node_power_id(self, node_power_id):
        """Sets the node_power_id of this NodePowerSupplyDetails.

        Numeric ID of the resource  # noqa: E501

        :param node_power_id: The node_power_id of this NodePowerSupplyDetails.  # noqa: E501
        :type: int
        """

        self._node_power_id = node_power_id

    @property
    def primary_node_id(self):
        """Gets the primary_node_id of this NodePowerSupplyDetails.  # noqa: E501

        Primary node ID.  # noqa: E501

        :return: The primary_node_id of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: int
        """
        return self._primary_node_id

    @primary_node_id.setter
    def primary_node_id(self, primary_node_id):
        """Sets the primary_node_id of this NodePowerSupplyDetails.

        Primary node ID.  # noqa: E501

        :param primary_node_id: The primary_node_id of this NodePowerSupplyDetails.  # noqa: E501
        :type: int
        """

        self._primary_node_id = primary_node_id

    @property
    def request_uri(self):
        """Gets the request_uri of this NodePowerSupplyDetails.  # noqa: E501

        requestUri for detailed node power object  # noqa: E501

        :return: The request_uri of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: str
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri):
        """Sets the request_uri of this NodePowerSupplyDetails.

        requestUri for detailed node power object  # noqa: E501

        :param request_uri: The request_uri of this NodePowerSupplyDetails.  # noqa: E501
        :type: str
        """

        self._request_uri = request_uri

    @property
    def resource_uri(self):
        """Gets the resource_uri of this NodePowerSupplyDetails.  # noqa: E501

        resourceUri for detailed node power object  # noqa: E501

        :return: The resource_uri of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this NodePowerSupplyDetails.

        resourceUri for detailed node power object  # noqa: E501

        :param resource_uri: The resource_uri of this NodePowerSupplyDetails.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

    @property
    def safe_to_remove(self):
        """Gets the safe_to_remove of this NodePowerSupplyDetails.  # noqa: E501

        Indicates if the component is safe to remove  # noqa: E501

        :return: The safe_to_remove of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._safe_to_remove

    @safe_to_remove.setter
    def safe_to_remove(self, safe_to_remove):
        """Sets the safe_to_remove of this NodePowerSupplyDetails.

        Indicates if the component is safe to remove  # noqa: E501

        :param safe_to_remove: The safe_to_remove of this NodePowerSupplyDetails.  # noqa: E501
        :type: bool
        """

        self._safe_to_remove = safe_to_remove

    @property
    def secondary_node_id(self):
        """Gets the secondary_node_id of this NodePowerSupplyDetails.  # noqa: E501

        Secondary node ID  # noqa: E501

        :return: The secondary_node_id of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: int
        """
        return self._secondary_node_id

    @secondary_node_id.setter
    def secondary_node_id(self, secondary_node_id):
        """Sets the secondary_node_id of this NodePowerSupplyDetails.

        Secondary node ID  # noqa: E501

        :param secondary_node_id: The secondary_node_id of this NodePowerSupplyDetails.  # noqa: E501
        :type: int
        """

        self._secondary_node_id = secondary_node_id

    @property
    def service_led(self):
        """Gets the service_led of this NodePowerSupplyDetails.  # noqa: E501


        :return: The service_led of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: LED
        """
        return self._service_led

    @service_led.setter
    def service_led(self, service_led):
        """Sets the service_led of this NodePowerSupplyDetails.


        :param service_led: The service_led of this NodePowerSupplyDetails.  # noqa: E501
        :type: LED
        """

        self._service_led = service_led

    @property
    def state(self):
        """Gets the state of this NodePowerSupplyDetails.  # noqa: E501


        :return: The state of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: STATE
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NodePowerSupplyDetails.


        :param state: The state of this NodePowerSupplyDetails.  # noqa: E501
        :type: STATE
        """

        self._state = state

    @property
    def system_id(self):
        """Gets the system_id of this NodePowerSupplyDetails.  # noqa: E501

        SystemUid/Serial Number  of the array.  # noqa: E501

        :return: The system_id of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this NodePowerSupplyDetails.

        SystemUid/Serial Number  of the array.  # noqa: E501

        :param system_id: The system_id of this NodePowerSupplyDetails.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def type(self):
        """Gets the type of this NodePowerSupplyDetails.  # noqa: E501

        type  # noqa: E501

        :return: The type of this NodePowerSupplyDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodePowerSupplyDetails.

        type  # noqa: E501

        :param type: The type of this NodePowerSupplyDetails.  # noqa: E501
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
        if not isinstance(other, NodePowerSupplyDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
