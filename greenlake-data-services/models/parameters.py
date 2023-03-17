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


class Parameters(object):
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
        'service_processor_cookie': 'str',
        'allow_domain_users_affect_no_domain': 'bool',
        'allow_ssz': 'bool',
        'allow_wrtback_single_node': 'int',
        'allow_wrtback_upgrade': 'int',
        'auto_admit_tune': 'bool',
        'auto_export_after_reboot': 'bool',
        'compliance_officer_approval': 'bool',
        'disable_chunklet_init_unmap': 'bool',
        'enable_ai_qo_s': 'str',
        'event_log_num': 'int',
        'event_log_size': 'str',
        'failover_matched_set': 'bool',
        'fc_raw_space_alert': 'int',
        'host_dif': 'str',
        'host_dif_template': 'str',
        'max_volume_retention': 'int',
        'nl_raw_space_alert': 'int',
        'overprov_ratio_limit': 'float',
        'overprov_ratio_warning': 'float',
        'persona_profile': 'str',
        'port_failover_enabled': 'bool',
        'r6_layout_version': 'str',
        'remote_copy_host_throttling': 'bool',
        'remote_sys_log': 'int',
        'remote_sys_log_host': 'str',
        'remote_sys_log_security_host': 'str',
        'session_timeout': 'int',
        'single_lun_host': 'bool',
        'ssd_raw_space_alert': 'int',
        'thermal_shutdown': 'bool'
    }

    attribute_map = {
        'service_processor_cookie': 'ServiceProcessorCookie',
        'allow_domain_users_affect_no_domain': 'allowDomainUsersAffectNoDomain',
        'allow_ssz': 'allowSSZ',
        'allow_wrtback_single_node': 'allowWrtbackSingleNode',
        'allow_wrtback_upgrade': 'allowWrtbackUpgrade',
        'auto_admit_tune': 'autoAdmitTune',
        'auto_export_after_reboot': 'autoExportAfterReboot',
        'compliance_officer_approval': 'complianceOfficerApproval',
        'disable_chunklet_init_unmap': 'disableChunkletInitUNMAP',
        'enable_ai_qo_s': 'enableAIQoS',
        'event_log_num': 'eventLogNum',
        'event_log_size': 'eventLogSize',
        'failover_matched_set': 'failoverMatchedSet',
        'fc_raw_space_alert': 'fcRawSpaceAlert',
        'host_dif': 'hostDIF',
        'host_dif_template': 'hostDIFTemplate',
        'max_volume_retention': 'maxVolumeRetention',
        'nl_raw_space_alert': 'nlRawSpaceAlert',
        'overprov_ratio_limit': 'overprovRatioLimit',
        'overprov_ratio_warning': 'overprovRatioWarning',
        'persona_profile': 'personaProfile',
        'port_failover_enabled': 'portFailoverEnabled',
        'r6_layout_version': 'r6LayoutVersion',
        'remote_copy_host_throttling': 'remoteCopyHostThrottling',
        'remote_sys_log': 'remoteSysLog',
        'remote_sys_log_host': 'remoteSysLogHost',
        'remote_sys_log_security_host': 'remoteSysLogSecurityHost',
        'session_timeout': 'sessionTimeout',
        'single_lun_host': 'singleLunHost',
        'ssd_raw_space_alert': 'ssdRawSpaceAlert',
        'thermal_shutdown': 'thermalShutdown'
    }

    def __init__(self, service_processor_cookie=None, allow_domain_users_affect_no_domain=None, allow_ssz=None, allow_wrtback_single_node=None, allow_wrtback_upgrade=None, auto_admit_tune=None, auto_export_after_reboot=None, compliance_officer_approval=None, disable_chunklet_init_unmap=None, enable_ai_qo_s=None, event_log_num=None, event_log_size=None, failover_matched_set=None, fc_raw_space_alert=None, host_dif=None, host_dif_template=None, max_volume_retention=None, nl_raw_space_alert=None, overprov_ratio_limit=None, overprov_ratio_warning=None, persona_profile=None, port_failover_enabled=None, r6_layout_version=None, remote_copy_host_throttling=None, remote_sys_log=None, remote_sys_log_host=None, remote_sys_log_security_host=None, session_timeout=None, single_lun_host=None, ssd_raw_space_alert=None, thermal_shutdown=None):  # noqa: E501
        """Parameters - a model defined in OpenAPI"""  # noqa: E501

        self._service_processor_cookie = None
        self._allow_domain_users_affect_no_domain = None
        self._allow_ssz = None
        self._allow_wrtback_single_node = None
        self._allow_wrtback_upgrade = None
        self._auto_admit_tune = None
        self._auto_export_after_reboot = None
        self._compliance_officer_approval = None
        self._disable_chunklet_init_unmap = None
        self._enable_ai_qo_s = None
        self._event_log_num = None
        self._event_log_size = None
        self._failover_matched_set = None
        self._fc_raw_space_alert = None
        self._host_dif = None
        self._host_dif_template = None
        self._max_volume_retention = None
        self._nl_raw_space_alert = None
        self._overprov_ratio_limit = None
        self._overprov_ratio_warning = None
        self._persona_profile = None
        self._port_failover_enabled = None
        self._r6_layout_version = None
        self._remote_copy_host_throttling = None
        self._remote_sys_log = None
        self._remote_sys_log_host = None
        self._remote_sys_log_security_host = None
        self._session_timeout = None
        self._single_lun_host = None
        self._ssd_raw_space_alert = None
        self._thermal_shutdown = None
        self.discriminator = None

        if service_processor_cookie is not None:
            self.service_processor_cookie = service_processor_cookie
        if allow_domain_users_affect_no_domain is not None:
            self.allow_domain_users_affect_no_domain = allow_domain_users_affect_no_domain
        if allow_ssz is not None:
            self.allow_ssz = allow_ssz
        if allow_wrtback_single_node is not None:
            self.allow_wrtback_single_node = allow_wrtback_single_node
        if allow_wrtback_upgrade is not None:
            self.allow_wrtback_upgrade = allow_wrtback_upgrade
        if auto_admit_tune is not None:
            self.auto_admit_tune = auto_admit_tune
        if auto_export_after_reboot is not None:
            self.auto_export_after_reboot = auto_export_after_reboot
        if compliance_officer_approval is not None:
            self.compliance_officer_approval = compliance_officer_approval
        if disable_chunklet_init_unmap is not None:
            self.disable_chunklet_init_unmap = disable_chunklet_init_unmap
        if enable_ai_qo_s is not None:
            self.enable_ai_qo_s = enable_ai_qo_s
        if event_log_num is not None:
            self.event_log_num = event_log_num
        if event_log_size is not None:
            self.event_log_size = event_log_size
        if failover_matched_set is not None:
            self.failover_matched_set = failover_matched_set
        if fc_raw_space_alert is not None:
            self.fc_raw_space_alert = fc_raw_space_alert
        if host_dif is not None:
            self.host_dif = host_dif
        if host_dif_template is not None:
            self.host_dif_template = host_dif_template
        if max_volume_retention is not None:
            self.max_volume_retention = max_volume_retention
        if nl_raw_space_alert is not None:
            self.nl_raw_space_alert = nl_raw_space_alert
        if overprov_ratio_limit is not None:
            self.overprov_ratio_limit = overprov_ratio_limit
        if overprov_ratio_warning is not None:
            self.overprov_ratio_warning = overprov_ratio_warning
        if persona_profile is not None:
            self.persona_profile = persona_profile
        if port_failover_enabled is not None:
            self.port_failover_enabled = port_failover_enabled
        if r6_layout_version is not None:
            self.r6_layout_version = r6_layout_version
        if remote_copy_host_throttling is not None:
            self.remote_copy_host_throttling = remote_copy_host_throttling
        if remote_sys_log is not None:
            self.remote_sys_log = remote_sys_log
        if remote_sys_log_host is not None:
            self.remote_sys_log_host = remote_sys_log_host
        if remote_sys_log_security_host is not None:
            self.remote_sys_log_security_host = remote_sys_log_security_host
        if session_timeout is not None:
            self.session_timeout = session_timeout
        if single_lun_host is not None:
            self.single_lun_host = single_lun_host
        if ssd_raw_space_alert is not None:
            self.ssd_raw_space_alert = ssd_raw_space_alert
        if thermal_shutdown is not None:
            self.thermal_shutdown = thermal_shutdown

    @property
    def service_processor_cookie(self):
        """Gets the service_processor_cookie of this Parameters.  # noqa: E501

        Service processor cookie  # noqa: E501

        :return: The service_processor_cookie of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._service_processor_cookie

    @service_processor_cookie.setter
    def service_processor_cookie(self, service_processor_cookie):
        """Sets the service_processor_cookie of this Parameters.

        Service processor cookie  # noqa: E501

        :param service_processor_cookie: The service_processor_cookie of this Parameters.  # noqa: E501
        :type: str
        """

        self._service_processor_cookie = service_processor_cookie

    @property
    def allow_domain_users_affect_no_domain(self):
        """Gets the allow_domain_users_affect_no_domain of this Parameters.  # noqa: E501


        :return: The allow_domain_users_affect_no_domain of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._allow_domain_users_affect_no_domain

    @allow_domain_users_affect_no_domain.setter
    def allow_domain_users_affect_no_domain(self, allow_domain_users_affect_no_domain):
        """Sets the allow_domain_users_affect_no_domain of this Parameters.


        :param allow_domain_users_affect_no_domain: The allow_domain_users_affect_no_domain of this Parameters.  # noqa: E501
        :type: bool
        """

        self._allow_domain_users_affect_no_domain = allow_domain_users_affect_no_domain

    @property
    def allow_ssz(self):
        """Gets the allow_ssz of this Parameters.  # noqa: E501

        Enables or disables support for using the -ssz option during CPG creation  # noqa: E501

        :return: The allow_ssz of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._allow_ssz

    @allow_ssz.setter
    def allow_ssz(self, allow_ssz):
        """Sets the allow_ssz of this Parameters.

        Enables or disables support for using the -ssz option during CPG creation  # noqa: E501

        :param allow_ssz: The allow_ssz of this Parameters.  # noqa: E501
        :type: bool
        """

        self._allow_ssz = allow_ssz

    @property
    def allow_wrtback_single_node(self):
        """Gets the allow_wrtback_single_node of this Parameters.  # noqa: E501

        Allow writeback single node setting in days  # noqa: E501

        :return: The allow_wrtback_single_node of this Parameters.  # noqa: E501
        :rtype: int
        """
        return self._allow_wrtback_single_node

    @allow_wrtback_single_node.setter
    def allow_wrtback_single_node(self, allow_wrtback_single_node):
        """Sets the allow_wrtback_single_node of this Parameters.

        Allow writeback single node setting in days  # noqa: E501

        :param allow_wrtback_single_node: The allow_wrtback_single_node of this Parameters.  # noqa: E501
        :type: int
        """

        self._allow_wrtback_single_node = allow_wrtback_single_node

    @property
    def allow_wrtback_upgrade(self):
        """Gets the allow_wrtback_upgrade of this Parameters.  # noqa: E501

        Allow the system to continue caching when in a single node state during an upgrade for up to the specified number of days  # noqa: E501

        :return: The allow_wrtback_upgrade of this Parameters.  # noqa: E501
        :rtype: int
        """
        return self._allow_wrtback_upgrade

    @allow_wrtback_upgrade.setter
    def allow_wrtback_upgrade(self, allow_wrtback_upgrade):
        """Sets the allow_wrtback_upgrade of this Parameters.

        Allow the system to continue caching when in a single node state during an upgrade for up to the specified number of days  # noqa: E501

        :param allow_wrtback_upgrade: The allow_wrtback_upgrade of this Parameters.  # noqa: E501
        :type: int
        """

        self._allow_wrtback_upgrade = allow_wrtback_upgrade

    @property
    def auto_admit_tune(self):
        """Gets the auto_admit_tune of this Parameters.  # noqa: E501

        Enables or disables automatic rebalancing when admithw detects new disks. Only applies to 2-node systems  # noqa: E501

        :return: The auto_admit_tune of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._auto_admit_tune

    @auto_admit_tune.setter
    def auto_admit_tune(self, auto_admit_tune):
        """Sets the auto_admit_tune of this Parameters.

        Enables or disables automatic rebalancing when admithw detects new disks. Only applies to 2-node systems  # noqa: E501

        :param auto_admit_tune: The auto_admit_tune of this Parameters.  # noqa: E501
        :type: bool
        """

        self._auto_admit_tune = auto_admit_tune

    @property
    def auto_export_after_reboot(self):
        """Gets the auto_export_after_reboot of this Parameters.  # noqa: E501

        Enables or disables automatically exporting vluns after a reboot. If disabled, vluns and host ports will not become active after a reboot until \"setsysmgr export_vluns\" is issued.  # noqa: E501

        :return: The auto_export_after_reboot of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._auto_export_after_reboot

    @auto_export_after_reboot.setter
    def auto_export_after_reboot(self, auto_export_after_reboot):
        """Sets the auto_export_after_reboot of this Parameters.

        Enables or disables automatically exporting vluns after a reboot. If disabled, vluns and host ports will not become active after a reboot until \"setsysmgr export_vluns\" is issued.  # noqa: E501

        :param auto_export_after_reboot: The auto_export_after_reboot of this Parameters.  # noqa: E501
        :type: bool
        """

        self._auto_export_after_reboot = auto_export_after_reboot

    @property
    def compliance_officer_approval(self):
        """Gets the compliance_officer_approval of this Parameters.  # noqa: E501

        Specifies whether to enable or disable the compliance officer approval mode.  # noqa: E501

        :return: The compliance_officer_approval of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._compliance_officer_approval

    @compliance_officer_approval.setter
    def compliance_officer_approval(self, compliance_officer_approval):
        """Sets the compliance_officer_approval of this Parameters.

        Specifies whether to enable or disable the compliance officer approval mode.  # noqa: E501

        :param compliance_officer_approval: The compliance_officer_approval of this Parameters.  # noqa: E501
        :type: bool
        """

        self._compliance_officer_approval = compliance_officer_approval

    @property
    def disable_chunklet_init_unmap(self):
        """Gets the disable_chunklet_init_unmap of this Parameters.  # noqa: E501

        Flag to know if the ChunkletInitUNMAP is disabled  # noqa: E501

        :return: The disable_chunklet_init_unmap of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._disable_chunklet_init_unmap

    @disable_chunklet_init_unmap.setter
    def disable_chunklet_init_unmap(self, disable_chunklet_init_unmap):
        """Sets the disable_chunklet_init_unmap of this Parameters.

        Flag to know if the ChunkletInitUNMAP is disabled  # noqa: E501

        :param disable_chunklet_init_unmap: The disable_chunklet_init_unmap of this Parameters.  # noqa: E501
        :type: bool
        """

        self._disable_chunklet_init_unmap = disable_chunklet_init_unmap

    @property
    def enable_ai_qo_s(self):
        """Gets the enable_ai_qo_s of this Parameters.  # noqa: E501

        Enable or disable AI QoS feature, values are:yes or no  # noqa: E501

        :return: The enable_ai_qo_s of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._enable_ai_qo_s

    @enable_ai_qo_s.setter
    def enable_ai_qo_s(self, enable_ai_qo_s):
        """Sets the enable_ai_qo_s of this Parameters.

        Enable or disable AI QoS feature, values are:yes or no  # noqa: E501

        :param enable_ai_qo_s: The enable_ai_qo_s of this Parameters.  # noqa: E501
        :type: str
        """

        self._enable_ai_qo_s = enable_ai_qo_s

    @property
    def event_log_num(self):
        """Gets the event_log_num of this Parameters.  # noqa: E501

        The number of event log files  # noqa: E501

        :return: The event_log_num of this Parameters.  # noqa: E501
        :rtype: int
        """
        return self._event_log_num

    @event_log_num.setter
    def event_log_num(self, event_log_num):
        """Sets the event_log_num of this Parameters.

        The number of event log files  # noqa: E501

        :param event_log_num: The event_log_num of this Parameters.  # noqa: E501
        :type: int
        """

        self._event_log_num = event_log_num

    @property
    def event_log_size(self):
        """Gets the event_log_size of this Parameters.  # noqa: E501

        The size of the event log file  # noqa: E501

        :return: The event_log_size of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._event_log_size

    @event_log_size.setter
    def event_log_size(self, event_log_size):
        """Sets the event_log_size of this Parameters.

        The size of the event log file  # noqa: E501

        :param event_log_size: The event_log_size of this Parameters.  # noqa: E501
        :type: str
        """

        self._event_log_size = event_log_size

    @property
    def failover_matched_set(self):
        """Gets the failover_matched_set of this Parameters.  # noqa: E501

        When using Matched Set VLUN templates for exports and Persistent Ports together, you must enable this parameter. The default for this setting is disabled  # noqa: E501

        :return: The failover_matched_set of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._failover_matched_set

    @failover_matched_set.setter
    def failover_matched_set(self, failover_matched_set):
        """Sets the failover_matched_set of this Parameters.

        When using Matched Set VLUN templates for exports and Persistent Ports together, you must enable this parameter. The default for this setting is disabled  # noqa: E501

        :param failover_matched_set: The failover_matched_set of this Parameters.  # noqa: E501
        :type: bool
        """

        self._failover_matched_set = failover_matched_set

    @property
    def fc_raw_space_alert(self):
        """Gets the fc_raw_space_alert of this Parameters.  # noqa: E501

        FC raw space alert setting in MiB  # noqa: E501

        :return: The fc_raw_space_alert of this Parameters.  # noqa: E501
        :rtype: int
        """
        return self._fc_raw_space_alert

    @fc_raw_space_alert.setter
    def fc_raw_space_alert(self, fc_raw_space_alert):
        """Sets the fc_raw_space_alert of this Parameters.

        FC raw space alert setting in MiB  # noqa: E501

        :param fc_raw_space_alert: The fc_raw_space_alert of this Parameters.  # noqa: E501
        :type: int
        """

        self._fc_raw_space_alert = fc_raw_space_alert

    @property
    def host_dif(self):
        """Gets the host_dif of this Parameters.  # noqa: E501

        Host Data Integrity Field type are:yes or no  # noqa: E501

        :return: The host_dif of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._host_dif

    @host_dif.setter
    def host_dif(self, host_dif):
        """Sets the host_dif of this Parameters.

        Host Data Integrity Field type are:yes or no  # noqa: E501

        :param host_dif: The host_dif of this Parameters.  # noqa: E501
        :type: str
        """

        self._host_dif = host_dif

    @property
    def host_dif_template(self):
        """Gets the host_dif_template of this Parameters.  # noqa: E501

        HostDIF Template  # noqa: E501

        :return: The host_dif_template of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._host_dif_template

    @host_dif_template.setter
    def host_dif_template(self, host_dif_template):
        """Sets the host_dif_template of this Parameters.

        HostDIF Template  # noqa: E501

        :param host_dif_template: The host_dif_template of this Parameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["NO_HOST_DIF", "THREEPAR_HOST_DIF", "STD_HOST_DIF", "HBA_HOST_DIF", "null"]  # noqa: E501
        if host_dif_template not in allowed_values:
            raise ValueError(
                "Invalid value for `host_dif_template` ({0}), must be one of {1}"  # noqa: E501
                .format(host_dif_template, allowed_values)
            )

        self._host_dif_template = host_dif_template

    @property
    def max_volume_retention(self):
        """Gets the max_volume_retention of this Parameters.  # noqa: E501

        Maximum global volume retention policy in seconds  # noqa: E501

        :return: The max_volume_retention of this Parameters.  # noqa: E501
        :rtype: int
        """
        return self._max_volume_retention

    @max_volume_retention.setter
    def max_volume_retention(self, max_volume_retention):
        """Sets the max_volume_retention of this Parameters.

        Maximum global volume retention policy in seconds  # noqa: E501

        :param max_volume_retention: The max_volume_retention of this Parameters.  # noqa: E501
        :type: int
        """

        self._max_volume_retention = max_volume_retention

    @property
    def nl_raw_space_alert(self):
        """Gets the nl_raw_space_alert of this Parameters.  # noqa: E501

        NL raw space alert setting in MiB  # noqa: E501

        :return: The nl_raw_space_alert of this Parameters.  # noqa: E501
        :rtype: int
        """
        return self._nl_raw_space_alert

    @nl_raw_space_alert.setter
    def nl_raw_space_alert(self, nl_raw_space_alert):
        """Sets the nl_raw_space_alert of this Parameters.

        NL raw space alert setting in MiB  # noqa: E501

        :param nl_raw_space_alert: The nl_raw_space_alert of this Parameters.  # noqa: E501
        :type: int
        """

        self._nl_raw_space_alert = nl_raw_space_alert

    @property
    def overprov_ratio_limit(self):
        """Gets the overprov_ratio_limit of this Parameters.  # noqa: E501

        Over provisioning ratio limit setting  # noqa: E501

        :return: The overprov_ratio_limit of this Parameters.  # noqa: E501
        :rtype: float
        """
        return self._overprov_ratio_limit

    @overprov_ratio_limit.setter
    def overprov_ratio_limit(self, overprov_ratio_limit):
        """Sets the overprov_ratio_limit of this Parameters.

        Over provisioning ratio limit setting  # noqa: E501

        :param overprov_ratio_limit: The overprov_ratio_limit of this Parameters.  # noqa: E501
        :type: float
        """

        self._overprov_ratio_limit = overprov_ratio_limit

    @property
    def overprov_ratio_warning(self):
        """Gets the overprov_ratio_warning of this Parameters.  # noqa: E501

        Over provisioning ratio warning setting  # noqa: E501

        :return: The overprov_ratio_warning of this Parameters.  # noqa: E501
        :rtype: float
        """
        return self._overprov_ratio_warning

    @overprov_ratio_warning.setter
    def overprov_ratio_warning(self, overprov_ratio_warning):
        """Sets the overprov_ratio_warning of this Parameters.

        Over provisioning ratio warning setting  # noqa: E501

        :param overprov_ratio_warning: The overprov_ratio_warning of this Parameters.  # noqa: E501
        :type: float
        """

        self._overprov_ratio_warning = overprov_ratio_warning

    @property
    def persona_profile(self):
        """Gets the persona_profile of this Parameters.  # noqa: E501

        If set to 'block-preferred' File persona is supported. The default is 'block-only'  # noqa: E501

        :return: The persona_profile of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._persona_profile

    @persona_profile.setter
    def persona_profile(self, persona_profile):
        """Sets the persona_profile of this Parameters.

        If set to 'block-preferred' File persona is supported. The default is 'block-only'  # noqa: E501

        :param persona_profile: The persona_profile of this Parameters.  # noqa: E501
        :type: str
        """

        self._persona_profile = persona_profile

    @property
    def port_failover_enabled(self):
        """Gets the port_failover_enabled of this Parameters.  # noqa: E501

        Enables or disables the automatic failover of target ports to their designated partner ports  # noqa: E501

        :return: The port_failover_enabled of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._port_failover_enabled

    @port_failover_enabled.setter
    def port_failover_enabled(self, port_failover_enabled):
        """Sets the port_failover_enabled of this Parameters.

        Enables or disables the automatic failover of target ports to their designated partner ports  # noqa: E501

        :param port_failover_enabled: The port_failover_enabled of this Parameters.  # noqa: E501
        :type: bool
        """

        self._port_failover_enabled = port_failover_enabled

    @property
    def r6_layout_version(self):
        """Gets the r6_layout_version of this Parameters.  # noqa: E501

        RAID6 implementation version in use  # noqa: E501

        :return: The r6_layout_version of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._r6_layout_version

    @r6_layout_version.setter
    def r6_layout_version(self, r6_layout_version):
        """Sets the r6_layout_version of this Parameters.

        RAID6 implementation version in use  # noqa: E501

        :param r6_layout_version: The r6_layout_version of this Parameters.  # noqa: E501
        :type: str
        """

        self._r6_layout_version = r6_layout_version

    @property
    def remote_copy_host_throttling(self):
        """Gets the remote_copy_host_throttling of this Parameters.  # noqa: E501

        Enables or disables Remote Copy throttling policy for host IO replicated in asynchronous streaming mode  # noqa: E501

        :return: The remote_copy_host_throttling of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._remote_copy_host_throttling

    @remote_copy_host_throttling.setter
    def remote_copy_host_throttling(self, remote_copy_host_throttling):
        """Sets the remote_copy_host_throttling of this Parameters.

        Enables or disables Remote Copy throttling policy for host IO replicated in asynchronous streaming mode  # noqa: E501

        :param remote_copy_host_throttling: The remote_copy_host_throttling of this Parameters.  # noqa: E501
        :type: bool
        """

        self._remote_copy_host_throttling = remote_copy_host_throttling

    @property
    def remote_sys_log(self):
        """Gets the remote_sys_log of this Parameters.  # noqa: E501

        Remote Syslog Enabled/Disabled  # noqa: E501

        :return: The remote_sys_log of this Parameters.  # noqa: E501
        :rtype: int
        """
        return self._remote_sys_log

    @remote_sys_log.setter
    def remote_sys_log(self, remote_sys_log):
        """Sets the remote_sys_log of this Parameters.

        Remote Syslog Enabled/Disabled  # noqa: E501

        :param remote_sys_log: The remote_sys_log of this Parameters.  # noqa: E501
        :type: int
        """

        self._remote_sys_log = remote_sys_log

    @property
    def remote_sys_log_host(self):
        """Gets the remote_sys_log_host of this Parameters.  # noqa: E501

        Host details for Remote Syslog  # noqa: E501

        :return: The remote_sys_log_host of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._remote_sys_log_host

    @remote_sys_log_host.setter
    def remote_sys_log_host(self, remote_sys_log_host):
        """Sets the remote_sys_log_host of this Parameters.

        Host details for Remote Syslog  # noqa: E501

        :param remote_sys_log_host: The remote_sys_log_host of this Parameters.  # noqa: E501
        :type: str
        """

        self._remote_sys_log_host = remote_sys_log_host

    @property
    def remote_sys_log_security_host(self):
        """Gets the remote_sys_log_security_host of this Parameters.  # noqa: E501

        Security Host details for Remote Syslog  # noqa: E501

        :return: The remote_sys_log_security_host of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._remote_sys_log_security_host

    @remote_sys_log_security_host.setter
    def remote_sys_log_security_host(self, remote_sys_log_security_host):
        """Sets the remote_sys_log_security_host of this Parameters.

        Security Host details for Remote Syslog  # noqa: E501

        :param remote_sys_log_security_host: The remote_sys_log_security_host of this Parameters.  # noqa: E501
        :type: str
        """

        self._remote_sys_log_security_host = remote_sys_log_security_host

    @property
    def session_timeout(self):
        """Gets the session_timeout of this Parameters.  # noqa: E501

        Idle session timeout for a CLI session  # noqa: E501

        :return: The session_timeout of this Parameters.  # noqa: E501
        :rtype: int
        """
        return self._session_timeout

    @session_timeout.setter
    def session_timeout(self, session_timeout):
        """Sets the session_timeout of this Parameters.

        Idle session timeout for a CLI session  # noqa: E501

        :param session_timeout: The session_timeout of this Parameters.  # noqa: E501
        :type: int
        """

        self._session_timeout = session_timeout

    @property
    def single_lun_host(self):
        """Gets the single_lun_host of this Parameters.  # noqa: E501

        Enables or disables support to limit volume exports such that each volume can only be exported to a given host one time  # noqa: E501

        :return: The single_lun_host of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._single_lun_host

    @single_lun_host.setter
    def single_lun_host(self, single_lun_host):
        """Sets the single_lun_host of this Parameters.

        Enables or disables support to limit volume exports such that each volume can only be exported to a given host one time  # noqa: E501

        :param single_lun_host: The single_lun_host of this Parameters.  # noqa: E501
        :type: bool
        """

        self._single_lun_host = single_lun_host

    @property
    def ssd_raw_space_alert(self):
        """Gets the ssd_raw_space_alert of this Parameters.  # noqa: E501

        SSD raw space alert setting in MiB  # noqa: E501

        :return: The ssd_raw_space_alert of this Parameters.  # noqa: E501
        :rtype: int
        """
        return self._ssd_raw_space_alert

    @ssd_raw_space_alert.setter
    def ssd_raw_space_alert(self, ssd_raw_space_alert):
        """Sets the ssd_raw_space_alert of this Parameters.

        SSD raw space alert setting in MiB  # noqa: E501

        :param ssd_raw_space_alert: The ssd_raw_space_alert of this Parameters.  # noqa: E501
        :type: int
        """

        self._ssd_raw_space_alert = ssd_raw_space_alert

    @property
    def thermal_shutdown(self):
        """Gets the thermal_shutdown of this Parameters.  # noqa: E501

        Enables or disables a system shutdown when the temperature gets too hot  # noqa: E501

        :return: The thermal_shutdown of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._thermal_shutdown

    @thermal_shutdown.setter
    def thermal_shutdown(self, thermal_shutdown):
        """Sets the thermal_shutdown of this Parameters.

        Enables or disables a system shutdown when the temperature gets too hot  # noqa: E501

        :param thermal_shutdown: The thermal_shutdown of this Parameters.  # noqa: E501
        :type: bool
        """

        self._thermal_shutdown = thermal_shutdown

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
        if not isinstance(other, Parameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other