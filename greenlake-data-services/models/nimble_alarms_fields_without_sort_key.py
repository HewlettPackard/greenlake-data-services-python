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


class NimbleAlarmsFieldsWithoutSortKey(object):
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
        'ack_time': 'int',
        'activity': 'str',
        'alarm_type': 'int',
        'array': 'str',
        'category': 'str',
        'curr_onset_event_id': 'str',
        'id': 'str',
        'next_notification_time': 'int',
        'object_id': 'str',
        'object_name': 'str',
        'object_type': 'str',
        'onset_time': 'int',
        'remind_every': 'int',
        'remind_every_unit': 'str',
        'severity': 'str',
        'status': 'str',
        'user_full_name': 'str',
        'user_id': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'ack_time': 'ack_time',
        'activity': 'activity',
        'alarm_type': 'alarm_type',
        'array': 'array',
        'category': 'category',
        'curr_onset_event_id': 'curr_onset_event_id',
        'id': 'id',
        'next_notification_time': 'next_notification_time',
        'object_id': 'object_id',
        'object_name': 'object_name',
        'object_type': 'object_type',
        'onset_time': 'onset_time',
        'remind_every': 'remind_every',
        'remind_every_unit': 'remind_every_unit',
        'severity': 'severity',
        'status': 'status',
        'user_full_name': 'user_full_name',
        'user_id': 'user_id',
        'user_name': 'user_name'
    }

    def __init__(self, ack_time=None, activity=None, alarm_type=None, array=None, category=None, curr_onset_event_id=None, id=None, next_notification_time=None, object_id=None, object_name=None, object_type=None, onset_time=None, remind_every=None, remind_every_unit=None, severity=None, status=None, user_full_name=None, user_id=None, user_name=None):  # noqa: E501
        """NimbleAlarmsFieldsWithoutSortKey - a model defined in OpenAPI"""  # noqa: E501

        self._ack_time = None
        self._activity = None
        self._alarm_type = None
        self._array = None
        self._category = None
        self._curr_onset_event_id = None
        self._id = None
        self._next_notification_time = None
        self._object_id = None
        self._object_name = None
        self._object_type = None
        self._onset_time = None
        self._remind_every = None
        self._remind_every_unit = None
        self._severity = None
        self._status = None
        self._user_full_name = None
        self._user_id = None
        self._user_name = None
        self.discriminator = None

        if ack_time is not None:
            self.ack_time = ack_time
        if activity is not None:
            self.activity = activity
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if array is not None:
            self.array = array
        if category is not None:
            self.category = category
        if curr_onset_event_id is not None:
            self.curr_onset_event_id = curr_onset_event_id
        if id is not None:
            self.id = id
        if next_notification_time is not None:
            self.next_notification_time = next_notification_time
        if object_id is not None:
            self.object_id = object_id
        if object_name is not None:
            self.object_name = object_name
        if object_type is not None:
            self.object_type = object_type
        if onset_time is not None:
            self.onset_time = onset_time
        if remind_every is not None:
            self.remind_every = remind_every
        if remind_every_unit is not None:
            self.remind_every_unit = remind_every_unit
        if severity is not None:
            self.severity = severity
        if status is not None:
            self.status = status
        if user_full_name is not None:
            self.user_full_name = user_full_name
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name

    @property
    def ack_time(self):
        """Gets the ack_time of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Time when this alarm was acknowledged. Seconds since last epoch i.e. 00:00 January 1, 1970.  # noqa: E501

        :return: The ack_time of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: int
        """
        return self._ack_time

    @ack_time.setter
    def ack_time(self, ack_time):
        """Sets the ack_time of this NimbleAlarmsFieldsWithoutSortKey.

        Time when this alarm was acknowledged. Seconds since last epoch i.e. 00:00 January 1, 1970.  # noqa: E501

        :param ack_time: The ack_time of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: int
        """

        self._ack_time = ack_time

    @property
    def activity(self):
        """Gets the activity of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Description of activity performed and recorded in alarm. String of 1-1476 printable characters.  # noqa: E501

        :return: The activity of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this NimbleAlarmsFieldsWithoutSortKey.

        Description of activity performed and recorded in alarm. String of 1-1476 printable characters.  # noqa: E501

        :param activity: The activity of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._activity = activity

    @property
    def alarm_type(self):
        """Gets the alarm_type of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Identifier for type of alarm. Non-negative integer in range [0,2147483647].  # noqa: E501

        :return: The alarm_type of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: int
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        """Sets the alarm_type of this NimbleAlarmsFieldsWithoutSortKey.

        Identifier for type of alarm. Non-negative integer in range [0,2147483647].  # noqa: E501

        :param alarm_type: The alarm_type of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: int
        """

        self._alarm_type = alarm_type

    @property
    def array(self):
        """Gets the array of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        The array name where the alarm is generated.  Possible values: array serial number, or '-'.  # noqa: E501

        :return: The array of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._array

    @array.setter
    def array(self, array):
        """Sets the array of this NimbleAlarmsFieldsWithoutSortKey.

        The array name where the alarm is generated.  Possible values: array serial number, or '-'.  # noqa: E501

        :param array: The array of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._array = array

    @property
    def category(self):
        """Gets the category of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Category of the alarm. Possible values: 'unknown', 'hardware', 'service', 'replication', 'volume', 'update', 'configuration', 'test', 'security', 'array_upgrade',cloud_console  # noqa: E501

        :return: The category of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this NimbleAlarmsFieldsWithoutSortKey.

        Category of the alarm. Possible values: 'unknown', 'hardware', 'service', 'replication', 'volume', 'update', 'configuration', 'test', 'security', 'array_upgrade',cloud_console  # noqa: E501

        :param category: The category of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def curr_onset_event_id(self):
        """Gets the curr_onset_event_id of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Identifier for the current onset event. A 42 digit hexadecimal number.  # noqa: E501

        :return: The curr_onset_event_id of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._curr_onset_event_id

    @curr_onset_event_id.setter
    def curr_onset_event_id(self, curr_onset_event_id):
        """Sets the curr_onset_event_id of this NimbleAlarmsFieldsWithoutSortKey.

        Identifier for the current onset event. A 42 digit hexadecimal number.  # noqa: E501

        :param curr_onset_event_id: The curr_onset_event_id of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._curr_onset_event_id = curr_onset_event_id

    @property
    def id(self):
        """Gets the id of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Identifier for the alarm record. A 42 digit hexadecimal number.  # noqa: E501

        :return: The id of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NimbleAlarmsFieldsWithoutSortKey.

        Identifier for the alarm record. A 42 digit hexadecimal number.  # noqa: E501

        :param id: The id of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def next_notification_time(self):
        """Gets the next_notification_time of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Time when next reminder for the alarm will be sent. Signed 64-bit integer.  # noqa: E501

        :return: The next_notification_time of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: int
        """
        return self._next_notification_time

    @next_notification_time.setter
    def next_notification_time(self, next_notification_time):
        """Sets the next_notification_time of this NimbleAlarmsFieldsWithoutSortKey.

        Time when next reminder for the alarm will be sent. Signed 64-bit integer.  # noqa: E501

        :param next_notification_time: The next_notification_time of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: int
        """

        self._next_notification_time = next_notification_time

    @property
    def object_id(self):
        """Gets the object_id of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Identifier of object operated upon. A 42 digit hexadecimal number.  # noqa: E501

        :return: The object_id of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this NimbleAlarmsFieldsWithoutSortKey.

        Identifier of object operated upon. A 42 digit hexadecimal number.  # noqa: E501

        :param object_id: The object_id of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def object_name(self):
        """Gets the object_name of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Name of object operated upon. String of up to 400 alphanumeric characters, - and . and : and \" \" are allowed after first character.  # noqa: E501

        :return: The object_name of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this NimbleAlarmsFieldsWithoutSortKey.

        Name of object operated upon. String of up to 400 alphanumeric characters, - and . and : and \" \" are allowed after first character.  # noqa: E501

        :param object_name: The object_name of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._object_name = object_name

    @property
    def object_type(self):
        """Gets the object_type of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Type of the object being operated upon. Possible values: 'active_directory', 'group', 'chapuser', 'initiatorgrp', 'perfpolicy', 'snapshot', 'snapcoll', 'vol', 'volcoll', 'partner', 'array', 'pool', 'initiator', 'protsched', 'volacl', 'throttle', 'sshkey', 'user', 'protpol', 'prottmpl', 'branch', 'route', 'role', 'privilege', 'netconfig', 'events', 'session', 'subnet', 'array_netconfig', 'nic', 'initiatorgrp_subnet', 'fc_initiator_alias', 'fc_port', 'fc_interface_collection', 'fc', 'event_dipatcher', 'fc_target_port_group', 'encrypt_key', 'encrypt_config', 'snapshot_lun', 'syslog', 'async_job', 'application_server', 'audit_log', 'ip address', 'disk', 'shelf', 'protocol_endpoint', 'folder', 'pe_acl', 'vvol', 'vvol_acl', 'alarm' ,'folset','hc_cluster_config','user group', 'user_policy', 'witness', 'support', 'keymanager', 'trusted_oauth_issuer', 'client_credential'.  # noqa: E501

        :return: The object_type of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this NimbleAlarmsFieldsWithoutSortKey.

        Type of the object being operated upon. Possible values: 'active_directory', 'group', 'chapuser', 'initiatorgrp', 'perfpolicy', 'snapshot', 'snapcoll', 'vol', 'volcoll', 'partner', 'array', 'pool', 'initiator', 'protsched', 'volacl', 'throttle', 'sshkey', 'user', 'protpol', 'prottmpl', 'branch', 'route', 'role', 'privilege', 'netconfig', 'events', 'session', 'subnet', 'array_netconfig', 'nic', 'initiatorgrp_subnet', 'fc_initiator_alias', 'fc_port', 'fc_interface_collection', 'fc', 'event_dipatcher', 'fc_target_port_group', 'encrypt_key', 'encrypt_config', 'snapshot_lun', 'syslog', 'async_job', 'application_server', 'audit_log', 'ip address', 'disk', 'shelf', 'protocol_endpoint', 'folder', 'pe_acl', 'vvol', 'vvol_acl', 'alarm' ,'folset','hc_cluster_config','user group', 'user_policy', 'witness', 'support', 'keymanager', 'trusted_oauth_issuer', 'client_credential'.  # noqa: E501

        :param object_type: The object_type of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._object_type = object_type

    @property
    def onset_time(self):
        """Gets the onset_time of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Time when this alarm was triggered. Seconds since last epoch i.e. 00:00 January 1, 1970.  # noqa: E501

        :return: The onset_time of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: int
        """
        return self._onset_time

    @onset_time.setter
    def onset_time(self, onset_time):
        """Sets the onset_time of this NimbleAlarmsFieldsWithoutSortKey.

        Time when this alarm was triggered. Seconds since last epoch i.e. 00:00 January 1, 1970.  # noqa: E501

        :param onset_time: The onset_time of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: int
        """

        self._onset_time = onset_time

    @property
    def remind_every(self):
        """Gets the remind_every of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Frequency of notification. This number and the remind_every_unit define how frequent one alarm notification is sent.  # noqa: E501

        :return: The remind_every of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: int
        """
        return self._remind_every

    @remind_every.setter
    def remind_every(self, remind_every):
        """Sets the remind_every of this NimbleAlarmsFieldsWithoutSortKey.

        Frequency of notification. This number and the remind_every_unit define how frequent one alarm notification is sent.  # noqa: E501

        :param remind_every: The remind_every of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: int
        """

        self._remind_every = remind_every

    @property
    def remind_every_unit(self):
        """Gets the remind_every_unit of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Time unit over which to send the number of notification specified in 'remind_every'. For example, a value of 'days' with a 'remind_every' of '1' results in one notification every day. Possible values: 'minutes', 'hours', 'days', 'weeks'.  # noqa: E501

        :return: The remind_every_unit of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._remind_every_unit

    @remind_every_unit.setter
    def remind_every_unit(self, remind_every_unit):
        """Sets the remind_every_unit of this NimbleAlarmsFieldsWithoutSortKey.

        Time unit over which to send the number of notification specified in 'remind_every'. For example, a value of 'days' with a 'remind_every' of '1' results in one notification every day. Possible values: 'minutes', 'hours', 'days', 'weeks'.  # noqa: E501

        :param remind_every_unit: The remind_every_unit of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._remind_every_unit = remind_every_unit

    @property
    def severity(self):
        """Gets the severity of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Severity level of the event. Possible values: 'warning', 'critical'.  # noqa: E501

        :return: The severity of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this NimbleAlarmsFieldsWithoutSortKey.

        Severity level of the event. Possible values: 'warning', 'critical'.  # noqa: E501

        :param severity: The severity of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def status(self):
        """Gets the status of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Status of the operation -- open or acknowledged. Possible values: 'open', 'acknowledged'.  # noqa: E501

        :return: The status of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NimbleAlarmsFieldsWithoutSortKey.

        Status of the operation -- open or acknowledged. Possible values: 'open', 'acknowledged'.  # noqa: E501

        :param status: The status of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def user_full_name(self):
        """Gets the user_full_name of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Full name of the user who acknowledged the alarm. Alphanumeric string of up to 64 chars, starts with letter, can include space, apostrophe('), hyphen(-).  # noqa: E501

        :return: The user_full_name of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._user_full_name

    @user_full_name.setter
    def user_full_name(self, user_full_name):
        """Sets the user_full_name of this NimbleAlarmsFieldsWithoutSortKey.

        Full name of the user who acknowledged the alarm. Alphanumeric string of up to 64 chars, starts with letter, can include space, apostrophe('), hyphen(-).  # noqa: E501

        :param user_full_name: The user_full_name of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._user_full_name = user_full_name

    @property
    def user_id(self):
        """Gets the user_id of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Identifier of the user who acknowledged the alarm. A 42 digit hexadecimal number.  # noqa: E501

        :return: The user_id of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NimbleAlarmsFieldsWithoutSortKey.

        Identifier of the user who acknowledged the alarm. A 42 digit hexadecimal number.  # noqa: E501

        :param user_id: The user_id of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501

        Username of the user who acknowledged the alarm. String of up to 80 alphanumeric characters, beginning with a letter. For Active Directory users, it can include backslash (\\), dash (-), period (.), underscore (_) and space.  # noqa: E501

        :return: The user_name of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this NimbleAlarmsFieldsWithoutSortKey.

        Username of the user who acknowledged the alarm. String of up to 80 alphanumeric characters, beginning with a letter. For Active Directory users, it can include backslash (\\), dash (-), period (.), underscore (_) and space.  # noqa: E501

        :param user_name: The user_name of this NimbleAlarmsFieldsWithoutSortKey.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if not isinstance(other, NimbleAlarmsFieldsWithoutSortKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
