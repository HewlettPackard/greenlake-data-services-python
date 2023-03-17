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


class NimbleVCollectionDetails(object):
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
        'agent_hostname': 'str',
        'app_sync': 'str',
        'associated_links': 'AssociatedLinks',
        'cache_pinned_volume_list': 'list[NimbleVolumeSummary]',
        'console_uri': 'str',
        'creation_time': 'int',
        'customer_id': 'str',
        'description': 'str',
        'full_name': 'str',
        'generation': 'int',
        'handover_replication_partner': 'str',
        'is_handing_over': 'bool',
        'is_standalone_volcoll': 'bool',
        'lag_time': 'int',
        'last_replicated_snapcoll': 'list[NimbleSnapcollSummary]',
        'last_snapcoll': 'list[NimbleSnapcollSummary]',
        'metadata': 'list[NimbleNsKeyValue]',
        'pol_owner_name': 'str',
        'protection_type': 'str',
        'repl_bytes_transferred': 'int',
        'repl_priority': 'str',
        'replication_partner': 'list[str]',
        'resource_uri': 'str',
        'schedule_list': 'list[NimbleNsSchedule]',
        'search_name': 'str',
        'snapcoll_count': 'int',
        'srep_last_sync': 'int',
        'srep_resync_percent': 'int',
        'total_repl_bytes': 'int',
        'type': 'str',
        'vcenter_hostname': 'str',
        'vcenter_username': 'str',
        'volume_count': 'int',
        'volume_list': 'list[NimbleVolumeSummary]'
    }

    attribute_map = {
        'agent_hostname': 'agent_hostname',
        'app_sync': 'app_sync',
        'associated_links': 'associated_links',
        'cache_pinned_volume_list': 'cache_pinned_volume_list',
        'console_uri': 'consoleUri',
        'creation_time': 'creation_time',
        'customer_id': 'customerId',
        'description': 'description',
        'full_name': 'full_name',
        'generation': 'generation',
        'handover_replication_partner': 'handover_replication_partner',
        'is_handing_over': 'is_handing_over',
        'is_standalone_volcoll': 'is_standalone_volcoll',
        'lag_time': 'lag_time',
        'last_replicated_snapcoll': 'last_replicated_snapcoll',
        'last_snapcoll': 'last_snapcoll',
        'metadata': 'metadata',
        'pol_owner_name': 'pol_owner_name',
        'protection_type': 'protection_type',
        'repl_bytes_transferred': 'repl_bytes_transferred',
        'repl_priority': 'repl_priority',
        'replication_partner': 'replication_partner',
        'resource_uri': 'resourceUri',
        'schedule_list': 'schedule_list',
        'search_name': 'search_name',
        'snapcoll_count': 'snapcoll_count',
        'srep_last_sync': 'srep_last_sync',
        'srep_resync_percent': 'srep_resync_percent',
        'total_repl_bytes': 'total_repl_bytes',
        'type': 'type',
        'vcenter_hostname': 'vcenter_hostname',
        'vcenter_username': 'vcenter_username',
        'volume_count': 'volume_count',
        'volume_list': 'volume_list'
    }

    def __init__(self, agent_hostname=None, app_sync=None, associated_links=None, cache_pinned_volume_list=None, console_uri=None, creation_time=None, customer_id=None, description=None, full_name=None, generation=None, handover_replication_partner=None, is_handing_over=None, is_standalone_volcoll=None, lag_time=None, last_replicated_snapcoll=None, last_snapcoll=None, metadata=None, pol_owner_name=None, protection_type=None, repl_bytes_transferred=None, repl_priority=None, replication_partner=None, resource_uri=None, schedule_list=None, search_name=None, snapcoll_count=None, srep_last_sync=None, srep_resync_percent=None, total_repl_bytes=None, type=None, vcenter_hostname=None, vcenter_username=None, volume_count=None, volume_list=None):  # noqa: E501
        """NimbleVCollectionDetails - a model defined in OpenAPI"""  # noqa: E501

        self._agent_hostname = None
        self._app_sync = None
        self._associated_links = None
        self._cache_pinned_volume_list = None
        self._console_uri = None
        self._creation_time = None
        self._customer_id = None
        self._description = None
        self._full_name = None
        self._generation = None
        self._handover_replication_partner = None
        self._is_handing_over = None
        self._is_standalone_volcoll = None
        self._lag_time = None
        self._last_replicated_snapcoll = None
        self._last_snapcoll = None
        self._metadata = None
        self._pol_owner_name = None
        self._protection_type = None
        self._repl_bytes_transferred = None
        self._repl_priority = None
        self._replication_partner = None
        self._resource_uri = None
        self._schedule_list = None
        self._search_name = None
        self._snapcoll_count = None
        self._srep_last_sync = None
        self._srep_resync_percent = None
        self._total_repl_bytes = None
        self._type = None
        self._vcenter_hostname = None
        self._vcenter_username = None
        self._volume_count = None
        self._volume_list = None
        self.discriminator = None

        if agent_hostname is not None:
            self.agent_hostname = agent_hostname
        if app_sync is not None:
            self.app_sync = app_sync
        if associated_links is not None:
            self.associated_links = associated_links
        if cache_pinned_volume_list is not None:
            self.cache_pinned_volume_list = cache_pinned_volume_list
        if console_uri is not None:
            self.console_uri = console_uri
        if creation_time is not None:
            self.creation_time = creation_time
        if customer_id is not None:
            self.customer_id = customer_id
        if description is not None:
            self.description = description
        if full_name is not None:
            self.full_name = full_name
        if generation is not None:
            self.generation = generation
        if handover_replication_partner is not None:
            self.handover_replication_partner = handover_replication_partner
        if is_handing_over is not None:
            self.is_handing_over = is_handing_over
        if is_standalone_volcoll is not None:
            self.is_standalone_volcoll = is_standalone_volcoll
        if lag_time is not None:
            self.lag_time = lag_time
        if last_replicated_snapcoll is not None:
            self.last_replicated_snapcoll = last_replicated_snapcoll
        if last_snapcoll is not None:
            self.last_snapcoll = last_snapcoll
        if metadata is not None:
            self.metadata = metadata
        if pol_owner_name is not None:
            self.pol_owner_name = pol_owner_name
        if protection_type is not None:
            self.protection_type = protection_type
        if repl_bytes_transferred is not None:
            self.repl_bytes_transferred = repl_bytes_transferred
        if repl_priority is not None:
            self.repl_priority = repl_priority
        if replication_partner is not None:
            self.replication_partner = replication_partner
        if resource_uri is not None:
            self.resource_uri = resource_uri
        if schedule_list is not None:
            self.schedule_list = schedule_list
        if search_name is not None:
            self.search_name = search_name
        if snapcoll_count is not None:
            self.snapcoll_count = snapcoll_count
        if srep_last_sync is not None:
            self.srep_last_sync = srep_last_sync
        if srep_resync_percent is not None:
            self.srep_resync_percent = srep_resync_percent
        if total_repl_bytes is not None:
            self.total_repl_bytes = total_repl_bytes
        if type is not None:
            self.type = type
        if vcenter_hostname is not None:
            self.vcenter_hostname = vcenter_hostname
        if vcenter_username is not None:
            self.vcenter_username = vcenter_username
        if volume_count is not None:
            self.volume_count = volume_count
        if volume_list is not None:
            self.volume_list = volume_list

    @property
    def agent_hostname(self):
        """Gets the agent_hostname of this NimbleVCollectionDetails.  # noqa: E501

        Generic backup agent hostname. Custom port number can be specified with agent hostname using \\\\\":\\\\\".  # noqa: E501

        :return: The agent_hostname of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._agent_hostname

    @agent_hostname.setter
    def agent_hostname(self, agent_hostname):
        """Sets the agent_hostname of this NimbleVCollectionDetails.

        Generic backup agent hostname. Custom port number can be specified with agent hostname using \\\\\":\\\\\".  # noqa: E501

        :param agent_hostname: The agent_hostname of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._agent_hostname = agent_hostname

    @property
    def app_sync(self):
        """Gets the app_sync of this NimbleVCollectionDetails.  # noqa: E501

        Application Synchronization. Possible values: 'vss', 'vmware', 'none', 'generic'.  # noqa: E501

        :return: The app_sync of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._app_sync

    @app_sync.setter
    def app_sync(self, app_sync):
        """Sets the app_sync of this NimbleVCollectionDetails.

        Application Synchronization. Possible values: 'vss', 'vmware', 'none', 'generic'.  # noqa: E501

        :param app_sync: The app_sync of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._app_sync = app_sync

    @property
    def associated_links(self):
        """Gets the associated_links of this NimbleVCollectionDetails.  # noqa: E501


        :return: The associated_links of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: AssociatedLinks
        """
        return self._associated_links

    @associated_links.setter
    def associated_links(self, associated_links):
        """Sets the associated_links of this NimbleVCollectionDetails.


        :param associated_links: The associated_links of this NimbleVCollectionDetails.  # noqa: E501
        :type: AssociatedLinks
        """

        self._associated_links = associated_links

    @property
    def cache_pinned_volume_list(self):
        """Gets the cache_pinned_volume_list of this NimbleVCollectionDetails.  # noqa: E501

        List of cache pinned volumes associated with volume collection.  # noqa: E501

        :return: The cache_pinned_volume_list of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: list[NimbleVolumeSummary]
        """
        return self._cache_pinned_volume_list

    @cache_pinned_volume_list.setter
    def cache_pinned_volume_list(self, cache_pinned_volume_list):
        """Sets the cache_pinned_volume_list of this NimbleVCollectionDetails.

        List of cache pinned volumes associated with volume collection.  # noqa: E501

        :param cache_pinned_volume_list: The cache_pinned_volume_list of this NimbleVCollectionDetails.  # noqa: E501
        :type: list[NimbleVolumeSummary]
        """

        self._cache_pinned_volume_list = cache_pinned_volume_list

    @property
    def console_uri(self):
        """Gets the console_uri of this NimbleVCollectionDetails.  # noqa: E501

        consoleUri for detailed storage object  # noqa: E501

        :return: The console_uri of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this NimbleVCollectionDetails.

        consoleUri for detailed storage object  # noqa: E501

        :param console_uri: The console_uri of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def creation_time(self):
        """Gets the creation_time of this NimbleVCollectionDetails.  # noqa: E501

        Application server hostname.  # noqa: E501

        :return: The creation_time of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this NimbleVCollectionDetails.

        Application server hostname.  # noqa: E501

        :param creation_time: The creation_time of this NimbleVCollectionDetails.  # noqa: E501
        :type: int
        """

        self._creation_time = creation_time

    @property
    def customer_id(self):
        """Gets the customer_id of this NimbleVCollectionDetails.  # noqa: E501

        customerId  # noqa: E501

        :return: The customer_id of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this NimbleVCollectionDetails.

        customerId  # noqa: E501

        :param customer_id: The customer_id of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def description(self):
        """Gets the description of this NimbleVCollectionDetails.  # noqa: E501

        Text descrption of volume collection.  # noqa: E501

        :return: The description of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NimbleVCollectionDetails.

        Text descrption of volume collection.  # noqa: E501

        :param description: The description of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def full_name(self):
        """Gets the full_name of this NimbleVCollectionDetails.  # noqa: E501

        Fully qualified name of volume collection.  # noqa: E501

        :return: The full_name of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this NimbleVCollectionDetails.

        Fully qualified name of volume collection.  # noqa: E501

        :param full_name: The full_name of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def generation(self):
        """Gets the generation of this NimbleVCollectionDetails.  # noqa: E501

        generation  # noqa: E501

        :return: The generation of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this NimbleVCollectionDetails.

        generation  # noqa: E501

        :param generation: The generation of this NimbleVCollectionDetails.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def handover_replication_partner(self):
        """Gets the handover_replication_partner of this NimbleVCollectionDetails.  # noqa: E501

        Replication partner to which ownership is being transferred as part of handover operation.  # noqa: E501

        :return: The handover_replication_partner of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._handover_replication_partner

    @handover_replication_partner.setter
    def handover_replication_partner(self, handover_replication_partner):
        """Sets the handover_replication_partner of this NimbleVCollectionDetails.

        Replication partner to which ownership is being transferred as part of handover operation.  # noqa: E501

        :param handover_replication_partner: The handover_replication_partner of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._handover_replication_partner = handover_replication_partner

    @property
    def is_handing_over(self):
        """Gets the is_handing_over of this NimbleVCollectionDetails.  # noqa: E501

        Indicates whether a handover operation is in progress on this volume collection.  # noqa: E501

        :return: The is_handing_over of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_handing_over

    @is_handing_over.setter
    def is_handing_over(self, is_handing_over):
        """Sets the is_handing_over of this NimbleVCollectionDetails.

        Indicates whether a handover operation is in progress on this volume collection.  # noqa: E501

        :param is_handing_over: The is_handing_over of this NimbleVCollectionDetails.  # noqa: E501
        :type: bool
        """

        self._is_handing_over = is_handing_over

    @property
    def is_standalone_volcoll(self):
        """Gets the is_standalone_volcoll of this NimbleVCollectionDetails.  # noqa: E501

        Last snapshot collection on this volume collection.  # noqa: E501

        :return: The is_standalone_volcoll of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_standalone_volcoll

    @is_standalone_volcoll.setter
    def is_standalone_volcoll(self, is_standalone_volcoll):
        """Sets the is_standalone_volcoll of this NimbleVCollectionDetails.

        Last snapshot collection on this volume collection.  # noqa: E501

        :param is_standalone_volcoll: The is_standalone_volcoll of this NimbleVCollectionDetails.  # noqa: E501
        :type: bool
        """

        self._is_standalone_volcoll = is_standalone_volcoll

    @property
    def lag_time(self):
        """Gets the lag_time of this NimbleVCollectionDetails.  # noqa: E501

        Replication lag time for volume collection.  # noqa: E501

        :return: The lag_time of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: int
        """
        return self._lag_time

    @lag_time.setter
    def lag_time(self, lag_time):
        """Sets the lag_time of this NimbleVCollectionDetails.

        Replication lag time for volume collection.  # noqa: E501

        :param lag_time: The lag_time of this NimbleVCollectionDetails.  # noqa: E501
        :type: int
        """

        self._lag_time = lag_time

    @property
    def last_replicated_snapcoll(self):
        """Gets the last_replicated_snapcoll of this NimbleVCollectionDetails.  # noqa: E501

        Last replicated snapshot collection on this volume collection.  # noqa: E501

        :return: The last_replicated_snapcoll of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: list[NimbleSnapcollSummary]
        """
        return self._last_replicated_snapcoll

    @last_replicated_snapcoll.setter
    def last_replicated_snapcoll(self, last_replicated_snapcoll):
        """Sets the last_replicated_snapcoll of this NimbleVCollectionDetails.

        Last replicated snapshot collection on this volume collection.  # noqa: E501

        :param last_replicated_snapcoll: The last_replicated_snapcoll of this NimbleVCollectionDetails.  # noqa: E501
        :type: list[NimbleSnapcollSummary]
        """

        self._last_replicated_snapcoll = last_replicated_snapcoll

    @property
    def last_snapcoll(self):
        """Gets the last_snapcoll of this NimbleVCollectionDetails.  # noqa: E501

        Last snapshot collection on this volume collection.  # noqa: E501

        :return: The last_snapcoll of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: list[NimbleSnapcollSummary]
        """
        return self._last_snapcoll

    @last_snapcoll.setter
    def last_snapcoll(self, last_snapcoll):
        """Sets the last_snapcoll of this NimbleVCollectionDetails.

        Last snapshot collection on this volume collection.  # noqa: E501

        :param last_snapcoll: The last_snapcoll of this NimbleVCollectionDetails.  # noqa: E501
        :type: list[NimbleSnapcollSummary]
        """

        self._last_snapcoll = last_snapcoll

    @property
    def metadata(self):
        """Gets the metadata of this NimbleVCollectionDetails.  # noqa: E501

        Key-value pairs that augment a volume collection's attributes.  # noqa: E501

        :return: The metadata of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: list[NimbleNsKeyValue]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NimbleVCollectionDetails.

        Key-value pairs that augment a volume collection's attributes.  # noqa: E501

        :param metadata: The metadata of this NimbleVCollectionDetails.  # noqa: E501
        :type: list[NimbleNsKeyValue]
        """

        self._metadata = metadata

    @property
    def pol_owner_name(self):
        """Gets the pol_owner_name of this NimbleVCollectionDetails.  # noqa: E501

        PolOwnerName - Owner group.  # noqa: E501

        :return: The pol_owner_name of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._pol_owner_name

    @pol_owner_name.setter
    def pol_owner_name(self, pol_owner_name):
        """Sets the pol_owner_name of this NimbleVCollectionDetails.

        PolOwnerName - Owner group.  # noqa: E501

        :param pol_owner_name: The pol_owner_name of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._pol_owner_name = pol_owner_name

    @property
    def protection_type(self):
        """Gets the protection_type of this NimbleVCollectionDetails.  # noqa: E501

        Specifies if volume collection is protected with schedules. If protected, indicated whether replication is setup.  # noqa: E501

        :return: The protection_type of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        """Sets the protection_type of this NimbleVCollectionDetails.

        Specifies if volume collection is protected with schedules. If protected, indicated whether replication is setup.  # noqa: E501

        :param protection_type: The protection_type of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._protection_type = protection_type

    @property
    def repl_bytes_transferred(self):
        """Gets the repl_bytes_transferred of this NimbleVCollectionDetails.  # noqa: E501

        Total size of volumes replicated for this volume collection.  # noqa: E501

        :return: The repl_bytes_transferred of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: int
        """
        return self._repl_bytes_transferred

    @repl_bytes_transferred.setter
    def repl_bytes_transferred(self, repl_bytes_transferred):
        """Sets the repl_bytes_transferred of this NimbleVCollectionDetails.

        Total size of volumes replicated for this volume collection.  # noqa: E501

        :param repl_bytes_transferred: The repl_bytes_transferred of this NimbleVCollectionDetails.  # noqa: E501
        :type: int
        """

        self._repl_bytes_transferred = repl_bytes_transferred

    @property
    def repl_priority(self):
        """Gets the repl_priority of this NimbleVCollectionDetails.  # noqa: E501

        Replication priority for the volume collection with the following choices: {normal | high}.  Possible values: 'normal', 'high'.  # noqa: E501

        :return: The repl_priority of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._repl_priority

    @repl_priority.setter
    def repl_priority(self, repl_priority):
        """Sets the repl_priority of this NimbleVCollectionDetails.

        Replication priority for the volume collection with the following choices: {normal | high}.  Possible values: 'normal', 'high'.  # noqa: E501

        :param repl_priority: The repl_priority of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._repl_priority = repl_priority

    @property
    def replication_partner(self):
        """Gets the replication_partner of this NimbleVCollectionDetails.  # noqa: E501

        List of replication partners associated with the volume collection.  # noqa: E501

        :return: The replication_partner of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._replication_partner

    @replication_partner.setter
    def replication_partner(self, replication_partner):
        """Sets the replication_partner of this NimbleVCollectionDetails.

        List of replication partners associated with the volume collection.  # noqa: E501

        :param replication_partner: The replication_partner of this NimbleVCollectionDetails.  # noqa: E501
        :type: list[str]
        """

        self._replication_partner = replication_partner

    @property
    def resource_uri(self):
        """Gets the resource_uri of this NimbleVCollectionDetails.  # noqa: E501


        :return: The resource_uri of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this NimbleVCollectionDetails.


        :param resource_uri: The resource_uri of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

    @property
    def schedule_list(self):
        """Gets the schedule_list of this NimbleVCollectionDetails.  # noqa: E501

        List of schedules for this volume collection.  # noqa: E501

        :return: The schedule_list of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: list[NimbleNsSchedule]
        """
        return self._schedule_list

    @schedule_list.setter
    def schedule_list(self, schedule_list):
        """Sets the schedule_list of this NimbleVCollectionDetails.

        List of schedules for this volume collection.  # noqa: E501

        :param schedule_list: The schedule_list of this NimbleVCollectionDetails.  # noqa: E501
        :type: list[NimbleNsSchedule]
        """

        self._schedule_list = schedule_list

    @property
    def search_name(self):
        """Gets the search_name of this NimbleVCollectionDetails.  # noqa: E501

        Name of volume collection used for object search.  # noqa: E501

        :return: The search_name of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._search_name

    @search_name.setter
    def search_name(self, search_name):
        """Sets the search_name of this NimbleVCollectionDetails.

        Name of volume collection used for object search.  # noqa: E501

        :param search_name: The search_name of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._search_name = search_name

    @property
    def snapcoll_count(self):
        """Gets the snapcoll_count of this NimbleVCollectionDetails.  # noqa: E501

        Count of snapshot collections associated with volume collection.  # noqa: E501

        :return: The snapcoll_count of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: int
        """
        return self._snapcoll_count

    @snapcoll_count.setter
    def snapcoll_count(self, snapcoll_count):
        """Sets the snapcoll_count of this NimbleVCollectionDetails.

        Count of snapshot collections associated with volume collection.  # noqa: E501

        :param snapcoll_count: The snapcoll_count of this NimbleVCollectionDetails.  # noqa: E501
        :type: int
        """

        self._snapcoll_count = snapcoll_count

    @property
    def srep_last_sync(self):
        """Gets the srep_last_sync of this NimbleVCollectionDetails.  # noqa: E501

        Time when a synchronously replicated volume collection was last synchronized.  # noqa: E501

        :return: The srep_last_sync of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: int
        """
        return self._srep_last_sync

    @srep_last_sync.setter
    def srep_last_sync(self, srep_last_sync):
        """Sets the srep_last_sync of this NimbleVCollectionDetails.

        Time when a synchronously replicated volume collection was last synchronized.  # noqa: E501

        :param srep_last_sync: The srep_last_sync of this NimbleVCollectionDetails.  # noqa: E501
        :type: int
        """

        self._srep_last_sync = srep_last_sync

    @property
    def srep_resync_percent(self):
        """Gets the srep_resync_percent of this NimbleVCollectionDetails.  # noqa: E501

        Percentage of the resync progress for a synchronously replicated volume collection.  # noqa: E501

        :return: The srep_resync_percent of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: int
        """
        return self._srep_resync_percent

    @srep_resync_percent.setter
    def srep_resync_percent(self, srep_resync_percent):
        """Sets the srep_resync_percent of this NimbleVCollectionDetails.

        Percentage of the resync progress for a synchronously replicated volume collection.  # noqa: E501

        :param srep_resync_percent: The srep_resync_percent of this NimbleVCollectionDetails.  # noqa: E501
        :type: int
        """

        self._srep_resync_percent = srep_resync_percent

    @property
    def total_repl_bytes(self):
        """Gets the total_repl_bytes of this NimbleVCollectionDetails.  # noqa: E501

        Total size of volumes to be replicated for this volume collection.  # noqa: E501

        :return: The total_repl_bytes of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: int
        """
        return self._total_repl_bytes

    @total_repl_bytes.setter
    def total_repl_bytes(self, total_repl_bytes):
        """Sets the total_repl_bytes of this NimbleVCollectionDetails.

        Total size of volumes to be replicated for this volume collection.  # noqa: E501

        :param total_repl_bytes: The total_repl_bytes of this NimbleVCollectionDetails.  # noqa: E501
        :type: int
        """

        self._total_repl_bytes = total_repl_bytes

    @property
    def type(self):
        """Gets the type of this NimbleVCollectionDetails.  # noqa: E501

        type  # noqa: E501

        :return: The type of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NimbleVCollectionDetails.

        type  # noqa: E501

        :param type: The type of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def vcenter_hostname(self):
        """Gets the vcenter_hostname of this NimbleVCollectionDetails.  # noqa: E501

        VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\\\\":\\\\\".  # noqa: E501

        :return: The vcenter_hostname of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._vcenter_hostname

    @vcenter_hostname.setter
    def vcenter_hostname(self, vcenter_hostname):
        """Sets the vcenter_hostname of this NimbleVCollectionDetails.

        VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\\\\":\\\\\".  # noqa: E501

        :param vcenter_hostname: The vcenter_hostname of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._vcenter_hostname = vcenter_hostname

    @property
    def vcenter_username(self):
        """Gets the vcenter_username of this NimbleVCollectionDetails.  # noqa: E501

        Application VMware vCenter username.  # noqa: E501

        :return: The vcenter_username of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: str
        """
        return self._vcenter_username

    @vcenter_username.setter
    def vcenter_username(self, vcenter_username):
        """Sets the vcenter_username of this NimbleVCollectionDetails.

        Application VMware vCenter username.  # noqa: E501

        :param vcenter_username: The vcenter_username of this NimbleVCollectionDetails.  # noqa: E501
        :type: str
        """

        self._vcenter_username = vcenter_username

    @property
    def volume_count(self):
        """Gets the volume_count of this NimbleVCollectionDetails.  # noqa: E501

        Count of volumes associated with the volume collection.  # noqa: E501

        :return: The volume_count of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: int
        """
        return self._volume_count

    @volume_count.setter
    def volume_count(self, volume_count):
        """Sets the volume_count of this NimbleVCollectionDetails.

        Count of volumes associated with the volume collection.  # noqa: E501

        :param volume_count: The volume_count of this NimbleVCollectionDetails.  # noqa: E501
        :type: int
        """

        self._volume_count = volume_count

    @property
    def volume_list(self):
        """Gets the volume_list of this NimbleVCollectionDetails.  # noqa: E501

        List of volumes associated with the volume collection.  # noqa: E501

        :return: The volume_list of this NimbleVCollectionDetails.  # noqa: E501
        :rtype: list[NimbleVolumeSummary]
        """
        return self._volume_list

    @volume_list.setter
    def volume_list(self, volume_list):
        """Sets the volume_list of this NimbleVCollectionDetails.

        List of volumes associated with the volume collection.  # noqa: E501

        :param volume_list: The volume_list of this NimbleVCollectionDetails.  # noqa: E501
        :type: list[NimbleVolumeSummary]
        """

        self._volume_list = volume_list

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
        if not isinstance(other, NimbleVCollectionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
