# PortsList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**PortsAssociatedLinks**](PortsAssociatedLinks.md) |  | [optional] 
**card_type** | [**CardType**](CardType.md) |  | [optional] 
**_class** | **int, none_type** | Fibre Channel class (can be either 2 or 3) | [optional] 
**class2** | **str, none_type** | Class2 state and configuration | [optional] 
**config** | **str, none_type** | Configuration state of port | [optional] 
**config_mode** | **str, none_type** | Connection mode of the port | [optional] 
**connection_type** | **str, none_type** | port connection type | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**devices** | [**ConnectedDevices**](ConnectedDevices.md) |  | [optional] 
**displayname** | **str, none_type** | Name to be used for display purposes | [optional] 
**domain** | **str, none_type** | Domain that the resource belongs to | [optional] 
**failover_status** | **str, none_type** | Failover status of this port and the partner &#x60;Filter, Sort&#x60; | [optional] 
**fc_data** | [**PortFC**](PortFC.md) |  | [optional] 
**fw_version** | **str, none_type** | Firmware version | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**id** | **str, none_type** | Unique Identifier of the resource &#x60;Filter&#x60; | [optional] 
**initiator_ports** | [**InitiatorPort**](InitiatorPort.md) |  | [optional] 
**interupt_coalesce** | **str, none_type** | Interupt Coalesce | [optional] 
**ip_data** | [**PortIP**](PortIP.md) |  | [optional] 
**iscsi_data** | [**PortISCSI**](PortISCSI.md) |  | [optional] 
**label** | **str, none_type** | Label &#x60;Filter, Sort&#x60; | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**mode** | **str, none_type** | Current mode the port is in &#x60;Filter, Sort&#x60; | [optional] 
**mode_change** | **str, none_type** | Indicates if the mode change is allowed or prohibited | [optional] 
**name** | **str, none_type** | Name of the resource &#x60;Filter, Sort&#x60; | [optional] 
**node_card_id** | **str, none_type** | Unique Identifier of the node adapter card | [optional] 
**node_id** | **str, none_type** | Unique Identifier of the node &#x60;Filter&#x60; | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**port_sfp** | [**PortSfp**](PortSfp.md) |  | [optional] 
**port_type** | **str, none_type** | Type of the port based on the device it is connected to &#x60;Filter, Sort&#x60; | [optional] 
**position** | [**PortPosition**](PortPosition.md) |  | [optional] 
**protocol** | **str, none_type** | Current protocol the port is in &#x60;Filter, Sort&#x60; | [optional] 
**resource_uri** | **str, none_type** | resourceUri for detailed port object | [optional] 
**revision** | **str, none_type** | Revision of the Host Bus Adapter | [optional] 
**smart_san** | **str, none_type** | Smart SAN status | [optional] 
**speed_actual** | **str, none_type** | Actual speed that port is running at  &#x60;Filter&#x60; | [optional] 
**speed_configured** | **str, none_type** | Speed that is configured to run as | [optional] 
**speed_max** | **str, none_type** | Maximum speed that port can run at | [optional] 
**speed_min** | **str, none_type** | Minimum speed that port can run at | [optional] 
**state** | [**STATE**](STATE.md) |  | [optional] 
**state_description** | [**StateDescription**](StateDescription.md) |  | [optional] 
**system_id** | **str, none_type** | SystemUid/SerialNumber of the array. | [optional] 
**tgt_mode_write_opt** | **str, none_type** | Target mode write optimization setting | [optional] 
**type** | **str, none_type** | type | [optional] 
**unique_wwn** | **str, none_type** | Unique WWN setting | [optional] 
**vlans** | [**[Vlan], none_type**](Vlan.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

