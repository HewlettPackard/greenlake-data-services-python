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
    from greenlake_data_services.model.nimble_perf_policy_summary import NimblePerfPolicySummary
    from greenlake_data_services.model.nimble_space_domain_details import NimbleSpaceDomainDetails
    from greenlake_data_services.model.nimble_space_domain_fields_without_sort_key import NimbleSpaceDomainFieldsWithoutSortKey
    from greenlake_data_services.model.nimble_volume_summary import NimbleVolumeSummary
    globals()['AssociatedLinks'] = AssociatedLinks
    globals()['NimblePerfPolicySummary'] = NimblePerfPolicySummary
    globals()['NimbleSpaceDomainDetails'] = NimbleSpaceDomainDetails
    globals()['NimbleSpaceDomainFieldsWithoutSortKey'] = NimbleSpaceDomainFieldsWithoutSortKey
    globals()['NimbleVolumeSummary'] = NimbleVolumeSummary


class NimbleSpaceDomainDetailsWithRequestUri(ModelComposed):
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
            'app_category_id': (str, none_type,),  # noqa: E501
            'app_category_name': (str, none_type,),  # noqa: E501
            'block_size': (int, none_type,),  # noqa: E501
            'clone_ratio': (float, none_type,),  # noqa: E501
            'compressed_usage_bytes': (int, none_type,),  # noqa: E501
            'compression_ratio': (float, none_type,),  # noqa: E501
            'dedupe_ratio': (float, none_type,),  # noqa: E501
            'deduped': (bool, none_type,),  # noqa: E501
            'encrypted': (bool, none_type,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'logical_dedupe_usage': (int, none_type,),  # noqa: E501
            'physical_dedupe_usage': (int, none_type,),  # noqa: E501
            'pool_id': (str, none_type,),  # noqa: E501
            'pool_name': (str, none_type,),  # noqa: E501
            'savings_clone': (int, none_type,),  # noqa: E501
            'savings_compression': (int, none_type,),  # noqa: E501
            'savings_dedupe': (int, none_type,),  # noqa: E501
            'snap_logical_usage': (int, none_type,),  # noqa: E501
            'uncompressed_usage_bytes': (int, none_type,),  # noqa: E501
            'usage': (int, none_type,),  # noqa: E501
            'vol_logical_usage': (int, none_type,),  # noqa: E501
            'vol_mapped_usage': (int, none_type,),  # noqa: E501
            'associated_links': (AssociatedLinks,),  # noqa: E501
            'console_uri': (str, none_type,),  # noqa: E501
            'customer_id': (str, none_type,),  # noqa: E501
            'deduped_volume_count': (int, none_type,),  # noqa: E501
            'generation': (int, none_type,),  # noqa: E501
            'perf_policy_names': ([NimblePerfPolicySummary], none_type,),  # noqa: E501
            'resource_uri': (str, none_type,),  # noqa: E501
            'sample_rate': (int, none_type,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
            'volume_count': (int, none_type,),  # noqa: E501
            'volumes': ([NimbleVolumeSummary], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'request_uri': 'requestUri',  # noqa: E501
        'app_category_id': 'app_category_id',  # noqa: E501
        'app_category_name': 'app_category_name',  # noqa: E501
        'block_size': 'block_size',  # noqa: E501
        'clone_ratio': 'clone_ratio',  # noqa: E501
        'compressed_usage_bytes': 'compressed_usage_bytes',  # noqa: E501
        'compression_ratio': 'compression_ratio',  # noqa: E501
        'dedupe_ratio': 'dedupe_ratio',  # noqa: E501
        'deduped': 'deduped',  # noqa: E501
        'encrypted': 'encrypted',  # noqa: E501
        'id': 'id',  # noqa: E501
        'logical_dedupe_usage': 'logical_dedupe_usage',  # noqa: E501
        'physical_dedupe_usage': 'physical_dedupe_usage',  # noqa: E501
        'pool_id': 'pool_id',  # noqa: E501
        'pool_name': 'pool_name',  # noqa: E501
        'savings_clone': 'savings_clone',  # noqa: E501
        'savings_compression': 'savings_compression',  # noqa: E501
        'savings_dedupe': 'savings_dedupe',  # noqa: E501
        'snap_logical_usage': 'snap_logical_usage',  # noqa: E501
        'uncompressed_usage_bytes': 'uncompressed_usage_bytes',  # noqa: E501
        'usage': 'usage',  # noqa: E501
        'vol_logical_usage': 'vol_logical_usage',  # noqa: E501
        'vol_mapped_usage': 'vol_mapped_usage',  # noqa: E501
        'associated_links': 'associated_links',  # noqa: E501
        'console_uri': 'consoleUri',  # noqa: E501
        'customer_id': 'customerId',  # noqa: E501
        'deduped_volume_count': 'deduped_volume_count',  # noqa: E501
        'generation': 'generation',  # noqa: E501
        'perf_policy_names': 'perf_policy_names',  # noqa: E501
        'resource_uri': 'resourceUri',  # noqa: E501
        'sample_rate': 'sample_rate',  # noqa: E501
        'type': 'type',  # noqa: E501
        'volume_count': 'volume_count',  # noqa: E501
        'volumes': 'volumes',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """NimbleSpaceDomainDetailsWithRequestUri - a model defined in OpenAPI

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
            request_uri (str, none_type): requestUri for detailed application-summary object. [optional]  # noqa: E501
            app_category_id (str, none_type): Identifier of the application category associated with the space domain.. [optional]  # noqa: E501
            app_category_name (str, none_type): Name of the application category associated with the space domain.. [optional]  # noqa: E501
            block_size (int, none_type): Block size in bytes of volumes belonging to the space domain.. [optional]  # noqa: E501
            clone_ratio (float, none_type): Clone savings for the space domain expressed as ratio.. [optional]  # noqa: E501
            compressed_usage_bytes (int, none_type): Compressed usage of volumes and snapshots in the space domain.. [optional]  # noqa: E501
            compression_ratio (float, none_type): Compression savings for the space domain expressed as ratio.. [optional]  # noqa: E501
            dedupe_ratio (float, none_type): Deduplication savings for the space domain expressed as ratio.. [optional]  # noqa: E501
            deduped (bool, none_type): Volumes in space domain are deduplicated by default.. [optional]  # noqa: E501
            encrypted (bool, none_type): Volumes in space domain are encrypted.. [optional]  # noqa: E501
            id (str, none_type): Identifier of the application summery.. [optional]  # noqa: E501
            logical_dedupe_usage (int, none_type): Logical space usage of volumes when deduped.. [optional]  # noqa: E501
            physical_dedupe_usage (int, none_type): Physical space usage of volumes including snapshots when deduped.. [optional]  # noqa: E501
            pool_id (str, none_type): Identifier associated with the pool in the storage pool table.. [optional]  # noqa: E501
            pool_name (str, none_type): Name of the pool containing the space domain.. [optional]  # noqa: E501
            savings_clone (int, none_type): Space usage savings in the space domain due to cloning of volumes.. [optional]  # noqa: E501
            savings_compression (int, none_type): Space usage savings in the space domain due to compression.. [optional]  # noqa: E501
            savings_dedupe (int, none_type): Space usage savings in the space domain due to deduplication.. [optional]  # noqa: E501
            snap_logical_usage (int, none_type): Logical usage of snapshots in the space domain.. [optional]  # noqa: E501
            uncompressed_usage_bytes (int, none_type): Uncompressed usage of volumes and snapshots in the space domain.. [optional]  # noqa: E501
            usage (int, none_type): Physical space usage of volumes in the space domain.. [optional]  # noqa: E501
            vol_logical_usage (int, none_type): Logical usage of volumes in the space domain.. [optional]  # noqa: E501
            vol_mapped_usage (int, none_type): Mapped usage of volumes in the space domain, useful for computing clone savings.. [optional]  # noqa: E501
            associated_links (AssociatedLinks): [optional]  # noqa: E501
            console_uri (str, none_type): consoleUri for detailed storage object. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            deduped_volume_count (int, none_type): Number of deduplicated volumes belonging to the space domain.. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            perf_policy_names ([NimblePerfPolicySummary], none_type): Name of the performance policies associated with the space domain.. [optional]  # noqa: E501
            resource_uri (str, none_type): Link to the object URI. [optional]  # noqa: E501
            sample_rate (int, none_type): Sample rate value.. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
            volume_count (int, none_type): Number of volumes belonging to the space domain.. [optional]  # noqa: E501
            volumes ([NimbleVolumeSummary], none_type): Volumes belonging to the space domain.. [optional]  # noqa: E501
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
        """NimbleSpaceDomainDetailsWithRequestUri - a model defined in OpenAPI

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
            request_uri (str, none_type): requestUri for detailed application-summary object. [optional]  # noqa: E501
            app_category_id (str, none_type): Identifier of the application category associated with the space domain.. [optional]  # noqa: E501
            app_category_name (str, none_type): Name of the application category associated with the space domain.. [optional]  # noqa: E501
            block_size (int, none_type): Block size in bytes of volumes belonging to the space domain.. [optional]  # noqa: E501
            clone_ratio (float, none_type): Clone savings for the space domain expressed as ratio.. [optional]  # noqa: E501
            compressed_usage_bytes (int, none_type): Compressed usage of volumes and snapshots in the space domain.. [optional]  # noqa: E501
            compression_ratio (float, none_type): Compression savings for the space domain expressed as ratio.. [optional]  # noqa: E501
            dedupe_ratio (float, none_type): Deduplication savings for the space domain expressed as ratio.. [optional]  # noqa: E501
            deduped (bool, none_type): Volumes in space domain are deduplicated by default.. [optional]  # noqa: E501
            encrypted (bool, none_type): Volumes in space domain are encrypted.. [optional]  # noqa: E501
            id (str, none_type): Identifier of the application summery.. [optional]  # noqa: E501
            logical_dedupe_usage (int, none_type): Logical space usage of volumes when deduped.. [optional]  # noqa: E501
            physical_dedupe_usage (int, none_type): Physical space usage of volumes including snapshots when deduped.. [optional]  # noqa: E501
            pool_id (str, none_type): Identifier associated with the pool in the storage pool table.. [optional]  # noqa: E501
            pool_name (str, none_type): Name of the pool containing the space domain.. [optional]  # noqa: E501
            savings_clone (int, none_type): Space usage savings in the space domain due to cloning of volumes.. [optional]  # noqa: E501
            savings_compression (int, none_type): Space usage savings in the space domain due to compression.. [optional]  # noqa: E501
            savings_dedupe (int, none_type): Space usage savings in the space domain due to deduplication.. [optional]  # noqa: E501
            snap_logical_usage (int, none_type): Logical usage of snapshots in the space domain.. [optional]  # noqa: E501
            uncompressed_usage_bytes (int, none_type): Uncompressed usage of volumes and snapshots in the space domain.. [optional]  # noqa: E501
            usage (int, none_type): Physical space usage of volumes in the space domain.. [optional]  # noqa: E501
            vol_logical_usage (int, none_type): Logical usage of volumes in the space domain.. [optional]  # noqa: E501
            vol_mapped_usage (int, none_type): Mapped usage of volumes in the space domain, useful for computing clone savings.. [optional]  # noqa: E501
            associated_links (AssociatedLinks): [optional]  # noqa: E501
            console_uri (str, none_type): consoleUri for detailed storage object. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            deduped_volume_count (int, none_type): Number of deduplicated volumes belonging to the space domain.. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            perf_policy_names ([NimblePerfPolicySummary], none_type): Name of the performance policies associated with the space domain.. [optional]  # noqa: E501
            resource_uri (str, none_type): Link to the object URI. [optional]  # noqa: E501
            sample_rate (int, none_type): Sample rate value.. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
            volume_count (int, none_type): Number of volumes belonging to the space domain.. [optional]  # noqa: E501
            volumes ([NimbleVolumeSummary], none_type): Volumes belonging to the space domain.. [optional]  # noqa: E501
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
              NimbleSpaceDomainDetails,
              NimbleSpaceDomainFieldsWithoutSortKey,
          ],
          'oneOf': [
          ],
        }
