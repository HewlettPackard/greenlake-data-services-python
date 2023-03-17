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


class HostGroupDetails(object):
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
        'associated_links': 'ScAssociatedLinks',
        'associated_systems': 'list[str]',
        'comment': 'str',
        'console_uri': 'str',
        'customer_id': 'str',
        'edit_status': 'str',
        'generation': 'int',
        'hosts': 'list[HostSummaryForHSObject]',
        'id': 'str',
        'marked_for_delete': 'bool',
        'name': 'str',
        'request_uri': 'str',
        'systems': 'list[str]',
        'type': 'str',
        'user_created': 'bool'
    }

    attribute_map = {
        'associated_links': 'associatedLinks',
        'associated_systems': 'associatedSystems',
        'comment': 'comment',
        'console_uri': 'consoleUri',
        'customer_id': 'customerId',
        'edit_status': 'editStatus',
        'generation': 'generation',
        'hosts': 'hosts',
        'id': 'id',
        'marked_for_delete': 'markedForDelete',
        'name': 'name',
        'request_uri': 'requestUri',
        'systems': 'systems',
        'type': 'type',
        'user_created': 'userCreated'
    }

    def __init__(self, associated_links=None, associated_systems=None, comment=None, console_uri=None, customer_id=None, edit_status=None, generation=None, hosts=None, id=None, marked_for_delete=None, name=None, request_uri=None, systems=None, type=None, user_created=None):  # noqa: E501
        """HostGroupDetails - a model defined in OpenAPI"""  # noqa: E501

        self._associated_links = None
        self._associated_systems = None
        self._comment = None
        self._console_uri = None
        self._customer_id = None
        self._edit_status = None
        self._generation = None
        self._hosts = None
        self._id = None
        self._marked_for_delete = None
        self._name = None
        self._request_uri = None
        self._systems = None
        self._type = None
        self._user_created = None
        self.discriminator = None

        if associated_links is not None:
            self.associated_links = associated_links
        if associated_systems is not None:
            self.associated_systems = associated_systems
        if comment is not None:
            self.comment = comment
        if console_uri is not None:
            self.console_uri = console_uri
        if customer_id is not None:
            self.customer_id = customer_id
        if edit_status is not None:
            self.edit_status = edit_status
        if generation is not None:
            self.generation = generation
        if hosts is not None:
            self.hosts = hosts
        if id is not None:
            self.id = id
        if marked_for_delete is not None:
            self.marked_for_delete = marked_for_delete
        if name is not None:
            self.name = name
        if request_uri is not None:
            self.request_uri = request_uri
        if systems is not None:
            self.systems = systems
        if type is not None:
            self.type = type
        if user_created is not None:
            self.user_created = user_created

    @property
    def associated_links(self):
        """Gets the associated_links of this HostGroupDetails.  # noqa: E501


        :return: The associated_links of this HostGroupDetails.  # noqa: E501
        :rtype: ScAssociatedLinks
        """
        return self._associated_links

    @associated_links.setter
    def associated_links(self, associated_links):
        """Sets the associated_links of this HostGroupDetails.


        :param associated_links: The associated_links of this HostGroupDetails.  # noqa: E501
        :type: ScAssociatedLinks
        """

        self._associated_links = associated_links

    @property
    def associated_systems(self):
        """Gets the associated_systems of this HostGroupDetails.  # noqa: E501

        system IDs to which the host group belongs to.  # noqa: E501

        :return: The associated_systems of this HostGroupDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._associated_systems

    @associated_systems.setter
    def associated_systems(self, associated_systems):
        """Sets the associated_systems of this HostGroupDetails.

        system IDs to which the host group belongs to.  # noqa: E501

        :param associated_systems: The associated_systems of this HostGroupDetails.  # noqa: E501
        :type: list[str]
        """

        self._associated_systems = associated_systems

    @property
    def comment(self):
        """Gets the comment of this HostGroupDetails.  # noqa: E501

        Comment  # noqa: E501

        :return: The comment of this HostGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this HostGroupDetails.

        Comment  # noqa: E501

        :param comment: The comment of this HostGroupDetails.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def console_uri(self):
        """Gets the console_uri of this HostGroupDetails.  # noqa: E501

        consoleUri for detailed storage object   # noqa: E501

        :return: The console_uri of this HostGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this HostGroupDetails.

        consoleUri for detailed storage object   # noqa: E501

        :param console_uri: The console_uri of this HostGroupDetails.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def customer_id(self):
        """Gets the customer_id of this HostGroupDetails.  # noqa: E501

        The customer application identifier  # noqa: E501

        :return: The customer_id of this HostGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this HostGroupDetails.

        The customer application identifier  # noqa: E501

        :param customer_id: The customer_id of this HostGroupDetails.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def edit_status(self):
        """Gets the edit_status of this HostGroupDetails.  # noqa: E501

        Host group Update or Delete progress status. Possible status are: Update_In_Progress,Update_Success,Update_Failed,Delete_In_Progress,Delete_Failed,Not_Applicable  # noqa: E501

        :return: The edit_status of this HostGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._edit_status

    @edit_status.setter
    def edit_status(self, edit_status):
        """Sets the edit_status of this HostGroupDetails.

        Host group Update or Delete progress status. Possible status are: Update_In_Progress,Update_Success,Update_Failed,Delete_In_Progress,Delete_Failed,Not_Applicable  # noqa: E501

        :param edit_status: The edit_status of this HostGroupDetails.  # noqa: E501
        :type: str
        """

        self._edit_status = edit_status

    @property
    def generation(self):
        """Gets the generation of this HostGroupDetails.  # noqa: E501

        A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.  # noqa: E501

        :return: The generation of this HostGroupDetails.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this HostGroupDetails.

        A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.  # noqa: E501

        :param generation: The generation of this HostGroupDetails.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def hosts(self):
        """Gets the hosts of this HostGroupDetails.  # noqa: E501

        List of hosts.  # noqa: E501

        :return: The hosts of this HostGroupDetails.  # noqa: E501
        :rtype: list[HostSummaryForHSObject]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this HostGroupDetails.

        List of hosts.  # noqa: E501

        :param hosts: The hosts of this HostGroupDetails.  # noqa: E501
        :type: list[HostSummaryForHSObject]
        """

        self._hosts = hosts

    @property
    def id(self):
        """Gets the id of this HostGroupDetails.  # noqa: E501

        Identifier for host group.  # noqa: E501

        :return: The id of this HostGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostGroupDetails.

        Identifier for host group.  # noqa: E501

        :param id: The id of this HostGroupDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def marked_for_delete(self):
        """Gets the marked_for_delete of this HostGroupDetails.  # noqa: E501

        Indicates whether host group is marked for deletion or not  # noqa: E501

        :return: The marked_for_delete of this HostGroupDetails.  # noqa: E501
        :rtype: bool
        """
        return self._marked_for_delete

    @marked_for_delete.setter
    def marked_for_delete(self, marked_for_delete):
        """Sets the marked_for_delete of this HostGroupDetails.

        Indicates whether host group is marked for deletion or not  # noqa: E501

        :param marked_for_delete: The marked_for_delete of this HostGroupDetails.  # noqa: E501
        :type: bool
        """

        self._marked_for_delete = marked_for_delete

    @property
    def name(self):
        """Gets the name of this HostGroupDetails.  # noqa: E501

        Name of the host group  # noqa: E501

        :return: The name of this HostGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostGroupDetails.

        Name of the host group  # noqa: E501

        :param name: The name of this HostGroupDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def request_uri(self):
        """Gets the request_uri of this HostGroupDetails.  # noqa: E501

        requestUri for host initiator groups  # noqa: E501

        :return: The request_uri of this HostGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri):
        """Sets the request_uri of this HostGroupDetails.

        requestUri for host initiator groups  # noqa: E501

        :param request_uri: The request_uri of this HostGroupDetails.  # noqa: E501
        :type: str
        """

        self._request_uri = request_uri

    @property
    def systems(self):
        """Gets the systems of this HostGroupDetails.  # noqa: E501

        system IDs to which the host group belongs to  # noqa: E501

        :return: The systems of this HostGroupDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """Sets the systems of this HostGroupDetails.

        system IDs to which the host group belongs to  # noqa: E501

        :param systems: The systems of this HostGroupDetails.  # noqa: E501
        :type: list[str]
        """

        self._systems = systems

    @property
    def type(self):
        """Gets the type of this HostGroupDetails.  # noqa: E501

        The type of resource.  # noqa: E501

        :return: The type of this HostGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HostGroupDetails.

        The type of resource.  # noqa: E501

        :param type: The type of this HostGroupDetails.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def user_created(self):
        """Gets the user_created of this HostGroupDetails.  # noqa: E501

        Idicates whether user created host or discovered host  # noqa: E501

        :return: The user_created of this HostGroupDetails.  # noqa: E501
        :rtype: bool
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this HostGroupDetails.

        Idicates whether user created host or discovered host  # noqa: E501

        :param user_created: The user_created of this HostGroupDetails.  # noqa: E501
        :type: bool
        """

        self._user_created = user_created

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
        if not isinstance(other, HostGroupDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other