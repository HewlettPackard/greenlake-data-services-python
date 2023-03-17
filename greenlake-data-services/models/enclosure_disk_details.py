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


class EnclosureDiskDetails(object):
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
        'associated_links': 'EdAssociatedLinks',
        'console_uri': 'str',
        'customer_id': 'str',
        'dc4data': 'EdDc4data',
        'dcsdata': 'EdDcsdata',
        'displayname': 'str',
        'domain': 'str',
        'enclosure_device_id': 'int',
        'enclosure_id': 'str',
        'enclosure_name': 'str',
        'enclosure_type': 'EnclosureTypeSingle',
        'generation': 'int',
        'id': 'str',
        'loop_a': 'EnclosureDiskLoop',
        'loop_b': 'EnclosureDiskLoop',
        'manufacturing': 'ManufacturingSingle',
        'name': 'str',
        'position': 'DiskPosition',
        'request_uri': 'str',
        'resource_uri': 'str',
        'system_id': 'str',
        'temperature': 'int',
        'type': 'str',
        'wwn': 'str'
    }

    attribute_map = {
        'associated_links': 'associatedLinks',
        'console_uri': 'consoleUri',
        'customer_id': 'customerId',
        'dc4data': 'dc4data',
        'dcsdata': 'dcsdata',
        'displayname': 'displayname',
        'domain': 'domain',
        'enclosure_device_id': 'enclosureDeviceId',
        'enclosure_id': 'enclosureId',
        'enclosure_name': 'enclosureName',
        'enclosure_type': 'enclosureType',
        'generation': 'generation',
        'id': 'id',
        'loop_a': 'loopA',
        'loop_b': 'loopB',
        'manufacturing': 'manufacturing',
        'name': 'name',
        'position': 'position',
        'request_uri': 'requestUri',
        'resource_uri': 'resourceUri',
        'system_id': 'systemId',
        'temperature': 'temperature',
        'type': 'type',
        'wwn': 'wwn'
    }

    def __init__(self, associated_links=None, console_uri=None, customer_id=None, dc4data=None, dcsdata=None, displayname=None, domain=None, enclosure_device_id=None, enclosure_id=None, enclosure_name=None, enclosure_type=None, generation=None, id=None, loop_a=None, loop_b=None, manufacturing=None, name=None, position=None, request_uri=None, resource_uri=None, system_id=None, temperature=None, type=None, wwn=None):  # noqa: E501
        """EnclosureDiskDetails - a model defined in OpenAPI"""  # noqa: E501

        self._associated_links = None
        self._console_uri = None
        self._customer_id = None
        self._dc4data = None
        self._dcsdata = None
        self._displayname = None
        self._domain = None
        self._enclosure_device_id = None
        self._enclosure_id = None
        self._enclosure_name = None
        self._enclosure_type = None
        self._generation = None
        self._id = None
        self._loop_a = None
        self._loop_b = None
        self._manufacturing = None
        self._name = None
        self._position = None
        self._request_uri = None
        self._resource_uri = None
        self._system_id = None
        self._temperature = None
        self._type = None
        self._wwn = None
        self.discriminator = None

        if associated_links is not None:
            self.associated_links = associated_links
        if console_uri is not None:
            self.console_uri = console_uri
        if customer_id is not None:
            self.customer_id = customer_id
        if dc4data is not None:
            self.dc4data = dc4data
        if dcsdata is not None:
            self.dcsdata = dcsdata
        if displayname is not None:
            self.displayname = displayname
        if domain is not None:
            self.domain = domain
        if enclosure_device_id is not None:
            self.enclosure_device_id = enclosure_device_id
        if enclosure_id is not None:
            self.enclosure_id = enclosure_id
        if enclosure_name is not None:
            self.enclosure_name = enclosure_name
        if enclosure_type is not None:
            self.enclosure_type = enclosure_type
        if generation is not None:
            self.generation = generation
        if id is not None:
            self.id = id
        if loop_a is not None:
            self.loop_a = loop_a
        if loop_b is not None:
            self.loop_b = loop_b
        if manufacturing is not None:
            self.manufacturing = manufacturing
        if name is not None:
            self.name = name
        if position is not None:
            self.position = position
        if request_uri is not None:
            self.request_uri = request_uri
        if resource_uri is not None:
            self.resource_uri = resource_uri
        if system_id is not None:
            self.system_id = system_id
        if temperature is not None:
            self.temperature = temperature
        if type is not None:
            self.type = type
        if wwn is not None:
            self.wwn = wwn

    @property
    def associated_links(self):
        """Gets the associated_links of this EnclosureDiskDetails.  # noqa: E501


        :return: The associated_links of this EnclosureDiskDetails.  # noqa: E501
        :rtype: EdAssociatedLinks
        """
        return self._associated_links

    @associated_links.setter
    def associated_links(self, associated_links):
        """Sets the associated_links of this EnclosureDiskDetails.


        :param associated_links: The associated_links of this EnclosureDiskDetails.  # noqa: E501
        :type: EdAssociatedLinks
        """

        self._associated_links = associated_links

    @property
    def console_uri(self):
        """Gets the console_uri of this EnclosureDiskDetails.  # noqa: E501

        consoleUri for detailed storage object  # noqa: E501

        :return: The console_uri of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this EnclosureDiskDetails.

        consoleUri for detailed storage object  # noqa: E501

        :param console_uri: The console_uri of this EnclosureDiskDetails.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def customer_id(self):
        """Gets the customer_id of this EnclosureDiskDetails.  # noqa: E501

        customerId  # noqa: E501

        :return: The customer_id of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this EnclosureDiskDetails.

        customerId  # noqa: E501

        :param customer_id: The customer_id of this EnclosureDiskDetails.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def dc4data(self):
        """Gets the dc4data of this EnclosureDiskDetails.  # noqa: E501


        :return: The dc4data of this EnclosureDiskDetails.  # noqa: E501
        :rtype: EdDc4data
        """
        return self._dc4data

    @dc4data.setter
    def dc4data(self, dc4data):
        """Sets the dc4data of this EnclosureDiskDetails.


        :param dc4data: The dc4data of this EnclosureDiskDetails.  # noqa: E501
        :type: EdDc4data
        """

        self._dc4data = dc4data

    @property
    def dcsdata(self):
        """Gets the dcsdata of this EnclosureDiskDetails.  # noqa: E501


        :return: The dcsdata of this EnclosureDiskDetails.  # noqa: E501
        :rtype: EdDcsdata
        """
        return self._dcsdata

    @dcsdata.setter
    def dcsdata(self, dcsdata):
        """Sets the dcsdata of this EnclosureDiskDetails.


        :param dcsdata: The dcsdata of this EnclosureDiskDetails.  # noqa: E501
        :type: EdDcsdata
        """

        self._dcsdata = dcsdata

    @property
    def displayname(self):
        """Gets the displayname of this EnclosureDiskDetails.  # noqa: E501

        Enclosure Display name  # noqa: E501

        :return: The displayname of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._displayname

    @displayname.setter
    def displayname(self, displayname):
        """Sets the displayname of this EnclosureDiskDetails.

        Enclosure Display name  # noqa: E501

        :param displayname: The displayname of this EnclosureDiskDetails.  # noqa: E501
        :type: str
        """

        self._displayname = displayname

    @property
    def domain(self):
        """Gets the domain of this EnclosureDiskDetails.  # noqa: E501

        Domain that the resource belongs to  # noqa: E501

        :return: The domain of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this EnclosureDiskDetails.

        Domain that the resource belongs to  # noqa: E501

        :param domain: The domain of this EnclosureDiskDetails.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def enclosure_device_id(self):
        """Gets the enclosure_device_id of this EnclosureDiskDetails.  # noqa: E501


        :return: The enclosure_device_id of this EnclosureDiskDetails.  # noqa: E501
        :rtype: int
        """
        return self._enclosure_device_id

    @enclosure_device_id.setter
    def enclosure_device_id(self, enclosure_device_id):
        """Sets the enclosure_device_id of this EnclosureDiskDetails.


        :param enclosure_device_id: The enclosure_device_id of this EnclosureDiskDetails.  # noqa: E501
        :type: int
        """

        self._enclosure_device_id = enclosure_device_id

    @property
    def enclosure_id(self):
        """Gets the enclosure_id of this EnclosureDiskDetails.  # noqa: E501

        Parent UID of the resource.  # noqa: E501

        :return: The enclosure_id of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._enclosure_id

    @enclosure_id.setter
    def enclosure_id(self, enclosure_id):
        """Sets the enclosure_id of this EnclosureDiskDetails.

        Parent UID of the resource.  # noqa: E501

        :param enclosure_id: The enclosure_id of this EnclosureDiskDetails.  # noqa: E501
        :type: str
        """

        self._enclosure_id = enclosure_id

    @property
    def enclosure_name(self):
        """Gets the enclosure_name of this EnclosureDiskDetails.  # noqa: E501

        Name of the enclosure  # noqa: E501

        :return: The enclosure_name of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._enclosure_name

    @enclosure_name.setter
    def enclosure_name(self, enclosure_name):
        """Sets the enclosure_name of this EnclosureDiskDetails.

        Name of the enclosure  # noqa: E501

        :param enclosure_name: The enclosure_name of this EnclosureDiskDetails.  # noqa: E501
        :type: str
        """

        self._enclosure_name = enclosure_name

    @property
    def enclosure_type(self):
        """Gets the enclosure_type of this EnclosureDiskDetails.  # noqa: E501


        :return: The enclosure_type of this EnclosureDiskDetails.  # noqa: E501
        :rtype: EnclosureTypeSingle
        """
        return self._enclosure_type

    @enclosure_type.setter
    def enclosure_type(self, enclosure_type):
        """Sets the enclosure_type of this EnclosureDiskDetails.


        :param enclosure_type: The enclosure_type of this EnclosureDiskDetails.  # noqa: E501
        :type: EnclosureTypeSingle
        """

        self._enclosure_type = enclosure_type

    @property
    def generation(self):
        """Gets the generation of this EnclosureDiskDetails.  # noqa: E501

        generation  # noqa: E501

        :return: The generation of this EnclosureDiskDetails.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this EnclosureDiskDetails.

        generation  # noqa: E501

        :param generation: The generation of this EnclosureDiskDetails.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def id(self):
        """Gets the id of this EnclosureDiskDetails.  # noqa: E501

        Unique Identifier of the resource.  # noqa: E501

        :return: The id of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnclosureDiskDetails.

        Unique Identifier of the resource.  # noqa: E501

        :param id: The id of this EnclosureDiskDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def loop_a(self):
        """Gets the loop_a of this EnclosureDiskDetails.  # noqa: E501


        :return: The loop_a of this EnclosureDiskDetails.  # noqa: E501
        :rtype: EnclosureDiskLoop
        """
        return self._loop_a

    @loop_a.setter
    def loop_a(self, loop_a):
        """Sets the loop_a of this EnclosureDiskDetails.


        :param loop_a: The loop_a of this EnclosureDiskDetails.  # noqa: E501
        :type: EnclosureDiskLoop
        """

        self._loop_a = loop_a

    @property
    def loop_b(self):
        """Gets the loop_b of this EnclosureDiskDetails.  # noqa: E501


        :return: The loop_b of this EnclosureDiskDetails.  # noqa: E501
        :rtype: EnclosureDiskLoop
        """
        return self._loop_b

    @loop_b.setter
    def loop_b(self, loop_b):
        """Sets the loop_b of this EnclosureDiskDetails.


        :param loop_b: The loop_b of this EnclosureDiskDetails.  # noqa: E501
        :type: EnclosureDiskLoop
        """

        self._loop_b = loop_b

    @property
    def manufacturing(self):
        """Gets the manufacturing of this EnclosureDiskDetails.  # noqa: E501


        :return: The manufacturing of this EnclosureDiskDetails.  # noqa: E501
        :rtype: ManufacturingSingle
        """
        return self._manufacturing

    @manufacturing.setter
    def manufacturing(self, manufacturing):
        """Sets the manufacturing of this EnclosureDiskDetails.


        :param manufacturing: The manufacturing of this EnclosureDiskDetails.  # noqa: E501
        :type: ManufacturingSingle
        """

        self._manufacturing = manufacturing

    @property
    def name(self):
        """Gets the name of this EnclosureDiskDetails.  # noqa: E501

        Name of the resource.  # noqa: E501

        :return: The name of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnclosureDiskDetails.

        Name of the resource.  # noqa: E501

        :param name: The name of this EnclosureDiskDetails.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def position(self):
        """Gets the position of this EnclosureDiskDetails.  # noqa: E501


        :return: The position of this EnclosureDiskDetails.  # noqa: E501
        :rtype: DiskPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this EnclosureDiskDetails.


        :param position: The position of this EnclosureDiskDetails.  # noqa: E501
        :type: DiskPosition
        """

        self._position = position

    @property
    def request_uri(self):
        """Gets the request_uri of this EnclosureDiskDetails.  # noqa: E501

        resourceUri for detailed enclosure object  # noqa: E501

        :return: The request_uri of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri):
        """Sets the request_uri of this EnclosureDiskDetails.

        resourceUri for detailed enclosure object  # noqa: E501

        :param request_uri: The request_uri of this EnclosureDiskDetails.  # noqa: E501
        :type: str
        """

        self._request_uri = request_uri

    @property
    def resource_uri(self):
        """Gets the resource_uri of this EnclosureDiskDetails.  # noqa: E501

        resourceUri for detailed enclosure object  # noqa: E501

        :return: The resource_uri of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this EnclosureDiskDetails.

        resourceUri for detailed enclosure object  # noqa: E501

        :param resource_uri: The resource_uri of this EnclosureDiskDetails.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

    @property
    def system_id(self):
        """Gets the system_id of this EnclosureDiskDetails.  # noqa: E501

        SystemUid/Serial Number  of the array.  # noqa: E501

        :return: The system_id of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this EnclosureDiskDetails.

        SystemUid/Serial Number  of the array.  # noqa: E501

        :param system_id: The system_id of this EnclosureDiskDetails.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def temperature(self):
        """Gets the temperature of this EnclosureDiskDetails.  # noqa: E501

        temperature of the resource part  # noqa: E501

        :return: The temperature of this EnclosureDiskDetails.  # noqa: E501
        :rtype: int
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this EnclosureDiskDetails.

        temperature of the resource part  # noqa: E501

        :param temperature: The temperature of this EnclosureDiskDetails.  # noqa: E501
        :type: int
        """

        self._temperature = temperature

    @property
    def type(self):
        """Gets the type of this EnclosureDiskDetails.  # noqa: E501

        type  # noqa: E501

        :return: The type of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EnclosureDiskDetails.

        type  # noqa: E501

        :param type: The type of this EnclosureDiskDetails.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def wwn(self):
        """Gets the wwn of this EnclosureDiskDetails.  # noqa: E501

        WWN of the resource.  # noqa: E501

        :return: The wwn of this EnclosureDiskDetails.  # noqa: E501
        :rtype: str
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """Sets the wwn of this EnclosureDiskDetails.

        WWN of the resource.  # noqa: E501

        :param wwn: The wwn of this EnclosureDiskDetails.  # noqa: E501
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
        if not isinstance(other, EnclosureDiskDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other