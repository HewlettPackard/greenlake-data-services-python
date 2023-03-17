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


class NimbleFibreChannelConfigsDetails(object):
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
        'array_list': 'list[NimbleArraysList]',
        'associated_links': 'AssociatedLinks',
        'console_uri': 'str',
        'controller_name': 'str',
        'customer_id': 'str',
        'generation': 'int',
        'group_leader_array': 'str',
        'id': 'str',
        'resource_uri': 'str',
        'type': 'str'
    }

    attribute_map = {
        'array_list': 'array_list',
        'associated_links': 'associated_links',
        'console_uri': 'consoleUri',
        'controller_name': 'controller_name',
        'customer_id': 'customerId',
        'generation': 'generation',
        'group_leader_array': 'group_leader_array',
        'id': 'id',
        'resource_uri': 'resourceUri',
        'type': 'type'
    }

    def __init__(self, array_list=None, associated_links=None, console_uri=None, controller_name=None, customer_id=None, generation=None, group_leader_array=None, id=None, resource_uri=None, type=None):  # noqa: E501
        """NimbleFibreChannelConfigsDetails - a model defined in OpenAPI"""  # noqa: E501

        self._array_list = None
        self._associated_links = None
        self._console_uri = None
        self._controller_name = None
        self._customer_id = None
        self._generation = None
        self._group_leader_array = None
        self._id = None
        self._resource_uri = None
        self._type = None
        self.discriminator = None

        if array_list is not None:
            self.array_list = array_list
        if associated_links is not None:
            self.associated_links = associated_links
        if console_uri is not None:
            self.console_uri = console_uri
        if controller_name is not None:
            self.controller_name = controller_name
        if customer_id is not None:
            self.customer_id = customer_id
        if generation is not None:
            self.generation = generation
        if group_leader_array is not None:
            self.group_leader_array = group_leader_array
        if id is not None:
            self.id = id
        if resource_uri is not None:
            self.resource_uri = resource_uri
        if type is not None:
            self.type = type

    @property
    def array_list(self):
        """Gets the array_list of this NimbleFibreChannelConfigsDetails.  # noqa: E501

        List of array Fibre Channel configs. List of array Fibre Channel configurations.  # noqa: E501

        :return: The array_list of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :rtype: list[NimbleArraysList]
        """
        return self._array_list

    @array_list.setter
    def array_list(self, array_list):
        """Sets the array_list of this NimbleFibreChannelConfigsDetails.

        List of array Fibre Channel configs. List of array Fibre Channel configurations.  # noqa: E501

        :param array_list: The array_list of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :type: list[NimbleArraysList]
        """

        self._array_list = array_list

    @property
    def associated_links(self):
        """Gets the associated_links of this NimbleFibreChannelConfigsDetails.  # noqa: E501


        :return: The associated_links of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :rtype: AssociatedLinks
        """
        return self._associated_links

    @associated_links.setter
    def associated_links(self, associated_links):
        """Sets the associated_links of this NimbleFibreChannelConfigsDetails.


        :param associated_links: The associated_links of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :type: AssociatedLinks
        """

        self._associated_links = associated_links

    @property
    def console_uri(self):
        """Gets the console_uri of this NimbleFibreChannelConfigsDetails.  # noqa: E501

        consoleUri for detailed storage object  # noqa: E501

        :return: The console_uri of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this NimbleFibreChannelConfigsDetails.

        consoleUri for detailed storage object  # noqa: E501

        :param console_uri: The console_uri of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def controller_name(self):
        """Gets the controller_name of this NimbleFibreChannelConfigsDetails.  # noqa: E501

        Name (A or B) of the controller where the interface is hosted. Plain string.  # noqa: E501

        :return: The controller_name of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :rtype: str
        """
        return self._controller_name

    @controller_name.setter
    def controller_name(self, controller_name):
        """Sets the controller_name of this NimbleFibreChannelConfigsDetails.

        Name (A or B) of the controller where the interface is hosted. Plain string.  # noqa: E501

        :param controller_name: The controller_name of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :type: str
        """

        self._controller_name = controller_name

    @property
    def customer_id(self):
        """Gets the customer_id of this NimbleFibreChannelConfigsDetails.  # noqa: E501

        customerId  # noqa: E501

        :return: The customer_id of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this NimbleFibreChannelConfigsDetails.

        customerId  # noqa: E501

        :param customer_id: The customer_id of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def generation(self):
        """Gets the generation of this NimbleFibreChannelConfigsDetails.  # noqa: E501

        generation  # noqa: E501

        :return: The generation of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this NimbleFibreChannelConfigsDetails.

        generation  # noqa: E501

        :param generation: The generation of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def group_leader_array(self):
        """Gets the group_leader_array of this NimbleFibreChannelConfigsDetails.  # noqa: E501

        Name of the group leader array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :return: The group_leader_array of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :rtype: str
        """
        return self._group_leader_array

    @group_leader_array.setter
    def group_leader_array(self, group_leader_array):
        """Sets the group_leader_array of this NimbleFibreChannelConfigsDetails.

        Name of the group leader array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  # noqa: E501

        :param group_leader_array: The group_leader_array of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :type: str
        """

        self._group_leader_array = group_leader_array

    @property
    def id(self):
        """Gets the id of this NimbleFibreChannelConfigsDetails.  # noqa: E501

        Identifier for the array. A 42 digit hexadecimal number.  # noqa: E501

        :return: The id of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NimbleFibreChannelConfigsDetails.

        Identifier for the array. A 42 digit hexadecimal number.  # noqa: E501

        :param id: The id of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_uri(self):
        """Gets the resource_uri of this NimbleFibreChannelConfigsDetails.  # noqa: E501


        :return: The resource_uri of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this NimbleFibreChannelConfigsDetails.


        :param resource_uri: The resource_uri of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

    @property
    def type(self):
        """Gets the type of this NimbleFibreChannelConfigsDetails.  # noqa: E501

        type  # noqa: E501

        :return: The type of this NimbleFibreChannelConfigsDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NimbleFibreChannelConfigsDetails.

        type  # noqa: E501

        :param type: The type of this NimbleFibreChannelConfigsDetails.  # noqa: E501
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
        if not isinstance(other, NimbleFibreChannelConfigsDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
