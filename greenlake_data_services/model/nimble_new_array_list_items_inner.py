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


def lazy_import():
    from greenlake_data_services.model.nic_details import NICDetails
    from greenlake_data_services.model.nimble_array_details import NimbleArrayDetails
    from greenlake_data_services.model.nimble_array_fields_without_sort_key import NimbleArrayFieldsWithoutSortKey
    from greenlake_data_services.model.public_key_details import PublicKeyDetails
    from greenlake_data_services.model.upgrade_details import UpgradeDetails
    from greenlake_data_services.model.z_conf_i_paddrs import ZConfIPaddrs
    globals()['NICDetails'] = NICDetails
    globals()['NimbleArrayDetails'] = NimbleArrayDetails
    globals()['NimbleArrayFieldsWithoutSortKey'] = NimbleArrayFieldsWithoutSortKey
    globals()['PublicKeyDetails'] = PublicKeyDetails
    globals()['UpgradeDetails'] = UpgradeDetails
    globals()['ZConfIPaddrs'] = ZConfIPaddrs


class NimbleNewArrayListItemsInner(ModelComposed):
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
        lazy_import()
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
        lazy_import()
        return {
            'id': (str, none_type,),  # noqa: E501
            'model': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'pool_id': (str, none_type,),  # noqa: E501
            'serial': (str, none_type,),  # noqa: E501
            'all_flash': (bool, none_type,),  # noqa: E501
            'allow_lower_limits': (bool, none_type,),  # noqa: E501
            'available_bytes': (int, none_type,),  # noqa: E501
            'brand': (str, none_type,),  # noqa: E501
            'create_pool': (bool, none_type,),  # noqa: E501
            'creation_time': (int, none_type,),  # noqa: E501
            'ctrlr_a_support_ip': (str, none_type,),  # noqa: E501
            'ctrlr_b_support_ip': (str, none_type,),  # noqa: E501
            'customer_id': (str, none_type,),  # noqa: E501
            'dedupe_capacity_bytes': (int, none_type,),  # noqa: E501
            'dedupe_usage_bytes': (int, none_type,),  # noqa: E501
            'extended_model': (str, none_type,),  # noqa: E501
            'fc_port_count': (int, none_type,),  # noqa: E501
            'force': (bool, none_type,),  # noqa: E501
            'full_name': (str, none_type,),  # noqa: E501
            'generation': (int, none_type,),  # noqa: E501
            'gig_nic_port_count': (int, none_type,),  # noqa: E501
            'group_state': (str, none_type,),  # noqa: E501
            'is_fully_dedupe_capable': (bool, none_type,),  # noqa: E501
            'is_sfa': (bool, none_type,),  # noqa: E501
            'is_supported_hw_config': (bool, none_type,),  # noqa: E501
            'last_modified': (int, none_type,),  # noqa: E501
            'model_sub_type': (str, none_type,),  # noqa: E501
            'nic_list': ([NICDetails], none_type,),  # noqa: E501
            'oem': (str, none_type,),  # noqa: E501
            'pending_delete_bytes': (int, none_type,),  # noqa: E501
            'pool_description': (str, none_type,),  # noqa: E501
            'pool_name': (str, none_type,),  # noqa: E501
            'public_key': (PublicKeyDetails,),  # noqa: E501
            'raw_capacity_bytes': (int, none_type,),  # noqa: E501
            'resource_uri': (str, none_type,),  # noqa: E501
            'role': (str, none_type,),  # noqa: E501
            'search_name': (str, none_type,),  # noqa: E501
            'secondary_mgmt_ip': (str, none_type,),  # noqa: E501
            'snap_compression': (float, none_type,),  # noqa: E501
            'snap_saved_bytes': (int, none_type,),  # noqa: E501
            'snap_space_reduction': (float, none_type,),  # noqa: E501
            'snap_usage_bytes': (int, none_type,),  # noqa: E501
            'snap_usage_uncompressed_bytes': (int, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'ten_gig_sfp_nic_port_count': (int, none_type,),  # noqa: E501
            'ten_gig_t_nic_port_count': (int, none_type,),  # noqa: E501
            'upgrade': (UpgradeDetails,),  # noqa: E501
            'usable_cache_capacity_bytes': (int, none_type,),  # noqa: E501
            'usable_capacity_bytes': (int, none_type,),  # noqa: E501
            'usage': (int, none_type,),  # noqa: E501
            'usage_valid': (bool, none_type,),  # noqa: E501
            'version': (str, none_type,),  # noqa: E501
            'vol_compression': (float, none_type,),  # noqa: E501
            'vol_saved_bytes': (int, none_type,),  # noqa: E501
            'vol_usage_bytes': (int, none_type,),  # noqa: E501
            'vol_usage_uncompressed_bytes': (int, none_type,),  # noqa: E501
            'zconf_ipaddrs': ([ZConfIPaddrs], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'model': 'model',  # noqa: E501
        'name': 'name',  # noqa: E501
        'pool_id': 'pool_id',  # noqa: E501
        'serial': 'serial',  # noqa: E501
        'all_flash': 'all_flash',  # noqa: E501
        'allow_lower_limits': 'allow_lower_limits',  # noqa: E501
        'available_bytes': 'available_bytes',  # noqa: E501
        'brand': 'brand',  # noqa: E501
        'create_pool': 'create_pool',  # noqa: E501
        'creation_time': 'creation_time',  # noqa: E501
        'ctrlr_a_support_ip': 'ctrlr_a_support_ip',  # noqa: E501
        'ctrlr_b_support_ip': 'ctrlr_b_support_ip',  # noqa: E501
        'customer_id': 'customerId',  # noqa: E501
        'dedupe_capacity_bytes': 'dedupe_capacity_bytes',  # noqa: E501
        'dedupe_usage_bytes': 'dedupe_usage_bytes',  # noqa: E501
        'extended_model': 'extended_model',  # noqa: E501
        'fc_port_count': 'fc_port_count',  # noqa: E501
        'force': 'force',  # noqa: E501
        'full_name': 'full_name',  # noqa: E501
        'generation': 'generation',  # noqa: E501
        'gig_nic_port_count': 'gig_nic_port_count',  # noqa: E501
        'group_state': 'group_state',  # noqa: E501
        'is_fully_dedupe_capable': 'is_fully_dedupe_capable',  # noqa: E501
        'is_sfa': 'is_sfa',  # noqa: E501
        'is_supported_hw_config': 'is_supported_hw_config',  # noqa: E501
        'last_modified': 'last_modified',  # noqa: E501
        'model_sub_type': 'model_sub_type',  # noqa: E501
        'nic_list': 'nic_list',  # noqa: E501
        'oem': 'oem',  # noqa: E501
        'pending_delete_bytes': 'pending_delete_bytes',  # noqa: E501
        'pool_description': 'pool_description',  # noqa: E501
        'pool_name': 'pool_name',  # noqa: E501
        'public_key': 'public_key',  # noqa: E501
        'raw_capacity_bytes': 'raw_capacity_bytes',  # noqa: E501
        'resource_uri': 'resourceUri',  # noqa: E501
        'role': 'role',  # noqa: E501
        'search_name': 'search_name',  # noqa: E501
        'secondary_mgmt_ip': 'secondary_mgmt_ip',  # noqa: E501
        'snap_compression': 'snap_compression',  # noqa: E501
        'snap_saved_bytes': 'snap_saved_bytes',  # noqa: E501
        'snap_space_reduction': 'snap_space_reduction',  # noqa: E501
        'snap_usage_bytes': 'snap_usage_bytes',  # noqa: E501
        'snap_usage_uncompressed_bytes': 'snap_usage_uncompressed_bytes',  # noqa: E501
        'status': 'status',  # noqa: E501
        'ten_gig_sfp_nic_port_count': 'ten_gig_sfp_nic_port_count',  # noqa: E501
        'ten_gig_t_nic_port_count': 'ten_gig_t_nic_port_count',  # noqa: E501
        'upgrade': 'upgrade',  # noqa: E501
        'usable_cache_capacity_bytes': 'usable_cache_capacity_bytes',  # noqa: E501
        'usable_capacity_bytes': 'usable_capacity_bytes',  # noqa: E501
        'usage': 'usage',  # noqa: E501
        'usage_valid': 'usage_valid',  # noqa: E501
        'version': 'version',  # noqa: E501
        'vol_compression': 'vol_compression',  # noqa: E501
        'vol_saved_bytes': 'vol_saved_bytes',  # noqa: E501
        'vol_usage_bytes': 'vol_usage_bytes',  # noqa: E501
        'vol_usage_uncompressed_bytes': 'vol_usage_uncompressed_bytes',  # noqa: E501
        'zconf_ipaddrs': 'zconf_ipaddrs',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """NimbleNewArrayListItemsInner - a model defined in OpenAPI

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
            id (str, none_type): Identifier for array. A 42 digit hexadecimal number.. [optional]  # noqa: E501
            model (str, none_type): Array model. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            name (str, none_type): The user provided name of the array. It is also the array's hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen.. [optional]  # noqa: E501
            pool_id (str, none_type): ID of pool to which this is a member. A 42 digit hexadecimal number.. [optional]  # noqa: E501
            serial (str, none_type): Serial number of the array.. [optional]  # noqa: E501
            all_flash (bool, none_type): Whether it is an all-flash array.. [optional]  # noqa: E501
            allow_lower_limits (bool, none_type): Setting this field to 'true'  will allow the addition of an array with lower limits to a pool with higher limits.. [optional]  # noqa: E501
            available_bytes (int, none_type): The available space of the array.. [optional]  # noqa: E501
            brand (str, none_type): Brand of the array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            create_pool (bool, none_type): Whether to create associated pool during array create.. [optional]  # noqa: E501
            creation_time (int, none_type): Time when this array object was created. Seconds since last epoch i.e. 00:00 January 1, 1970.. [optional]  # noqa: E501
            ctrlr_a_support_ip (str, none_type): Controller A Support IP address.. [optional]  # noqa: E501
            ctrlr_b_support_ip (str, none_type): Controller B Support IP address.. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            dedupe_capacity_bytes (int, none_type): The dedupe capacity of a hybrid array. Does not apply to all-flash arrays.. [optional]  # noqa: E501
            dedupe_usage_bytes (int, none_type): The dedupe usage of a hybrid array. Does not apply to all-flash arrays.. [optional]  # noqa: E501
            extended_model (str, none_type): Extended model of the array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            fc_port_count (int, none_type): Count of Fibre Channel Ports installed on the array.. [optional]  # noqa: E501
            force (bool, none_type): Forcibly delete the specified array.. [optional]  # noqa: E501
            full_name (str, none_type): The array's fully qualified name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            gig_nic_port_count (int, none_type): Count of 1G NIC Ports installed on the array.. [optional]  # noqa: E501
            group_state (str, none_type): Group state. State of the array in the group. Possible values: 'invalid', 'initialized', 'unused', 'removing'.. [optional]  # noqa: E501
            is_fully_dedupe_capable (bool, none_type): Flag specifies if the array fully capable to dedupe its usable capacity or not.. [optional]  # noqa: E501
            is_sfa (bool, none_type): Flag specifies if the array is sfa or not.. [optional]  # noqa: E501
            is_supported_hw_config (bool, none_type): Whether it is a supported hardware config.. [optional]  # noqa: E501
            last_modified (int, none_type): Time when this array object was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970.. [optional]  # noqa: E501
            model_sub_type (str, none_type): Array model sub-type.. [optional]  # noqa: E501
            nic_list ([NICDetails], none_type): List of NICs information. Used while creating an array.. [optional]  # noqa: E501
            oem (str, none_type): OEM brand of the array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            pending_delete_bytes (int, none_type): The pending delete bytes in he tarray.. [optional]  # noqa: E501
            pool_description (str, none_type): Text description of the pool to be created during array creation. String of up to 255 printable ASCII characters.. [optional]  # noqa: E501
            pool_name (str, none_type): Name of pool to which this is a member. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            public_key (PublicKeyDetails): [optional]  # noqa: E501
            raw_capacity_bytes (int, none_type): The raw capacity bytes of the array.. [optional]  # noqa: E501
            resource_uri (str, none_type): Link to the object URI. [optional]  # noqa: E501
            role (str, none_type): Role of an array in the group. Possible values: 'leader', 'non_member', 'invalid', 'backup_leader', 'member', 'failed'.. [optional]  # noqa: E501
            search_name (str, none_type): The array name used for object search. Alphanumeric string, up to 64 characters including hyphen, period, colon.. [optional]  # noqa: E501
            secondary_mgmt_ip (str, none_type): Secondary management IP address for the Group.. [optional]  # noqa: E501
            snap_compression (float, none_type): The compression rate of snapshots in the array expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            snap_saved_bytes (int, none_type): The saved space of snapshots in the array.. [optional]  # noqa: E501
            snap_space_reduction (float, none_type): The space reduction rate of snapshots in the array expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            snap_usage_bytes (int, none_type): The compressed usage of snapshots in array.. [optional]  # noqa: E501
            snap_usage_uncompressed_bytes (int, none_type): Snap usage uncompressed bytes.. [optional]  # noqa: E501
            status (str, none_type): Reachability status of the array in the group. Possible values: 'unreachable', 'reachable'.. [optional]  # noqa: E501
            ten_gig_sfp_nic_port_count (int, none_type): Count of 10G SFP NIC Ports installed on the array.. [optional]  # noqa: E501
            ten_gig_t_nic_port_count (int, none_type): Count of 10G BaseT NIC Ports installed on the array.. [optional]  # noqa: E501
            upgrade (UpgradeDetails): [optional]  # noqa: E501
            usable_cache_capacity_bytes (int, none_type): Usable cache capacity in bytes.. [optional]  # noqa: E501
            usable_capacity_bytes (int, none_type): The usable capacity bytes of the array.. [optional]  # noqa: E501
            usage (int, none_type): Used space of the array in bytes.. [optional]  # noqa: E501
            usage_valid (bool, none_type): Indicates whether the usage of the array is valid.. [optional]  # noqa: E501
            version (str, none_type): Software version of the array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            vol_compression (float, none_type): The compression rate of volumes in the array expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            vol_saved_bytes (int, none_type): The saved space of volumes in the array.. [optional]  # noqa: E501
            vol_usage_bytes (int, none_type): The compressed usage of volumes in the array.. [optional]  # noqa: E501
            vol_usage_uncompressed_bytes (int, none_type): The volume usage uncompressed bytes.. [optional]  # noqa: E501
            zconf_ipaddrs ([ZConfIPaddrs], none_type): List of link-local zero-configuration addresses of the array.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """NimbleNewArrayListItemsInner - a model defined in OpenAPI

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
            id (str, none_type): Identifier for array. A 42 digit hexadecimal number.. [optional]  # noqa: E501
            model (str, none_type): Array model. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            name (str, none_type): The user provided name of the array. It is also the array's hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen.. [optional]  # noqa: E501
            pool_id (str, none_type): ID of pool to which this is a member. A 42 digit hexadecimal number.. [optional]  # noqa: E501
            serial (str, none_type): Serial number of the array.. [optional]  # noqa: E501
            all_flash (bool, none_type): Whether it is an all-flash array.. [optional]  # noqa: E501
            allow_lower_limits (bool, none_type): Setting this field to 'true'  will allow the addition of an array with lower limits to a pool with higher limits.. [optional]  # noqa: E501
            available_bytes (int, none_type): The available space of the array.. [optional]  # noqa: E501
            brand (str, none_type): Brand of the array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            create_pool (bool, none_type): Whether to create associated pool during array create.. [optional]  # noqa: E501
            creation_time (int, none_type): Time when this array object was created. Seconds since last epoch i.e. 00:00 January 1, 1970.. [optional]  # noqa: E501
            ctrlr_a_support_ip (str, none_type): Controller A Support IP address.. [optional]  # noqa: E501
            ctrlr_b_support_ip (str, none_type): Controller B Support IP address.. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            dedupe_capacity_bytes (int, none_type): The dedupe capacity of a hybrid array. Does not apply to all-flash arrays.. [optional]  # noqa: E501
            dedupe_usage_bytes (int, none_type): The dedupe usage of a hybrid array. Does not apply to all-flash arrays.. [optional]  # noqa: E501
            extended_model (str, none_type): Extended model of the array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            fc_port_count (int, none_type): Count of Fibre Channel Ports installed on the array.. [optional]  # noqa: E501
            force (bool, none_type): Forcibly delete the specified array.. [optional]  # noqa: E501
            full_name (str, none_type): The array's fully qualified name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            gig_nic_port_count (int, none_type): Count of 1G NIC Ports installed on the array.. [optional]  # noqa: E501
            group_state (str, none_type): Group state. State of the array in the group. Possible values: 'invalid', 'initialized', 'unused', 'removing'.. [optional]  # noqa: E501
            is_fully_dedupe_capable (bool, none_type): Flag specifies if the array fully capable to dedupe its usable capacity or not.. [optional]  # noqa: E501
            is_sfa (bool, none_type): Flag specifies if the array is sfa or not.. [optional]  # noqa: E501
            is_supported_hw_config (bool, none_type): Whether it is a supported hardware config.. [optional]  # noqa: E501
            last_modified (int, none_type): Time when this array object was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970.. [optional]  # noqa: E501
            model_sub_type (str, none_type): Array model sub-type.. [optional]  # noqa: E501
            nic_list ([NICDetails], none_type): List of NICs information. Used while creating an array.. [optional]  # noqa: E501
            oem (str, none_type): OEM brand of the array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            pending_delete_bytes (int, none_type): The pending delete bytes in he tarray.. [optional]  # noqa: E501
            pool_description (str, none_type): Text description of the pool to be created during array creation. String of up to 255 printable ASCII characters.. [optional]  # noqa: E501
            pool_name (str, none_type): Name of pool to which this is a member. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            public_key (PublicKeyDetails): [optional]  # noqa: E501
            raw_capacity_bytes (int, none_type): The raw capacity bytes of the array.. [optional]  # noqa: E501
            resource_uri (str, none_type): Link to the object URI. [optional]  # noqa: E501
            role (str, none_type): Role of an array in the group. Possible values: 'leader', 'non_member', 'invalid', 'backup_leader', 'member', 'failed'.. [optional]  # noqa: E501
            search_name (str, none_type): The array name used for object search. Alphanumeric string, up to 64 characters including hyphen, period, colon.. [optional]  # noqa: E501
            secondary_mgmt_ip (str, none_type): Secondary management IP address for the Group.. [optional]  # noqa: E501
            snap_compression (float, none_type): The compression rate of snapshots in the array expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            snap_saved_bytes (int, none_type): The saved space of snapshots in the array.. [optional]  # noqa: E501
            snap_space_reduction (float, none_type): The space reduction rate of snapshots in the array expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            snap_usage_bytes (int, none_type): The compressed usage of snapshots in array.. [optional]  # noqa: E501
            snap_usage_uncompressed_bytes (int, none_type): Snap usage uncompressed bytes.. [optional]  # noqa: E501
            status (str, none_type): Reachability status of the array in the group. Possible values: 'unreachable', 'reachable'.. [optional]  # noqa: E501
            ten_gig_sfp_nic_port_count (int, none_type): Count of 10G SFP NIC Ports installed on the array.. [optional]  # noqa: E501
            ten_gig_t_nic_port_count (int, none_type): Count of 10G BaseT NIC Ports installed on the array.. [optional]  # noqa: E501
            upgrade (UpgradeDetails): [optional]  # noqa: E501
            usable_cache_capacity_bytes (int, none_type): Usable cache capacity in bytes.. [optional]  # noqa: E501
            usable_capacity_bytes (int, none_type): The usable capacity bytes of the array.. [optional]  # noqa: E501
            usage (int, none_type): Used space of the array in bytes.. [optional]  # noqa: E501
            usage_valid (bool, none_type): Indicates whether the usage of the array is valid.. [optional]  # noqa: E501
            version (str, none_type): Software version of the array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            vol_compression (float, none_type): The compression rate of volumes in the array expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            vol_saved_bytes (int, none_type): The saved space of volumes in the array.. [optional]  # noqa: E501
            vol_usage_bytes (int, none_type): The compressed usage of volumes in the array.. [optional]  # noqa: E501
            vol_usage_uncompressed_bytes (int, none_type): The volume usage uncompressed bytes.. [optional]  # noqa: E501
            zconf_ipaddrs ([ZConfIPaddrs], none_type): List of link-local zero-configuration addresses of the array.. [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              NimbleArrayDetails,
              NimbleArrayFieldsWithoutSortKey,
          ],
          'oneOf': [
          ],
        }
