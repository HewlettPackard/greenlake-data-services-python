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


class PrimeraHostSets(object):
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
        'comment': 'str',
        'displayname': 'str',
        'domain': 'str',
        'generation': 'int',
        'host_set_id': 'int',
        'id': 'str',
        'members': 'list[str]',
        'name': 'str',
        'resource_uri': 'str',
        'sc_host_group_id': 'str',
        'system_uid': 'str',
        'system_wwn': 'str',
        'uri': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'associated_links': 'associatedLinks',
        'comment': 'comment',
        'displayname': 'displayname',
        'domain': 'domain',
        'generation': 'generation',
        'host_set_id': 'hostSetId',
        'id': 'id',
        'members': 'members',
        'name': 'name',
        'resource_uri': 'resourceUri',
        'sc_host_group_id': 'sc_HostGroupId',
        'system_uid': 'systemUid',
        'system_wwn': 'systemWWN',
        'uri': 'uri',
        'uuid': 'uuid'
    }

    def __init__(self, associated_links=None, comment=None, displayname=None, domain=None, generation=None, host_set_id=None, id=None, members=None, name=None, resource_uri=None, sc_host_group_id=None, system_uid=None, system_wwn=None, uri=None, uuid=None):  # noqa: E501
        """PrimeraHostSets - a model defined in OpenAPI"""  # noqa: E501

        self._associated_links = None
        self._comment = None
        self._displayname = None
        self._domain = None
        self._generation = None
        self._host_set_id = None
        self._id = None
        self._members = None
        self._name = None
        self._resource_uri = None
        self._sc_host_group_id = None
        self._system_uid = None
        self._system_wwn = None
        self._uri = None
        self._uuid = None
        self.discriminator = None

        if associated_links is not None:
            self.associated_links = associated_links
        if comment is not None:
            self.comment = comment
        if displayname is not None:
            self.displayname = displayname
        if domain is not None:
            self.domain = domain
        if generation is not None:
            self.generation = generation
        if host_set_id is not None:
            self.host_set_id = host_set_id
        if id is not None:
            self.id = id
        if members is not None:
            self.members = members
        if name is not None:
            self.name = name
        if resource_uri is not None:
            self.resource_uri = resource_uri
        if sc_host_group_id is not None:
            self.sc_host_group_id = sc_host_group_id
        if system_uid is not None:
            self.system_uid = system_uid
        if system_wwn is not None:
            self.system_wwn = system_wwn
        if uri is not None:
            self.uri = uri
        if uuid is not None:
            self.uuid = uuid

    @property
    def associated_links(self):
        """Gets the associated_links of this PrimeraHostSets.  # noqa: E501

        Associated Links Details  # noqa: E501

        :return: The associated_links of this PrimeraHostSets.  # noqa: E501
        :rtype: list[AssociatedLinksInner]
        """
        return self._associated_links

    @associated_links.setter
    def associated_links(self, associated_links):
        """Sets the associated_links of this PrimeraHostSets.

        Associated Links Details  # noqa: E501

        :param associated_links: The associated_links of this PrimeraHostSets.  # noqa: E501
        :type: list[AssociatedLinksInner]
        """

        self._associated_links = associated_links

    @property
    def comment(self):
        """Gets the comment of this PrimeraHostSets.  # noqa: E501

        Comment on the Host Set  # noqa: E501

        :return: The comment of this PrimeraHostSets.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PrimeraHostSets.

        Comment on the Host Set  # noqa: E501

        :param comment: The comment of this PrimeraHostSets.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def displayname(self):
        """Gets the displayname of this PrimeraHostSets.  # noqa: E501

        Name to be used for display purposes  # noqa: E501

        :return: The displayname of this PrimeraHostSets.  # noqa: E501
        :rtype: str
        """
        return self._displayname

    @displayname.setter
    def displayname(self, displayname):
        """Sets the displayname of this PrimeraHostSets.

        Name to be used for display purposes  # noqa: E501

        :param displayname: The displayname of this PrimeraHostSets.  # noqa: E501
        :type: str
        """

        self._displayname = displayname

    @property
    def domain(self):
        """Gets the domain of this PrimeraHostSets.  # noqa: E501

        Domain name of the Host Set  # noqa: E501

        :return: The domain of this PrimeraHostSets.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this PrimeraHostSets.

        Domain name of the Host Set  # noqa: E501

        :param domain: The domain of this PrimeraHostSets.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def generation(self):
        """Gets the generation of this PrimeraHostSets.  # noqa: E501

        Generation Time of the Resource  # noqa: E501

        :return: The generation of this PrimeraHostSets.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this PrimeraHostSets.

        Generation Time of the Resource  # noqa: E501

        :param generation: The generation of this PrimeraHostSets.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def host_set_id(self):
        """Gets the host_set_id of this PrimeraHostSets.  # noqa: E501

        Numeric ID of the resource  # noqa: E501

        :return: The host_set_id of this PrimeraHostSets.  # noqa: E501
        :rtype: int
        """
        return self._host_set_id

    @host_set_id.setter
    def host_set_id(self, host_set_id):
        """Sets the host_set_id of this PrimeraHostSets.

        Numeric ID of the resource  # noqa: E501

        :param host_set_id: The host_set_id of this PrimeraHostSets.  # noqa: E501
        :type: int
        """

        self._host_set_id = host_set_id

    @property
    def id(self):
        """Gets the id of this PrimeraHostSets.  # noqa: E501

        HostSet Resource UID  # noqa: E501

        :return: The id of this PrimeraHostSets.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrimeraHostSets.

        HostSet Resource UID  # noqa: E501

        :param id: The id of this PrimeraHostSets.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def members(self):
        """Gets the members of this PrimeraHostSets.  # noqa: E501

        system ntp addresses  # noqa: E501

        :return: The members of this PrimeraHostSets.  # noqa: E501
        :rtype: list[str]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this PrimeraHostSets.

        system ntp addresses  # noqa: E501

        :param members: The members of this PrimeraHostSets.  # noqa: E501
        :type: list[str]
        """

        self._members = members

    @property
    def name(self):
        """Gets the name of this PrimeraHostSets.  # noqa: E501

        Host Set Name  # noqa: E501

        :return: The name of this PrimeraHostSets.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PrimeraHostSets.

        Host Set Name  # noqa: E501

        :param name: The name of this PrimeraHostSets.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def resource_uri(self):
        """Gets the resource_uri of this PrimeraHostSets.  # noqa: E501

        resourceUri for detailed hostset object  # noqa: E501

        :return: The resource_uri of this PrimeraHostSets.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this PrimeraHostSets.

        resourceUri for detailed hostset object  # noqa: E501

        :param resource_uri: The resource_uri of this PrimeraHostSets.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

    @property
    def sc_host_group_id(self):
        """Gets the sc_host_group_id of this PrimeraHostSets.  # noqa: E501

        Host Service HostGroup Id  # noqa: E501

        :return: The sc_host_group_id of this PrimeraHostSets.  # noqa: E501
        :rtype: str
        """
        return self._sc_host_group_id

    @sc_host_group_id.setter
    def sc_host_group_id(self, sc_host_group_id):
        """Sets the sc_host_group_id of this PrimeraHostSets.

        Host Service HostGroup Id  # noqa: E501

        :param sc_host_group_id: The sc_host_group_id of this PrimeraHostSets.  # noqa: E501
        :type: str
        """

        self._sc_host_group_id = sc_host_group_id

    @property
    def system_uid(self):
        """Gets the system_uid of this PrimeraHostSets.  # noqa: E501

        Serail Number of the system  # noqa: E501

        :return: The system_uid of this PrimeraHostSets.  # noqa: E501
        :rtype: str
        """
        return self._system_uid

    @system_uid.setter
    def system_uid(self, system_uid):
        """Sets the system_uid of this PrimeraHostSets.

        Serail Number of the system  # noqa: E501

        :param system_uid: The system_uid of this PrimeraHostSets.  # noqa: E501
        :type: str
        """

        self._system_uid = system_uid

    @property
    def system_wwn(self):
        """Gets the system_wwn of this PrimeraHostSets.  # noqa: E501

        System wwn  # noqa: E501

        :return: The system_wwn of this PrimeraHostSets.  # noqa: E501
        :rtype: str
        """
        return self._system_wwn

    @system_wwn.setter
    def system_wwn(self, system_wwn):
        """Sets the system_wwn of this PrimeraHostSets.

        System wwn  # noqa: E501

        :param system_wwn: The system_wwn of this PrimeraHostSets.  # noqa: E501
        :type: str
        """

        self._system_wwn = system_wwn

    @property
    def uri(self):
        """Gets the uri of this PrimeraHostSets.  # noqa: E501

        Uri  # noqa: E501

        :return: The uri of this PrimeraHostSets.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this PrimeraHostSets.

        Uri  # noqa: E501

        :param uri: The uri of this PrimeraHostSets.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def uuid(self):
        """Gets the uuid of this PrimeraHostSets.  # noqa: E501

        HostSet Resource UUID  # noqa: E501

        :return: The uuid of this PrimeraHostSets.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PrimeraHostSets.

        HostSet Resource UUID  # noqa: E501

        :param uuid: The uuid of this PrimeraHostSets.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if not isinstance(other, PrimeraHostSets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
