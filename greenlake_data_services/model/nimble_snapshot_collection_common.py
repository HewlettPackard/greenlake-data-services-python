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
    from greenlake_data_services.model.key_value import KeyValue
    from greenlake_data_services.model.nimble_snap_coll_snapshot import NimbleSnapCollSnapshot
    globals()['AssociatedLinks'] = AssociatedLinks
    globals()['KeyValue'] = KeyValue
    globals()['NimbleSnapCollSnapshot'] = NimbleSnapCollSnapshot


class NimbleSnapshotCollectionCommon(ModelNormal):
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
            'allow_writes': (bool, none_type,),  # noqa: E501
            'associated_links': (AssociatedLinks,),  # noqa: E501
            'console_uri': (str, none_type,),  # noqa: E501
            'creation_time': (int, none_type,),  # noqa: E501
            'customer_id': (str, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'generation': (int, none_type,),  # noqa: E501
            'is_complete': (bool, none_type,),  # noqa: E501
            'is_external_trigger': (bool, none_type,),  # noqa: E501
            'is_manual': (bool, none_type,),  # noqa: E501
            'is_manually_managed': (bool, none_type,),  # noqa: E501
            'is_replica': (bool, none_type,),  # noqa: E501
            'is_unmanaged': (bool, none_type,),  # noqa: E501
            'last_modified': (int, none_type,),  # noqa: E501
            'metadata': ([KeyValue], none_type,),  # noqa: E501
            'origin_name': (str, none_type,),  # noqa: E501
            'peer_snapcoll_id': (str, none_type,),  # noqa: E501
            'replicate_to': (str, none_type,),  # noqa: E501
            'resource_uri': (str, none_type,),  # noqa: E501
            'snapshots_list': ([NimbleSnapCollSnapshot], none_type,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'allow_writes': 'allow_writes',  # noqa: E501
        'associated_links': 'associated_links',  # noqa: E501
        'console_uri': 'consoleUri',  # noqa: E501
        'creation_time': 'creation_time',  # noqa: E501
        'customer_id': 'customerId',  # noqa: E501
        'description': 'description',  # noqa: E501
        'generation': 'generation',  # noqa: E501
        'is_complete': 'is_complete',  # noqa: E501
        'is_external_trigger': 'is_external_trigger',  # noqa: E501
        'is_manual': 'is_manual',  # noqa: E501
        'is_manually_managed': 'is_manually_managed',  # noqa: E501
        'is_replica': 'is_replica',  # noqa: E501
        'is_unmanaged': 'is_unmanaged',  # noqa: E501
        'last_modified': 'last_modified',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'origin_name': 'origin_name',  # noqa: E501
        'peer_snapcoll_id': 'peer_snapcoll_id',  # noqa: E501
        'replicate_to': 'replicate_to',  # noqa: E501
        'resource_uri': 'resourceUri',  # noqa: E501
        'snapshots_list': 'snapshots_list',  # noqa: E501
        'type': 'type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """NimbleSnapshotCollectionCommon - a model defined in OpenAPI

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
            allow_writes (bool, none_type): Allow applications to write to created snapshot(s). Mandatory and must be set to 'true' for VSS application synchronized snapshots.. [optional]  # noqa: E501
            associated_links (AssociatedLinks): [optional]  # noqa: E501
            console_uri (str, none_type): consoleUri for detailed storage object. [optional]  # noqa: E501
            creation_time (int, none_type): Time when this snapshot collection was created. Seconds since last epoch i.e. 00:00 January 1, 1970.. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            description (str, none_type): Text description of snapshot collection. String of up to 255 printable ASCII characters.. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            is_complete (bool, none_type): Is complete.. [optional]  # noqa: E501
            is_external_trigger (bool, none_type): Is externally triggered.. [optional]  # noqa: E501
            is_manual (bool, none_type): Is manual.. [optional]  # noqa: E501
            is_manually_managed (bool, none_type): Is snapshot collection manually managed, i.e., snapshot collection is manually or third party created or created by system at the time of volume restore or resize.. [optional]  # noqa: E501
            is_replica (bool, none_type): Snapshot collection is a replica from upstream replication partner.. [optional]  # noqa: E501
            is_unmanaged (bool, none_type): Indicates whether a snapshot collection is unmanaged. This is based on the state of individual snapshots.. [optional]  # noqa: E501
            last_modified (int, none_type): Time when this snapshot collection was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970.. [optional]  # noqa: E501
            metadata ([KeyValue], none_type): Key-value pairs that augment a snapshot collection's attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed.. [optional]  # noqa: E501
            origin_name (str, none_type): Origination group name/ID. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            peer_snapcoll_id (str, none_type): ID of the peer snapshot collection created by synchronous replication. Field will be null if no peer snapshot_collection was created by synchronous replication. A 42 digit hexadecimal number.. [optional]  # noqa: E501
            replicate_to (str, none_type): Specifies the partner name that the snapshots in this snapshot collection are replicated to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            resource_uri (str, none_type): Link to the object URI. [optional]  # noqa: E501
            snapshots_list ([NimbleSnapCollSnapshot], none_type): Snapshot list for a SnapshotCollection. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
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
        """NimbleSnapshotCollectionCommon - a model defined in OpenAPI

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
            allow_writes (bool, none_type): Allow applications to write to created snapshot(s). Mandatory and must be set to 'true' for VSS application synchronized snapshots.. [optional]  # noqa: E501
            associated_links (AssociatedLinks): [optional]  # noqa: E501
            console_uri (str, none_type): consoleUri for detailed storage object. [optional]  # noqa: E501
            creation_time (int, none_type): Time when this snapshot collection was created. Seconds since last epoch i.e. 00:00 January 1, 1970.. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            description (str, none_type): Text description of snapshot collection. String of up to 255 printable ASCII characters.. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            is_complete (bool, none_type): Is complete.. [optional]  # noqa: E501
            is_external_trigger (bool, none_type): Is externally triggered.. [optional]  # noqa: E501
            is_manual (bool, none_type): Is manual.. [optional]  # noqa: E501
            is_manually_managed (bool, none_type): Is snapshot collection manually managed, i.e., snapshot collection is manually or third party created or created by system at the time of volume restore or resize.. [optional]  # noqa: E501
            is_replica (bool, none_type): Snapshot collection is a replica from upstream replication partner.. [optional]  # noqa: E501
            is_unmanaged (bool, none_type): Indicates whether a snapshot collection is unmanaged. This is based on the state of individual snapshots.. [optional]  # noqa: E501
            last_modified (int, none_type): Time when this snapshot collection was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970.. [optional]  # noqa: E501
            metadata ([KeyValue], none_type): Key-value pairs that augment a snapshot collection's attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed.. [optional]  # noqa: E501
            origin_name (str, none_type): Origination group name/ID. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            peer_snapcoll_id (str, none_type): ID of the peer snapshot collection created by synchronous replication. Field will be null if no peer snapshot_collection was created by synchronous replication. A 42 digit hexadecimal number.. [optional]  # noqa: E501
            replicate_to (str, none_type): Specifies the partner name that the snapshots in this snapshot collection are replicated to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.. [optional]  # noqa: E501
            resource_uri (str, none_type): Link to the object URI. [optional]  # noqa: E501
            snapshots_list ([NimbleSnapCollSnapshot], none_type): Snapshot list for a SnapshotCollection. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
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
