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


class NimblePerformancePolicyDetails(object):
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
        'associated_links': 'AssociatedLinks',
        'block_size': 'int',
        'console_uri': 'str',
        'customer_id': 'str',
        'dedupe_override_pools': 'list[NimbleNsPoolSummary]',
        'description': 'str',
        'full_name': 'str',
        'generation': 'int',
        'resource_uri': 'str',
        'search_name': 'str',
        'type': 'str',
        'volume_count': 'int'
    }

    attribute_map = {
        'associated_links': 'associated_links',
        'block_size': 'block_size',
        'console_uri': 'consoleUri',
        'customer_id': 'customerId',
        'dedupe_override_pools': 'dedupe_override_pools',
        'description': 'description',
        'full_name': 'full_name',
        'generation': 'generation',
        'resource_uri': 'resourceUri',
        'search_name': 'search_name',
        'type': 'type',
        'volume_count': 'volume_count'
    }

    def __init__(self, associated_links=None, block_size=None, console_uri=None, customer_id=None, dedupe_override_pools=None, description=None, full_name=None, generation=None, resource_uri=None, search_name=None, type=None, volume_count=None):  # noqa: E501
        """NimblePerformancePolicyDetails - a model defined in OpenAPI"""  # noqa: E501

        self._associated_links = None
        self._block_size = None
        self._console_uri = None
        self._customer_id = None
        self._dedupe_override_pools = None
        self._description = None
        self._full_name = None
        self._generation = None
        self._resource_uri = None
        self._search_name = None
        self._type = None
        self._volume_count = None
        self.discriminator = None

        if associated_links is not None:
            self.associated_links = associated_links
        if block_size is not None:
            self.block_size = block_size
        if console_uri is not None:
            self.console_uri = console_uri
        if customer_id is not None:
            self.customer_id = customer_id
        if dedupe_override_pools is not None:
            self.dedupe_override_pools = dedupe_override_pools
        if description is not None:
            self.description = description
        if full_name is not None:
            self.full_name = full_name
        if generation is not None:
            self.generation = generation
        if resource_uri is not None:
            self.resource_uri = resource_uri
        if search_name is not None:
            self.search_name = search_name
        if type is not None:
            self.type = type
        if volume_count is not None:
            self.volume_count = volume_count

    @property
    def associated_links(self):
        """Gets the associated_links of this NimblePerformancePolicyDetails.  # noqa: E501


        :return: The associated_links of this NimblePerformancePolicyDetails.  # noqa: E501
        :rtype: AssociatedLinks
        """
        return self._associated_links

    @associated_links.setter
    def associated_links(self, associated_links):
        """Sets the associated_links of this NimblePerformancePolicyDetails.


        :param associated_links: The associated_links of this NimblePerformancePolicyDetails.  # noqa: E501
        :type: AssociatedLinks
        """

        self._associated_links = associated_links

    @property
    def block_size(self):
        """Gets the block_size of this NimblePerformancePolicyDetails.  # noqa: E501

        Block Size in bytes to be used by the volumes created with this specific performance policy. Supported block sizes are 4096 bytes (4 KB), 8192 bytes (8 KB), 16384 bytes(16 KB), and 32768 bytes (32 KB). Block size of a performance policy cannot be changed once the performance policy is created.  # noqa: E501

        :return: The block_size of this NimblePerformancePolicyDetails.  # noqa: E501
        :rtype: int
        """
        return self._block_size

    @block_size.setter
    def block_size(self, block_size):
        """Sets the block_size of this NimblePerformancePolicyDetails.

        Block Size in bytes to be used by the volumes created with this specific performance policy. Supported block sizes are 4096 bytes (4 KB), 8192 bytes (8 KB), 16384 bytes(16 KB), and 32768 bytes (32 KB). Block size of a performance policy cannot be changed once the performance policy is created.  # noqa: E501

        :param block_size: The block_size of this NimblePerformancePolicyDetails.  # noqa: E501
        :type: int
        """

        self._block_size = block_size

    @property
    def console_uri(self):
        """Gets the console_uri of this NimblePerformancePolicyDetails.  # noqa: E501

        consoleUri for detailed storage object  # noqa: E501

        :return: The console_uri of this NimblePerformancePolicyDetails.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this NimblePerformancePolicyDetails.

        consoleUri for detailed storage object  # noqa: E501

        :param console_uri: The console_uri of this NimblePerformancePolicyDetails.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def customer_id(self):
        """Gets the customer_id of this NimblePerformancePolicyDetails.  # noqa: E501

        customerId  # noqa: E501

        :return: The customer_id of this NimblePerformancePolicyDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this NimblePerformancePolicyDetails.

        customerId  # noqa: E501

        :param customer_id: The customer_id of this NimblePerformancePolicyDetails.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def dedupe_override_pools(self):
        """Gets the dedupe_override_pools of this NimblePerformancePolicyDetails.  # noqa: E501

        List of pools that override performance policy's dedupe setting.  # noqa: E501

        :return: The dedupe_override_pools of this NimblePerformancePolicyDetails.  # noqa: E501
        :rtype: list[NimbleNsPoolSummary]
        """
        return self._dedupe_override_pools

    @dedupe_override_pools.setter
    def dedupe_override_pools(self, dedupe_override_pools):
        """Sets the dedupe_override_pools of this NimblePerformancePolicyDetails.

        List of pools that override performance policy's dedupe setting.  # noqa: E501

        :param dedupe_override_pools: The dedupe_override_pools of this NimblePerformancePolicyDetails.  # noqa: E501
        :type: list[NimbleNsPoolSummary]
        """

        self._dedupe_override_pools = dedupe_override_pools

    @property
    def description(self):
        """Gets the description of this NimblePerformancePolicyDetails.  # noqa: E501

        Description of a performance policy.  # noqa: E501

        :return: The description of this NimblePerformancePolicyDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NimblePerformancePolicyDetails.

        Description of a performance policy.  # noqa: E501

        :param description: The description of this NimblePerformancePolicyDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def full_name(self):
        """Gets the full_name of this NimblePerformancePolicyDetails.  # noqa: E501

        Fully qualified name of the Performance Policy.  # noqa: E501

        :return: The full_name of this NimblePerformancePolicyDetails.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this NimblePerformancePolicyDetails.

        Fully qualified name of the Performance Policy.  # noqa: E501

        :param full_name: The full_name of this NimblePerformancePolicyDetails.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def generation(self):
        """Gets the generation of this NimblePerformancePolicyDetails.  # noqa: E501

        generation  # noqa: E501

        :return: The generation of this NimblePerformancePolicyDetails.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this NimblePerformancePolicyDetails.

        generation  # noqa: E501

        :param generation: The generation of this NimblePerformancePolicyDetails.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def resource_uri(self):
        """Gets the resource_uri of this NimblePerformancePolicyDetails.  # noqa: E501


        :return: The resource_uri of this NimblePerformancePolicyDetails.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this NimblePerformancePolicyDetails.


        :param resource_uri: The resource_uri of this NimblePerformancePolicyDetails.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

    @property
    def search_name(self):
        """Gets the search_name of this NimblePerformancePolicyDetails.  # noqa: E501

        Name of the Performance Policy used for object search.  # noqa: E501

        :return: The search_name of this NimblePerformancePolicyDetails.  # noqa: E501
        :rtype: str
        """
        return self._search_name

    @search_name.setter
    def search_name(self, search_name):
        """Sets the search_name of this NimblePerformancePolicyDetails.

        Name of the Performance Policy used for object search.  # noqa: E501

        :param search_name: The search_name of this NimblePerformancePolicyDetails.  # noqa: E501
        :type: str
        """

        self._search_name = search_name

    @property
    def type(self):
        """Gets the type of this NimblePerformancePolicyDetails.  # noqa: E501

        type  # noqa: E501

        :return: The type of this NimblePerformancePolicyDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NimblePerformancePolicyDetails.

        type  # noqa: E501

        :param type: The type of this NimblePerformancePolicyDetails.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def volume_count(self):
        """Gets the volume_count of this NimblePerformancePolicyDetails.  # noqa: E501

        Number of volumes using this performance policy.  # noqa: E501

        :return: The volume_count of this NimblePerformancePolicyDetails.  # noqa: E501
        :rtype: int
        """
        return self._volume_count

    @volume_count.setter
    def volume_count(self, volume_count):
        """Sets the volume_count of this NimblePerformancePolicyDetails.

        Number of volumes using this performance policy.  # noqa: E501

        :param volume_count: The volume_count of this NimblePerformancePolicyDetails.  # noqa: E501
        :type: int
        """

        self._volume_count = volume_count

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
        if not isinstance(other, NimblePerformancePolicyDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other