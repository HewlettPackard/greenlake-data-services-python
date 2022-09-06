"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from greenlake_data_services.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from greenlake_data_services.exceptions import ApiAttributeError



class NimbleAlarmsFieldsWithSortKey(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = True

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'ack_time': (int, none_type,),  # noqa: E501
            'activity': (str, none_type,),  # noqa: E501
            'array': (str, none_type,),  # noqa: E501
            'category': (str, none_type,),  # noqa: E501
            'curr_onset_event_id': (str, none_type,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'next_notification_time': (int, none_type,),  # noqa: E501
            'object_id': (str, none_type,),  # noqa: E501
            'object_name': (str, none_type,),  # noqa: E501
            'object_type': (str, none_type,),  # noqa: E501
            'onset_time': (int, none_type,),  # noqa: E501
            'remind_every': (int, none_type,),  # noqa: E501
            'remind_every_unit': (str, none_type,),  # noqa: E501
            'severity': (str, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'user_full_name': (str, none_type,),  # noqa: E501
            'user_id': (str, none_type,),  # noqa: E501
            'user_name': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'ack_time': 'ack_time',  # noqa: E501
        'activity': 'activity',  # noqa: E501
        'array': 'array',  # noqa: E501
        'category': 'category',  # noqa: E501
        'curr_onset_event_id': 'curr_onset_event_id',  # noqa: E501
        'id': 'id',  # noqa: E501
        'next_notification_time': 'next_notification_time',  # noqa: E501
        'object_id': 'object_id',  # noqa: E501
        'object_name': 'object_name',  # noqa: E501
        'object_type': 'object_type',  # noqa: E501
        'onset_time': 'onset_time',  # noqa: E501
        'remind_every': 'remind_every',  # noqa: E501
        'remind_every_unit': 'remind_every_unit',  # noqa: E501
        'severity': 'severity',  # noqa: E501
        'status': 'status',  # noqa: E501
        'user_full_name': 'user_full_name',  # noqa: E501
        'user_id': 'user_id',  # noqa: E501
        'user_name': 'user_name',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """NimbleAlarmsFieldsWithSortKey - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            ack_time (int, none_type): Time when this alarm was acknowledged. Seconds since last epoch i.e. 00:00 January 1, 1970. `Filter, Sort`. [optional]  # noqa: E501
            activity (str, none_type): Description of activity performed and recorded in alarm. String of 1-1476 printable characters. `Filter, Sort`. [optional]  # noqa: E501
            array (str, none_type): The array name where the alarm is generated.  Possible values: array serial number, or '-'. `Filter, Sort`. [optional]  # noqa: E501
            category (str, none_type): Category of the alarm. Possible values: 'unknown', 'hardware', 'service', 'replication', 'volume', 'update', 'configuration', 'test', 'security', 'array_upgrade',cloud_console `Filter, Sort`. [optional]  # noqa: E501
            curr_onset_event_id (str, none_type): Identifier for the current onset event. A 42 digit hexadecimal number. `Filter, Sort`. [optional]  # noqa: E501
            id (str, none_type): Identifier for the alarm record. A 42 digit hexadecimal number. `Filter, Sort`. [optional]  # noqa: E501
            next_notification_time (int, none_type): Time when next reminder for the alarm will be sent. Signed 64-bit integer. `Filter, Sort`. [optional]  # noqa: E501
            object_id (str, none_type): Identifier of object operated upon. A 42 digit hexadecimal number.  `Filter, Sort`. [optional]  # noqa: E501
            object_name (str, none_type): Name of object operated upon. String of up to 400 alphanumeric characters, - and . and : and \" \" are allowed after first character.  `Filter, Sort`. [optional]  # noqa: E501
            object_type (str, none_type): Type of the object being operated upon. Possible values: 'active_directory', 'group', 'chapuser', 'initiatorgrp', 'perfpolicy', 'snapshot', 'snapcoll', 'vol', 'volcoll', 'partner', 'array', 'pool', 'initiator', 'protsched', 'volacl', 'throttle', 'sshkey', 'user', 'protpol', 'prottmpl', 'branch', 'route', 'role', 'privilege', 'netconfig', 'events', 'session', 'subnet', 'array_netconfig', 'nic', 'initiatorgrp_subnet', 'fc_initiator_alias', 'fc_port', 'fc_interface_collection', 'fc', 'event_dipatcher', 'fc_target_port_group', 'encrypt_key', 'encrypt_config', 'snapshot_lun', 'syslog', 'async_job', 'application_server', 'audit_log', 'ip address', 'disk', 'shelf', 'protocol_endpoint', 'folder', 'pe_acl', 'vvol', 'vvol_acl', 'alarm' ,'folset','hc_cluster_config','user group', 'user_policy', 'witness', 'support', 'keymanager', 'trusted_oauth_issuer', 'client_credential'. `Filter, Sort`. [optional]  # noqa: E501
            onset_time (int, none_type): Time when this alarm was triggered. Seconds since last epoch i.e. 00:00 January 1, 1970. `Filter, Sort`. [optional]  # noqa: E501
            remind_every (int, none_type): Frequency of notification. This number and the remind_every_unit define how frequent one alarm notification is sent. `Filter, Sort`. [optional]  # noqa: E501
            remind_every_unit (str, none_type): Time unit over which to send the number of notification specified in 'remind_every'. For example, a value of 'days' with a 'remind_every' of '1' results in one notification every day. Possible values: 'minutes', 'hours', 'days', 'weeks'. `Filter, Sort`. [optional]  # noqa: E501
            severity (str, none_type): Severity level of the event. Possible values: 'warning', 'critical'. `Filter, Sort`. [optional]  # noqa: E501
            status (str, none_type): Status of the operation -- open or acknowledged. Possible values: 'open', 'acknowledged'. `Filter, Sort`. [optional]  # noqa: E501
            user_full_name (str, none_type): Full name of the user who acknowledged the alarm. Alphanumeric string of up to 64 chars, starts with letter, can include space, apostrophe('), hyphen(-). `Filter, Sort`. [optional]  # noqa: E501
            user_id (str, none_type): Identifier of the user who acknowledged the alarm. A 42 digit hexadecimal number.  `Filter, Sort`. [optional]  # noqa: E501
            user_name (str, none_type): Username of the user who acknowledged the alarm. String of up to 80 alphanumeric characters, beginning with a letter. For Active Directory users, it can include backslash (\\), dash (-), period (.), underscore (_) and space.  `Filter, Sort`. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """NimbleAlarmsFieldsWithSortKey - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            ack_time (int, none_type): Time when this alarm was acknowledged. Seconds since last epoch i.e. 00:00 January 1, 1970. `Filter, Sort`. [optional]  # noqa: E501
            activity (str, none_type): Description of activity performed and recorded in alarm. String of 1-1476 printable characters. `Filter, Sort`. [optional]  # noqa: E501
            array (str, none_type): The array name where the alarm is generated.  Possible values: array serial number, or '-'. `Filter, Sort`. [optional]  # noqa: E501
            category (str, none_type): Category of the alarm. Possible values: 'unknown', 'hardware', 'service', 'replication', 'volume', 'update', 'configuration', 'test', 'security', 'array_upgrade',cloud_console `Filter, Sort`. [optional]  # noqa: E501
            curr_onset_event_id (str, none_type): Identifier for the current onset event. A 42 digit hexadecimal number. `Filter, Sort`. [optional]  # noqa: E501
            id (str, none_type): Identifier for the alarm record. A 42 digit hexadecimal number. `Filter, Sort`. [optional]  # noqa: E501
            next_notification_time (int, none_type): Time when next reminder for the alarm will be sent. Signed 64-bit integer. `Filter, Sort`. [optional]  # noqa: E501
            object_id (str, none_type): Identifier of object operated upon. A 42 digit hexadecimal number.  `Filter, Sort`. [optional]  # noqa: E501
            object_name (str, none_type): Name of object operated upon. String of up to 400 alphanumeric characters, - and . and : and \" \" are allowed after first character.  `Filter, Sort`. [optional]  # noqa: E501
            object_type (str, none_type): Type of the object being operated upon. Possible values: 'active_directory', 'group', 'chapuser', 'initiatorgrp', 'perfpolicy', 'snapshot', 'snapcoll', 'vol', 'volcoll', 'partner', 'array', 'pool', 'initiator', 'protsched', 'volacl', 'throttle', 'sshkey', 'user', 'protpol', 'prottmpl', 'branch', 'route', 'role', 'privilege', 'netconfig', 'events', 'session', 'subnet', 'array_netconfig', 'nic', 'initiatorgrp_subnet', 'fc_initiator_alias', 'fc_port', 'fc_interface_collection', 'fc', 'event_dipatcher', 'fc_target_port_group', 'encrypt_key', 'encrypt_config', 'snapshot_lun', 'syslog', 'async_job', 'application_server', 'audit_log', 'ip address', 'disk', 'shelf', 'protocol_endpoint', 'folder', 'pe_acl', 'vvol', 'vvol_acl', 'alarm' ,'folset','hc_cluster_config','user group', 'user_policy', 'witness', 'support', 'keymanager', 'trusted_oauth_issuer', 'client_credential'. `Filter, Sort`. [optional]  # noqa: E501
            onset_time (int, none_type): Time when this alarm was triggered. Seconds since last epoch i.e. 00:00 January 1, 1970. `Filter, Sort`. [optional]  # noqa: E501
            remind_every (int, none_type): Frequency of notification. This number and the remind_every_unit define how frequent one alarm notification is sent. `Filter, Sort`. [optional]  # noqa: E501
            remind_every_unit (str, none_type): Time unit over which to send the number of notification specified in 'remind_every'. For example, a value of 'days' with a 'remind_every' of '1' results in one notification every day. Possible values: 'minutes', 'hours', 'days', 'weeks'. `Filter, Sort`. [optional]  # noqa: E501
            severity (str, none_type): Severity level of the event. Possible values: 'warning', 'critical'. `Filter, Sort`. [optional]  # noqa: E501
            status (str, none_type): Status of the operation -- open or acknowledged. Possible values: 'open', 'acknowledged'. `Filter, Sort`. [optional]  # noqa: E501
            user_full_name (str, none_type): Full name of the user who acknowledged the alarm. Alphanumeric string of up to 64 chars, starts with letter, can include space, apostrophe('), hyphen(-). `Filter, Sort`. [optional]  # noqa: E501
            user_id (str, none_type): Identifier of the user who acknowledged the alarm. A 42 digit hexadecimal number.  `Filter, Sort`. [optional]  # noqa: E501
            user_name (str, none_type): Username of the user who acknowledged the alarm. String of up to 80 alphanumeric characters, beginning with a letter. For Active Directory users, it can include backslash (\\), dash (-), period (.), underscore (_) and space.  `Filter, Sort`. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
