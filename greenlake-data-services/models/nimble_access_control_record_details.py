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


class NimbleAccessControlRecordDetails(object):
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
        'apply_to': 'str',
        'associated_links': 'AssociatedLinks',
        'console_uri': 'str',
        'customer_id': 'str',
        'generation': 'int',
        'pe_ids': 'list[str]',
        'resource_uri': 'str',
        'snapluns': 'list[NimbleNsSnapLunInfo]',
        'type': 'str',
        'vol_agent_type': 'str'
    }

    attribute_map = {
        'apply_to': 'apply_to',
        'associated_links': 'associated_links',
        'console_uri': 'consoleUri',
        'customer_id': 'customerId',
        'generation': 'generation',
        'pe_ids': 'pe_ids',
        'resource_uri': 'resourceUri',
        'snapluns': 'snapluns',
        'type': 'type',
        'vol_agent_type': 'vol_agent_type'
    }

    def __init__(self, apply_to=None, associated_links=None, console_uri=None, customer_id=None, generation=None, pe_ids=None, resource_uri=None, snapluns=None, type=None, vol_agent_type=None):  # noqa: E501
        """NimbleAccessControlRecordDetails - a model defined in OpenAPI"""  # noqa: E501

        self._apply_to = None
        self._associated_links = None
        self._console_uri = None
        self._customer_id = None
        self._generation = None
        self._pe_ids = None
        self._resource_uri = None
        self._snapluns = None
        self._type = None
        self._vol_agent_type = None
        self.discriminator = None

        if apply_to is not None:
            self.apply_to = apply_to
        if associated_links is not None:
            self.associated_links = associated_links
        if console_uri is not None:
            self.console_uri = console_uri
        if customer_id is not None:
            self.customer_id = customer_id
        if generation is not None:
            self.generation = generation
        if pe_ids is not None:
            self.pe_ids = pe_ids
        if resource_uri is not None:
            self.resource_uri = resource_uri
        if snapluns is not None:
            self.snapluns = snapluns
        if type is not None:
            self.type = type
        if vol_agent_type is not None:
            self.vol_agent_type = vol_agent_type

    @property
    def apply_to(self):
        """Gets the apply_to of this NimbleAccessControlRecordDetails.  # noqa: E501

        External management agent type. Possible values:'volume', 'pe', 'vvol_volume', 'vvol_snapshot', 'snapshot', 'both'.  # noqa: E501

        :return: The apply_to of this NimbleAccessControlRecordDetails.  # noqa: E501
        :rtype: str
        """
        return self._apply_to

    @apply_to.setter
    def apply_to(self, apply_to):
        """Sets the apply_to of this NimbleAccessControlRecordDetails.

        External management agent type. Possible values:'volume', 'pe', 'vvol_volume', 'vvol_snapshot', 'snapshot', 'both'.  # noqa: E501

        :param apply_to: The apply_to of this NimbleAccessControlRecordDetails.  # noqa: E501
        :type: str
        """

        self._apply_to = apply_to

    @property
    def associated_links(self):
        """Gets the associated_links of this NimbleAccessControlRecordDetails.  # noqa: E501


        :return: The associated_links of this NimbleAccessControlRecordDetails.  # noqa: E501
        :rtype: AssociatedLinks
        """
        return self._associated_links

    @associated_links.setter
    def associated_links(self, associated_links):
        """Sets the associated_links of this NimbleAccessControlRecordDetails.


        :param associated_links: The associated_links of this NimbleAccessControlRecordDetails.  # noqa: E501
        :type: AssociatedLinks
        """

        self._associated_links = associated_links

    @property
    def console_uri(self):
        """Gets the console_uri of this NimbleAccessControlRecordDetails.  # noqa: E501

        consoleUri for detailed storage object  # noqa: E501

        :return: The console_uri of this NimbleAccessControlRecordDetails.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this NimbleAccessControlRecordDetails.

        consoleUri for detailed storage object  # noqa: E501

        :param console_uri: The console_uri of this NimbleAccessControlRecordDetails.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def customer_id(self):
        """Gets the customer_id of this NimbleAccessControlRecordDetails.  # noqa: E501

        customerId  # noqa: E501

        :return: The customer_id of this NimbleAccessControlRecordDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this NimbleAccessControlRecordDetails.

        customerId  # noqa: E501

        :param customer_id: The customer_id of this NimbleAccessControlRecordDetails.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def generation(self):
        """Gets the generation of this NimbleAccessControlRecordDetails.  # noqa: E501

        generation  # noqa: E501

        :return: The generation of this NimbleAccessControlRecordDetails.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this NimbleAccessControlRecordDetails.

        generation  # noqa: E501

        :param generation: The generation of this NimbleAccessControlRecordDetails.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def pe_ids(self):
        """Gets the pe_ids of this NimbleAccessControlRecordDetails.  # noqa: E501

        List of candidate protocol endpoints that may be used to access the Virtual Volume. One of them will be selected for the access control record. This field is required only when creating an access control record for a Virtual Volume.  # noqa: E501

        :return: The pe_ids of this NimbleAccessControlRecordDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._pe_ids

    @pe_ids.setter
    def pe_ids(self, pe_ids):
        """Sets the pe_ids of this NimbleAccessControlRecordDetails.

        List of candidate protocol endpoints that may be used to access the Virtual Volume. One of them will be selected for the access control record. This field is required only when creating an access control record for a Virtual Volume.  # noqa: E501

        :param pe_ids: The pe_ids of this NimbleAccessControlRecordDetails.  # noqa: E501
        :type: list[str]
        """

        self._pe_ids = pe_ids

    @property
    def resource_uri(self):
        """Gets the resource_uri of this NimbleAccessControlRecordDetails.  # noqa: E501


        :return: The resource_uri of this NimbleAccessControlRecordDetails.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this NimbleAccessControlRecordDetails.


        :param resource_uri: The resource_uri of this NimbleAccessControlRecordDetails.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

    @property
    def snapluns(self):
        """Gets the snapluns of this NimbleAccessControlRecordDetails.  # noqa: E501

        Information about the snapshot LUNs associated with this access control record. This field is meaningful when the online snapshot can be accessed as a LUN in the group.  # noqa: E501

        :return: The snapluns of this NimbleAccessControlRecordDetails.  # noqa: E501
        :rtype: list[NimbleNsSnapLunInfo]
        """
        return self._snapluns

    @snapluns.setter
    def snapluns(self, snapluns):
        """Sets the snapluns of this NimbleAccessControlRecordDetails.

        Information about the snapshot LUNs associated with this access control record. This field is meaningful when the online snapshot can be accessed as a LUN in the group.  # noqa: E501

        :param snapluns: The snapluns of this NimbleAccessControlRecordDetails.  # noqa: E501
        :type: list[NimbleNsSnapLunInfo]
        """

        self._snapluns = snapluns

    @property
    def type(self):
        """Gets the type of this NimbleAccessControlRecordDetails.  # noqa: E501

        type  # noqa: E501

        :return: The type of this NimbleAccessControlRecordDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NimbleAccessControlRecordDetails.

        type  # noqa: E501

        :param type: The type of this NimbleAccessControlRecordDetails.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def vol_agent_type(self):
        """Gets the vol_agent_type of this NimbleAccessControlRecordDetails.  # noqa: E501

        External management agent type. Possible values:'smis', 'vvol', 'openstack', 'openstackv2', 'none'.  # noqa: E501

        :return: The vol_agent_type of this NimbleAccessControlRecordDetails.  # noqa: E501
        :rtype: str
        """
        return self._vol_agent_type

    @vol_agent_type.setter
    def vol_agent_type(self, vol_agent_type):
        """Sets the vol_agent_type of this NimbleAccessControlRecordDetails.

        External management agent type. Possible values:'smis', 'vvol', 'openstack', 'openstackv2', 'none'.  # noqa: E501

        :param vol_agent_type: The vol_agent_type of this NimbleAccessControlRecordDetails.  # noqa: E501
        :type: str
        """

        self._vol_agent_type = vol_agent_type

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
        if not isinstance(other, NimbleAccessControlRecordDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
