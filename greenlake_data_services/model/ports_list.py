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
    from greenlake_data_services.model.card_type import CardType
    from greenlake_data_services.model.connected_devices import ConnectedDevices
    from greenlake_data_services.model.initiator_port import InitiatorPort
    from greenlake_data_services.model.manufacturing_single import ManufacturingSingle
    from greenlake_data_services.model.partner import Partner
    from greenlake_data_services.model.port_fc import PortFC
    from greenlake_data_services.model.port_ip import PortIP
    from greenlake_data_services.model.port_iscsi import PortISCSI
    from greenlake_data_services.model.port_position import PortPosition
    from greenlake_data_services.model.port_sfp import PortSfp
    from greenlake_data_services.model.ports_associated_links import PortsAssociatedLinks
    from greenlake_data_services.model.state import STATE
    from greenlake_data_services.model.state_description import StateDescription
    from greenlake_data_services.model.vlan import Vlan
    globals()['CardType'] = CardType
    globals()['ConnectedDevices'] = ConnectedDevices
    globals()['InitiatorPort'] = InitiatorPort
    globals()['ManufacturingSingle'] = ManufacturingSingle
    globals()['Partner'] = Partner
    globals()['PortFC'] = PortFC
    globals()['PortIP'] = PortIP
    globals()['PortISCSI'] = PortISCSI
    globals()['PortPosition'] = PortPosition
    globals()['PortSfp'] = PortSfp
    globals()['PortsAssociatedLinks'] = PortsAssociatedLinks
    globals()['STATE'] = STATE
    globals()['StateDescription'] = StateDescription
    globals()['Vlan'] = Vlan


