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


class FleetSystemVolumeset(object):
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
        'app_type': 'str',
        'associated_links': 'list[AssociatedLinksInner]',
        'console_uri': 'str',
        'customer_id': 'str',
        'generation': 'int',
        'id': 'str',
        'name': 'str',
        'product_family': 'str',
        'request_uri': 'str',
        'resource_uri': 'str',
        'system_id': 'str',
        'type': 'str',
        'volumes_count': 'int'
    }

    attribute_map = {
        'app_type': 'appType',
        'associated_links': 'associatedLinks',
        'console_uri': 'consoleUri',
        'customer_id': 'customerId',
        'generation': 'generation',
        'id': 'id',
        'name': 'name',
        'product_family': 'productFamily',
        'request_uri': 'requestUri',
        'resource_uri': 'resourceUri',
        'system_id': 'systemId',
        'type': 'type',
        'volumes_count': 'volumesCount'
    }

    def __init__(self, app_type=None, associated_links=None, console_uri=None, customer_id=None, generation=None, id=None, name=None, product_family=None, request_uri=None, resource_uri=None, system_id=None, type=None, volumes_count=None):  # noqa: E501
        """FleetSystemVolumeset - a model defined in OpenAPI"""  # noqa: E501

        self._app_type = None
        self._associated_links = None
        self._console_uri = None
        self._customer_id = None
        self._generation = None
        self._id = None
        self._name = None
        self._product_family = None
        self._request_uri = None
        self._resource_uri = None
        self._system_id = None
        self._type = None
        self._volumes_count = None
        self.discriminator = None

        if app_type is not None:
            self.app_type = app_type
        if associated_links is not None:
            self.associated_links = associated_links
        if console_uri is not None:
            self.console_uri = console_uri
        if customer_id is not None:
            self.customer_id = customer_id
        if generation is not None:
            self.generation = generation
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if product_family is not None:
            self.product_family = product_family
        if request_uri is not None:
            self.request_uri = request_uri
        if resource_uri is not None:
            self.resource_uri = resource_uri
        if system_id is not None:
            self.system_id = system_id
        if type is not None:
            self.type = type
        if volumes_count is not None:
            self.volumes_count = volumes_count

    @property
    def app_type(self):
        """Gets the app_type of this FleetSystemVolumeset.  # noqa: E501

        Application name `Filter`  # noqa: E501

        :return: The app_type of this FleetSystemVolumeset.  # noqa: E501
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this FleetSystemVolumeset.

        Application name `Filter`  # noqa: E501

        :param app_type: The app_type of this FleetSystemVolumeset.  # noqa: E501
        :type: str
        """

        self._app_type = app_type

    @property
    def associated_links(self):
        """Gets the associated_links of this FleetSystemVolumeset.  # noqa: E501

        Associated Links Details  # noqa: E501

        :return: The associated_links of this FleetSystemVolumeset.  # noqa: E501
        :rtype: list[AssociatedLinksInner]
        """
        return self._associated_links

    @associated_links.setter
    def associated_links(self, associated_links):
        """Sets the associated_links of this FleetSystemVolumeset.

        Associated Links Details  # noqa: E501

        :param associated_links: The associated_links of this FleetSystemVolumeset.  # noqa: E501
        :type: list[AssociatedLinksInner]
        """

        self._associated_links = associated_links

    @property
    def console_uri(self):
        """Gets the console_uri of this FleetSystemVolumeset.  # noqa: E501

        consoleUri for detailed storage object  # noqa: E501

        :return: The console_uri of this FleetSystemVolumeset.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this FleetSystemVolumeset.

        consoleUri for detailed storage object  # noqa: E501

        :param console_uri: The console_uri of this FleetSystemVolumeset.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def customer_id(self):
        """Gets the customer_id of this FleetSystemVolumeset.  # noqa: E501

        customerId  # noqa: E501

        :return: The customer_id of this FleetSystemVolumeset.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this FleetSystemVolumeset.

        customerId  # noqa: E501

        :param customer_id: The customer_id of this FleetSystemVolumeset.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def generation(self):
        """Gets the generation of this FleetSystemVolumeset.  # noqa: E501

        generation `Filter, Sort`  # noqa: E501

        :return: The generation of this FleetSystemVolumeset.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this FleetSystemVolumeset.

        generation `Filter, Sort`  # noqa: E501

        :param generation: The generation of this FleetSystemVolumeset.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def id(self):
        """Gets the id of this FleetSystemVolumeset.  # noqa: E501

        id of the volume set `Filter`  # noqa: E501

        :return: The id of this FleetSystemVolumeset.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FleetSystemVolumeset.

        id of the volume set `Filter`  # noqa: E501

        :param id: The id of this FleetSystemVolumeset.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FleetSystemVolumeset.  # noqa: E501

        name of volume-set `Filter, Sort`  # noqa: E501

        :return: The name of this FleetSystemVolumeset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FleetSystemVolumeset.

        name of volume-set `Filter, Sort`  # noqa: E501

        :param name: The name of this FleetSystemVolumeset.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def product_family(self):
        """Gets the product_family of this FleetSystemVolumeset.  # noqa: E501

        Product Family  # noqa: E501

        :return: The product_family of this FleetSystemVolumeset.  # noqa: E501
        :rtype: str
        """
        return self._product_family

    @product_family.setter
    def product_family(self, product_family):
        """Sets the product_family of this FleetSystemVolumeset.

        Product Family  # noqa: E501

        :param product_family: The product_family of this FleetSystemVolumeset.  # noqa: E501
        :type: str
        """

        self._product_family = product_family

    @property
    def request_uri(self):
        """Gets the request_uri of this FleetSystemVolumeset.  # noqa: E501

        RequestUri for applicationsets resources  # noqa: E501

        :return: The request_uri of this FleetSystemVolumeset.  # noqa: E501
        :rtype: str
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri):
        """Sets the request_uri of this FleetSystemVolumeset.

        RequestUri for applicationsets resources  # noqa: E501

        :param request_uri: The request_uri of this FleetSystemVolumeset.  # noqa: E501
        :type: str
        """

        self._request_uri = request_uri

    @property
    def resource_uri(self):
        """Gets the resource_uri of this FleetSystemVolumeset.  # noqa: E501

        resourceUri for detailed volume object  # noqa: E501

        :return: The resource_uri of this FleetSystemVolumeset.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this FleetSystemVolumeset.

        resourceUri for detailed volume object  # noqa: E501

        :param resource_uri: The resource_uri of this FleetSystemVolumeset.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

    @property
    def system_id(self):
        """Gets the system_id of this FleetSystemVolumeset.  # noqa: E501

        system ID. `Filter, Sort`  # noqa: E501

        :return: The system_id of this FleetSystemVolumeset.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this FleetSystemVolumeset.

        system ID. `Filter, Sort`  # noqa: E501

        :param system_id: The system_id of this FleetSystemVolumeset.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def type(self):
        """Gets the type of this FleetSystemVolumeset.  # noqa: E501

        type  # noqa: E501

        :return: The type of this FleetSystemVolumeset.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FleetSystemVolumeset.

        type  # noqa: E501

        :param type: The type of this FleetSystemVolumeset.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def volumes_count(self):
        """Gets the volumes_count of this FleetSystemVolumeset.  # noqa: E501

        The number of volumes in an application  # noqa: E501

        :return: The volumes_count of this FleetSystemVolumeset.  # noqa: E501
        :rtype: int
        """
        return self._volumes_count

    @volumes_count.setter
    def volumes_count(self, volumes_count):
        """Sets the volumes_count of this FleetSystemVolumeset.

        The number of volumes in an application  # noqa: E501

        :param volumes_count: The volumes_count of this FleetSystemVolumeset.  # noqa: E501
        :type: int
        """

        self._volumes_count = volumes_count

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
        if not isinstance(other, FleetSystemVolumeset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
