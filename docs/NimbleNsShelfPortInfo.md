# NimbleNsShelfPortInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_errors** | **str, none_type** | Comma separated list of integers to indicate error conditions. | [optional] 
**port_idx** | **int, none_type** | Index of the port, starting from 0. | [optional] 
**port_name** | **str, none_type** | Name of the port. | [optional] 
**port_status** | **str, none_type** | Status of the port. Possible values:&#39;connected&#39;, &#39;disconnected&#39;, &#39;unknown&#39;,&#39;disabled&#39;. | [optional] 
**port_type** | **str, none_type** | Type of the sas port (e.g. upstream/downstream). Possible values:&#39;upstream&#39;, &#39;downstream&#39;, &#39;unknown&#39;. | [optional] 
**remote_loc_id** | **int, none_type** | The location ID of the controller that connects to this port. | [optional] 
**remote_port_id** | **int, none_type** | The pord_id of the remote SAS port that connects to this port. | [optional] 
**remote_sas_addr** | **str, none_type** | SAS address for the connected. | [optional] 
**remote_sas_domain** | **str, none_type** | The sas domain (A or B side) it connects to. Possible values:&#39;A&#39;, &#39;B&#39;, &#39;unknown&#39;. | [optional] 
**remote_sas_phy_id** | **str, none_type** | Comma separated list of phy ids that this port connects to. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


