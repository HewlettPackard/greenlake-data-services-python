"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
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



class NimbleEditGroupInput(ModelNormal):
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

    _nullable = False

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
            'auto_switchover_enabled': (bool, none_type,),  # noqa: E501
            'autoclean_unmanaged_snapshots_enabled': (bool, none_type,),  # noqa: E501
            'autoclean_unmanaged_snapshots_ttl_unit': (int, none_type,),  # noqa: E501
            'cc_mode_enabled': (bool, none_type,),  # noqa: E501
            'date': (int, none_type,),  # noqa: E501
            'default_iscsi_target_scope': (str, none_type,),  # noqa: E501
            'group_snapshot_ttl': (int, none_type,),  # noqa: E501
            'group_target_name': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'ntp_server': (str, none_type,),  # noqa: E501
            'tdz_enabled': (bool, none_type,),  # noqa: E501
            'tdz_prefix': (str, none_type,),  # noqa: E501
            'timezone': (str, none_type,),  # noqa: E501
            'tlsv1_enabled': (bool, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'auto_switchover_enabled': 'auto_switchover_enabled',  # noqa: E501
        'autoclean_unmanaged_snapshots_enabled': 'autoclean_unmanaged_snapshots_enabled',  # noqa: E501
        'autoclean_unmanaged_snapshots_ttl_unit': 'autoclean_unmanaged_snapshots_ttl_unit',  # noqa: E501
        'cc_mode_enabled': 'cc_mode_enabled',  # noqa: E501
        'date': 'date',  # noqa: E501
        'default_iscsi_target_scope': 'default_iscsi_target_scope',  # noqa: E501
        'group_snapshot_ttl': 'group_snapshot_ttl',  # noqa: E501
        'group_target_name': 'group_target_name',  # noqa: E501
        'name': 'name',  # noqa: E501
        'ntp_server': 'ntp_server',  # noqa: E501
        'tdz_enabled': 'tdz_enabled',  # noqa: E501
        'tdz_prefix': 'tdz_prefix',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
        'tlsv1_enabled': 'tlsv1_enabled',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """NimbleEditGroupInput - a model defined in OpenAPI

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
            auto_switchover_enabled (bool, none_type): Whether automatic switchover of Group management services feature is enabled.. [optional]  # noqa: E501
            autoclean_unmanaged_snapshots_enabled (bool, none_type): Whether auto-clean unmanaged snapshots feature is enabled.. [optional]  # noqa: E501
            autoclean_unmanaged_snapshots_ttl_unit (int, none_type): Unit for unmanaged snapshot time to live.. [optional]  # noqa: E501
            cc_mode_enabled (bool, none_type): Enable or disable Common Criteria mode.. [optional]  # noqa: E501
            date (int, none_type): Unix epoch time local to the group. Seconds since last epoch i.e. 00:00 January 1, 1970. Setting this along with ntp_server causes ntp_server to be reset.. [optional]  # noqa: E501
            default_iscsi_target_scope (str, none_type): Newly created volumes are exported under iSCSI Group Target or iSCSI Volume Target.. [optional]  # noqa: E501
            group_snapshot_ttl (int, none_type): Snapshot Time-to-live(TTL) configured at group level for automatic deletion of unmanaged snapshots. Value 0 indicates unlimited TTL.. [optional]  # noqa: E501
            group_target_name (str, none_type): Iscsi target name for this group. Plain string.. [optional]  # noqa: E501
            name (str, none_type): Name of the group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            ntp_server (str, none_type): Either IP address or hostname of the NTP server for this group.. [optional]  # noqa: E501
            tdz_enabled (bool, none_type): Is Target Driven Zoning (TDZ) enabled on this group.. [optional]  # noqa: E501
            tdz_prefix (str, none_type): Target Driven Zoning (TDZ) prefix for peer zones created by TDZ.. [optional]  # noqa: E501
            timezone (str, none_type): Timezone in which this group is located. Plain string.. [optional]  # noqa: E501
            tlsv1_enabled (bool, none_type): Enable or disable TLSv1.0 and TLSv1.1.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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
        """NimbleEditGroupInput - a model defined in OpenAPI

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
            auto_switchover_enabled (bool, none_type): Whether automatic switchover of Group management services feature is enabled.. [optional]  # noqa: E501
            autoclean_unmanaged_snapshots_enabled (bool, none_type): Whether auto-clean unmanaged snapshots feature is enabled.. [optional]  # noqa: E501
            autoclean_unmanaged_snapshots_ttl_unit (int, none_type): Unit for unmanaged snapshot time to live.. [optional]  # noqa: E501
            cc_mode_enabled (bool, none_type): Enable or disable Common Criteria mode.. [optional]  # noqa: E501
            date (int, none_type): Unix epoch time local to the group. Seconds since last epoch i.e. 00:00 January 1, 1970. Setting this along with ntp_server causes ntp_server to be reset.. [optional]  # noqa: E501
            default_iscsi_target_scope (str, none_type): Newly created volumes are exported under iSCSI Group Target or iSCSI Volume Target.. [optional]  # noqa: E501
            group_snapshot_ttl (int, none_type): Snapshot Time-to-live(TTL) configured at group level for automatic deletion of unmanaged snapshots. Value 0 indicates unlimited TTL.. [optional]  # noqa: E501
            group_target_name (str, none_type): Iscsi target name for this group. Plain string.. [optional]  # noqa: E501
            name (str, none_type): Name of the group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            ntp_server (str, none_type): Either IP address or hostname of the NTP server for this group.. [optional]  # noqa: E501
            tdz_enabled (bool, none_type): Is Target Driven Zoning (TDZ) enabled on this group.. [optional]  # noqa: E501
            tdz_prefix (str, none_type): Target Driven Zoning (TDZ) prefix for peer zones created by TDZ.. [optional]  # noqa: E501
            timezone (str, none_type): Timezone in which this group is located. Plain string.. [optional]  # noqa: E501
            tlsv1_enabled (bool, none_type): Enable or disable TLSv1.0 and TLSv1.1.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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
