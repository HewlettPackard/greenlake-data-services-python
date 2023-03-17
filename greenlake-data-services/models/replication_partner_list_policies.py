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


class ReplicationPartnerListPolicies(object):
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
        'active_active': 'bool',
        'auto_failover': 'bool',
        'auto_recover': 'bool',
        'auto_synchronize': 'bool',
        'multi_target_peer_persistence': 'bool',
        'over_period_alert': 'bool',
        'path_management': 'bool'
    }

    attribute_map = {
        'active_active': 'activeActive',
        'auto_failover': 'autoFailover',
        'auto_recover': 'autoRecover',
        'auto_synchronize': 'autoSynchronize',
        'multi_target_peer_persistence': 'multiTargetPeerPersistence',
        'over_period_alert': 'overPeriodAlert',
        'path_management': 'pathManagement'
    }

    def __init__(self, active_active=None, auto_failover=None, auto_recover=None, auto_synchronize=None, multi_target_peer_persistence=None, over_period_alert=None, path_management=None):  # noqa: E501
        """ReplicationPartnerListPolicies - a model defined in OpenAPI"""  # noqa: E501

        self._active_active = None
        self._auto_failover = None
        self._auto_recover = None
        self._auto_synchronize = None
        self._multi_target_peer_persistence = None
        self._over_period_alert = None
        self._path_management = None
        self.discriminator = None

        if active_active is not None:
            self.active_active = active_active
        if auto_failover is not None:
            self.auto_failover = auto_failover
        if auto_recover is not None:
            self.auto_recover = auto_recover
        if auto_synchronize is not None:
            self.auto_synchronize = auto_synchronize
        if multi_target_peer_persistence is not None:
            self.multi_target_peer_persistence = multi_target_peer_persistence
        if over_period_alert is not None:
            self.over_period_alert = over_period_alert
        if path_management is not None:
            self.path_management = path_management

    @property
    def active_active(self):
        """Gets the active_active of this ReplicationPartnerListPolicies.  # noqa: E501

        Specifies active active policy of the group.  # noqa: E501

        :return: The active_active of this ReplicationPartnerListPolicies.  # noqa: E501
        :rtype: bool
        """
        return self._active_active

    @active_active.setter
    def active_active(self, active_active):
        """Sets the active_active of this ReplicationPartnerListPolicies.

        Specifies active active policy of the group.  # noqa: E501

        :param active_active: The active_active of this ReplicationPartnerListPolicies.  # noqa: E501
        :type: bool
        """

        self._active_active = active_active

    @property
    def auto_failover(self):
        """Gets the auto_failover of this ReplicationPartnerListPolicies.  # noqa: E501

        Automatic failover on a group.  # noqa: E501

        :return: The auto_failover of this ReplicationPartnerListPolicies.  # noqa: E501
        :rtype: bool
        """
        return self._auto_failover

    @auto_failover.setter
    def auto_failover(self, auto_failover):
        """Sets the auto_failover of this ReplicationPartnerListPolicies.

        Automatic failover on a group.  # noqa: E501

        :param auto_failover: The auto_failover of this ReplicationPartnerListPolicies.  # noqa: E501
        :type: bool
        """

        self._auto_failover = auto_failover

    @property
    def auto_recover(self):
        """Gets the auto_recover of this ReplicationPartnerListPolicies.  # noqa: E501

        If the group is stopped as a result of links going down, the group can be automatically restarted after the links come back up.  # noqa: E501

        :return: The auto_recover of this ReplicationPartnerListPolicies.  # noqa: E501
        :rtype: bool
        """
        return self._auto_recover

    @auto_recover.setter
    def auto_recover(self, auto_recover):
        """Sets the auto_recover of this ReplicationPartnerListPolicies.

        If the group is stopped as a result of links going down, the group can be automatically restarted after the links come back up.  # noqa: E501

        :param auto_recover: The auto_recover of this ReplicationPartnerListPolicies.  # noqa: E501
        :type: bool
        """

        self._auto_recover = auto_recover

    @property
    def auto_synchronize(self):
        """Gets the auto_synchronize of this ReplicationPartnerListPolicies.  # noqa: E501

        Specifies auto synchronization of the group.  # noqa: E501

        :return: The auto_synchronize of this ReplicationPartnerListPolicies.  # noqa: E501
        :rtype: bool
        """
        return self._auto_synchronize

    @auto_synchronize.setter
    def auto_synchronize(self, auto_synchronize):
        """Sets the auto_synchronize of this ReplicationPartnerListPolicies.

        Specifies auto synchronization of the group.  # noqa: E501

        :param auto_synchronize: The auto_synchronize of this ReplicationPartnerListPolicies.  # noqa: E501
        :type: bool
        """

        self._auto_synchronize = auto_synchronize

    @property
    def multi_target_peer_persistence(self):
        """Gets the multi_target_peer_persistence of this ReplicationPartnerListPolicies.  # noqa: E501

        Specifies that the group is participating in a Multi-target Peer Persistence configuration. The group must have two targets, one of which must be synchronous.The synchronous group target also requires pathManagement and auto Fail over policy settings.  # noqa: E501

        :return: The multi_target_peer_persistence of this ReplicationPartnerListPolicies.  # noqa: E501
        :rtype: bool
        """
        return self._multi_target_peer_persistence

    @multi_target_peer_persistence.setter
    def multi_target_peer_persistence(self, multi_target_peer_persistence):
        """Sets the multi_target_peer_persistence of this ReplicationPartnerListPolicies.

        Specifies that the group is participating in a Multi-target Peer Persistence configuration. The group must have two targets, one of which must be synchronous.The synchronous group target also requires pathManagement and auto Fail over policy settings.  # noqa: E501

        :param multi_target_peer_persistence: The multi_target_peer_persistence of this ReplicationPartnerListPolicies.  # noqa: E501
        :type: bool
        """

        self._multi_target_peer_persistence = multi_target_peer_persistence

    @property
    def over_period_alert(self):
        """Gets the over_period_alert of this ReplicationPartnerListPolicies.  # noqa: E501

        If synchronization of an asynchronous periodic group takes longer to complete than its synchronization period, an alert is generated.  # noqa: E501

        :return: The over_period_alert of this ReplicationPartnerListPolicies.  # noqa: E501
        :rtype: bool
        """
        return self._over_period_alert

    @over_period_alert.setter
    def over_period_alert(self, over_period_alert):
        """Sets the over_period_alert of this ReplicationPartnerListPolicies.

        If synchronization of an asynchronous periodic group takes longer to complete than its synchronization period, an alert is generated.  # noqa: E501

        :param over_period_alert: The over_period_alert of this ReplicationPartnerListPolicies.  # noqa: E501
        :type: bool
        """

        self._over_period_alert = over_period_alert

    @property
    def path_management(self):
        """Gets the path_management of this ReplicationPartnerListPolicies.  # noqa: E501

        Path management on a group.  # noqa: E501

        :return: The path_management of this ReplicationPartnerListPolicies.  # noqa: E501
        :rtype: bool
        """
        return self._path_management

    @path_management.setter
    def path_management(self, path_management):
        """Sets the path_management of this ReplicationPartnerListPolicies.

        Path management on a group.  # noqa: E501

        :param path_management: The path_management of this ReplicationPartnerListPolicies.  # noqa: E501
        :type: bool
        """

        self._path_management = path_management

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
        if not isinstance(other, ReplicationPartnerListPolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other