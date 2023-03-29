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
    from greenlake_data_services.model.associated_links import AssociatedLinks
    from greenlake_data_services.model.nimble_arr_summary import NimbleArrSummary
    from greenlake_data_services.model.nimble_array_detail import NimbleArrayDetail
    from greenlake_data_services.model.nimble_folder_summary import NimbleFolderSummary
    from greenlake_data_services.model.nimble_pinned_volume_info import NimblePinnedVolumeInfo
    from greenlake_data_services.model.nimble_volume_summary import NimbleVolumeSummary
    globals()['AssociatedLinks'] = AssociatedLinks
    globals()['NimbleArrSummary'] = NimbleArrSummary
    globals()['NimbleArrayDetail'] = NimbleArrayDetail
    globals()['NimbleFolderSummary'] = NimbleFolderSummary
    globals()['NimblePinnedVolumeInfo'] = NimblePinnedVolumeInfo
    globals()['NimbleVolumeSummary'] = NimbleVolumeSummary


class NimblePoolDetails(ModelNormal):
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
        lazy_import()
        return {
            'all_flash': (bool, none_type,),  # noqa: E501
            'array_count': (int, none_type,),  # noqa: E501
            'array_list': ([NimbleArrayDetail], none_type,),  # noqa: E501
            'associated_links': (AssociatedLinks,),  # noqa: E501
            'cache_capacity': (int, none_type,),  # noqa: E501
            'capacity': (int, none_type,),  # noqa: E501
            'clone_ratio': (float, none_type,),  # noqa: E501
            'compression_ratio': (float, none_type,),  # noqa: E501
            'console_uri': (str, none_type,),  # noqa: E501
            'creation_time': (int, none_type,),  # noqa: E501
            'customer_id': (str, none_type,),  # noqa: E501
            'data_reduction_ratio': (float, none_type,),  # noqa: E501
            'dedupe_all_volumes': (bool, none_type,),  # noqa: E501
            'dedupe_capable': (bool, none_type,),  # noqa: E501
            'dedupe_capacity_bytes': (int, none_type,),  # noqa: E501
            'dedupe_ratio': (float, none_type,),  # noqa: E501
            'dedupe_usage_bytes': (int, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'folder_list': ([NimbleFolderSummary], none_type,),  # noqa: E501
            'free_space': (int, none_type,),  # noqa: E501
            'full_name': (str, none_type,),  # noqa: E501
            'generation': (int, none_type,),  # noqa: E501
            'is_default': (bool, none_type,),  # noqa: E501
            'last_modified': (int, none_type,),  # noqa: E501
            'pinnable_cache_capacity': (int, none_type,),  # noqa: E501
            'pinned_cache_capacity': (int, none_type,),  # noqa: E501
            'pinned_vol_list': ([NimblePinnedVolumeInfo], none_type,),  # noqa: E501
            'resource_uri': (str, none_type,),  # noqa: E501
            'savings': (int, none_type,),  # noqa: E501
            'savings_clone': (int, none_type,),  # noqa: E501
            'savings_compression': (int, none_type,),  # noqa: E501
            'savings_data_reduction': (int, none_type,),  # noqa: E501
            'savings_dedupe': (int, none_type,),  # noqa: E501
            'savings_ratio': (float, none_type,),  # noqa: E501
            'savings_vol_thin_provisioning': (int, none_type,),  # noqa: E501
            'search_name': (str, none_type,),  # noqa: E501
            'snap_count': (int, none_type,),  # noqa: E501
            'snapcoll_count': (int, none_type,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
            'unassigned_array_list': ([NimbleArrSummary], none_type,),  # noqa: E501
            'unused_reserve': (int, none_type,),  # noqa: E501
            'usage': (int, none_type,),  # noqa: E501
            'usage_valid': (bool, none_type,),  # noqa: E501
            'vol_count': (int, none_type,),  # noqa: E501
            'vol_list': ([NimbleVolumeSummary], none_type,),  # noqa: E501
            'vol_thin_provisioning_ratio': (float, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'all_flash': 'all_flash',  # noqa: E501
        'array_count': 'array_count',  # noqa: E501
        'array_list': 'array_list',  # noqa: E501
        'associated_links': 'associated_links',  # noqa: E501
        'cache_capacity': 'cache_capacity',  # noqa: E501
        'capacity': 'capacity',  # noqa: E501
        'clone_ratio': 'clone_ratio',  # noqa: E501
        'compression_ratio': 'compression_ratio',  # noqa: E501
        'console_uri': 'consoleUri',  # noqa: E501
        'creation_time': 'creation_time',  # noqa: E501
        'customer_id': 'customerId',  # noqa: E501
        'data_reduction_ratio': 'data_reduction_ratio',  # noqa: E501
        'dedupe_all_volumes': 'dedupe_all_volumes',  # noqa: E501
        'dedupe_capable': 'dedupe_capable',  # noqa: E501
        'dedupe_capacity_bytes': 'dedupe_capacity_bytes',  # noqa: E501
        'dedupe_ratio': 'dedupe_ratio',  # noqa: E501
        'dedupe_usage_bytes': 'dedupe_usage_bytes',  # noqa: E501
        'description': 'description',  # noqa: E501
        'folder_list': 'folder_list',  # noqa: E501
        'free_space': 'free_space',  # noqa: E501
        'full_name': 'full_name',  # noqa: E501
        'generation': 'generation',  # noqa: E501
        'is_default': 'is_default',  # noqa: E501
        'last_modified': 'last_modified',  # noqa: E501
        'pinnable_cache_capacity': 'pinnable_cache_capacity',  # noqa: E501
        'pinned_cache_capacity': 'pinned_cache_capacity',  # noqa: E501
        'pinned_vol_list': 'pinned_vol_list',  # noqa: E501
        'resource_uri': 'resourceUri',  # noqa: E501
        'savings': 'savings',  # noqa: E501
        'savings_clone': 'savings_clone',  # noqa: E501
        'savings_compression': 'savings_compression',  # noqa: E501
        'savings_data_reduction': 'savings_data_reduction',  # noqa: E501
        'savings_dedupe': 'savings_dedupe',  # noqa: E501
        'savings_ratio': 'savings_ratio',  # noqa: E501
        'savings_vol_thin_provisioning': 'savings_vol_thin_provisioning',  # noqa: E501
        'search_name': 'search_name',  # noqa: E501
        'snap_count': 'snap_count',  # noqa: E501
        'snapcoll_count': 'snapcoll_count',  # noqa: E501
        'type': 'type',  # noqa: E501
        'unassigned_array_list': 'unassigned_array_list',  # noqa: E501
        'unused_reserve': 'unused_reserve',  # noqa: E501
        'usage': 'usage',  # noqa: E501
        'usage_valid': 'usage_valid',  # noqa: E501
        'vol_count': 'vol_count',  # noqa: E501
        'vol_list': 'vol_list',  # noqa: E501
        'vol_thin_provisioning_ratio': 'vol_thin_provisioning_ratio',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """NimblePoolDetails - a model defined in OpenAPI

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
            all_flash (bool, none_type): Indicate whether the pool is an all_flash pool.. [optional]  # noqa: E501
            array_count (int, none_type): Number of arrays in the pool.. [optional]  # noqa: E501
            array_list ([NimbleArrayDetail], none_type): List of arrays in the pool with detailed information. When create/update array list, only arrays' id is required.. [optional]  # noqa: E501
            associated_links (AssociatedLinks): [optional]  # noqa: E501
            cache_capacity (int, none_type): Total usable cache capacity of the pool in bytes.. [optional]  # noqa: E501
            capacity (int, none_type): Total storage space of the pool in bytes.. [optional]  # noqa: E501
            clone_ratio (float, none_type): Clone savings for the pool expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            compression_ratio (float, none_type): Compression savings for the pool expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            console_uri (str, none_type): consoleUri for detailed storage object. [optional]  # noqa: E501
            creation_time (int, none_type): Time when this pool was created. Seconds since last epoch i.e. 00:00 January 1, 1970.. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            data_reduction_ratio (float, none_type): Space usage savings in the pool expressed as ratio that does not include thin-provisioning savings. Fraction expressed as floating point number.. [optional]  # noqa: E501
            dedupe_all_volumes (bool, none_type): Indicates if dedupe is enabled by default for new volumes on this pool.. [optional]  # noqa: E501
            dedupe_capable (bool, none_type): Indicates whether the pool is capable of hosting deduped volumes.. [optional]  # noqa: E501
            dedupe_capacity_bytes (int, none_type): The dedupe capacity of a hybrid pool. Does not apply to all-flash pools.. [optional]  # noqa: E501
            dedupe_ratio (float, none_type): Dedupe savings for the pool expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            dedupe_usage_bytes (int, none_type): The dedupe usage of a hybrid pool. Does not apply to all-flash pools.. [optional]  # noqa: E501
            description (str, none_type): Text description of pool. String of up to 255 printable ASCII characters.. [optional]  # noqa: E501
            folder_list ([NimbleFolderSummary], none_type): The list of fully qualified names of folders in the pool.. [optional]  # noqa: E501
            free_space (int, none_type): Free space of the pool in bytes.. [optional]  # noqa: E501
            full_name (str, none_type): Fully qualified name of pool. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            is_default (bool, none_type): Indicates if this is the default pool.. [optional]  # noqa: E501
            last_modified (int, none_type): Time when this pool was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970.. [optional]  # noqa: E501
            pinnable_cache_capacity (int, none_type): Total pinnable cache capacity of the pool in bytes.. [optional]  # noqa: E501
            pinned_cache_capacity (int, none_type): Total pinned cache capacity of the pool in bytes.. [optional]  # noqa: E501
            pinned_vol_list ([NimblePinnedVolumeInfo], none_type): The list of pinned volumes in the pool.. [optional]  # noqa: E501
            resource_uri (str, none_type): Link to the object URI. [optional]  # noqa: E501
            savings (int, none_type): Overall space usage savings in the pool.. [optional]  # noqa: E501
            savings_clone (int, none_type): Space usage savings in the pool due to cloning of volumes.. [optional]  # noqa: E501
            savings_compression (int, none_type): Space usage savings in the pool due to compression.. [optional]  # noqa: E501
            savings_data_reduction (int, none_type): Space usage savings in the pool that does not include thin-provisioning savings.. [optional]  # noqa: E501
            savings_dedupe (int, none_type): Space usage savings in the pool due to deduplication.. [optional]  # noqa: E501
            savings_ratio (float, none_type): Overall space usage savings in the pool expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            savings_vol_thin_provisioning (int, none_type): Space usage savings in the pool due to thin provisioning of volumes.. [optional]  # noqa: E501
            search_name (str, none_type): Name of pool used for object search. Alphanumeric string, up to 64 characters including hyphen, period, colon.. [optional]  # noqa: E501
            snap_count (int, none_type): Snapshot count.. [optional]  # noqa: E501
            snapcoll_count (int, none_type): Snapshot collection count.. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
            unassigned_array_list ([NimbleArrSummary], none_type): List of arrays being unassigned from the pool.. [optional]  # noqa: E501
            unused_reserve (int, none_type): Unused reserve space of the pool in bytes.. [optional]  # noqa: E501
            usage (int, none_type): Used space of the pool in bytes.. [optional]  # noqa: E501
            usage_valid (bool, none_type): Identifier of pool. A 42 digit hexadecimal number.. [optional]  # noqa: E501
            vol_count (int, none_type): Number of volumes assigned to the pool.. [optional]  # noqa: E501
            vol_list ([NimbleVolumeSummary], none_type): The list of volumes in the pool.. [optional]  # noqa: E501
            vol_thin_provisioning_ratio (float, none_type): Thin provisioning savings for volumes in the pool expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
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
        """NimblePoolDetails - a model defined in OpenAPI

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
            all_flash (bool, none_type): Indicate whether the pool is an all_flash pool.. [optional]  # noqa: E501
            array_count (int, none_type): Number of arrays in the pool.. [optional]  # noqa: E501
            array_list ([NimbleArrayDetail], none_type): List of arrays in the pool with detailed information. When create/update array list, only arrays' id is required.. [optional]  # noqa: E501
            associated_links (AssociatedLinks): [optional]  # noqa: E501
            cache_capacity (int, none_type): Total usable cache capacity of the pool in bytes.. [optional]  # noqa: E501
            capacity (int, none_type): Total storage space of the pool in bytes.. [optional]  # noqa: E501
            clone_ratio (float, none_type): Clone savings for the pool expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            compression_ratio (float, none_type): Compression savings for the pool expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            console_uri (str, none_type): consoleUri for detailed storage object. [optional]  # noqa: E501
            creation_time (int, none_type): Time when this pool was created. Seconds since last epoch i.e. 00:00 January 1, 1970.. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            data_reduction_ratio (float, none_type): Space usage savings in the pool expressed as ratio that does not include thin-provisioning savings. Fraction expressed as floating point number.. [optional]  # noqa: E501
            dedupe_all_volumes (bool, none_type): Indicates if dedupe is enabled by default for new volumes on this pool.. [optional]  # noqa: E501
            dedupe_capable (bool, none_type): Indicates whether the pool is capable of hosting deduped volumes.. [optional]  # noqa: E501
            dedupe_capacity_bytes (int, none_type): The dedupe capacity of a hybrid pool. Does not apply to all-flash pools.. [optional]  # noqa: E501
            dedupe_ratio (float, none_type): Dedupe savings for the pool expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            dedupe_usage_bytes (int, none_type): The dedupe usage of a hybrid pool. Does not apply to all-flash pools.. [optional]  # noqa: E501
            description (str, none_type): Text description of pool. String of up to 255 printable ASCII characters.. [optional]  # noqa: E501
            folder_list ([NimbleFolderSummary], none_type): The list of fully qualified names of folders in the pool.. [optional]  # noqa: E501
            free_space (int, none_type): Free space of the pool in bytes.. [optional]  # noqa: E501
            full_name (str, none_type): Fully qualified name of pool. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            is_default (bool, none_type): Indicates if this is the default pool.. [optional]  # noqa: E501
            last_modified (int, none_type): Time when this pool was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970.. [optional]  # noqa: E501
            pinnable_cache_capacity (int, none_type): Total pinnable cache capacity of the pool in bytes.. [optional]  # noqa: E501
            pinned_cache_capacity (int, none_type): Total pinned cache capacity of the pool in bytes.. [optional]  # noqa: E501
            pinned_vol_list ([NimblePinnedVolumeInfo], none_type): The list of pinned volumes in the pool.. [optional]  # noqa: E501
            resource_uri (str, none_type): Link to the object URI. [optional]  # noqa: E501
            savings (int, none_type): Overall space usage savings in the pool.. [optional]  # noqa: E501
            savings_clone (int, none_type): Space usage savings in the pool due to cloning of volumes.. [optional]  # noqa: E501
            savings_compression (int, none_type): Space usage savings in the pool due to compression.. [optional]  # noqa: E501
            savings_data_reduction (int, none_type): Space usage savings in the pool that does not include thin-provisioning savings.. [optional]  # noqa: E501
            savings_dedupe (int, none_type): Space usage savings in the pool due to deduplication.. [optional]  # noqa: E501
            savings_ratio (float, none_type): Overall space usage savings in the pool expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
            savings_vol_thin_provisioning (int, none_type): Space usage savings in the pool due to thin provisioning of volumes.. [optional]  # noqa: E501
            search_name (str, none_type): Name of pool used for object search. Alphanumeric string, up to 64 characters including hyphen, period, colon.. [optional]  # noqa: E501
            snap_count (int, none_type): Snapshot count.. [optional]  # noqa: E501
            snapcoll_count (int, none_type): Snapshot collection count.. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
            unassigned_array_list ([NimbleArrSummary], none_type): List of arrays being unassigned from the pool.. [optional]  # noqa: E501
            unused_reserve (int, none_type): Unused reserve space of the pool in bytes.. [optional]  # noqa: E501
            usage (int, none_type): Used space of the pool in bytes.. [optional]  # noqa: E501
            usage_valid (bool, none_type): Identifier of pool. A 42 digit hexadecimal number.. [optional]  # noqa: E501
            vol_count (int, none_type): Number of volumes assigned to the pool.. [optional]  # noqa: E501
            vol_list ([NimbleVolumeSummary], none_type): The list of volumes in the pool.. [optional]  # noqa: E501
            vol_thin_provisioning_ratio (float, none_type): Thin provisioning savings for volumes in the pool expressed as ratio. Fraction expressed as floating point number.. [optional]  # noqa: E501
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
