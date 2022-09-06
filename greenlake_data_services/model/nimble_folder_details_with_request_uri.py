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


def lazy_import():
    from greenlake_data_services.model.associated_links import AssociatedLinks
    from greenlake_data_services.model.nimble_folder_details import NimbleFolderDetails
    from greenlake_data_services.model.nimble_folder_fields_without_sort_key import NimbleFolderFieldsWithoutSortKey
    from greenlake_data_services.model.nimble_volume_summary import NimbleVolumeSummary
    globals()['AssociatedLinks'] = AssociatedLinks
    globals()['NimbleFolderDetails'] = NimbleFolderDetails
    globals()['NimbleFolderFieldsWithoutSortKey'] = NimbleFolderFieldsWithoutSortKey
    globals()['NimbleVolumeSummary'] = NimbleVolumeSummary


class NimbleFolderDetailsWithRequestUri(ModelComposed):
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
            'request_uri': (str, none_type,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'pool_id': (str, none_type,),  # noqa: E501
            'pool_name': (str, none_type,),  # noqa: E501
            'access_protocol': (str, none_type,),  # noqa: E501
            'agent_type': (str, none_type,),  # noqa: E501
            'app_uuid': (str, none_type,),  # noqa: E501
            'appserver_id': (str, none_type,),  # noqa: E501
            'appserver_name': (str, none_type,),  # noqa: E501
            'associated_links': (AssociatedLinks,),  # noqa: E501
            'capacity_bytes': (int, none_type,),  # noqa: E501
            'compressed_snap_usage_bytes': (int, none_type,),  # noqa: E501
            'compressed_vol_usage_bytes': (int, none_type,),  # noqa: E501
            'compression_ratio': (float, none_type,),  # noqa: E501
            'console_uri': (str, none_type,),  # noqa: E501
            'creation_time': (int, none_type,),  # noqa: E501
            'customer_id': (str, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'folset_id': (str, none_type,),  # noqa: E501
            'folset_name': (str, none_type,),  # noqa: E501
            'fqn': (str, none_type,),  # noqa: E501
            'free_space_bytes': (int, none_type,),  # noqa: E501
            'full_name': (str, none_type,),  # noqa: E501
            'generation': (int, none_type,),  # noqa: E501
            'inherited_vol_perfpol_id': (str, none_type,),  # noqa: E501
            'inherited_vol_perfpol_name': (str, none_type,),  # noqa: E501
            'last_modified': (int, none_type,),  # noqa: E501
            'limit_bytes': (int, none_type,),  # noqa: E501
            'limit_bytes_specified': (bool, none_type,),  # noqa: E501
            'limit_iops': (int, none_type,),  # noqa: E501
            'limit_mbps': (int, none_type,),  # noqa: E501
            'limit_size_bytes': (int, none_type,),  # noqa: E501
            'num_snapcolls': (int, none_type,),  # noqa: E501
            'num_snaps': (int, none_type,),  # noqa: E501
            'overdraft_limit_pct': (int, none_type,),  # noqa: E501
            'provisioned_bytes': (int, none_type,),  # noqa: E501
            'provisioned_limit_size_bytes': (int, none_type,),  # noqa: E501
            'resource_uri': (str, none_type,),  # noqa: E501
            'search_name': (str, none_type,),  # noqa: E501
            'snap_compression_ratio': (float, none_type,),  # noqa: E501
            'tenant_id': (str, none_type,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
            'uncompressed_snap_usage_bytes': (int, none_type,),  # noqa: E501
            'uncompressed_vol_usage_bytes': (int, none_type,),  # noqa: E501
            'unused_reserve_bytes': (str, none_type,),  # noqa: E501
            'unused_snap_reserve_bytes': (int, none_type,),  # noqa: E501
            'usage_bytes': (int, none_type,),  # noqa: E501
            'usage_valid': (bool, none_type,),  # noqa: E501
            'vol_compression_ratio': (float, none_type,),  # noqa: E501
            'volume_list': ([NimbleVolumeSummary], none_type,),  # noqa: E501
            'volume_mapped_bytes': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'request_uri': 'requestUri',  # noqa: E501
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'pool_id': 'pool_id',  # noqa: E501
        'pool_name': 'pool_name',  # noqa: E501
        'access_protocol': 'access_protocol',  # noqa: E501
        'agent_type': 'agent_type',  # noqa: E501
        'app_uuid': 'app_uuid',  # noqa: E501
        'appserver_id': 'appserver_id',  # noqa: E501
        'appserver_name': 'appserver_name',  # noqa: E501
        'associated_links': 'associated_links',  # noqa: E501
        'capacity_bytes': 'capacity_bytes',  # noqa: E501
        'compressed_snap_usage_bytes': 'compressed_snap_usage_bytes',  # noqa: E501
        'compressed_vol_usage_bytes': 'compressed_vol_usage_bytes',  # noqa: E501
        'compression_ratio': 'compression_ratio',  # noqa: E501
        'console_uri': 'consoleUri',  # noqa: E501
        'creation_time': 'creation_time',  # noqa: E501
        'customer_id': 'customerId',  # noqa: E501
        'description': 'description',  # noqa: E501
        'folset_id': 'folset_id',  # noqa: E501
        'folset_name': 'folset_name',  # noqa: E501
        'fqn': 'fqn',  # noqa: E501
        'free_space_bytes': 'free_space_bytes',  # noqa: E501
        'full_name': 'full_name',  # noqa: E501
        'generation': 'generation',  # noqa: E501
        'inherited_vol_perfpol_id': 'inherited_vol_perfpol_id',  # noqa: E501
        'inherited_vol_perfpol_name': 'inherited_vol_perfpol_name',  # noqa: E501
        'last_modified': 'last_modified',  # noqa: E501
        'limit_bytes': 'limit_bytes',  # noqa: E501
        'limit_bytes_specified': 'limit_bytes_specified',  # noqa: E501
        'limit_iops': 'limit_iops',  # noqa: E501
        'limit_mbps': 'limit_mbps',  # noqa: E501
        'limit_size_bytes': 'limit_size_bytes',  # noqa: E501
        'num_snapcolls': 'num_snapcolls',  # noqa: E501
        'num_snaps': 'num_snaps',  # noqa: E501
        'overdraft_limit_pct': 'overdraft_limit_pct',  # noqa: E501
        'provisioned_bytes': 'provisioned_bytes',  # noqa: E501
        'provisioned_limit_size_bytes': 'provisioned_limit_size_bytes',  # noqa: E501
        'resource_uri': 'resourceUri',  # noqa: E501
        'search_name': 'search_name',  # noqa: E501
        'snap_compression_ratio': 'snap_compression_ratio',  # noqa: E501
        'tenant_id': 'tenant_id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'uncompressed_snap_usage_bytes': 'uncompressed_snap_usage_bytes',  # noqa: E501
        'uncompressed_vol_usage_bytes': 'uncompressed_vol_usage_bytes',  # noqa: E501
        'unused_reserve_bytes': 'unused_reserve_bytes',  # noqa: E501
        'unused_snap_reserve_bytes': 'unused_snap_reserve_bytes',  # noqa: E501
        'usage_bytes': 'usage_bytes',  # noqa: E501
        'usage_valid': 'usage_valid',  # noqa: E501
        'vol_compression_ratio': 'vol_compression_ratio',  # noqa: E501
        'volume_list': 'volume_list',  # noqa: E501
        'volume_mapped_bytes': 'volume_mapped_bytes',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """NimbleFolderDetailsWithRequestUri - a model defined in OpenAPI

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
            request_uri (str, none_type): requestUri for detailed folder object. [optional]  # noqa: E501
            id (str, none_type): Identifier of the folder.. [optional]  # noqa: E501
            name (str, none_type): Name of the folder.. [optional]  # noqa: E501
            pool_id (str, none_type): ID of the pool where the folder resides.. [optional]  # noqa: E501
            pool_name (str, none_type): Name of the pool where the folder resides.. [optional]  # noqa: E501
            access_protocol (str, none_type): Access protocol of the folder. This attribute is used by the VASA Provider to determine the access protocol of the bind request. If not specified in the creation request, it will be the access protocol supported by the group. If the group supports multiple protocols, the default will be Fibre Channel. This field is meaningful only to VVol folder. Possible values: 'iscsi', 'fc'.. [optional]  # noqa: E501
            agent_type (str, none_type): External management agent type. Possible values: 'none', 'smis', 'vvol', 'openstack'.. [optional]  # noqa: E501
            app_uuid (str, none_type): Application identifier of the folder.. [optional]  # noqa: E501
            appserver_id (str, none_type): Identifier of the application server associated with the folder.. [optional]  # noqa: E501
            appserver_name (str, none_type): Name of the application server associated with the folder.. [optional]  # noqa: E501
            associated_links (AssociatedLinks): [optional]  # noqa: E501
            capacity_bytes (int, none_type): Capacity of the folder in bytes. If the folder's size has a usage limit, capacity_bytes will be the folder's usage limit. If the folder's size does not have a usage limit, capacity_bytes will be the pool's capacity. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            compressed_snap_usage_bytes (int, none_type): Compressed usage of snapshots in the folder. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            compressed_vol_usage_bytes (int, none_type): Compressed usage of volumes in the folder. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            compression_ratio (float, none_type): Compression savings for the folder expressed as ratio. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            console_uri (str, none_type): consoleUri for detailed storage object. [optional]  # noqa: E501
            creation_time (int, none_type): Time when this folder was created.. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            description (str, none_type): Text description of folder.. [optional]  # noqa: E501
            folset_id (str, none_type): Identifier of the folder set associated with the folder. Only VVol folder can be associated with the folder set. The folder and the containing folder set must be associated with the same application server.. [optional]  # noqa: E501
            folset_name (str, none_type): Name of the folder set associated with the folder. Only VVol folder can be associated with the folder set. The folder and the containing folder set must be associated with the same application server.. [optional]  # noqa: E501
            fqn (str, none_type): Fully qualified name of folder in the pool.. [optional]  # noqa: E501
            free_space_bytes (int, none_type): Free space in the folder in bytes. If the folder has a usage limit, free_space_bytes will be the folder's free space (the folder's usage limit minus the folder's space usage). If the folder does not have a usage limit, free_space_bytes will be the pool's free space. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            full_name (str, none_type): Fully qualified name of folder in the group.. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            inherited_vol_perfpol_id (str, none_type): Identifier of the default performance policy for a newly created volume.. [optional]  # noqa: E501
            inherited_vol_perfpol_name (str, none_type): Name of the default performance policy for a newly created volume.. [optional]  # noqa: E501
            last_modified (int, none_type): Identifier of the default performance policy for a newly created volume.. [optional]  # noqa: E501
            limit_bytes (int, none_type): Folder limit size in bytes. By default, a folder (except SMIS and VVol types) does not have a limit. If limit_bytes is not specified when a folder is created, or if limit_bytes is set to the largest possible 64-bit signed integer (9223372036854775807), then the folder has no limit. Otherwise, a limit smaller than the capacity of the pool can be set. On output, if the folder has a limit, the limit_bytes_specified attribute will be true and limit_bytes will be the limit. If the folder does not have a limit, the limit_bytes_specified attribute will be false and limit_bytes will be interpreted based on the value of the usage_valid attribute. If the usage_valid attribute is true, limits_byte will be the capacity of the pool. Otherwise, limits_bytes is not meaningful and can be null. SMIS and VVol folders require a size limit. This attribute is superseded by limit_size_bytes.. [optional]  # noqa: E501
            limit_bytes_specified (bool, none_type): Indicates whether the folder has a limit.. [optional]  # noqa: E501
            limit_iops (int, none_type): IOPS limit for this folder. If limit_iops is not specified when a folder is created, or if limit_iops is set to -1, then the folder has no IOPS limit. IOPS limit should be in range [256, 4294967294] or -1 for unlimited.. [optional]  # noqa: E501
            limit_mbps (int, none_type): Throughput limit for this folder in MB/s. If limit_mbps is not specified when a folder is created, or if limit_mbps is set to -1, then the folder has no throughput limit. MBPS limit should be in range [1, 4294967294] or -1 for unlimited.. [optional]  # noqa: E501
            limit_size_bytes (int, none_type): Folder size limit in bytes. If limit_size_bytes is not specified when a folder is created, or if limit_size_bytes is set to -1, then the folder has no limit. Otherwise, a limit smaller than the capacity of the pool can be set. Folders with an agent_type of 'smis' or 'vvol' must have a size limit.. [optional]  # noqa: E501
            num_snapcolls (int, none_type): Number of snapshot collections inside the folder. This attribute is deprecated and has no meaningful value.. [optional]  # noqa: E501
            num_snaps (int, none_type): Number of snapshots inside the folder. This attribute is deprecated and has no meaningful value.. [optional]  # noqa: E501
            overdraft_limit_pct (int, none_type): Amount of space to consider as overdraft range for this folder as a percentage of folder used limit. Valid values are from 0% - 200%. This is the limit above the folder usage limit beyond which enforcement action(volume offline/non-writable) is issued.. [optional]  # noqa: E501
            provisioned_bytes (int, none_type): Sum of provisioned size of volumes in the folder.. [optional]  # noqa: E501
            provisioned_limit_size_bytes (int, none_type): Limit on the provisioned size of volumes in a folder. If provisioned_limit_size_bytes is not specified when a folder is created, or if provisioned_limit_size_bytes is set to -1, then the folder has no provisioned size limit.. [optional]  # noqa: E501
            resource_uri (str, none_type): Link to the object URI. [optional]  # noqa: E501
            search_name (str, none_type): Name of folder used for object search.. [optional]  # noqa: E501
            snap_compression_ratio (float, none_type): Identifier of the default performance policy for a newly created volume.. [optional]  # noqa: E501
            tenant_id (str, none_type): Tenant ID of the folder. This is used to determine what tenant context the folder belongs to.. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
            uncompressed_snap_usage_bytes (int, none_type): Uncompressed usage of snapshots in the folder. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            uncompressed_vol_usage_bytes (int, none_type): Uncompressed usage of volumes in the folder. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            unused_reserve_bytes (str, none_type): Unused reserve of volumes in the folder in bytes. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            unused_snap_reserve_bytes (int, none_type): Unused reserve of snapshots of volumes in the folder in bytes. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            usage_bytes (int, none_type): Sum of mapped usage and snapshot uncompressed usage of volumes in the folder.. [optional]  # noqa: E501
            usage_valid (bool, none_type): Indicate whether the space usage attributes of folder are valid.. [optional]  # noqa: E501
            vol_compression_ratio (float, none_type): Compression ratio of volumes in the folder. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            volume_list ([NimbleVolumeSummary], none_type): List of volumes contained by the folder.. [optional]  # noqa: E501
            volume_mapped_bytes (int, none_type): Sum of mapped usage of volumes in the folder.. [optional]  # noqa: E501
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
        """NimbleFolderDetailsWithRequestUri - a model defined in OpenAPI

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
            request_uri (str, none_type): requestUri for detailed folder object. [optional]  # noqa: E501
            id (str, none_type): Identifier of the folder.. [optional]  # noqa: E501
            name (str, none_type): Name of the folder.. [optional]  # noqa: E501
            pool_id (str, none_type): ID of the pool where the folder resides.. [optional]  # noqa: E501
            pool_name (str, none_type): Name of the pool where the folder resides.. [optional]  # noqa: E501
            access_protocol (str, none_type): Access protocol of the folder. This attribute is used by the VASA Provider to determine the access protocol of the bind request. If not specified in the creation request, it will be the access protocol supported by the group. If the group supports multiple protocols, the default will be Fibre Channel. This field is meaningful only to VVol folder. Possible values: 'iscsi', 'fc'.. [optional]  # noqa: E501
            agent_type (str, none_type): External management agent type. Possible values: 'none', 'smis', 'vvol', 'openstack'.. [optional]  # noqa: E501
            app_uuid (str, none_type): Application identifier of the folder.. [optional]  # noqa: E501
            appserver_id (str, none_type): Identifier of the application server associated with the folder.. [optional]  # noqa: E501
            appserver_name (str, none_type): Name of the application server associated with the folder.. [optional]  # noqa: E501
            associated_links (AssociatedLinks): [optional]  # noqa: E501
            capacity_bytes (int, none_type): Capacity of the folder in bytes. If the folder's size has a usage limit, capacity_bytes will be the folder's usage limit. If the folder's size does not have a usage limit, capacity_bytes will be the pool's capacity. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            compressed_snap_usage_bytes (int, none_type): Compressed usage of snapshots in the folder. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            compressed_vol_usage_bytes (int, none_type): Compressed usage of volumes in the folder. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            compression_ratio (float, none_type): Compression savings for the folder expressed as ratio. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            console_uri (str, none_type): consoleUri for detailed storage object. [optional]  # noqa: E501
            creation_time (int, none_type): Time when this folder was created.. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            description (str, none_type): Text description of folder.. [optional]  # noqa: E501
            folset_id (str, none_type): Identifier of the folder set associated with the folder. Only VVol folder can be associated with the folder set. The folder and the containing folder set must be associated with the same application server.. [optional]  # noqa: E501
            folset_name (str, none_type): Name of the folder set associated with the folder. Only VVol folder can be associated with the folder set. The folder and the containing folder set must be associated with the same application server.. [optional]  # noqa: E501
            fqn (str, none_type): Fully qualified name of folder in the pool.. [optional]  # noqa: E501
            free_space_bytes (int, none_type): Free space in the folder in bytes. If the folder has a usage limit, free_space_bytes will be the folder's free space (the folder's usage limit minus the folder's space usage). If the folder does not have a usage limit, free_space_bytes will be the pool's free space. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            full_name (str, none_type): Fully qualified name of folder in the group.. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            inherited_vol_perfpol_id (str, none_type): Identifier of the default performance policy for a newly created volume.. [optional]  # noqa: E501
            inherited_vol_perfpol_name (str, none_type): Name of the default performance policy for a newly created volume.. [optional]  # noqa: E501
            last_modified (int, none_type): Identifier of the default performance policy for a newly created volume.. [optional]  # noqa: E501
            limit_bytes (int, none_type): Folder limit size in bytes. By default, a folder (except SMIS and VVol types) does not have a limit. If limit_bytes is not specified when a folder is created, or if limit_bytes is set to the largest possible 64-bit signed integer (9223372036854775807), then the folder has no limit. Otherwise, a limit smaller than the capacity of the pool can be set. On output, if the folder has a limit, the limit_bytes_specified attribute will be true and limit_bytes will be the limit. If the folder does not have a limit, the limit_bytes_specified attribute will be false and limit_bytes will be interpreted based on the value of the usage_valid attribute. If the usage_valid attribute is true, limits_byte will be the capacity of the pool. Otherwise, limits_bytes is not meaningful and can be null. SMIS and VVol folders require a size limit. This attribute is superseded by limit_size_bytes.. [optional]  # noqa: E501
            limit_bytes_specified (bool, none_type): Indicates whether the folder has a limit.. [optional]  # noqa: E501
            limit_iops (int, none_type): IOPS limit for this folder. If limit_iops is not specified when a folder is created, or if limit_iops is set to -1, then the folder has no IOPS limit. IOPS limit should be in range [256, 4294967294] or -1 for unlimited.. [optional]  # noqa: E501
            limit_mbps (int, none_type): Throughput limit for this folder in MB/s. If limit_mbps is not specified when a folder is created, or if limit_mbps is set to -1, then the folder has no throughput limit. MBPS limit should be in range [1, 4294967294] or -1 for unlimited.. [optional]  # noqa: E501
            limit_size_bytes (int, none_type): Folder size limit in bytes. If limit_size_bytes is not specified when a folder is created, or if limit_size_bytes is set to -1, then the folder has no limit. Otherwise, a limit smaller than the capacity of the pool can be set. Folders with an agent_type of 'smis' or 'vvol' must have a size limit.. [optional]  # noqa: E501
            num_snapcolls (int, none_type): Number of snapshot collections inside the folder. This attribute is deprecated and has no meaningful value.. [optional]  # noqa: E501
            num_snaps (int, none_type): Number of snapshots inside the folder. This attribute is deprecated and has no meaningful value.. [optional]  # noqa: E501
            overdraft_limit_pct (int, none_type): Amount of space to consider as overdraft range for this folder as a percentage of folder used limit. Valid values are from 0% - 200%. This is the limit above the folder usage limit beyond which enforcement action(volume offline/non-writable) is issued.. [optional]  # noqa: E501
            provisioned_bytes (int, none_type): Sum of provisioned size of volumes in the folder.. [optional]  # noqa: E501
            provisioned_limit_size_bytes (int, none_type): Limit on the provisioned size of volumes in a folder. If provisioned_limit_size_bytes is not specified when a folder is created, or if provisioned_limit_size_bytes is set to -1, then the folder has no provisioned size limit.. [optional]  # noqa: E501
            resource_uri (str, none_type): Link to the object URI. [optional]  # noqa: E501
            search_name (str, none_type): Name of folder used for object search.. [optional]  # noqa: E501
            snap_compression_ratio (float, none_type): Identifier of the default performance policy for a newly created volume.. [optional]  # noqa: E501
            tenant_id (str, none_type): Tenant ID of the folder. This is used to determine what tenant context the folder belongs to.. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
            uncompressed_snap_usage_bytes (int, none_type): Uncompressed usage of snapshots in the folder. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            uncompressed_vol_usage_bytes (int, none_type): Uncompressed usage of volumes in the folder. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            unused_reserve_bytes (str, none_type): Unused reserve of volumes in the folder in bytes. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            unused_snap_reserve_bytes (int, none_type): Unused reserve of snapshots of volumes in the folder in bytes. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            usage_bytes (int, none_type): Sum of mapped usage and snapshot uncompressed usage of volumes in the folder.. [optional]  # noqa: E501
            usage_valid (bool, none_type): Indicate whether the space usage attributes of folder are valid.. [optional]  # noqa: E501
            vol_compression_ratio (float, none_type): Compression ratio of volumes in the folder. This field is meaningful only when the usage_valid attribute is true.. [optional]  # noqa: E501
            volume_list ([NimbleVolumeSummary], none_type): List of volumes contained by the folder.. [optional]  # noqa: E501
            volume_mapped_bytes (int, none_type): Sum of mapped usage of volumes in the folder.. [optional]  # noqa: E501
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
              NimbleFolderDetails,
              NimbleFolderFieldsWithoutSortKey,
          ],
          'oneOf': [
          ],
        }
