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
    from greenlake_data_services.model.allocation import Allocation
    from greenlake_data_services.model.cpg_alert import CpgAlert
    from greenlake_data_services.model.cpg_grow import CpgGrow
    from greenlake_data_services.model.poolsprimera_associated_links import PoolsprimeraAssociatedLinks
    from greenlake_data_services.model.primera_pool_details_dedup_version import PrimeraPoolDetailsDedupVersion
    from greenlake_data_services.model.snap_space import SnapSpace
    from greenlake_data_services.model.state import State
    globals()['Allocation'] = Allocation
    globals()['CpgAlert'] = CpgAlert
    globals()['CpgGrow'] = CpgGrow
    globals()['PoolsprimeraAssociatedLinks'] = PoolsprimeraAssociatedLinks
    globals()['PrimeraPoolDetailsDedupVersion'] = PrimeraPoolDetailsDedupVersion
    globals()['SnapSpace'] = SnapSpace
    globals()['State'] = State


class PrimeraPoolDetails(ModelNormal):
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
        ('name',): {
            'max_length': 255,
        },
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
            'alert': (CpgAlert,),  # noqa: E501
            'allocation_settings': (Allocation,),  # noqa: E501
            'ao_config_id': (float,),  # noqa: E501
            'associated_links': (PoolsprimeraAssociatedLinks,),  # noqa: E501
            'base_size_mi_b': (int,),  # noqa: E501
            'base_size_private_mi_b': (float,),  # noqa: E501
            'base_size_raw_mi_b': (float,),  # noqa: E501
            'compact_ratio': (float,),  # noqa: E501
            'compress_ratio': (float,),  # noqa: E501
            'customer_id': (str, none_type,),  # noqa: E501
            'data_reduce_ratio': (float,),  # noqa: E501
            'dedup_capable': (bool,),  # noqa: E501
            'dedup_ratio': (float,),  # noqa: E501
            'dedup_version': (PrimeraPoolDetailsDedupVersion,),  # noqa: E501
            'displayname': (str, none_type,),  # noqa: E501
            'domain': (str,),  # noqa: E501
            'free_for_allocation_mi_b': (float,),  # noqa: E501
            'free_size_mi_b': (float,),  # noqa: E501
            'free_size_raw_mi_b': (float,),  # noqa: E501
            'generation': (int, none_type,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'number_of_snap_rc': (float,),  # noqa: E501
            'number_of_tdvv': (float,),  # noqa: E501
            'number_of_tpvv': (float,),  # noqa: E501
            'number_of_user_rc': (float,),  # noqa: E501
            'over_prov_ratio': (float,),  # noqa: E501
            'resource_uri': (str,),  # noqa: E501
            'sa_grow': (CpgGrow,),  # noqa: E501
            'sd_grow': (CpgGrow,),  # noqa: E501
            'shared_size_mi_b': (float,),  # noqa: E501
            'snap_size_private_mi_b': (float,),  # noqa: E501
            'snap_size_raw_mi_b': (float,),  # noqa: E501
            'snap_space_admin': (SnapSpace,),  # noqa: E501
            'snap_space_data': (SnapSpace,),  # noqa: E501
            'state': (State,),  # noqa: E501
            'storage_pool_id': (float,),  # noqa: E501
            'system_id': (str,),  # noqa: E501
            'total_reserved_mi_b': (float,),  # noqa: E501
            'total_size_mi_b': (int,),  # noqa: E501
            'total_size_raw_mi_b': (float,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
            'user_space': (SnapSpace,),  # noqa: E501
            'warn_percent': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'alert': 'alert',  # noqa: E501
        'allocation_settings': 'allocationSettings',  # noqa: E501
        'ao_config_id': 'aoConfigID',  # noqa: E501
        'associated_links': 'associatedLinks',  # noqa: E501
        'base_size_mi_b': 'baseSizeMiB',  # noqa: E501
        'base_size_private_mi_b': 'baseSizePrivateMiB',  # noqa: E501
        'base_size_raw_mi_b': 'baseSizeRawMiB',  # noqa: E501
        'compact_ratio': 'compactRatio',  # noqa: E501
        'compress_ratio': 'compressRatio',  # noqa: E501
        'customer_id': 'customerId',  # noqa: E501
        'data_reduce_ratio': 'dataReduceRatio',  # noqa: E501
        'dedup_capable': 'dedupCapable',  # noqa: E501
        'dedup_ratio': 'dedupRatio',  # noqa: E501
        'dedup_version': 'dedupVersion',  # noqa: E501
        'displayname': 'displayname',  # noqa: E501
        'domain': 'domain',  # noqa: E501
        'free_for_allocation_mi_b': 'freeForAllocationMiB',  # noqa: E501
        'free_size_mi_b': 'freeSizeMiB',  # noqa: E501
        'free_size_raw_mi_b': 'freeSizeRawMiB',  # noqa: E501
        'generation': 'generation',  # noqa: E501
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'number_of_snap_rc': 'numberOfSnapRC',  # noqa: E501
        'number_of_tdvv': 'numberOfTDVV',  # noqa: E501
        'number_of_tpvv': 'numberOfTPVV',  # noqa: E501
        'number_of_user_rc': 'numberOfUserRC',  # noqa: E501
        'over_prov_ratio': 'overProvRatio',  # noqa: E501
        'resource_uri': 'resourceUri',  # noqa: E501
        'sa_grow': 'saGrow',  # noqa: E501
        'sd_grow': 'sdGrow',  # noqa: E501
        'shared_size_mi_b': 'sharedSizeMiB',  # noqa: E501
        'snap_size_private_mi_b': 'snapSizePrivateMiB',  # noqa: E501
        'snap_size_raw_mi_b': 'snapSizeRawMiB',  # noqa: E501
        'snap_space_admin': 'snapSpaceAdmin',  # noqa: E501
        'snap_space_data': 'snapSpaceData',  # noqa: E501
        'state': 'state',  # noqa: E501
        'storage_pool_id': 'storagePoolId',  # noqa: E501
        'system_id': 'systemId',  # noqa: E501
        'total_reserved_mi_b': 'totalReservedMiB',  # noqa: E501
        'total_size_mi_b': 'totalSizeMiB',  # noqa: E501
        'total_size_raw_mi_b': 'totalSizeRawMiB',  # noqa: E501
        'type': 'type',  # noqa: E501
        'user_space': 'userSpace',  # noqa: E501
        'warn_percent': 'warnPercent',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """PrimeraPoolDetails - a model defined in OpenAPI

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
            alert (CpgAlert): [optional]  # noqa: E501
            allocation_settings (Allocation): [optional]  # noqa: E501
            ao_config_id (float): Numeric ID of the AO config where the CPG is a member. [optional]  # noqa: E501
            associated_links (PoolsprimeraAssociatedLinks): [optional]  # noqa: E501
            base_size_mi_b (int): Number of LD MiB used in base virtual volumes. [optional]  # noqa: E501
            base_size_private_mi_b (float): Number of LD MiB private to individual base virtual volumes, not shared by deduplication. [optional]  # noqa: E501
            base_size_raw_mi_b (float): Number of physical (raw) MiB used in base virtual volumes. [optional]  # noqa: E501
            compact_ratio (float): Ratio between the virtual sizes of all volumes in the CPG and the amount of disk space they are currently using. [optional]  # noqa: E501
            compress_ratio (float): Ratio between the amount of data written to Dedup Volumes and the amount that is not duplicated. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            data_reduce_ratio (float): Ratio between the amount written to all volumes in the CPG and the amount of disk space used after compression and deduplication. [optional]  # noqa: E501
            dedup_capable (bool): Indicates whether the CPG supports dedup. [optional]  # noqa: E501
            dedup_ratio (float): Ratio between the amount of data written to Dedup Volumes and the amount that is not duplicated. [optional]  # noqa: E501
            dedup_version (PrimeraPoolDetailsDedupVersion): [optional]  # noqa: E501
            displayname (str, none_type): Name to be used for display purposes. [optional]  # noqa: E501
            domain (str): Name of the domain that the CPG belongs to. [optional]  # noqa: E501
            free_for_allocation_mi_b (float): Estimated free space for volume allocation (MiB). [optional]  # noqa: E501
            free_size_mi_b (float): Number of LD MiB allocated and available in the CPG. [optional]  # noqa: E501
            free_size_raw_mi_b (float): Number of physical (raw) MiB allocated and available in the CPG. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            id (str): Unique Identifier of the resource          . [optional]  # noqa: E501
            name (str): Name of the resource. [optional]  # noqa: E501
            number_of_snap_rc (float): Number of VVs used for Remote copy snapshot CPG usage. [optional]  # noqa: E501
            number_of_tdvv (float): Number of TDVVs using the CPG. [optional]  # noqa: E501
            number_of_tpvv (float): Number of TPVVs using the CPG. [optional]  # noqa: E501
            number_of_user_rc (float): Number of VVs used for Remote copy user CPG usage. [optional]  # noqa: E501
            over_prov_ratio (float): Ratio between the virtual sizes of all volumes and the amount of used and free disk spaces. [optional]  # noqa: E501
            resource_uri (str): resourceUri for detailed storage-pool object. [optional]  # noqa: E501
            sa_grow (CpgGrow): [optional]  # noqa: E501
            sd_grow (CpgGrow): [optional]  # noqa: E501
            shared_size_mi_b (float): Number of LD MiB shared between volumes via deduplication. [optional]  # noqa: E501
            snap_size_private_mi_b (float): Number of LD MiB private to individual snapshot virtual volumes, not shared by deduplication. [optional]  # noqa: E501
            snap_size_raw_mi_b (float): Number of physical (raw) MiB used in snapshot virtual volumes. [optional]  # noqa: E501
            snap_space_admin (SnapSpace): [optional]  # noqa: E501
            snap_space_data (SnapSpace): [optional]  # noqa: E501
            state (State): [optional]  # noqa: E501
            storage_pool_id (float): Numeric ID of the resource. [optional]  # noqa: E501
            system_id (str): SystemID of the array. [optional]  # noqa: E501
            total_reserved_mi_b (float): Total amount of space reserved by CPG  (MiB). [optional]  # noqa: E501
            total_size_mi_b (int): Total logical capacity in the user/snapshot space (MiB). [optional]  # noqa: E501
            total_size_raw_mi_b (float): Total physical (raw) MiB in the user/snapshot space. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
            user_space (SnapSpace): [optional]  # noqa: E501
            warn_percent (float): Allocation warning percentage. [optional]  # noqa: E501
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
        """PrimeraPoolDetails - a model defined in OpenAPI

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
            alert (CpgAlert): [optional]  # noqa: E501
            allocation_settings (Allocation): [optional]  # noqa: E501
            ao_config_id (float): Numeric ID of the AO config where the CPG is a member. [optional]  # noqa: E501
            associated_links (PoolsprimeraAssociatedLinks): [optional]  # noqa: E501
            base_size_mi_b (int): Number of LD MiB used in base virtual volumes. [optional]  # noqa: E501
            base_size_private_mi_b (float): Number of LD MiB private to individual base virtual volumes, not shared by deduplication. [optional]  # noqa: E501
            base_size_raw_mi_b (float): Number of physical (raw) MiB used in base virtual volumes. [optional]  # noqa: E501
            compact_ratio (float): Ratio between the virtual sizes of all volumes in the CPG and the amount of disk space they are currently using. [optional]  # noqa: E501
            compress_ratio (float): Ratio between the amount of data written to Dedup Volumes and the amount that is not duplicated. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            data_reduce_ratio (float): Ratio between the amount written to all volumes in the CPG and the amount of disk space used after compression and deduplication. [optional]  # noqa: E501
            dedup_capable (bool): Indicates whether the CPG supports dedup. [optional]  # noqa: E501
            dedup_ratio (float): Ratio between the amount of data written to Dedup Volumes and the amount that is not duplicated. [optional]  # noqa: E501
            dedup_version (PrimeraPoolDetailsDedupVersion): [optional]  # noqa: E501
            displayname (str, none_type): Name to be used for display purposes. [optional]  # noqa: E501
            domain (str): Name of the domain that the CPG belongs to. [optional]  # noqa: E501
            free_for_allocation_mi_b (float): Estimated free space for volume allocation (MiB). [optional]  # noqa: E501
            free_size_mi_b (float): Number of LD MiB allocated and available in the CPG. [optional]  # noqa: E501
            free_size_raw_mi_b (float): Number of physical (raw) MiB allocated and available in the CPG. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            id (str): Unique Identifier of the resource          . [optional]  # noqa: E501
            name (str): Name of the resource. [optional]  # noqa: E501
            number_of_snap_rc (float): Number of VVs used for Remote copy snapshot CPG usage. [optional]  # noqa: E501
            number_of_tdvv (float): Number of TDVVs using the CPG. [optional]  # noqa: E501
            number_of_tpvv (float): Number of TPVVs using the CPG. [optional]  # noqa: E501
            number_of_user_rc (float): Number of VVs used for Remote copy user CPG usage. [optional]  # noqa: E501
            over_prov_ratio (float): Ratio between the virtual sizes of all volumes and the amount of used and free disk spaces. [optional]  # noqa: E501
            resource_uri (str): resourceUri for detailed storage-pool object. [optional]  # noqa: E501
            sa_grow (CpgGrow): [optional]  # noqa: E501
            sd_grow (CpgGrow): [optional]  # noqa: E501
            shared_size_mi_b (float): Number of LD MiB shared between volumes via deduplication. [optional]  # noqa: E501
            snap_size_private_mi_b (float): Number of LD MiB private to individual snapshot virtual volumes, not shared by deduplication. [optional]  # noqa: E501
            snap_size_raw_mi_b (float): Number of physical (raw) MiB used in snapshot virtual volumes. [optional]  # noqa: E501
            snap_space_admin (SnapSpace): [optional]  # noqa: E501
            snap_space_data (SnapSpace): [optional]  # noqa: E501
            state (State): [optional]  # noqa: E501
            storage_pool_id (float): Numeric ID of the resource. [optional]  # noqa: E501
            system_id (str): SystemID of the array. [optional]  # noqa: E501
            total_reserved_mi_b (float): Total amount of space reserved by CPG  (MiB). [optional]  # noqa: E501
            total_size_mi_b (int): Total logical capacity in the user/snapshot space (MiB). [optional]  # noqa: E501
            total_size_raw_mi_b (float): Total physical (raw) MiB in the user/snapshot space. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
            user_space (SnapSpace): [optional]  # noqa: E501
            warn_percent (float): Allocation warning percentage. [optional]  # noqa: E501
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
