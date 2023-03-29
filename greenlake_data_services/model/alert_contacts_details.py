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



class AlertContactsDetails(ModelNormal):
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
            'company': (str, none_type,),  # noqa: E501
            'company_code': (str, none_type,),  # noqa: E501
            'console_uri': (str, none_type,),  # noqa: E501
            'country': (str, none_type,),  # noqa: E501
            'customer_id': (str,),  # noqa: E501
            'fax': (str, none_type,),  # noqa: E501
            'first_name': (str, none_type,),  # noqa: E501
            'generation': (int,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'include_svc_alerts': (bool, none_type,),  # noqa: E501
            'last_name': (str, none_type,),  # noqa: E501
            'notification_severities': ([int], none_type,),  # noqa: E501
            'preferred_language': (str, none_type,),  # noqa: E501
            'primary_email': (str, none_type,),  # noqa: E501
            'primary_phone': (str, none_type,),  # noqa: E501
            'receive_email': (bool, none_type,),  # noqa: E501
            'receive_grouped': (bool, none_type,),  # noqa: E501
            'secondary_email': (str, none_type,),  # noqa: E501
            'secondary_phone': (str, none_type,),  # noqa: E501
            'system_id': (str, none_type,),  # noqa: E501
            'system_support_contact': (bool, none_type,),  # noqa: E501
            'type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'company': 'company',  # noqa: E501
        'company_code': 'companyCode',  # noqa: E501
        'console_uri': 'consoleUri',  # noqa: E501
        'country': 'country',  # noqa: E501
        'customer_id': 'customerId',  # noqa: E501
        'fax': 'fax',  # noqa: E501
        'first_name': 'firstName',  # noqa: E501
        'generation': 'generation',  # noqa: E501
        'id': 'id',  # noqa: E501
        'include_svc_alerts': 'includeSvcAlerts',  # noqa: E501
        'last_name': 'lastName',  # noqa: E501
        'notification_severities': 'notificationSeverities',  # noqa: E501
        'preferred_language': 'preferredLanguage',  # noqa: E501
        'primary_email': 'primaryEmail',  # noqa: E501
        'primary_phone': 'primaryPhone',  # noqa: E501
        'receive_email': 'receiveEmail',  # noqa: E501
        'receive_grouped': 'receiveGrouped',  # noqa: E501
        'secondary_email': 'secondaryEmail',  # noqa: E501
        'secondary_phone': 'secondaryPhone',  # noqa: E501
        'system_id': 'systemId',  # noqa: E501
        'system_support_contact': 'systemSupportContact',  # noqa: E501
        'type': 'type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AlertContactsDetails - a model defined in OpenAPI

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
            company (str, none_type): Company. [optional]  # noqa: E501
            company_code (str, none_type): Company code. [optional]  # noqa: E501
            console_uri (str, none_type): consoleUri for detailed storage object. [optional]  # noqa: E501
            country (str, none_type): Country. [optional]  # noqa: E501
            customer_id (str): The customer application identifier. [optional]  # noqa: E501
            fax (str, none_type): Fax number. [optional]  # noqa: E501
            first_name (str, none_type): First name. [optional]  # noqa: E501
            generation (int): A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. . [optional]  # noqa: E501
            id (str, none_type): Unique Identifier of the contact. [optional]  # noqa: E501
            include_svc_alerts (bool, none_type): Email sent to contact shall include service alert. [optional]  # noqa: E501
            last_name (str, none_type): Last name. [optional]  # noqa: E501
            notification_severities ([int], none_type): Severities of notifications the contact will be notificated. An array of number: 0 - Fatal, 1 - Critical, 2 - Major, 3 - Minor, 4 - Degraded, 5 - Info, 6 - Debug. [optional]  # noqa: E501
            preferred_language (str, none_type): Preferred language when being contacted or emailed. [optional]  # noqa: E501
            primary_email (str, none_type): Primary email address. [optional]  # noqa: E501
            primary_phone (str, none_type): Primary phone. [optional]  # noqa: E501
            receive_email (bool, none_type): Contact will receive email notifications. This is a deprecated field and will always pass true to be inline with UI.. [optional]  # noqa: E501
            receive_grouped (bool, none_type): Contact will receive grouped low urgency email notifications. [optional]  # noqa: E501
            secondary_email (str, none_type): Secondary email address. [optional]  # noqa: E501
            secondary_phone (str, none_type): Secondary phone. [optional]  # noqa: E501
            system_id (str, none_type): SystemId/serialNumber of the array.. [optional]  # noqa: E501
            system_support_contact (bool, none_type): Contact will be called for any system issues. [optional]  # noqa: E501
            type (str): The type of resource. [optional]  # noqa: E501
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
        """AlertContactsDetails - a model defined in OpenAPI

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
            company (str, none_type): Company. [optional]  # noqa: E501
            company_code (str, none_type): Company code. [optional]  # noqa: E501
            console_uri (str, none_type): consoleUri for detailed storage object. [optional]  # noqa: E501
            country (str, none_type): Country. [optional]  # noqa: E501
            customer_id (str): The customer application identifier. [optional]  # noqa: E501
            fax (str, none_type): Fax number. [optional]  # noqa: E501
            first_name (str, none_type): First name. [optional]  # noqa: E501
            generation (int): A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. . [optional]  # noqa: E501
            id (str, none_type): Unique Identifier of the contact. [optional]  # noqa: E501
            include_svc_alerts (bool, none_type): Email sent to contact shall include service alert. [optional]  # noqa: E501
            last_name (str, none_type): Last name. [optional]  # noqa: E501
            notification_severities ([int], none_type): Severities of notifications the contact will be notificated. An array of number: 0 - Fatal, 1 - Critical, 2 - Major, 3 - Minor, 4 - Degraded, 5 - Info, 6 - Debug. [optional]  # noqa: E501
            preferred_language (str, none_type): Preferred language when being contacted or emailed. [optional]  # noqa: E501
            primary_email (str, none_type): Primary email address. [optional]  # noqa: E501
            primary_phone (str, none_type): Primary phone. [optional]  # noqa: E501
            receive_email (bool, none_type): Contact will receive email notifications. This is a deprecated field and will always pass true to be inline with UI.. [optional]  # noqa: E501
            receive_grouped (bool, none_type): Contact will receive grouped low urgency email notifications. [optional]  # noqa: E501
            secondary_email (str, none_type): Secondary email address. [optional]  # noqa: E501
            secondary_phone (str, none_type): Secondary phone. [optional]  # noqa: E501
            system_id (str, none_type): SystemId/serialNumber of the array.. [optional]  # noqa: E501
            system_support_contact (bool, none_type): Contact will be called for any system issues. [optional]  # noqa: E501
            type (str): The type of resource. [optional]  # noqa: E501
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
