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
    from greenlake_data_services.model.nimble_ns_shelf_ctrlr_attr_set import NimbleNsShelfCtrlrAttrSet
    from greenlake_data_services.model.nimble_ns_shelf_port_info import NimbleNsShelfPortInfo
    from greenlake_data_services.model.nimble_ns_shelf_sensor import NimbleNsShelfSensor
    globals()['NimbleNsShelfCtrlrAttrSet'] = NimbleNsShelfCtrlrAttrSet
    globals()['NimbleNsShelfPortInfo'] = NimbleNsShelfPortInfo
    globals()['NimbleNsShelfSensor'] = NimbleNsShelfSensor


class NimbleNsShelfCtrlr(ModelNormal):
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
            'cached_serial': (str, none_type,),  # noqa: E501
            'ctrlr_attrset_list': ([NimbleNsShelfCtrlrAttrSet], none_type,),  # noqa: E501
            'ctrlr_hw_model': (str, none_type,),  # noqa: E501
            'ctrlr_sensor_last_run': (int, none_type,),  # noqa: E501
            'ctrlr_sensors': ([NimbleNsShelfSensor], none_type,),  # noqa: E501
            'ctrlr_side': (str, none_type,),  # noqa: E501
            'enc_loc_id': (int, none_type,),  # noqa: E501
            'exp_sas_addr': (str, none_type,),  # noqa: E501
            'extra_attributes': ([str, none_type], none_type,),  # noqa: E501
            'fan_overall_status': (str, none_type,),  # noqa: E501
            'hw_master_state': (str, none_type,),  # noqa: E501
            'hw_mship_failure': (bool, none_type,),  # noqa: E501
            'identify_status': (bool, none_type,),  # noqa: E501
            'port_info': ([NimbleNsShelfPortInfo], none_type,),  # noqa: E501
            'psu_overall_status': (str, none_type,),  # noqa: E501
            'sw_master_state': (str, none_type,),  # noqa: E501
            'temp_overall_status': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'cached_serial': 'cached_serial',  # noqa: E501
        'ctrlr_attrset_list': 'ctrlr_attrset_list',  # noqa: E501
        'ctrlr_hw_model': 'ctrlr_hw_model',  # noqa: E501
        'ctrlr_sensor_last_run': 'ctrlr_sensor_last_run',  # noqa: E501
        'ctrlr_sensors': 'ctrlr_sensors',  # noqa: E501
        'ctrlr_side': 'ctrlr_side',  # noqa: E501
        'enc_loc_id': 'enc_loc_id',  # noqa: E501
        'exp_sas_addr': 'exp_sas_addr',  # noqa: E501
        'extra_attributes': 'extra_attributes',  # noqa: E501
        'fan_overall_status': 'fan_overall_status',  # noqa: E501
        'hw_master_state': 'hw_master_state',  # noqa: E501
        'hw_mship_failure': 'hw_mship_failure',  # noqa: E501
        'identify_status': 'identify_status',  # noqa: E501
        'port_info': 'port_info',  # noqa: E501
        'psu_overall_status': 'psu_overall_status',  # noqa: E501
        'sw_master_state': 'sw_master_state',  # noqa: E501
        'temp_overall_status': 'temp_overall_status',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """NimbleNsShelfCtrlr - a model defined in OpenAPI

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
            cached_serial (str, none_type): CachedSerial - Cached serial.. [optional]  # noqa: E501
            ctrlr_attrset_list ([NimbleNsShelfCtrlrAttrSet], none_type): List of ctrlr attribute set for each logical controller.. [optional]  # noqa: E501
            ctrlr_hw_model (str, none_type): Controller hardware model. Possible values:'head_x9', 'head_x8', 'head_gen5_2u', 'es2_4u', 'head_vmware', 'es1_3u', 'head_x9_2u', 'head_x10', 'head_gen5', 'es3_4u', 'unknown'.. [optional]  # noqa: E501
            ctrlr_sensor_last_run (int, none_type): The time of last valid sensor reading, in epoch seconds.. [optional]  # noqa: E501
            ctrlr_sensors ([NimbleNsShelfSensor], none_type): The list of individual sensor reading in this controller.. [optional]  # noqa: E501
            ctrlr_side (str, none_type): Position of this controller in the chassis. Possible values:'A', 'B', 'unknown'.. [optional]  # noqa: E501
            enc_loc_id (int, none_type): Location ID based on SAS topology.. [optional]  # noqa: E501
            exp_sas_addr (str, none_type): Expander SAS address.. [optional]  # noqa: E501
            extra_attributes ([str, none_type], none_type): Extra attributes as attribute value pairs.. [optional]  # noqa: E501
            fan_overall_status (str, none_type): The overall status for the fans on this controller. Possible values:'Missing', 'Failed', 'OK', 'Alerted'.. [optional]  # noqa: E501
            hw_master_state (str, none_type): SES device hardware mastership state. Possible values:'not master', 'failed', 'unknown', 'master'.. [optional]  # noqa: E501
            hw_mship_failure (bool, none_type): SES device hardware mastership failure.. [optional]  # noqa: E501
            identify_status (bool, none_type): Status of chassis identifier.. [optional]  # noqa: E501
            port_info ([NimbleNsShelfPortInfo], none_type): Port info for each SAS port.. [optional]  # noqa: E501
            psu_overall_status (str, none_type): The overall status for the PSU on this controller.. Possible values: 'OK', 'Alerted', 'Failed', 'Missing'.. [optional]  # noqa: E501
            sw_master_state (str, none_type): SES device software mastership state. Possible values:'not master', 'want master', 'unknown', 'master', 'release master'.. [optional]  # noqa: E501
            temp_overall_status (str, none_type): The overall status for the temperature of this controller.  Possible values:'Missing', 'Failed', 'OK', 'Alerted'.. [optional]  # noqa: E501
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
        """NimbleNsShelfCtrlr - a model defined in OpenAPI

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
            cached_serial (str, none_type): CachedSerial - Cached serial.. [optional]  # noqa: E501
            ctrlr_attrset_list ([NimbleNsShelfCtrlrAttrSet], none_type): List of ctrlr attribute set for each logical controller.. [optional]  # noqa: E501
            ctrlr_hw_model (str, none_type): Controller hardware model. Possible values:'head_x9', 'head_x8', 'head_gen5_2u', 'es2_4u', 'head_vmware', 'es1_3u', 'head_x9_2u', 'head_x10', 'head_gen5', 'es3_4u', 'unknown'.. [optional]  # noqa: E501
            ctrlr_sensor_last_run (int, none_type): The time of last valid sensor reading, in epoch seconds.. [optional]  # noqa: E501
            ctrlr_sensors ([NimbleNsShelfSensor], none_type): The list of individual sensor reading in this controller.. [optional]  # noqa: E501
            ctrlr_side (str, none_type): Position of this controller in the chassis. Possible values:'A', 'B', 'unknown'.. [optional]  # noqa: E501
            enc_loc_id (int, none_type): Location ID based on SAS topology.. [optional]  # noqa: E501
            exp_sas_addr (str, none_type): Expander SAS address.. [optional]  # noqa: E501
            extra_attributes ([str, none_type], none_type): Extra attributes as attribute value pairs.. [optional]  # noqa: E501
            fan_overall_status (str, none_type): The overall status for the fans on this controller. Possible values:'Missing', 'Failed', 'OK', 'Alerted'.. [optional]  # noqa: E501
            hw_master_state (str, none_type): SES device hardware mastership state. Possible values:'not master', 'failed', 'unknown', 'master'.. [optional]  # noqa: E501
            hw_mship_failure (bool, none_type): SES device hardware mastership failure.. [optional]  # noqa: E501
            identify_status (bool, none_type): Status of chassis identifier.. [optional]  # noqa: E501
            port_info ([NimbleNsShelfPortInfo], none_type): Port info for each SAS port.. [optional]  # noqa: E501
            psu_overall_status (str, none_type): The overall status for the PSU on this controller.. Possible values: 'OK', 'Alerted', 'Failed', 'Missing'.. [optional]  # noqa: E501
            sw_master_state (str, none_type): SES device software mastership state. Possible values:'not master', 'want master', 'unknown', 'master', 'release master'.. [optional]  # noqa: E501
            temp_overall_status (str, none_type): The overall status for the temperature of this controller.  Possible values:'Missing', 'Failed', 'OK', 'Alerted'.. [optional]  # noqa: E501
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