class PortsList(ModelNormal):
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
            'associated_links': (PortsAssociatedLinks,),  # noqa: E501
            'card_type': (CardType,),  # noqa: E501
            '_class': (int, none_type,),  # noqa: E501
            'class2': (str, none_type,),  # noqa: E501
            'config': (str, none_type,),  # noqa: E501
            'config_mode': (str, none_type,),  # noqa: E501
            'connection_type': (str, none_type,),  # noqa: E501
            'customer_id': (str, none_type,),  # noqa: E501
            'devices': (ConnectedDevices,),  # noqa: E501
            'displayname': (str, none_type,),  # noqa: E501
            'domain': (str, none_type,),  # noqa: E501
            'failover_status': (str, none_type,),  # noqa: E501
            'fc_data': (PortFC,),  # noqa: E501
            'fw_version': (str, none_type,),  # noqa: E501
            'generation': (int, none_type,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'initiator_ports': (InitiatorPort,),  # noqa: E501
            'interupt_coalesce': (str, none_type,),  # noqa: E501
            'ip_data': (PortIP,),  # noqa: E501
            'iscsi_data': (PortISCSI,),  # noqa: E501
            'label': (str, none_type,),  # noqa: E501
            'manufacturing': (ManufacturingSingle,),  # noqa: E501
            'mode': (str, none_type,),  # noqa: E501
            'mode_change': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'node_card_id': (str, none_type,),  # noqa: E501
            'node_id': (str, none_type,),  # noqa: E501
            'partner': (Partner,),  # noqa: E501
            'port_sfp': (PortSfp,),  # noqa: E501
            'port_type': (str, none_type,),  # noqa: E501
            'position': (PortPosition,),  # noqa: E501
            'protocol': (str, none_type,),  # noqa: E501
            'resource_uri': (str, none_type,),  # noqa: E501
            'revision': (str, none_type,),  # noqa: E501
            'smart_san': (str, none_type,),  # noqa: E501
            'speed_actual': (str, none_type,),  # noqa: E501
            'speed_configured': (str, none_type,),  # noqa: E501
            'speed_max': (str, none_type,),  # noqa: E501
            'speed_min': (str, none_type,),  # noqa: E501
            'state': (STATE,),  # noqa: E501
            'state_description': (StateDescription,),  # noqa: E501
            'system_id': (str, none_type,),  # noqa: E501
            'tgt_mode_write_opt': (str, none_type,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
            'unique_wwn': (str, none_type,),  # noqa: E501
            'vlans': ([Vlan], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'associated_links': 'associatedLinks',  # noqa: E501
        'card_type': 'cardType',  # noqa: E501
        '_class': 'class',  # noqa: E501
        'class2': 'class2',  # noqa: E501
        'config': 'config',  # noqa: E501
        'config_mode': 'configMode',  # noqa: E501
        'connection_type': 'connectionType',  # noqa: E501
        'customer_id': 'customerId',  # noqa: E501
        'devices': 'devices',  # noqa: E501
        'displayname': 'displayname',  # noqa: E501
        'domain': 'domain',  # noqa: E501
        'failover_status': 'failoverStatus',  # noqa: E501
        'fc_data': 'fcData',  # noqa: E501
        'fw_version': 'fwVersion',  # noqa: E501
        'generation': 'generation',  # noqa: E501
        'id': 'id',  # noqa: E501
        'initiator_ports': 'initiatorPorts',  # noqa: E501
        'interupt_coalesce': 'interuptCoalesce',  # noqa: E501
        'ip_data': 'ipData',  # noqa: E501
        'iscsi_data': 'iscsiData',  # noqa: E501
        'label': 'label',  # noqa: E501
        'manufacturing': 'manufacturing',  # noqa: E501
        'mode': 'mode',  # noqa: E501
        'mode_change': 'modeChange',  # noqa: E501
        'name': 'name',  # noqa: E501
        'node_card_id': 'nodeCardId',  # noqa: E501
        'node_id': 'nodeId',  # noqa: E501
        'partner': 'partner',  # noqa: E501
        'port_sfp': 'portSfp',  # noqa: E501
        'port_type': 'portType',  # noqa: E501
        'position': 'position',  # noqa: E501
        'protocol': 'protocol',  # noqa: E501
        'resource_uri': 'resourceUri',  # noqa: E501
        'revision': 'revision',  # noqa: E501
        'smart_san': 'smartSAN',  # noqa: E501
        'speed_actual': 'speedActual',  # noqa: E501
        'speed_configured': 'speedConfigured',  # noqa: E501
        'speed_max': 'speedMax',  # noqa: E501
        'speed_min': 'speedMin',  # noqa: E501
        'state': 'state',  # noqa: E501
        'state_description': 'stateDescription',  # noqa: E501
        'system_id': 'systemId',  # noqa: E501
        'tgt_mode_write_opt': 'tgtModeWriteOpt',  # noqa: E501
        'type': 'type',  # noqa: E501
        'unique_wwn': 'uniqueWWN',  # noqa: E501
        'vlans': 'vlans',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """PortsList - a model defined in OpenAPI

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
            associated_links (PortsAssociatedLinks): [optional]  # noqa: E501
            card_type (CardType): [optional]  # noqa: E501
            _class (int, none_type): Fibre Channel class (can be either 2 or 3). [optional]  # noqa: E501
            class2 (str, none_type): Class2 state and configuration. [optional]  # noqa: E501
            config (str, none_type): Configuration state of port. [optional]  # noqa: E501
            config_mode (str, none_type): Connection mode of the port. [optional]  # noqa: E501
            connection_type (str, none_type): port connection type. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            devices (ConnectedDevices): [optional]  # noqa: E501
            displayname (str, none_type): Name to be used for display purposes. [optional]  # noqa: E501
            domain (str, none_type): Domain that the resource belongs to. [optional]  # noqa: E501
            failover_status (str, none_type): Failover status of this port and the partner `Filter, Sort`. [optional]  # noqa: E501
            fc_data (PortFC): [optional]  # noqa: E501
            fw_version (str, none_type): Firmware version. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            id (str, none_type): Unique Identifier of the resource `Filter`. [optional]  # noqa: E501
            initiator_ports (InitiatorPort): [optional]  # noqa: E501
            interupt_coalesce (str, none_type): Interupt Coalesce. [optional]  # noqa: E501
            ip_data (PortIP): [optional]  # noqa: E501
            iscsi_data (PortISCSI): [optional]  # noqa: E501
            label (str, none_type): Label `Filter, Sort`. [optional]  # noqa: E501
            manufacturing (ManufacturingSingle): [optional]  # noqa: E501
            mode (str, none_type): Current mode the port is in `Filter, Sort`. [optional]  # noqa: E501
            mode_change (str, none_type): Indicates if the mode change is allowed or prohibited. [optional]  # noqa: E501
            name (str, none_type): Name of the resource `Filter, Sort`. [optional]  # noqa: E501
            node_card_id (str, none_type): Unique Identifier of the node adapter card. [optional]  # noqa: E501
            node_id (str, none_type): Unique Identifier of the node `Filter`. [optional]  # noqa: E501
            partner (Partner): [optional]  # noqa: E501
            port_sfp (PortSfp): [optional]  # noqa: E501
            port_type (str, none_type): Type of the port based on the device it is connected to `Filter, Sort`. [optional]  # noqa: E501
            position (PortPosition): [optional]  # noqa: E501
            protocol (str, none_type): Current protocol the port is in `Filter, Sort`. [optional]  # noqa: E501
            resource_uri (str, none_type): resourceUri for detailed port object. [optional]  # noqa: E501
            revision (str, none_type): Revision of the Host Bus Adapter. [optional]  # noqa: E501
            smart_san (str, none_type): Smart SAN status. [optional]  # noqa: E501
            speed_actual (str, none_type): Actual speed that port is running at  `Filter`. [optional]  # noqa: E501
            speed_configured (str, none_type): Speed that is configured to run as. [optional]  # noqa: E501
            speed_max (str, none_type): Maximum speed that port can run at. [optional]  # noqa: E501
            speed_min (str, none_type): Minimum speed that port can run at. [optional]  # noqa: E501
            state (STATE): [optional]  # noqa: E501
            state_description (StateDescription): [optional]  # noqa: E501
            system_id (str, none_type): SystemUid/SerialNumber of the array.. [optional]  # noqa: E501
            tgt_mode_write_opt (str, none_type): Target mode write optimization setting. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
            unique_wwn (str, none_type): Unique WWN setting. [optional]  # noqa: E501
            vlans ([Vlan], none_type): [optional]  # noqa: E501
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
        """PortsList - a model defined in OpenAPI

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
            associated_links (PortsAssociatedLinks): [optional]  # noqa: E501
            card_type (CardType): [optional]  # noqa: E501
            _class (int, none_type): Fibre Channel class (can be either 2 or 3). [optional]  # noqa: E501
            class2 (str, none_type): Class2 state and configuration. [optional]  # noqa: E501
            config (str, none_type): Configuration state of port. [optional]  # noqa: E501
            config_mode (str, none_type): Connection mode of the port. [optional]  # noqa: E501
            connection_type (str, none_type): port connection type. [optional]  # noqa: E501
            customer_id (str, none_type): customerId. [optional]  # noqa: E501
            devices (ConnectedDevices): [optional]  # noqa: E501
            displayname (str, none_type): Name to be used for display purposes. [optional]  # noqa: E501
            domain (str, none_type): Domain that the resource belongs to. [optional]  # noqa: E501
            failover_status (str, none_type): Failover status of this port and the partner `Filter, Sort`. [optional]  # noqa: E501
            fc_data (PortFC): [optional]  # noqa: E501
            fw_version (str, none_type): Firmware version. [optional]  # noqa: E501
            generation (int, none_type): generation. [optional]  # noqa: E501
            id (str, none_type): Unique Identifier of the resource `Filter`. [optional]  # noqa: E501
            initiator_ports (InitiatorPort): [optional]  # noqa: E501
            interupt_coalesce (str, none_type): Interupt Coalesce. [optional]  # noqa: E501
            ip_data (PortIP): [optional]  # noqa: E501
            iscsi_data (PortISCSI): [optional]  # noqa: E501
            label (str, none_type): Label `Filter, Sort`. [optional]  # noqa: E501
            manufacturing (ManufacturingSingle): [optional]  # noqa: E501
            mode (str, none_type): Current mode the port is in `Filter, Sort`. [optional]  # noqa: E501
            mode_change (str, none_type): Indicates if the mode change is allowed or prohibited. [optional]  # noqa: E501
            name (str, none_type): Name of the resource `Filter, Sort`. [optional]  # noqa: E501
            node_card_id (str, none_type): Unique Identifier of the node adapter card. [optional]  # noqa: E501
            node_id (str, none_type): Unique Identifier of the node `Filter`. [optional]  # noqa: E501
            partner (Partner): [optional]  # noqa: E501
            port_sfp (PortSfp): [optional]  # noqa: E501
            port_type (str, none_type): Type of the port based on the device it is connected to `Filter, Sort`. [optional]  # noqa: E501
            position (PortPosition): [optional]  # noqa: E501
            protocol (str, none_type): Current protocol the port is in `Filter, Sort`. [optional]  # noqa: E501
            resource_uri (str, none_type): resourceUri for detailed port object. [optional]  # noqa: E501
            revision (str, none_type): Revision of the Host Bus Adapter. [optional]  # noqa: E501
            smart_san (str, none_type): Smart SAN status. [optional]  # noqa: E501
            speed_actual (str, none_type): Actual speed that port is running at  `Filter`. [optional]  # noqa: E501
            speed_configured (str, none_type): Speed that is configured to run as. [optional]  # noqa: E501
            speed_max (str, none_type): Maximum speed that port can run at. [optional]  # noqa: E501
            speed_min (str, none_type): Minimum speed that port can run at. [optional]  # noqa: E501
            state (STATE): [optional]  # noqa: E501
            state_description (StateDescription): [optional]  # noqa: E501
            system_id (str, none_type): SystemUid/SerialNumber of the array.. [optional]  # noqa: E501
            tgt_mode_write_opt (str, none_type): Target mode write optimization setting. [optional]  # noqa: E501
            type (str, none_type): type. [optional]  # noqa: E501
            unique_wwn (str, none_type): Unique WWN setting. [optional]  # noqa: E501
            vlans ([Vlan], none_type): [optional]  # noqa: E501
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
