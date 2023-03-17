# greenlake-data-services.SystemSettingsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_trusted_certificates**](SystemSettingsApi.md#add_trusted_certificates) | **POST** /api/v1/storage-systems/device-type1/{systemId}/trust-certificates | Add trusted certificates for storage system Primera / Alletra 9K identified by {systemId}
[**alert_contacts_create**](SystemSettingsApi.md#alert_contacts_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/alert-contacts | Add Alert/Mail contact details
[**alert_contacts_delete**](SystemSettingsApi.md#alert_contacts_delete) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/alert-contacts/{id} | Delete Alert/Email contact of storage system Primera / Alletra 9K identified by {id}
[**alert_contacts_update**](SystemSettingsApi.md#alert_contacts_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/alert-contacts/{id} | Edit Alert/Email contact details of storage system Primera / Alletra 9K identified by {id}
[**device_type1_alert_contacts_get_by_id**](SystemSettingsApi.md#device_type1_alert_contacts_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/alert-contacts/{id} | Get alert-contact details for a storage system Primera / Alletra 9K identified by {id}
[**device_type1_alert_contacts_list**](SystemSettingsApi.md#device_type1_alert_contacts_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/alert-contacts | Get alert-contact details for a storage system Primera / Alletra 9K
[**device_type1_certificates_get_by_id**](SystemSettingsApi.md#device_type1_certificates_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/certificates/{id} | Get array certificates by Primera / Alletra 9K identified by {id}
[**device_type1_certificates_list**](SystemSettingsApi.md#device_type1_certificates_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/certificates | Get array certificates by Primera / Alletra 9K
[**device_type1_delete_quorum_witness**](SystemSettingsApi.md#device_type1_delete_quorum_witness) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/system-settings/quorum-witness/{replicationPartnerId} | Delete quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_delete_v_center_settings**](SystemSettingsApi.md#device_type1_delete_v_center_settings) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/vm-manager-settings/{vcenterSettingId} | Delete vcenter setting identified by {vcenterSettingId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_get_quorum_witness**](SystemSettingsApi.md#device_type1_get_quorum_witness) | **GET** /api/v1/storage-systems/device-type1/{systemId}/system-settings/quorum-witness | Get quorum witness configuration details from storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_get_quorum_witness_with_id**](SystemSettingsApi.md#device_type1_get_quorum_witness_with_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/system-settings/quorum-witness/{replicationPartnerId} | Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_get_replication_partner_with_id**](SystemSettingsApi.md#device_type1_get_replication_partner_with_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/system-settings/replication-partners/{replicationPartnerId} | Get details of replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_get_replication_partners**](SystemSettingsApi.md#device_type1_get_replication_partners) | **GET** /api/v1/storage-systems/device-type1/{systemId}/system-settings/replication-partners | Get details of replication partners on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_mail_settings_get**](SystemSettingsApi.md#device_type1_mail_settings_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/mail-settings | Get the system&#39;s SMTP/Mail server settigs
[**device_type1_network_service_cim_get**](SystemSettingsApi.md#device_type1_network_service_cim_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/network-services/cim | Get CIM Network-Service details for a storage system Primera / Alletra 9K
[**device_type1_network_service_snmp_mgr_get_by_id**](SystemSettingsApi.md#device_type1_network_service_snmp_mgr_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/network-services/snmp-mgr/{id} | Get a specific SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K
[**device_type1_network_service_snmp_mgr_list**](SystemSettingsApi.md#device_type1_network_service_snmp_mgr_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/network-services/snmp-mgr | Get SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K
[**device_type1_network_service_vasa_configure**](SystemSettingsApi.md#device_type1_network_service_vasa_configure) | **POST** /api/v1/storage-systems/device-type1/{systemId}/network-services/vasa/{vasaId} | Configures vasa service for the specified id.
[**device_type1_network_service_vasa_get**](SystemSettingsApi.md#device_type1_network_service_vasa_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/network-services/vasa | Get VASA Network-Service details for a storage system Primera / Alletra 9K
[**device_type1_network_settings_get**](SystemSettingsApi.md#device_type1_network_settings_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/network-settings | Get Network-Settings details for a storage system Primera / Alletra 9K
[**device_type1_node_service_ports_get_by_id**](SystemSettingsApi.md#device_type1_node_service_ports_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/service-ports | Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId} and {nodeId }
[**device_type1_node_service_ports_list**](SystemSettingsApi.md#device_type1_node_service_ports_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/service-ports | Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId}
[**device_type1_post_quorum_witness**](SystemSettingsApi.md#device_type1_post_quorum_witness) | **POST** /api/v1/storage-systems/device-type1/{systemId}/system-settings/quorum-witness | Create quorum witness on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_post_remove_replication_partners**](SystemSettingsApi.md#device_type1_post_remove_replication_partners) | **POST** /api/v1/storage-systems/device-type1/{systemId}/system-settings/replication-partners/remove | Delete replication partner from storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_post_replication_partners**](SystemSettingsApi.md#device_type1_post_replication_partners) | **POST** /api/v1/storage-systems/device-type1/{systemId}/system-settings/replication-partners | Create replication partners on Primera / Alletra 9K identified by {systemId}
[**device_type1_post_v_center_settings**](SystemSettingsApi.md#device_type1_post_v_center_settings) | **POST** /api/v1/storage-systems/device-type1/{systemId}/vm-manager-settings | Add vCenter settings to storage system Primera / Alletra 9K
[**device_type1_put_quorum_witness**](SystemSettingsApi.md#device_type1_put_quorum_witness) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/system-settings/quorum-witness/{replicationPartnerId} | Edit quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_put_replication_partner**](SystemSettingsApi.md#device_type1_put_replication_partner) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/system-settings/replication-partners/{replicationPartnerId} | Edit replication partner identified by {replicationPartnerId} on Primera / Alletra 9K identified by {systemId}
[**device_type1_put_v_center_settings**](SystemSettingsApi.md#device_type1_put_v_center_settings) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/vm-manager-settings/{vcenterSettingId} | Edit vCenter setting identified by {vcenterSettingId} on Primera / Alletra 9K identified by {systemId}
[**device_type1_support_data_collect**](SystemSettingsApi.md#device_type1_support_data_collect) | **POST** /api/v1/storage-systems/device-type1/{systemId}/collect-support-data | Trigger a collection on the storage system Primera / Alletra 9K
[**device_type1_support_settings_get**](SystemSettingsApi.md#device_type1_support_settings_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/support-settings | Get support settings for a storage system Primera / Alletra 9K
[**device_type1_system_settings_list**](SystemSettingsApi.md#device_type1_system_settings_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/system-settings | Get the system settings configuration details
[**device_type1_telemetry_get**](SystemSettingsApi.md#device_type1_telemetry_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/telemetry | Get telemetry status for a storage system Primera / Alletra 9K
[**device_type1_trusted_certificates_get_by_id**](SystemSettingsApi.md#device_type1_trusted_certificates_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/trust-certificates/{id} | Get certificates trusted by Primera / Alletra 9K identified by {id}
[**device_type1_trusted_certificates_list**](SystemSettingsApi.md#device_type1_trusted_certificates_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/trust-certificates | Get certificates trusted by Primera / Alletra 9K
[**device_type1_vm_manager_settings_get_by_id**](SystemSettingsApi.md#device_type1_vm_manager_settings_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/vm-manager-settings/{vcenterSettingId} | Get vcenter setting detail for a given vcenter setting of a storage system Primera / Alletra 9K
[**device_type1_vm_manager_settings_list**](SystemSettingsApi.md#device_type1_vm_manager_settings_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/vm-manager-settings | Get vcenter settings for a storage system Primera / Alletra 9K
[**device_type2_application_server_create**](SystemSettingsApi.md#device_type2_application_server_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/application-servers | Create Nimble / Alletra 6K application server in system identified by {systemId}
[**device_type2_application_server_edit**](SystemSettingsApi.md#device_type2_application_server_edit) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/application-servers/{applicationServerId} | Modify Nimble / Alletra 6K application server in system identified by {systemId}
[**device_type2_create_replication_partners**](SystemSettingsApi.md#device_type2_create_replication_partners) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners | Create replication partner pair for Nimble / Alletra 6K
[**device_type2_create_witness**](SystemSettingsApi.md#device_type2_create_witness) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/witnesses | Create a new witness configuration Nimble / Alletra 6K
[**device_type2_edit_mail_settings**](SystemSettingsApi.md#device_type2_edit_mail_settings) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/mail-settings | Edit Nimble Mail Settings of Nimble / Alletra 6K
[**device_type2_edit_network_setting_by_id**](SystemSettingsApi.md#device_type2_edit_network_setting_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/network-settings/{networkSettingId} | Edit Nimble / Alletra 6K network setting identified by {networkSettingId}
[**device_type2_edit_replication_partners_by_id**](SystemSettingsApi.md#device_type2_edit_replication_partners_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners/{replicationpartnerId} | Edit a replication partner for Nimble / Alletra 6K given by replicationpartnerId
[**device_type2_edit_system_settings**](SystemSettingsApi.md#device_type2_edit_system_settings) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/system-settings | Edit system settings of Nimble / Alletra 6K
[**device_type2_get_all_application_servers**](SystemSettingsApi.md#device_type2_get_all_application_servers) | **GET** /api/v1/storage-systems/device-type2/{systemId}/application-servers | Get all application servers details by Nimble / Alletra 6K
[**device_type2_get_all_network_settings**](SystemSettingsApi.md#device_type2_get_all_network_settings) | **GET** /api/v1/storage-systems/device-type2/{systemId}/network-settings | Get all network settings details by Nimble / Alletra 6K
[**device_type2_get_application_server_by_id**](SystemSettingsApi.md#device_type2_get_application_server_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/application-servers/{applicationServerId} | Get details of Nimble / Alletra 6K application server identified by {applicationServerId}
[**device_type2_get_network_setting_by_id**](SystemSettingsApi.md#device_type2_get_network_setting_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/network-settings/{networkSettingId} | Get details of Nimble / Alletra 6K network setting identified by {networkSettingId}
[**device_type2_get_replication_partners**](SystemSettingsApi.md#device_type2_get_replication_partners) | **GET** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners | Get all replication-partners details for Nimble / Alletra 6K
[**device_type2_get_replication_partners_by_id**](SystemSettingsApi.md#device_type2_get_replication_partners_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners/{replicationpartnerId} | Get details of Nimble / Alletra 6K replication-partner identified by {replicationpartnerId}
[**device_type2_get_witnesses**](SystemSettingsApi.md#device_type2_get_witnesses) | **GET** /api/v1/storage-systems/device-type2/{systemId}/system-settings/witnesses | Get all witness configuration details by Nimble / Alletra 6K
[**device_type2_get_witnesses_by_id**](SystemSettingsApi.md#device_type2_get_witnesses_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/system-settings/witnesses/{witnessId} | Get details of Nimble / Alletra 6K witness configuration identified by {witnessId}
[**device_type2_pause_replication_partner**](SystemSettingsApi.md#device_type2_pause_replication_partner) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners/actions/pause | Pause the replication pair of Nimble / Alletra 6K
[**device_type2_remove_application_server_by_id**](SystemSettingsApi.md#device_type2_remove_application_server_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/application-servers/{applicationServerId} | Remove application server identified by {applicationServerId} from Nimble / Alletra 6K
[**device_type2_remove_replication_partner**](SystemSettingsApi.md#device_type2_remove_replication_partner) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners/remove | Remove list of replication partner for Nimble / Alletra 6K
[**device_type2_remove_witnesses_by_id**](SystemSettingsApi.md#device_type2_remove_witnesses_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/system-settings/witnesses/{witnessId} | Remove witness identified by {witnessId} from Nimble / Alletra 6K
[**device_type2_resume_replication_partner**](SystemSettingsApi.md#device_type2_resume_replication_partner) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners/actions/resume | Resume the replication pair of Nimble / Alletra 6K
[**device_type2_send_auto_support**](SystemSettingsApi.md#device_type2_send_auto_support) | **POST** /api/v1/storage-systems/device-type2/{systemId}/autosupport/actions/send | Send auto support information of Nimble / Alletra 6K identified by {systemId}
[**device_type2_test_replication_configuration**](SystemSettingsApi.md#device_type2_test_replication_configuration) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/replication-partners/actions/test | Test the replication partner pair of Nimble / Alletra 6K
[**device_type2_test_witnesses_by_id**](SystemSettingsApi.md#device_type2_test_witnesses_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/system-settings/witnesses/{witnessId}/actions/test | Test and validate the witness configuration between the host identified by {witnessId} from Nimble / Alletra 6K identified by {systemId}
[**mail_settings_associate**](SystemSettingsApi.md#mail_settings_associate) | **POST** /api/v1/storage-systems/device-type1/{systemId}/mail-settings | Add SMTP/Mail server settigs
[**mail_settings_delete**](SystemSettingsApi.md#mail_settings_delete) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/mail-settings | Delete SMTP/mail server settings
[**mail_settings_update**](SystemSettingsApi.md#mail_settings_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/mail-settings | Edit SMTP/Mail server settigs
[**network_service_cim_update**](SystemSettingsApi.md#network_service_cim_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/network-services/cim | Edit CIM network service configuration
[**network_service_snmp_mgr_create**](SystemSettingsApi.md#network_service_snmp_mgr_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/network-services/snmp-mgr | Add SNMP Manager settings
[**network_service_snmp_mgr_delete**](SystemSettingsApi.md#network_service_snmp_mgr_delete) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/network-services/snmp-mgr/{id} | Delete SNMP manager settings identified by {id}
[**network_service_snmp_mgr_update**](SystemSettingsApi.md#network_service_snmp_mgr_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/network-services/snmp-mgr/{id} | Edit SNMP Manager settings for the specified Id
[**network_settings_associate**](SystemSettingsApi.md#network_settings_associate) | **POST** /api/v1/storage-systems/device-type1/{systemId}/network-settings | Post Network-Settings details for a storage system Primera / Alletra 9K
[**post_certificate**](SystemSettingsApi.md#post_certificate) | **POST** /api/v1/storage-systems/device-type1/{systemId}/certificates | Create certificate on storage system Primera / Alletra 9K identified by {systemId}
[**put_certificate**](SystemSettingsApi.md#put_certificate) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/certificates/{id} | Import certificate identified by {id} on storage system Primera / Alletra 9K identified by {systemId}
[**remove_certificates**](SystemSettingsApi.md#remove_certificates) | **POST** /api/v1/storage-systems/device-type1/{systemId}/certificates/remove | Delete certificates from storage system Primera / Alletra 9K identified by {systemId}
[**remove_trusted_certificates**](SystemSettingsApi.md#remove_trusted_certificates) | **POST** /api/v1/storage-systems/device-type1/{systemId}/trust-certificates/remove | Delete trusted certificates from storage system Primera / Alletra 9K identified by {systemId}
[**support_settings_associate**](SystemSettingsApi.md#support_settings_associate) | **POST** /api/v1/storage-systems/device-type1/{systemId}/support-settings | Add support settings for a storage system Primera / Alletra 9K
[**support_settings_update**](SystemSettingsApi.md#support_settings_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/support-settings | Edit support settings for a storage system Primera / Alletra 9K
[**system_settings_associate**](SystemSettingsApi.md#system_settings_associate) | **POST** /api/v1/storage-systems/device-type1/{systemId}/system-settings | Edit system settings configuration
[**system_settings_update**](SystemSettingsApi.md#system_settings_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/system-settings | Edit system settings configuration


# **add_trusted_certificates**
> TaskResponse add_trusted_certificates(system_id, add_trusted_certificate_input)

Add trusted certificates for storage system Primera / Alletra 9K identified by {systemId}

Add trusted certificates for storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
add_trusted_certificate_input = greenlake-data-services.AddTrustedCertificateInput() # AddTrustedCertificateInput | 

try:
    # Add trusted certificates for storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.add_trusted_certificates(system_id, add_trusted_certificate_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->add_trusted_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **add_trusted_certificate_input** | [**AddTrustedCertificateInput**](AddTrustedCertificateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_contacts_create**
> TaskResponse alert_contacts_create(system_id, alert_contact_input)

Add Alert/Mail contact details

Add Alert/Mail contact details

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
alert_contact_input = greenlake-data-services.AlertContactInput() # AlertContactInput | 

try:
    # Add Alert/Mail contact details
    api_response = api_instance.alert_contacts_create(system_id, alert_contact_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->alert_contacts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **alert_contact_input** | [**AlertContactInput**](AlertContactInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_contacts_delete**
> TaskResponse alert_contacts_delete(system_id, id)

Delete Alert/Email contact of storage system Primera / Alletra 9K identified by {id}

Delete Alert/Email contact of storage system Primera / Alletra 9K identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | Unique Identifier of the alert contact

try:
    # Delete Alert/Email contact of storage system Primera / Alletra 9K identified by {id}
    api_response = api_instance.alert_contacts_delete(system_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->alert_contacts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| Unique Identifier of the alert contact | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_contacts_update**
> TaskResponse alert_contacts_update(system_id, id, alert_contact_input)

Edit Alert/Email contact details of storage system Primera / Alletra 9K identified by {id}

Edit Alert/Email contact details of storage system Primera / Alletra 9K identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | Unique Identifier of the alert contact
alert_contact_input = greenlake-data-services.AlertContactInput() # AlertContactInput | 

try:
    # Edit Alert/Email contact details of storage system Primera / Alletra 9K identified by {id}
    api_response = api_instance.alert_contacts_update(system_id, id, alert_contact_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->alert_contacts_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| Unique Identifier of the alert contact | 
 **alert_contact_input** | [**AlertContactInput**](AlertContactInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_alert_contacts_get_by_id**
> AlertContactsDetailsList device_type1_alert_contacts_get_by_id(system_id, id, select=select)

Get alert-contact details for a storage system Primera / Alletra 9K identified by {id}

Get alert-contact details for a storage system Primera / Alletra 9K identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | Unique Identifier of the alert contact
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get alert-contact details for a storage system Primera / Alletra 9K identified by {id}
    api_response = api_instance.device_type1_alert_contacts_get_by_id(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_alert_contacts_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| Unique Identifier of the alert contact | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**AlertContactsDetailsList**](AlertContactsDetailsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_alert_contacts_list**
> AlertContacts device_type1_alert_contacts_list(system_id, limit=limit, offset=offset, select=select)

Get alert-contact details for a storage system Primera / Alletra 9K

Get alert-contact details for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get alert-contact details for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_alert_contacts_list(system_id, limit=limit, offset=offset, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_alert_contacts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**AlertContacts**](AlertContacts.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_certificates_get_by_id**
> CertificateDetails device_type1_certificates_get_by_id(system_id, id, select=select)

Get array certificates by Primera / Alletra 9K identified by {id}

Get array certificates by Primera / Alletra 9K identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | ID of the certificate
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get array certificates by Primera / Alletra 9K identified by {id}
    api_response = api_instance.device_type1_certificates_get_by_id(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_certificates_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| ID of the certificate | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**CertificateDetails**](CertificateDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_certificates_list**
> CertificatesSummaryList device_type1_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)

Get array certificates by Primera / Alletra 9K

Get array certificates by Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter Certificates by Key. (optional)

try:
    # Get array certificates by Primera / Alletra 9K
    api_response = api_instance.device_type1_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_certificates_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Certificates by Key. | [optional] 

### Return type

[**CertificatesSummaryList**](CertificatesSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_delete_quorum_witness**
> TaskResponse device_type1_delete_quorum_witness(system_id, replication_partner_id)

Delete quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

Delete quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
replication_partner_id = 'replication_partner_id_example' # str | id of device-type1 replication partner

try:
    # Delete quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_delete_quorum_witness(system_id, replication_partner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_delete_quorum_witness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_delete_v_center_settings**
> TaskResponse device_type1_delete_v_center_settings(system_id, vcenter_setting_id)

Delete vcenter setting identified by {vcenterSettingId} on storage system Primera / Alletra 9K identified by {systemId}

Delete vcenter setting identified by {vcenterSettingId} on storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
vcenter_setting_id = 'vcenter_setting_id_example' # str | UID(vcenterSettingId) of the storage system

try:
    # Delete vcenter setting identified by {vcenterSettingId} on storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_delete_v_center_settings(system_id, vcenter_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_delete_v_center_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **vcenter_setting_id** | **str**| UID(vcenterSettingId) of the storage system | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_quorum_witness**
> WitnessList device_type1_get_quorum_witness(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get quorum witness configuration details from storage system Primera / Alletra 9K identified by {systemId}

Get quorum witness configuration details from storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter witness by key. (optional)
sort = 'sort_example' # str | oData query to sort witness resource by key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get quorum witness configuration details from storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_get_quorum_witness(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_get_quorum_witness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter witness by key. | [optional] 
 **sort** | **str**| oData query to sort witness resource by key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**WitnessList**](WitnessList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_quorum_witness_with_id**
> WitnessDetails device_type1_get_quorum_witness_with_id(system_id, replication_partner_id, select=select)

Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
replication_partner_id = 'replication_partner_id_example' # str | id of device-type1 replication partner
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_get_quorum_witness_with_id(system_id, replication_partner_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_get_quorum_witness_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**WitnessDetails**](WitnessDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_replication_partner_with_id**
> ReplicationPartnerDetails device_type1_get_replication_partner_with_id(system_id, replication_partner_id, select=select)

Get details of replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

Get details of replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
replication_partner_id = 'replication_partner_id_example' # str | id of device-type1 replication partner
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_get_replication_partner_with_id(system_id, replication_partner_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_get_replication_partner_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ReplicationPartnerDetails**](ReplicationPartnerDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_replication_partners**
> ReplicationPartnersList device_type1_get_replication_partners(system_id, limit=limit, offset=offset, filter=filter, sort=sort, include_indirect_partners=include_indirect_partners, select=select)

Get details of replication partners on storage system Primera / Alletra 9K identified by {systemId}

Get details of replication partners on storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter replication partners by key. (optional)
sort = 'sort_example' # str | oData query to sort nodes resource by key. (optional)
include_indirect_partners = True # bool | Include indirect partners. Indirect partners are excluded by default. This parameter cannot be used with other query parameters. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of replication partners on storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_get_replication_partners(system_id, limit=limit, offset=offset, filter=filter, sort=sort, include_indirect_partners=include_indirect_partners, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_get_replication_partners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter replication partners by key. | [optional] 
 **sort** | **str**| oData query to sort nodes resource by key. | [optional] 
 **include_indirect_partners** | **bool**| Include indirect partners. Indirect partners are excluded by default. This parameter cannot be used with other query parameters. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ReplicationPartnersList**](ReplicationPartnersList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_mail_settings_get**
> Mailsettings device_type1_mail_settings_get(system_id, select=select)

Get the system's SMTP/Mail server settigs

Get the system's SMTP/Mail server settigs

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get the system's SMTP/Mail server settigs
    api_response = api_instance.device_type1_mail_settings_get(system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_mail_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**Mailsettings**](Mailsettings.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_cim_get**
> NetworkServicesCim device_type1_network_service_cim_get(system_id, select=select)

Get CIM Network-Service details for a storage system Primera / Alletra 9K

Get CIM Network-Service details for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get CIM Network-Service details for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_network_service_cim_get(system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_network_service_cim_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NetworkServicesCim**](NetworkServicesCim.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_snmp_mgr_get_by_id**
> NetworkServicesSnmp device_type1_network_service_snmp_mgr_get_by_id(system_id, id, select=select)

Get a specific SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K

Get a specific SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | ID of the SNMP manager
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get a specific SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_network_service_snmp_mgr_get_by_id(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_network_service_snmp_mgr_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| ID of the SNMP manager | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NetworkServicesSnmp**](NetworkServicesSnmp.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_snmp_mgr_list**
> NetworkServicesSnmp device_type1_network_service_snmp_mgr_list(system_id, limit=limit, offset=offset, select=select)

Get SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K

Get SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_network_service_snmp_mgr_list(system_id, limit=limit, offset=offset, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_network_service_snmp_mgr_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NetworkServicesSnmp**](NetworkServicesSnmp.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_vasa_configure**
> TaskResponse device_type1_network_service_vasa_configure(system_id, vasa_id, vasa_config)

Configures vasa service for the specified id.

Enables or disable vasa service  on a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
vasa_id = 'vasa_id_example' # str | ID of the VASA service
vasa_config = greenlake-data-services.VasaConfig() # VasaConfig | 

try:
    # Configures vasa service for the specified id.
    api_response = api_instance.device_type1_network_service_vasa_configure(system_id, vasa_id, vasa_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_network_service_vasa_configure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **vasa_id** | **str**| ID of the VASA service | 
 **vasa_config** | [**VasaConfig**](VasaConfig.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_vasa_get**
> NetworkServicesVasa device_type1_network_service_vasa_get(system_id, select=select)

Get VASA Network-Service details for a storage system Primera / Alletra 9K

Get VASA Network-Service details for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get VASA Network-Service details for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_network_service_vasa_get(system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_network_service_vasa_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NetworkServicesVasa**](NetworkServicesVasa.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_settings_get**
> NetworkSettings device_type1_network_settings_get(system_id, select=select)

Get Network-Settings details for a storage system Primera / Alletra 9K

Get Network-Settings details for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get Network-Settings details for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_network_settings_get(system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_network_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NetworkSettings**](NetworkSettings.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_node_service_ports_get_by_id**
> ServicePortsList device_type1_node_service_ports_get_by_id(node_id, system_id, limit=limit, offset=offset, filter=filter, select=select)

Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId} and {nodeId }

Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId} and {nodeId }

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
node_id = 'node_id_example' # str | Primary ID of the node
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter systems by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId} and {nodeId }
    api_response = api_instance.device_type1_node_service_ports_get_by_id(node_id, system_id, limit=limit, offset=offset, filter=filter, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_node_service_ports_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Primary ID of the node | 
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter systems by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ServicePortsList**](ServicePortsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_node_service_ports_list**
> ServicePortsList device_type1_node_service_ports_list(system_id, limit=limit, offset=offset, filter=filter, select=select)

Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId}

Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter systems by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_node_service_ports_list(system_id, limit=limit, offset=offset, filter=filter, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_node_service_ports_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter systems by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ServicePortsList**](ServicePortsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_post_quorum_witness**
> TaskResponse device_type1_post_quorum_witness(system_id, create_quorum_witness_input)

Create quorum witness on storage system Primera / Alletra 9K identified by {systemId}

Create quorum witness on storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
create_quorum_witness_input = greenlake-data-services.CreateQuorumWitnessInput() # CreateQuorumWitnessInput | 

try:
    # Create quorum witness on storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_post_quorum_witness(system_id, create_quorum_witness_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_post_quorum_witness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **create_quorum_witness_input** | [**CreateQuorumWitnessInput**](CreateQuorumWitnessInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_post_remove_replication_partners**
> TaskResponse device_type1_post_remove_replication_partners(system_id, remove_replication_partners_input)

Delete replication partner from storage system Primera / Alletra 9K identified by {systemId}

Delete replication partner from storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
remove_replication_partners_input = greenlake-data-services.RemoveReplicationPartnersInput() # RemoveReplicationPartnersInput | 

try:
    # Delete replication partner from storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_post_remove_replication_partners(system_id, remove_replication_partners_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_post_remove_replication_partners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **remove_replication_partners_input** | [**RemoveReplicationPartnersInput**](RemoveReplicationPartnersInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_post_replication_partners**
> TaskResponse device_type1_post_replication_partners(system_id, create_replication_partners_input)

Create replication partners on Primera / Alletra 9K identified by {systemId}

Create replication partners on Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
create_replication_partners_input = greenlake-data-services.CreateReplicationPartnersInput() # CreateReplicationPartnersInput | 

try:
    # Create replication partners on Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_post_replication_partners(system_id, create_replication_partners_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_post_replication_partners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **create_replication_partners_input** | [**CreateReplicationPartnersInput**](CreateReplicationPartnersInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_post_v_center_settings**
> TaskResponse device_type1_post_v_center_settings(system_id, v_center_settings_input)

Add vCenter settings to storage system Primera / Alletra 9K

Add vCenter settings to storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
v_center_settings_input = greenlake-data-services.VCenterSettingsInput() # VCenterSettingsInput | 

try:
    # Add vCenter settings to storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_post_v_center_settings(system_id, v_center_settings_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_post_v_center_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **v_center_settings_input** | [**VCenterSettingsInput**](VCenterSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_put_quorum_witness**
> TaskResponse device_type1_put_quorum_witness(system_id, replication_partner_id, edit_quorum_witness_input)

Edit quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

Edit quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
replication_partner_id = 'replication_partner_id_example' # str | id of device-type1 replication partner
edit_quorum_witness_input = greenlake-data-services.EditQuorumWitnessInput() # EditQuorumWitnessInput | 

try:
    # Edit quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_put_quorum_witness(system_id, replication_partner_id, edit_quorum_witness_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_put_quorum_witness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **edit_quorum_witness_input** | [**EditQuorumWitnessInput**](EditQuorumWitnessInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_put_replication_partner**
> TaskResponse device_type1_put_replication_partner(system_id, replication_partner_id, edit_replication_partner_input)

Edit replication partner identified by {replicationPartnerId} on Primera / Alletra 9K identified by {systemId}

Edit replication partner identified by {replicationPartnerId} on Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
replication_partner_id = 'replication_partner_id_example' # str | id of device-type1 replication partner
edit_replication_partner_input = greenlake-data-services.EditReplicationPartnerInput() # EditReplicationPartnerInput | 

try:
    # Edit replication partner identified by {replicationPartnerId} on Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_put_replication_partner(system_id, replication_partner_id, edit_replication_partner_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_put_replication_partner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **edit_replication_partner_input** | [**EditReplicationPartnerInput**](EditReplicationPartnerInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_put_v_center_settings**
> TaskResponse device_type1_put_v_center_settings(system_id, vcenter_setting_id, edit_v_center_settings_input)

Edit vCenter setting identified by {vcenterSettingId} on Primera / Alletra 9K identified by {systemId}

Edit vCenter setting identified by {vcenterSettingId} on Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
vcenter_setting_id = 'vcenter_setting_id_example' # str | UID(vcenterSettingId) of the storage system
edit_v_center_settings_input = greenlake-data-services.EditVCenterSettingsInput() # EditVCenterSettingsInput | 

try:
    # Edit vCenter setting identified by {vcenterSettingId} on Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_put_v_center_settings(system_id, vcenter_setting_id, edit_v_center_settings_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_put_v_center_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **vcenter_setting_id** | **str**| UID(vcenterSettingId) of the storage system | 
 **edit_v_center_settings_input** | [**EditVCenterSettingsInput**](EditVCenterSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_support_data_collect**
> TaskResponse device_type1_support_data_collect(system_id, collect_support_data_input)

Trigger a collection on the storage system Primera / Alletra 9K

Trigger a collection on the storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
collect_support_data_input = NULL # list[CollectSupportDataInput] | 

try:
    # Trigger a collection on the storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_support_data_collect(system_id, collect_support_data_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_support_data_collect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **collect_support_data_input** | [**list[CollectSupportDataInput]**](list.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_support_settings_get**
> SupportSetting device_type1_support_settings_get(system_id, select=select)

Get support settings for a storage system Primera / Alletra 9K

Get support settings for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get support settings for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_support_settings_get(system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_support_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**SupportSetting**](SupportSetting.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_settings_list**
> SystemConfigParams device_type1_system_settings_list(system_id, select=select)

Get the system settings configuration details

Get the system settings configuration details

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get the system settings configuration details
    api_response = api_instance.device_type1_system_settings_list(system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_system_settings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**SystemConfigParams**](SystemConfigParams.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_telemetry_get**
> TelemetryStatus device_type1_telemetry_get(system_id, select=select)

Get telemetry status for a storage system Primera / Alletra 9K

Get telemetry status for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get telemetry status for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_telemetry_get(system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_telemetry_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**TelemetryStatus**](TelemetryStatus.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_trusted_certificates_get_by_id**
> TrustedCertificateDetails device_type1_trusted_certificates_get_by_id(system_id, id, select=select)

Get certificates trusted by Primera / Alletra 9K identified by {id}

Get certificates trusted by Primera / Alletra 9K identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | ID of the certificate
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get certificates trusted by Primera / Alletra 9K identified by {id}
    api_response = api_instance.device_type1_trusted_certificates_get_by_id(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_trusted_certificates_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| ID of the certificate | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**TrustedCertificateDetails**](TrustedCertificateDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_trusted_certificates_list**
> TrustedCertificatesSummaryList device_type1_trusted_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)

Get certificates trusted by Primera / Alletra 9K

Get certificates trusted by Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter Certificates by Key. (optional)

try:
    # Get certificates trusted by Primera / Alletra 9K
    api_response = api_instance.device_type1_trusted_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_trusted_certificates_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Certificates by Key. | [optional] 

### Return type

[**TrustedCertificatesSummaryList**](TrustedCertificatesSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vm_manager_settings_get_by_id**
> VcenterSettingDetail device_type1_vm_manager_settings_get_by_id(system_id, vcenter_setting_id, select=select)

Get vcenter setting detail for a given vcenter setting of a storage system Primera / Alletra 9K

Get vcenter setting detail for a given vcenter setting of a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
vcenter_setting_id = 'vcenter_setting_id_example' # str | UID(vcenterSettingId) of the storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get vcenter setting detail for a given vcenter setting of a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_vm_manager_settings_get_by_id(system_id, vcenter_setting_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_vm_manager_settings_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **vcenter_setting_id** | **str**| UID(vcenterSettingId) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**VcenterSettingDetail**](VcenterSettingDetail.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vm_manager_settings_list**
> VcenterSettingsSumarryList device_type1_vm_manager_settings_list(system_id, select=select, limit=limit, offset=offset)

Get vcenter settings for a storage system Primera / Alletra 9K

Get vcenter settings for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)

try:
    # Get vcenter settings for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_vm_manager_settings_list(system_id, select=select, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type1_vm_manager_settings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 

### Return type

[**VcenterSettingsSumarryList**](VcenterSettingsSumarryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_application_server_create**
> TaskResponse device_type2_application_server_create(system_id, create_application_server)

Create Nimble / Alletra 6K application server in system identified by {systemId}

Create Nimble / Alletra 6K application server in system identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
create_application_server = greenlake-data-services.CreateApplicationServer() # CreateApplicationServer | 

try:
    # Create Nimble / Alletra 6K application server in system identified by {systemId}
    api_response = api_instance.device_type2_application_server_create(system_id, create_application_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_application_server_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **create_application_server** | [**CreateApplicationServer**](CreateApplicationServer.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_application_server_edit**
> TaskResponse device_type2_application_server_edit(system_id, application_server_id, edit_application_server)

Modify Nimble / Alletra 6K application server in system identified by {systemId}

Modify Nimble / Alletra 6K application server in system identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
application_server_id = 'application_server_id_example' # str | Identifier of application server. A 42 digit hexadecimal number.
edit_application_server = greenlake-data-services.EditApplicationServer() # EditApplicationServer | 

try:
    # Modify Nimble / Alletra 6K application server in system identified by {systemId}
    api_response = api_instance.device_type2_application_server_edit(system_id, application_server_id, edit_application_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_application_server_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **application_server_id** | **str**| Identifier of application server. A 42 digit hexadecimal number. | 
 **edit_application_server** | [**EditApplicationServer**](EditApplicationServer.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_create_replication_partners**
> TaskResponse device_type2_create_replication_partners(system_id, nimble_create_replication_partner_input)

Create replication partner pair for Nimble / Alletra 6K

Create replication partner pair for Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_replication_partner_input = greenlake-data-services.NimbleCreateReplicationPartnerInput() # NimbleCreateReplicationPartnerInput | 

try:
    # Create replication partner pair for Nimble / Alletra 6K
    api_response = api_instance.device_type2_create_replication_partners(system_id, nimble_create_replication_partner_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_create_replication_partners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_replication_partner_input** | [**NimbleCreateReplicationPartnerInput**](NimbleCreateReplicationPartnerInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_create_witness**
> TaskResponse device_type2_create_witness(system_id, nimble_create_witness_input)

Create a new witness configuration Nimble / Alletra 6K

Create a new witness configuration Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_witness_input = greenlake-data-services.NimbleCreateWitnessInput() # NimbleCreateWitnessInput | 

try:
    # Create a new witness configuration Nimble / Alletra 6K
    api_response = api_instance.device_type2_create_witness(system_id, nimble_create_witness_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_create_witness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_witness_input** | [**NimbleCreateWitnessInput**](NimbleCreateWitnessInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_mail_settings**
> TaskResponse device_type2_edit_mail_settings(system_id, nimble_mail_setting_input)

Edit Nimble Mail Settings of Nimble / Alletra 6K

Edit Nimble Mail Settings of Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_mail_setting_input = greenlake-data-services.NimbleMailSettingInput() # NimbleMailSettingInput | 

try:
    # Edit Nimble Mail Settings of Nimble / Alletra 6K
    api_response = api_instance.device_type2_edit_mail_settings(system_id, nimble_mail_setting_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_edit_mail_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_mail_setting_input** | [**NimbleMailSettingInput**](NimbleMailSettingInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_network_setting_by_id**
> TaskResponse device_type2_edit_network_setting_by_id(system_id, network_setting_id, nimble_edit_network_settings)

Edit Nimble / Alletra 6K network setting identified by {networkSettingId}

Edit Nimble / Alletra 6K network setting identified by {networkSettingId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
network_setting_id = 'network_setting_id_example' # str | Identifier of network setting. A 42 digit hexadecimal number.
nimble_edit_network_settings = greenlake-data-services.NimbleEditNetworkSettings() # NimbleEditNetworkSettings | 

try:
    # Edit Nimble / Alletra 6K network setting identified by {networkSettingId}
    api_response = api_instance.device_type2_edit_network_setting_by_id(system_id, network_setting_id, nimble_edit_network_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_edit_network_setting_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **network_setting_id** | **str**| Identifier of network setting. A 42 digit hexadecimal number. | 
 **nimble_edit_network_settings** | [**NimbleEditNetworkSettings**](NimbleEditNetworkSettings.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_replication_partners_by_id**
> TaskResponse device_type2_edit_replication_partners_by_id(system_id, replicationpartner_id, nimble_edit_replication_partner_input)

Edit a replication partner for Nimble / Alletra 6K given by replicationpartnerId

Edit a replication partner for Nimble / Alletra 6K given by replicationpartnerId

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
replicationpartner_id = 'replicationpartner_id_example' # str | Identifier of replicationpartner. A 42 digit hexadecimal number.
nimble_edit_replication_partner_input = greenlake-data-services.NimbleEditReplicationPartnerInput() # NimbleEditReplicationPartnerInput | 

try:
    # Edit a replication partner for Nimble / Alletra 6K given by replicationpartnerId
    api_response = api_instance.device_type2_edit_replication_partners_by_id(system_id, replicationpartner_id, nimble_edit_replication_partner_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_edit_replication_partners_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **replicationpartner_id** | **str**| Identifier of replicationpartner. A 42 digit hexadecimal number. | 
 **nimble_edit_replication_partner_input** | [**NimbleEditReplicationPartnerInput**](NimbleEditReplicationPartnerInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_system_settings**
> TaskResponse device_type2_edit_system_settings(system_id, nimble_edit_system_settings)

Edit system settings of Nimble / Alletra 6K

Edit system settings of Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_edit_system_settings = greenlake-data-services.NimbleEditSystemSettings() # NimbleEditSystemSettings | 

try:
    # Edit system settings of Nimble / Alletra 6K
    api_response = api_instance.device_type2_edit_system_settings(system_id, nimble_edit_system_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_edit_system_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_edit_system_settings** | [**NimbleEditSystemSettings**](NimbleEditSystemSettings.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_application_servers**
> ApplicationServersList device_type2_get_all_application_servers(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all application servers details by Nimble / Alletra 6K

Get all application servers details by Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter application servers by Key. (optional)
sort = 'sort_example' # str | oData query to sort application servers by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all application servers details by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_application_servers(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_get_all_application_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter application servers by Key. | [optional] 
 **sort** | **str**| oData query to sort application servers by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ApplicationServersList**](ApplicationServersList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_network_settings**
> NimbleNetworkSettingsList device_type2_get_all_network_settings(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all network settings details by Nimble / Alletra 6K

Get all network settings details by Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter network settings by Key. (optional)
sort = 'sort_example' # str | oData query to sort network settings resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all network settings details by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_network_settings(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_get_all_network_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter network settings by Key. | [optional] 
 **sort** | **str**| oData query to sort network settings resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleNetworkSettingsList**](NimbleNetworkSettingsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_application_server_by_id**
> ApplicationServerDetails device_type2_get_application_server_by_id(system_id, application_server_id, select=select)

Get details of Nimble / Alletra 6K application server identified by {applicationServerId}

Get details of Nimble / Alletra 6K application server identified by {applicationServerId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
application_server_id = 'application_server_id_example' # str | Identifier of application server. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K application server identified by {applicationServerId}
    api_response = api_instance.device_type2_get_application_server_by_id(system_id, application_server_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_get_application_server_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **application_server_id** | **str**| Identifier of application server. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**ApplicationServerDetails**](ApplicationServerDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_network_setting_by_id**
> NimbleNetworkSettingsDetailsWithRequestUri device_type2_get_network_setting_by_id(system_id, network_setting_id, select=select)

Get details of Nimble / Alletra 6K network setting identified by {networkSettingId}

Get details of Nimble / Alletra 6K network setting identified by {networkSettingId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
network_setting_id = 'network_setting_id_example' # str | Identifier of network setting. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K network setting identified by {networkSettingId}
    api_response = api_instance.device_type2_get_network_setting_by_id(system_id, network_setting_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_get_network_setting_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **network_setting_id** | **str**| Identifier of network setting. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleNetworkSettingsDetailsWithRequestUri**](NimbleNetworkSettingsDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_replication_partners**
> NimbleReplicationPartnersList device_type2_get_replication_partners(system_id, limit=limit, offset=offset, filter=filter, sort=sort, include_indirect_partners=include_indirect_partners, select=select)

Get all replication-partners details for Nimble / Alletra 6K

Get all replication-partners details for Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter replication partners by Key. (optional)
sort = 'sort_example' # str | oData query to sort replication partner resource by Key. (optional)
include_indirect_partners = True # bool | Include indirect partners. Indirect partners are excluded by default. This parameter cannot be used with other query parameters. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all replication-partners details for Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_replication_partners(system_id, limit=limit, offset=offset, filter=filter, sort=sort, include_indirect_partners=include_indirect_partners, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_get_replication_partners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter replication partners by Key. | [optional] 
 **sort** | **str**| oData query to sort replication partner resource by Key. | [optional] 
 **include_indirect_partners** | **bool**| Include indirect partners. Indirect partners are excluded by default. This parameter cannot be used with other query parameters. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleReplicationPartnersList**](NimbleReplicationPartnersList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_replication_partners_by_id**
> NimbleReplicationPartnerDetails device_type2_get_replication_partners_by_id(system_id, replicationpartner_id, select=select)

Get details of Nimble / Alletra 6K replication-partner identified by {replicationpartnerId}

Get details of Nimble / Alletra 6K replication-partner identified by {replicationpartnerId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
replicationpartner_id = 'replicationpartner_id_example' # str | Identifier of replicationpartner. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K replication-partner identified by {replicationpartnerId}
    api_response = api_instance.device_type2_get_replication_partners_by_id(system_id, replicationpartner_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_get_replication_partners_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **replicationpartner_id** | **str**| Identifier of replicationpartner. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleReplicationPartnerDetails**](NimbleReplicationPartnerDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_witnesses**
> NimbleWitnessesList device_type2_get_witnesses(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all witness configuration details by Nimble / Alletra 6K

Get all witness configuration details by Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter witnesses by Key. (optional)
sort = 'sort_example' # str | oData query to sort witnesses resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all witness configuration details by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_witnesses(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_get_witnesses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter witnesses by Key. | [optional] 
 **sort** | **str**| oData query to sort witnesses resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleWitnessesList**](NimbleWitnessesList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_witnesses_by_id**
> NimbleWitnessDetails device_type2_get_witnesses_by_id(system_id, witness_id, select=select)

Get details of Nimble / Alletra 6K witness configuration identified by {witnessId}

Get details of Nimble / Alletra 6K witness configuration identified by {witnessId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
witness_id = 'witness_id_example' # str | Identifier of witness. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K witness configuration identified by {witnessId}
    api_response = api_instance.device_type2_get_witnesses_by_id(system_id, witness_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_get_witnesses_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **witness_id** | **str**| Identifier of witness. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleWitnessDetails**](NimbleWitnessDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_pause_replication_partner**
> TaskResponse device_type2_pause_replication_partner(system_id, pause_resume_nimble_replication_partner_pair_input)

Pause the replication pair of Nimble / Alletra 6K

Pause the replication pair of Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
pause_resume_nimble_replication_partner_pair_input = greenlake-data-services.PauseResumeNimbleReplicationPartnerPairInput() # PauseResumeNimbleReplicationPartnerPairInput | 

try:
    # Pause the replication pair of Nimble / Alletra 6K
    api_response = api_instance.device_type2_pause_replication_partner(system_id, pause_resume_nimble_replication_partner_pair_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_pause_replication_partner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **pause_resume_nimble_replication_partner_pair_input** | [**PauseResumeNimbleReplicationPartnerPairInput**](PauseResumeNimbleReplicationPartnerPairInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_application_server_by_id**
> TaskResponse device_type2_remove_application_server_by_id(system_id, application_server_id)

Remove application server identified by {applicationServerId} from Nimble / Alletra 6K

Remove application server identified by {applicationServerId} from Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
application_server_id = 'application_server_id_example' # str | Identifier of application server. A 42 digit hexadecimal number.

try:
    # Remove application server identified by {applicationServerId} from Nimble / Alletra 6K
    api_response = api_instance.device_type2_remove_application_server_by_id(system_id, application_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_remove_application_server_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **application_server_id** | **str**| Identifier of application server. A 42 digit hexadecimal number. | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_replication_partner**
> TaskResponse device_type2_remove_replication_partner(system_id, remove_replication_partners)

Remove list of replication partner for Nimble / Alletra 6K

Remove list of replication partner for Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
remove_replication_partners = greenlake-data-services.RemoveReplicationPartners() # RemoveReplicationPartners | 

try:
    # Remove list of replication partner for Nimble / Alletra 6K
    api_response = api_instance.device_type2_remove_replication_partner(system_id, remove_replication_partners)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_remove_replication_partner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **remove_replication_partners** | [**RemoveReplicationPartners**](RemoveReplicationPartners.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_witnesses_by_id**
> TaskResponse device_type2_remove_witnesses_by_id(system_id, witness_id)

Remove witness identified by {witnessId} from Nimble / Alletra 6K

Remove witness identified by {witnessId} from Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
witness_id = 'witness_id_example' # str | Identifier of witness. A 42 digit hexadecimal number.

try:
    # Remove witness identified by {witnessId} from Nimble / Alletra 6K
    api_response = api_instance.device_type2_remove_witnesses_by_id(system_id, witness_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_remove_witnesses_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **witness_id** | **str**| Identifier of witness. A 42 digit hexadecimal number. | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_resume_replication_partner**
> TaskResponse device_type2_resume_replication_partner(system_id, pause_resume_nimble_replication_partner_pair_input)

Resume the replication pair of Nimble / Alletra 6K

Resume the replication pair of Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
pause_resume_nimble_replication_partner_pair_input = greenlake-data-services.PauseResumeNimbleReplicationPartnerPairInput() # PauseResumeNimbleReplicationPartnerPairInput | 

try:
    # Resume the replication pair of Nimble / Alletra 6K
    api_response = api_instance.device_type2_resume_replication_partner(system_id, pause_resume_nimble_replication_partner_pair_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_resume_replication_partner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **pause_resume_nimble_replication_partner_pair_input** | [**PauseResumeNimbleReplicationPartnerPairInput**](PauseResumeNimbleReplicationPartnerPairInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_send_auto_support**
> TaskResponse device_type2_send_auto_support(system_id)

Send auto support information of Nimble / Alletra 6K identified by {systemId}

Send auto support information of Nimble / Alletra 6K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system

try:
    # Send auto support information of Nimble / Alletra 6K identified by {systemId}
    api_response = api_instance.device_type2_send_auto_support(system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_send_auto_support: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_test_replication_configuration**
> TaskResponseReplication device_type2_test_replication_configuration(system_id, pause_resume_nimble_replication_partner_pair_input)

Test the replication partner pair of Nimble / Alletra 6K

Test the replication partner pair of Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
pause_resume_nimble_replication_partner_pair_input = greenlake-data-services.PauseResumeNimbleReplicationPartnerPairInput() # PauseResumeNimbleReplicationPartnerPairInput | 

try:
    # Test the replication partner pair of Nimble / Alletra 6K
    api_response = api_instance.device_type2_test_replication_configuration(system_id, pause_resume_nimble_replication_partner_pair_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_test_replication_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **pause_resume_nimble_replication_partner_pair_input** | [**PauseResumeNimbleReplicationPartnerPairInput**](PauseResumeNimbleReplicationPartnerPairInput.md)|  | 

### Return type

[**TaskResponseReplication**](TaskResponseReplication.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_test_witnesses_by_id**
> NimbleTestWitnessResponse device_type2_test_witnesses_by_id(system_id, witness_id)

Test and validate the witness configuration between the host identified by {witnessId} from Nimble / Alletra 6K identified by {systemId}

Test and validate the witness configuration between the host identified by {witnessId} from Nimble / Alletra 6K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
witness_id = 'witness_id_example' # str | Identifier of witness. A 42 digit hexadecimal number.

try:
    # Test and validate the witness configuration between the host identified by {witnessId} from Nimble / Alletra 6K identified by {systemId}
    api_response = api_instance.device_type2_test_witnesses_by_id(system_id, witness_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->device_type2_test_witnesses_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **witness_id** | **str**| Identifier of witness. A 42 digit hexadecimal number. | 

### Return type

[**NimbleTestWitnessResponse**](NimbleTestWitnessResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_settings_associate**
> TaskResponse mail_settings_associate(system_id, mailsettings_input)

Add SMTP/Mail server settigs

Add SMTP/Mail server settigs

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
mailsettings_input = greenlake-data-services.MailsettingsInput() # MailsettingsInput | 

try:
    # Add SMTP/Mail server settigs
    api_response = api_instance.mail_settings_associate(system_id, mailsettings_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->mail_settings_associate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **mailsettings_input** | [**MailsettingsInput**](MailsettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_settings_delete**
> TaskResponse mail_settings_delete(system_id)

Delete SMTP/mail server settings

Delete SMTP/mail server settings

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system

try:
    # Delete SMTP/mail server settings
    api_response = api_instance.mail_settings_delete(system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->mail_settings_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_settings_update**
> TaskResponse mail_settings_update(system_id, mailsettings_input)

Edit SMTP/Mail server settigs

Edit SMTP/Mail server settigs

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
mailsettings_input = greenlake-data-services.MailsettingsInput() # MailsettingsInput | 

try:
    # Edit SMTP/Mail server settigs
    api_response = api_instance.mail_settings_update(system_id, mailsettings_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->mail_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **mailsettings_input** | [**MailsettingsInput**](MailsettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_service_cim_update**
> TaskResponse network_service_cim_update(system_id, nw_cim_edit)

Edit CIM network service configuration

Edit CIM network service configuration

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
nw_cim_edit = greenlake-data-services.NwCimEdit() # NwCimEdit | 

try:
    # Edit CIM network service configuration
    api_response = api_instance.network_service_cim_update(system_id, nw_cim_edit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->network_service_cim_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **nw_cim_edit** | [**NwCimEdit**](NwCimEdit.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_service_snmp_mgr_create**
> TaskResponse network_service_snmp_mgr_create(system_id, nw_add_snmp_mgr)

Add SNMP Manager settings

Add SNMP Manager settings

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
nw_add_snmp_mgr = greenlake-data-services.NwAddSnmpMgr() # NwAddSnmpMgr | 

try:
    # Add SNMP Manager settings
    api_response = api_instance.network_service_snmp_mgr_create(system_id, nw_add_snmp_mgr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->network_service_snmp_mgr_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **nw_add_snmp_mgr** | [**NwAddSnmpMgr**](NwAddSnmpMgr.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_service_snmp_mgr_delete**
> TaskResponse network_service_snmp_mgr_delete(system_id, id)

Delete SNMP manager settings identified by {id}

Delete SNMP manager settings identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | ID of the SNMP manager

try:
    # Delete SNMP manager settings identified by {id}
    api_response = api_instance.network_service_snmp_mgr_delete(system_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->network_service_snmp_mgr_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| ID of the SNMP manager | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_service_snmp_mgr_update**
> TaskResponse network_service_snmp_mgr_update(system_id, id, nw_snmp_mgr_edit)

Edit SNMP Manager settings for the specified Id

Edit SNMP Manager settings for the specified Id

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | ID of the SNMP manager
nw_snmp_mgr_edit = greenlake-data-services.NwSnmpMgrEdit() # NwSnmpMgrEdit | 

try:
    # Edit SNMP Manager settings for the specified Id
    api_response = api_instance.network_service_snmp_mgr_update(system_id, id, nw_snmp_mgr_edit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->network_service_snmp_mgr_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| ID of the SNMP manager | 
 **nw_snmp_mgr_edit** | [**NwSnmpMgrEdit**](NwSnmpMgrEdit.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_settings_associate**
> TaskResponse network_settings_associate(system_id, edit_network_settings_input)

Post Network-Settings details for a storage system Primera / Alletra 9K

Post Network-Settings details for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
edit_network_settings_input = greenlake-data-services.EditNetworkSettingsInput() # EditNetworkSettingsInput | 

try:
    # Post Network-Settings details for a storage system Primera / Alletra 9K
    api_response = api_instance.network_settings_associate(system_id, edit_network_settings_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->network_settings_associate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **edit_network_settings_input** | [**EditNetworkSettingsInput**](EditNetworkSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_certificate**
> TaskResponse post_certificate(system_id, create_certificate_input)

Create certificate on storage system Primera / Alletra 9K identified by {systemId}

Create certificate on storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
create_certificate_input = greenlake-data-services.CreateCertificateInput() # CreateCertificateInput | 

try:
    # Create certificate on storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.post_certificate(system_id, create_certificate_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->post_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **create_certificate_input** | [**CreateCertificateInput**](CreateCertificateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_certificate**
> TaskResponse put_certificate(system_id, id, import_certificate_input)

Import certificate identified by {id} on storage system Primera / Alletra 9K identified by {systemId}

Import certificate identified by {id} on storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | ID of the certificate
import_certificate_input = greenlake-data-services.ImportCertificateInput() # ImportCertificateInput | 

try:
    # Import certificate identified by {id} on storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.put_certificate(system_id, id, import_certificate_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->put_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| ID of the certificate | 
 **import_certificate_input** | [**ImportCertificateInput**](ImportCertificateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_certificates**
> TaskResponse remove_certificates(system_id, remove_certificates_input)

Delete certificates from storage system Primera / Alletra 9K identified by {systemId}

Delete certificates from storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
remove_certificates_input = greenlake-data-services.RemoveCertificatesInput() # RemoveCertificatesInput | 

try:
    # Delete certificates from storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.remove_certificates(system_id, remove_certificates_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->remove_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **remove_certificates_input** | [**RemoveCertificatesInput**](RemoveCertificatesInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_trusted_certificates**
> TaskResponse remove_trusted_certificates(system_id, remove_trusted_certificates_input)

Delete trusted certificates from storage system Primera / Alletra 9K identified by {systemId}

Delete trusted certificates from storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
remove_trusted_certificates_input = greenlake-data-services.RemoveTrustedCertificatesInput() # RemoveTrustedCertificatesInput | 

try:
    # Delete trusted certificates from storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.remove_trusted_certificates(system_id, remove_trusted_certificates_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->remove_trusted_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **remove_trusted_certificates_input** | [**RemoveTrustedCertificatesInput**](RemoveTrustedCertificatesInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_settings_associate**
> TaskResponse support_settings_associate(system_id, support_settings_input)

Add support settings for a storage system Primera / Alletra 9K

Add support settings for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
support_settings_input = greenlake-data-services.SupportSettingsInput() # SupportSettingsInput | 

try:
    # Add support settings for a storage system Primera / Alletra 9K
    api_response = api_instance.support_settings_associate(system_id, support_settings_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->support_settings_associate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **support_settings_input** | [**SupportSettingsInput**](SupportSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_settings_update**
> TaskResponse support_settings_update(system_id, support_settings_input)

Edit support settings for a storage system Primera / Alletra 9K

Edit support settings for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
support_settings_input = greenlake-data-services.SupportSettingsInput() # SupportSettingsInput | 

try:
    # Edit support settings for a storage system Primera / Alletra 9K
    api_response = api_instance.support_settings_update(system_id, support_settings_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->support_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **support_settings_input** | [**SupportSettingsInput**](SupportSettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_associate**
> TaskResponse system_settings_associate(system_id, system_config_params_edit_input)

Edit system settings configuration

Edit system settings configuration

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
system_config_params_edit_input = greenlake-data-services.SystemConfigParamsEditInput() # SystemConfigParamsEditInput | 

try:
    # Edit system settings configuration
    api_response = api_instance.system_settings_associate(system_id, system_config_params_edit_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->system_settings_associate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **system_config_params_edit_input** | [**SystemConfigParamsEditInput**](SystemConfigParamsEditInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_update**
> TaskResponse system_settings_update(system_id, system_config_params_edit_input)

Edit system settings configuration

Edit system settings configuration

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.SystemSettingsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
system_config_params_edit_input = greenlake-data-services.SystemConfigParamsEditInput() # SystemConfigParamsEditInput | 

try:
    # Edit system settings configuration
    api_response = api_instance.system_settings_update(system_id, system_config_params_edit_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemSettingsApi->system_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **system_config_params_edit_input** | [**SystemConfigParamsEditInput**](SystemConfigParamsEditInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

