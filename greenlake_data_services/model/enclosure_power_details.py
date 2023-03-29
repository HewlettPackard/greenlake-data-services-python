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
    from greenlake_data_services.model.enclosure_type_single import EnclosureTypeSingle
    from greenlake_data_services.model.ep_associated_links import EpAssociatedLinks
    from greenlake_data_services.model.manufacturing_single import ManufacturingSingle
    from greenlake_data_services.model.state import STATE
    globals()['EnclosureTypeSingle'] = EnclosureTypeSingle
    globals()['EpAssociatedLinks'] = EpAssociatedLinks
    globals()['ManufacturingSingle'] = ManufacturingSingle
    globals()['STATE'] = STATE


class EnclosurePowerDetails(ModelNormal):
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
            'ac_status': (str, none_type,),  # noqa: E501
            'associated_links': (EpAssociatedLinks,),  # noqa: E501
            'console_uri': (str, none_type,),  # noqa: E501
            'customer_id': (str, none_type,),  # noqa: E501
            'dc_status': (str, none_type,),  # noqa: E501
            'displayname': (str, none_type,),  # noqa: E501
            'domain': (str, none_type,),  # noqa: E501
            'element_status_code': (str, none_type,),  # noqa: E501
            'enclosure_device_id': (int, none_type,),  # noqa: E501
            'enclosure_id': (str, none_type,),  # noqa: E501
            'enclosure_name': (str, none_type,),  # noqa: E501
            'enclosure_power_id': (int, none_type,),  # noqa: E501
            'enclosure_type': (EnclosureTypeSingle,),  # noqa: E501
            'fail_indicator': (bool, none_type,),  # noqa: E501
            'fail_input': (bool, none_type,),  # noqa: E501
            'fail_output': (bool, none_type,),  # noqa: E501
            'generation': (int, none_type,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'locate_enabled': (bool, none_type,),  # noqa: E501
            'manufacturing': (ManufacturingSingle,),  # noqa: E501
            'model_read_only': (bool, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'request_uri': (str, none_type,),  # noqa: E501
            'resource_uri': (str, none_type,),  # noqa: E501
            'safe_to_remove': (bool, none_type,),  # noqa: E501
            'state': (STATE,),  # noqa: E501
            'system_id': (str, none_type,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'ac_status': 'acStatus',  # noqa: E501
        'associated_links': 'associatedLinks',  # noqa: E501
        'console_uri': 'consoleUri',  # noqa: E501
        'customer_id': 'customerId',  # noqa: E501
        'dc_status': 'dcStatus',  # noqa: E501
        'displayname': 'displayname',  # noqa: E501
        'domain': 'domain',  # noqa: E501
        'element_status_code': 'elementStatusCode',  # noqa: E501
        'enclosure_device_id': 'enclosureDeviceId',  # noqa: E501
        'enclosure_id': 'enclosureId',  # noqa: E501
        'enclosure_name': 'enclosureName',  # noqa: E501
        'enclosure_power_id': 'enclosurePowerId',  # noqa: E501
        'enclosure_type': 'enclosureType',  # noqa: E501
        'fail_indicator': 'failIndicator',  # noqa: E501
        'fail_input': 'failInput',  # noqa: E501
        'fail_output': 'failOutput',  # noqa: E501
        'generation': 'generation',  # noqa: E501
        'id': 'id',  # noqa: E501
        'locate_enabled': 'locateEnabled',  # noqa: E501
        'manufacturing': 'manufacturing',  # noqa: E501
        'model_read_only': 'modelReadOnly',  # noqa: E501
        'name': 'name',  # noqa: E501
        'request_uri': 'requestUri',  # noqa: E501
        'resource_uri': 'resourceUri',  # noqa: E501
        'safe_to_remove': 'safeToRemove',  # noqa: E501
        'state': 'state',  # noqa: E501
        'system_id': 'systemId',  # noqa: E501
        'type': 'type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EnclosurePowerDetails - a model defined in OpenAPI

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
            ac_status (str, none_type): [optional]  # noqa: E501
            associated_links (EpAssociatedLinks): [optional]  # noqa: E501
            console_uri (str, none_type): consoleUri for detailed storage object. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            dc_status (str, none_type): [optional]  # noqa: E501
            displayname (str, none_type): Enclosure power Display name. [optional]  # noqa: E501
            domain (str, none_type): Domain that the resource belongs to. [optional]  # noqa: E501
            element_status_code (str, none_type): Enclosure status code. [optional]  # noqa: E501
            enclosure_device_id (int, none_type): [optional]  # noqa: E501
            enclosure_id (str, none_type): Parent UID of the resource.. [optional]  # noqa: E501
            enclosure_name (str, none_type): Name of the enclosure power.. [optional]  # noqa: E501
            enclosure_power_id (int, none_type): Numeric ID of the resource. [optional]  # noqa: E501
            enclosure_type (EnclosureTypeSingle): [optional]  # noqa: E501
            fail_indicator (bool, none_type): [optional]  # noqa: E501
            fail_input (bool, none_type): [optional]  # noqa: E501
            fail_output (bool, none_type): [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            id (str, none_type): Unique Identifier of the resource.. [optional]  # noqa: E501
            locate_enabled (bool, none_type): Indicates if the locate beacon is enabled or not. [optional]  # noqa: E501
            manufacturing (ManufacturingSingle): [optional]  # noqa: E501
            model_read_only (bool, none_type): [optional]  # noqa: E501
            name (str, none_type): Name of the resource.. [optional]  # noqa: E501
            request_uri (str, none_type): resourceUri for detailed enclosure object. [optional]  # noqa: E501
            resource_uri (str, none_type): resourceUri for detailed enclosure object. [optional]  # noqa: E501
            safe_to_remove (bool, none_type): [optional]  # noqa: E501
            state (STATE): [optional]  # noqa: E501
            system_id (str, none_type): SystemUid/Serial Number  of the array.. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
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
        """EnclosurePowerDetails - a model defined in OpenAPI

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
            ac_status (str, none_type): [optional]  # noqa: E501
            associated_links (EpAssociatedLinks): [optional]  # noqa: E501
            console_uri (str, none_type): consoleUri for detailed storage object. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            dc_status (str, none_type): [optional]  # noqa: E501
            displayname (str, none_type): Enclosure power Display name. [optional]  # noqa: E501
            domain (str, none_type): Domain that the resource belongs to. [optional]  # noqa: E501
            element_status_code (str, none_type): Enclosure status code. [optional]  # noqa: E501
            enclosure_device_id (int, none_type): [optional]  # noqa: E501
            enclosure_id (str, none_type): Parent UID of the resource.. [optional]  # noqa: E501
            enclosure_name (str, none_type): Name of the enclosure power.. [optional]  # noqa: E501
            enclosure_power_id (int, none_type): Numeric ID of the resource. [optional]  # noqa: E501
            enclosure_type (EnclosureTypeSingle): [optional]  # noqa: E501
            fail_indicator (bool, none_type): [optional]  # noqa: E501
            fail_input (bool, none_type): [optional]  # noqa: E501
            fail_output (bool, none_type): [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            id (str, none_type): Unique Identifier of the resource.. [optional]  # noqa: E501
            locate_enabled (bool, none_type): Indicates if the locate beacon is enabled or not. [optional]  # noqa: E501
            manufacturing (ManufacturingSingle): [optional]  # noqa: E501
            model_read_only (bool, none_type): [optional]  # noqa: E501
            name (str, none_type): Name of the resource.. [optional]  # noqa: E501
            request_uri (str, none_type): resourceUri for detailed enclosure object. [optional]  # noqa: E501
            resource_uri (str, none_type): resourceUri for detailed enclosure object. [optional]  # noqa: E501
            safe_to_remove (bool, none_type): [optional]  # noqa: E501
            state (STATE): [optional]  # noqa: E501
            system_id (str, none_type): SystemUid/Serial Number  of the array.. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
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
