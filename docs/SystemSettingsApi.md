# greenlake_data_services.SystemSettingsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
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
[**support_settings_associate**](SystemSettingsApi.md#support_settings_associate) | **POST** /api/v1/storage-systems/device-type1/{systemId}/support-settings | Add support settings for a storage system Primera / Alletra 9K
[**support_settings_update**](SystemSettingsApi.md#support_settings_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/support-settings | Edit support settings for a storage system Primera / Alletra 9K
[**system_settings_associate**](SystemSettingsApi.md#system_settings_associate) | **POST** /api/v1/storage-systems/device-type1/{systemId}/system-settings | Edit system settings configuration
[**system_settings_update**](SystemSettingsApi.md#system_settings_update) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/system-settings | Edit system settings configuration


# **alert_contacts_create**
> TaskResponse alert_contacts_create(system_id, alert_contact_input)

Add Alert/Mail contact details

Add Alert/Mail contact details

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.alert_contact_input import AlertContactInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    alert_contact_input = AlertContactInput(
        company="HPE",
        company_code="HPE",
        country="US",
        fax="fax_id",
        first_name="john",
        include_svc_alerts=False,
        last_name="kevin",
        notification_severities=[0,1,2,3,4,5],
        preferred_language="en",
        primary_email="kevin.john@hpe.com",
        primary_phone="98783456",
        receive_email=True,
        receive_grouped=True,
        secondary_email="winny.pooh@hpe.com",
        secondary_phone="23456789",
    ) # AlertContactInput | 

    # example passing only required values which don't have defaults set
    try:
        # Add Alert/Mail contact details
        api_response = api_instance.alert_contacts_create(system_id, alert_contact_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_contacts_delete**
> TaskResponse alert_contacts_delete(system_id, id)

Delete Alert/Email contact of storage system Primera / Alletra 9K identified by {id}

Delete Alert/Email contact of storage system Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a4c78226-69cd-b9e7-af3e-445ca8f8a655" # str | Unique Identifier of the alert contact

    # example passing only required values which don't have defaults set
    try:
        # Delete Alert/Email contact of storage system Primera / Alletra 9K identified by {id}
        api_response = api_instance.alert_contacts_delete(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_contacts_update**
> TaskResponse alert_contacts_update(system_id, id, alert_contact_input)

Edit Alert/Email contact details of storage system Primera / Alletra 9K identified by {id}

Edit Alert/Email contact details of storage system Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.alert_contact_input import AlertContactInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a4c78226-69cd-b9e7-af3e-445ca8f8a655" # str | Unique Identifier of the alert contact
    alert_contact_input = AlertContactInput(
        company="HPE",
        company_code="HPE",
        country="US",
        fax="fax_id",
        first_name="john",
        include_svc_alerts=False,
        last_name="kevin",
        notification_severities=[0,1,2,3,4,5],
        preferred_language="en",
        primary_email="kevin.john@hpe.com",
        primary_phone="98783456",
        receive_email=True,
        receive_grouped=True,
        secondary_email="winny.pooh@hpe.com",
        secondary_phone="23456789",
    ) # AlertContactInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit Alert/Email contact details of storage system Primera / Alletra 9K identified by {id}
        api_response = api_instance.alert_contacts_update(system_id, id, alert_contact_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_alert_contacts_get_by_id**
> AlertContactsDetailsList device_type1_alert_contacts_get_by_id(system_id, id)

Get alert-contact details for a storage system Primera / Alletra 9K identified by {id}

Get alert-contact details for a storage system Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.alert_contacts_details_list import AlertContactsDetailsList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a4c78226-69cd-b9e7-af3e-445ca8f8a655" # str | Unique Identifier of the alert contact
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get alert-contact details for a storage system Primera / Alletra 9K identified by {id}
        api_response = api_instance.device_type1_alert_contacts_get_by_id(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_alert_contacts_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get alert-contact details for a storage system Primera / Alletra 9K identified by {id}
        api_response = api_instance.device_type1_alert_contacts_get_by_id(system_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_alert_contacts_list**
> AlertContacts device_type1_alert_contacts_list(system_id)

Get alert-contact details for a storage system Primera / Alletra 9K

Get alert-contact details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.alert_contacts import AlertContacts
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get alert-contact details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_alert_contacts_list(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_alert_contacts_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get alert-contact details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_alert_contacts_list(system_id, limit=limit, offset=offset, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_certificates_get_by_id**
> CertificateDetails device_type1_certificates_get_by_id(system_id, id)

Get array certificates by Primera / Alletra 9K identified by {id}

Get array certificates by Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.certificate_details import CertificateDetails
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "99691e493067b2b2acf1774fc0ccc011" # str | ID of the certificate
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get array certificates by Primera / Alletra 9K identified by {id}
        api_response = api_instance.device_type1_certificates_get_by_id(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_certificates_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get array certificates by Primera / Alletra 9K identified by {id}
        api_response = api_instance.device_type1_certificates_get_by_id(system_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_certificates_list**
> CertificatesSummaryList device_type1_certificates_list(system_id)

Get array certificates by Primera / Alletra 9K

Get array certificates by Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.certificates_summary_list import CertificatesSummaryList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "service eq qw-client" # str | Lucene query to filter Certificates by Key. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get array certificates by Primera / Alletra 9K
        api_response = api_instance.device_type1_certificates_list(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_certificates_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get array certificates by Primera / Alletra 9K
        api_response = api_instance.device_type1_certificates_list(system_id, select=select, limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_delete_quorum_witness**
> TaskResponse device_type1_delete_quorum_witness(system_id, replication_partner_id)

Delete quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

Delete quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    replication_partner_id = "aedec7d11d02f73611a6ff992c256bdb" # str | id of device-type1 replication partner

    # example passing only required values which don't have defaults set
    try:
        # Delete quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_delete_quorum_witness(system_id, replication_partner_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_delete_v_center_settings**
> TaskResponse device_type1_delete_v_center_settings(system_id, vcenter_setting_id)

Delete vcenter setting identified by {vcenterSettingId} on storage system Primera / Alletra 9K identified by {systemId}

Delete vcenter setting identified by {vcenterSettingId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    vcenter_setting_id = "7e92269a-12d1-35b4-60e8-5919edfc5475" # str | UID(vcenterSettingId) of the storage system

    # example passing only required values which don't have defaults set
    try:
        # Delete vcenter setting identified by {vcenterSettingId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_delete_v_center_settings(system_id, vcenter_setting_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_quorum_witness**
> WitnessList device_type1_get_quorum_witness(system_id)

Get quorum witness configuration details from storage system Primera / Alletra 9K identified by {systemId}

Get quorum witness configuration details from storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.witness_list import WitnessList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq afb4961e47212e5bc88dd35db5be5c83" # str | oData query to filter witness by key. (optional)
    sort = "id desc" # str | oData query to sort witness resource by key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get quorum witness configuration details from storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_quorum_witness(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_get_quorum_witness: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get quorum witness configuration details from storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_quorum_witness(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_quorum_witness_with_id**
> WitnessDetails device_type1_get_quorum_witness_with_id(system_id, replication_partner_id)

Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.witness_details import WitnessDetails
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    replication_partner_id = "aedec7d11d02f73611a6ff992c256bdb" # str | id of device-type1 replication partner
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_quorum_witness_with_id(system_id, replication_partner_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_get_quorum_witness_with_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of quorum witness configured on replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_quorum_witness_with_id(system_id, replication_partner_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_replication_partner_with_id**
> ReplicationPartnerDetails device_type1_get_replication_partner_with_id(system_id, replication_partner_id)

Get details of replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

Get details of replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.replication_partner_details import ReplicationPartnerDetails
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    replication_partner_id = "aedec7d11d02f73611a6ff992c256bdb" # str | id of device-type1 replication partner
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_replication_partner_with_id(system_id, replication_partner_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_get_replication_partner_with_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of replication partner identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_replication_partner_with_id(system_id, replication_partner_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_replication_partners**
> ReplicationPartnersList device_type1_get_replication_partners(system_id)

Get details of replication partners on storage system Primera / Alletra 9K identified by {systemId}

Get details of replication partners on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.replication_partners_list import ReplicationPartnersList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "systemId eq 7CE751P312" # str | oData query to filter replication partners by key. (optional)
    sort = "systemId desc" # str | oData query to sort nodes resource by key. (optional)
    include_indirect_partners = True # bool | Include indirect partners. Indirect partners are excluded by default. This parameter cannot be used with other query parameters. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of replication partners on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_replication_partners(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_get_replication_partners: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of replication partners on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_get_replication_partners(system_id, limit=limit, offset=offset, filter=filter, sort=sort, include_indirect_partners=include_indirect_partners, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_mail_settings_get**
> Mailsettings device_type1_mail_settings_get(system_id)

Get the system's SMTP/Mail server settigs

Get the system's SMTP/Mail server settigs

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.mailsettings import Mailsettings
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the system's SMTP/Mail server settigs
        api_response = api_instance.device_type1_mail_settings_get(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_mail_settings_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the system's SMTP/Mail server settigs
        api_response = api_instance.device_type1_mail_settings_get(system_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - Current entity tag for the selected resource <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_cim_get**
> NetworkServicesCim device_type1_network_service_cim_get(system_id)

Get CIM Network-Service details for a storage system Primera / Alletra 9K

Get CIM Network-Service details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.network_services_cim import NetworkServicesCim
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get CIM Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_service_cim_get(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_network_service_cim_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get CIM Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_service_cim_get(system_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_snmp_mgr_get_by_id**
> NetworkServicesSnmp device_type1_network_service_snmp_mgr_get_by_id(system_id, id)

Get a specific SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K

Get a specific SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.network_services_snmp import NetworkServicesSnmp
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | ID of the SNMP manager
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a specific SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_service_snmp_mgr_get_by_id(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_network_service_snmp_mgr_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a specific SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_service_snmp_mgr_get_by_id(system_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | SNMP Manager object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_snmp_mgr_list**
> NetworkServicesSnmp device_type1_network_service_snmp_mgr_list(system_id)

Get SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K

Get SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.network_services_snmp import NetworkServicesSnmp
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_service_snmp_mgr_list(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_network_service_snmp_mgr_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get SNMP-Manager Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_service_snmp_mgr_list(system_id, limit=limit, offset=offset, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_service_vasa_get**
> NetworkServicesVasa device_type1_network_service_vasa_get(system_id)

Get VASA Network-Service details for a storage system Primera / Alletra 9K

Get VASA Network-Service details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.network_services_vasa import NetworkServicesVasa
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get VASA Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_service_vasa_get(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_network_service_vasa_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get VASA Network-Service details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_service_vasa_get(system_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_network_settings_get**
> NetworkSettings device_type1_network_settings_get(system_id)

Get Network-Settings details for a storage system Primera / Alletra 9K

Get Network-Settings details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.network_settings import NetworkSettings
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Network-Settings details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_settings_get(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_network_settings_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Network-Settings details for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_network_settings_get(system_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_node_service_ports_get_by_id**
> ServicePortsList device_type1_node_service_ports_get_by_id(node_id, system_id)

Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId} and {nodeId }

Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId} and {nodeId }

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.service_ports_list import ServicePortsList
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | Primary ID of the node
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "ipv4address eq "169.254.77.160"" # str | oData query to filter systems by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId} and {nodeId }
        api_response = api_instance.device_type1_node_service_ports_get_by_id(node_id, system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_node_service_ports_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId} and {nodeId }
        api_response = api_instance.device_type1_node_service_ports_get_by_id(node_id, system_id, limit=limit, offset=offset, filter=filter, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_node_service_ports_list**
> ServicePortsList device_type1_node_service_ports_list(system_id)

Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId}

Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.service_ports_list import ServicePortsList
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "ipv4address eq "169.254.77.160"" # str | oData query to filter systems by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_node_service_ports_list(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_node_service_ports_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get service ports for nodes of all storage systems of Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_node_service_ports_list(system_id, limit=limit, offset=offset, filter=filter, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_post_quorum_witness**
> TaskResponse device_type1_post_quorum_witness(system_id, create_quorum_witness_input)

Create quorum witness on storage system Primera / Alletra 9K identified by {systemId}

Create quorum witness on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.create_quorum_witness_input import CreateQuorumWitnessInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    create_quorum_witness_input = CreateQuorumWitnessInput(
        parameters=CreateQuorumWitnessInputParameters(
            ip_address="15.112.47.239",
            port=8843,
            ssl=True,
        ),
        replication_partner_system_id="7CE816P0SR",
        src_replication_id="afb4961e47212e5bc88dd35db5be5c83",
        start_quorum_witness=True,
        target_replication_id="afb4961e47212e5bc88dd35db5be5c83",
    ) # CreateQuorumWitnessInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create quorum witness on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_post_quorum_witness(system_id, create_quorum_witness_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_post_remove_replication_partners**
> TaskResponse device_type1_post_remove_replication_partners(system_id, remove_replication_partners_input)

Delete replication partner from storage system Primera / Alletra 9K identified by {systemId}

Delete replication partner from storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.remove_replication_partners_input import RemoveReplicationPartnersInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    remove_replication_partners_input = RemoveReplicationPartnersInput(
        replication_partners=[
            RemoveRemoteCopyTargetInput(
                replication_partner_system_id="7CE816P0SR",
                src_replication_id="afb4961e47212e5bc88dd35db5be5c83",
                target_replication_id="afb4961e47212e5bc88dd35db5be5c83",
            ),
        ],
    ) # RemoveReplicationPartnersInput | 

    # example passing only required values which don't have defaults set
    try:
        # Delete replication partner from storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_post_remove_replication_partners(system_id, remove_replication_partners_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_post_replication_partners**
> TaskResponse device_type1_post_replication_partners(system_id, create_replication_partners_input)

Create replication partners on Primera / Alletra 9K identified by {systemId}

Create replication partners on Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.create_replication_partners_input import CreateReplicationPartnersInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    create_replication_partners_input = CreateReplicationPartnersInput(
        replication_partners=[
            ReplicationPartnerInput(
                replication_partner_system_id="replication_partner_system_id_example",
                source=CreateRemoteCopyTargetInput(
                    disabled=True,
                    name="sample_RCtarget",
                    node_wwn="2FF70002AC020DA1",
                    port_pos_and_link=[
                        PortPosAndLinkInput(
                            link="10.100.65.128",
                            port_position=PortPositionInput(
                                node=0,
                                port=3,
                                slot=1,
                            ),
                        ),
                    ],
                    type=1,
                ),
                target=CreateRemoteCopyTargetInput(
                    disabled=True,
                    name="sample_RCtarget",
                    node_wwn="2FF70002AC020DA1",
                    port_pos_and_link=[
                        PortPosAndLinkInput(
                            link="10.100.65.128",
                            port_position=PortPositionInput(
                                node=0,
                                port=3,
                                slot=1,
                            ),
                        ),
                    ],
                    type=1,
                ),
            ),
        ],
    ) # CreateReplicationPartnersInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create replication partners on Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_post_replication_partners(system_id, create_replication_partners_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_post_v_center_settings**
> TaskResponse device_type1_post_v_center_settings(system_id, v_center_settings_input)

Add vCenter settings to storage system Primera / Alletra 9K

Add vCenter settings to storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.v_center_settings_input import VCenterSettingsInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    v_center_settings_input = VCenterSettingsInput(
        cert_chain_pem='''-----BEGIN CERTIFICATE-----
MIID2jCCAsKgAwIBAgIJAOiAEUfqLBfBMA0GCSqGSIb3DQEBCwUAMIGQMQswCQYD
-----END CERTIFICATE-----
''',
        description="vCenter - dataCenter1",
        inetaddress="15.71.130.25",
        name="dataCenter1",
        password="pass",
        port=443,
        username="user1",
    ) # VCenterSettingsInput | 

    # example passing only required values which don't have defaults set
    try:
        # Add vCenter settings to storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_post_v_center_settings(system_id, v_center_settings_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_put_quorum_witness**
> TaskResponse device_type1_put_quorum_witness(system_id, replication_partner_id, edit_quorum_witness_input)

Edit quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

Edit quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.edit_quorum_witness_input import EditQuorumWitnessInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    replication_partner_id = "aedec7d11d02f73611a6ff992c256bdb" # str | id of device-type1 replication partner
    edit_quorum_witness_input = EditQuorumWitnessInput(
        replication_partner_system_id="7CE816P0SR",
        start_quorum_witness=True,
        target_replication_id="afb4961e47212e5bc88dd35db5be5c83",
    ) # EditQuorumWitnessInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit quorum witness identified by {replicationPartnerId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_put_quorum_witness(system_id, replication_partner_id, edit_quorum_witness_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_put_replication_partner**
> TaskResponse device_type1_put_replication_partner(system_id, replication_partner_id, edit_replication_partner_input)

Edit replication partner identified by {replicationPartnerId} on Primera / Alletra 9K identified by {systemId}

Edit replication partner identified by {replicationPartnerId} on Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.edit_replication_partner_input import EditReplicationPartnerInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    replication_partner_id = "aedec7d11d02f73611a6ff992c256bdb" # str | id of device-type1 replication partner
    edit_replication_partner_input = EditReplicationPartnerInput(
        add_rc_links=AddRemoteCopyLinks(
            replication_partner_system_id="7CE816P0SR",
            source=[
                CreateRemoteCopyLinkInput(
                    address="10.100.65.128",
                    port_pos=CreateRemoteCopyLinkInputPortPos(
                        node=0,
                        port=3,
                        slot=1,
                    ),
                    target_name="Sample_RCTarget",
                    type=1,
                ),
            ],
            target=[
                CreateRemoteCopyLinkInput(
                    address="10.100.65.128",
                    port_pos=CreateRemoteCopyLinkInputPortPos(
                        node=0,
                        port=3,
                        slot=1,
                    ),
                    target_name="Sample_RCTarget",
                    type=1,
                ),
            ],
        ),
        remove_rc_links=RemoveRemoteCopyLinksInput(
            replication_partner_system_id="7CE816P0SR",
            source=[
                RCLinkId(
                    rc_link_id="afb4961e47212e5bc88dd35db5be5c82",
                ),
            ],
            target=[
                RCLinkId(
                    rc_link_id="afb4961e47212e5bc88dd35db5be5c82",
                ),
            ],
        ),
    ) # EditReplicationPartnerInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit replication partner identified by {replicationPartnerId} on Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_put_replication_partner(system_id, replication_partner_id, edit_replication_partner_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_put_v_center_settings**
> TaskResponse device_type1_put_v_center_settings(system_id, vcenter_setting_id, edit_v_center_settings_input)

Edit vCenter setting identified by {vcenterSettingId} on Primera / Alletra 9K identified by {systemId}

Edit vCenter setting identified by {vcenterSettingId} on Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.edit_v_center_settings_input import EditVCenterSettingsInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    vcenter_setting_id = "7e92269a-12d1-35b4-60e8-5919edfc5475" # str | UID(vcenterSettingId) of the storage system
    edit_v_center_settings_input = EditVCenterSettingsInput(
        cert_chain_pem='''-----BEGIN CERTIFICATE-----
MIID2jCCAsKgAwIBAgIJAOiAEUfqLBfBMA0GCSqGSIb3DQEBCwUAMIGQMQswCQYD
-----END CERTIFICATE-----
''',
        description="vCenter - dataCenter1",
        inetaddress="15.71.130.25",
        name="dataCenter1",
        password="pass",
        port=443,
        username="user1",
    ) # EditVCenterSettingsInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit vCenter setting identified by {vcenterSettingId} on Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_put_v_center_settings(system_id, vcenter_setting_id, edit_v_center_settings_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_support_data_collect**
> TaskResponse device_type1_support_data_collect(system_id, collect_support_data_array_input)

Trigger a collection on the storage system Primera / Alletra 9K

Trigger a collection on the storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.collect_support_data_array_input import CollectSupportDataArrayInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    collect_support_data_array_input = CollectSupportDataArrayInput([
        CollectSupportDataInput(
            action="PERFCOLLECTION",
            options=[
                "options_example",
            ],
        ),
    ]) # CollectSupportDataArrayInput | 

    # example passing only required values which don't have defaults set
    try:
        # Trigger a collection on the storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_support_data_collect(system_id, collect_support_data_array_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_support_data_collect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **collect_support_data_array_input** | [**CollectSupportDataArrayInput**](CollectSupportDataArrayInput.md)|  |

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_support_settings_get**
> SupportSetting device_type1_support_settings_get(system_id)

Get support settings for a storage system Primera / Alletra 9K

Get support settings for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.support_setting import SupportSetting
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get support settings for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_support_settings_get(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_support_settings_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get support settings for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_support_settings_get(system_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_settings_list**
> SystemConfigParams device_type1_system_settings_list(system_id)

Get the system settings configuration details

Get the system settings configuration details

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.system_config_params import SystemConfigParams
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the system settings configuration details
        api_response = api_instance.device_type1_system_settings_list(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_system_settings_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the system settings configuration details
        api_response = api_instance.device_type1_system_settings_list(system_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - Current entity tag for the selected resource <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_telemetry_get**
> TelemetryStatus device_type1_telemetry_get(system_id)

Get telemetry status for a storage system Primera / Alletra 9K

Get telemetry status for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.telemetry_status import TelemetryStatus
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get telemetry status for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_telemetry_get(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_telemetry_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get telemetry status for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_telemetry_get(system_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vm_manager_settings_get_by_id**
> VcenterSettingDetail device_type1_vm_manager_settings_get_by_id(system_id, vcenter_setting_id)

Get vcenter setting detail for a given vcenter setting of a storage system Primera / Alletra 9K

Get vcenter setting detail for a given vcenter setting of a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.vcenter_setting_detail import VcenterSettingDetail
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    vcenter_setting_id = "7e92269a-12d1-35b4-60e8-5919edfc5475" # str | UID(vcenterSettingId) of the storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get vcenter setting detail for a given vcenter setting of a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_vm_manager_settings_get_by_id(system_id, vcenter_setting_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_vm_manager_settings_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get vcenter setting detail for a given vcenter setting of a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_vm_manager_settings_get_by_id(system_id, vcenter_setting_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vm_manager_settings_list**
> VcenterSettingsSumarryList device_type1_vm_manager_settings_list(system_id)

Get vcenter settings for a storage system Primera / Alletra 9K

Get vcenter settings for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.vcenter_settings_sumarry_list import VcenterSettingsSumarryList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get vcenter settings for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_vm_manager_settings_list(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type1_vm_manager_settings_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get vcenter settings for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_vm_manager_settings_list(system_id, select=select, limit=limit, offset=offset)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_application_server_create**
> TaskResponse device_type2_application_server_create(system_id, create_application_server)

Create Nimble / Alletra 6K application server in system identified by {systemId}

Create Nimble / Alletra 6K application server in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.create_application_server import CreateApplicationServer
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    create_application_server = CreateApplicationServer(
        description="99.9999% availability",
        hostname="nimble-appserver.com",
        metadata=[
            AppKeyValue(
                key="key1",
                value="value1",
            ),
        ],
        name="AppServer101",
        port=1048,
        server_type="vmware",
        username="user256",
    ) # CreateApplicationServer | 

    # example passing only required values which don't have defaults set
    try:
        # Create Nimble / Alletra 6K application server in system identified by {systemId}
        api_response = api_instance.device_type2_application_server_create(system_id, create_application_server)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_application_server_edit**
> TaskResponse device_type2_application_server_edit(system_id, application_server_id, edit_application_server)

Modify Nimble / Alletra 6K application server in system identified by {systemId}

Modify Nimble / Alletra 6K application server in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.edit_application_server import EditApplicationServer
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    application_server_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of application server. A 42 digit hexadecimal number.
    edit_application_server = EditApplicationServer(
        description="99.9999% availability",
        hostname="nimble-appserver.com",
        metadata=[
            AppKeyValue(
                key="key1",
                value="value1",
            ),
        ],
        name="AppServer101",
        port=1048,
        server_type="vmware",
        username="user256",
    ) # EditApplicationServer | 

    # example passing only required values which don't have defaults set
    try:
        # Modify Nimble / Alletra 6K application server in system identified by {systemId}
        api_response = api_instance.device_type2_application_server_edit(system_id, application_server_id, edit_application_server)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_create_replication_partners**
> TaskResponse device_type2_create_replication_partners(system_id, nimble_create_replication_partner_input)

Create replication partner pair for Nimble / Alletra 6K

Create replication partner pair for Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.nimble_create_replication_partner_input import NimbleCreateReplicationPartnerInput
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_create_replication_partner_input = NimbleCreateReplicationPartnerInput(
        replication_partners=[
            ReplicationPartnerObj(
                control_port=1024,
                data_port=1024,
                description="99.9999% availability",
                repl_hostname="15.213.204.121",
                source=Source(
                    hostname="15.213.204.163",
                    name="replicationPartner1",
                    subnet_label="myobject-5",
                    subnet_type="mgmt",
                ),
                subnet_label="myobject-5",
                subnet_type="mgmt",
                target=Target(
                    hostname="15.213.204.164",
                    name="replicationPartner2",
                    subnet_label="myobject-5",
                    subnet_type="mgmt",
                ),
                target_system_id="005319ed73385876a4000000000000000000000001",
                throttles=[
                    ReplicationThrottle(
                        days="example day",
                        description="Throttle one",
                        name="Throttle1",
                        thr_at_time=10800,
                        thr_bandwidth=14,
                        thr_until_time=14400,
                    ),
                ],
            ),
        ],
    ) # NimbleCreateReplicationPartnerInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create replication partner pair for Nimble / Alletra 6K
        api_response = api_instance.device_type2_create_replication_partners(system_id, nimble_create_replication_partner_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_create_witness**
> TaskResponse device_type2_create_witness(system_id, nimble_create_witness_input)

Create a new witness configuration Nimble / Alletra 6K

Create a new witness configuration Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_create_witness_input import NimbleCreateWitnessInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_create_witness_input = NimbleCreateWitnessInput(
        host="witness-host9801.sjcvlab.com",
        password="password_25-24",
        port=5395,
        username="witness9801",
    ) # NimbleCreateWitnessInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new witness configuration Nimble / Alletra 6K
        api_response = api_instance.device_type2_create_witness(system_id, nimble_create_witness_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_mail_settings**
> TaskResponse device_type2_edit_mail_settings(system_id, nimble_mail_setting_input)

Edit Nimble Mail Settings of Nimble / Alletra 6K

Edit Nimble Mail Settings of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from greenlake_data_services.model.nimble_mail_setting_input import NimbleMailSettingInput
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_mail_setting_input = NimbleMailSettingInput(
        smtp_port=25,
        smtp_server="example-1.com",
    ) # NimbleMailSettingInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit Nimble Mail Settings of Nimble / Alletra 6K
        api_response = api_instance.device_type2_edit_mail_settings(system_id, nimble_mail_setting_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_network_setting_by_id**
> TaskResponse device_type2_edit_network_setting_by_id(system_id, network_setting_id, nimble_edit_network_settings)

Edit Nimble / Alletra 6K network setting identified by {networkSettingId}

Edit Nimble / Alletra 6K network setting identified by {networkSettingId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_edit_network_settings import NimbleEditNetworkSettings
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    network_setting_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | Identifier of network setting. A 42 digit hexadecimal number.
    nimble_edit_network_settings = NimbleEditNetworkSettings(
        array_list=[
            NimbleEditArrayNet(
                ctrlr_a_support_ip="127.0.0.102",
                ctrlr_b_support_ip="127.0.0.103",
                name="g1a16",
                nic_list=[
                    NimbleNIC(
                        data_ip="127.0.0.102",
                        name="eth1",
                        subnet_label="subnet1",
                        tagged=True,
                    ),
                ],
            ),
        ],
        iscsi_automatic_connection_method=True,
        iscsi_connection_rebalancing=True,
        mgmt_ip="128.0.0.1",
        name="draft",
        route_list=[
            NimbleRoute(
                gateway="127.0.0.2",
                tgt_netmask="255.255.255.0",
                tgt_network="127.0.2.0",
            ),
        ],
        secondary_mgmt_ip="128.0.0.1",
        subnet_list=[
            NimbleSubnet(
                allow_group=True,
                allow_iscsi=True,
                discovery_ip="127.0.0.102",
                failover=True,
                failover_enable_time=1591599192000,
                label="subnet1",
                mtu=1500,
                netmask="255.0.0.0",
                network="127.0.0.108",
                netzone_type="single",
                type="mgmt",
                vlan_id=0,
            ),
        ],
    ) # NimbleEditNetworkSettings | 

    # example passing only required values which don't have defaults set
    try:
        # Edit Nimble / Alletra 6K network setting identified by {networkSettingId}
        api_response = api_instance.device_type2_edit_network_setting_by_id(system_id, network_setting_id, nimble_edit_network_settings)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_replication_partners_by_id**
> TaskResponse device_type2_edit_replication_partners_by_id(system_id, replicationpartner_id, nimble_edit_replication_partner_input)

Edit a replication partner for Nimble / Alletra 6K given by replicationpartnerId

Edit a replication partner for Nimble / Alletra 6K given by replicationpartnerId

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_edit_replication_partner_input import NimbleEditReplicationPartnerInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    replicationpartner_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | Identifier of replicationpartner. A 42 digit hexadecimal number.
    nimble_edit_replication_partner_input = NimbleEditReplicationPartnerInput(
        replication_partners=[
            EditReplicationPartner(
                control_port=1024,
                data_port=1024,
                description="99.9999% availability",
                remote_partner_id="005319ed73385876a4000000000000000000000006",
                repl_hostname="15.213.204.121",
                source=EditSourcePartner(
                    hostname="15.213.204.163",
                    name="replicationPartner1",
                    subnet_label="myobject-5",
                    subnet_type="mgmt",
                ),
                subnet_label="myobject-5",
                subnet_type="mgmt",
                target=EditTargetPartner(
                    hostname="15.213.204.164",
                    name="replicationPartner2",
                    subnet_label="myobject-5",
                    subnet_type="mgmt",
                ),
                target_system_id="005319ed73385876a4000000000000000000000001",
                throttles=[
                    ReplicationThrottle(
                        days="example day",
                        description="Throttle one",
                        name="Throttle1",
                        thr_at_time=10800,
                        thr_bandwidth=14,
                        thr_until_time=14400,
                    ),
                ],
            ),
        ],
    ) # NimbleEditReplicationPartnerInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit a replication partner for Nimble / Alletra 6K given by replicationpartnerId
        api_response = api_instance.device_type2_edit_replication_partners_by_id(system_id, replicationpartner_id, nimble_edit_replication_partner_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_system_settings**
> TaskResponse device_type2_edit_system_settings(system_id, nimble_edit_system_settings)

Edit system settings of Nimble / Alletra 6K

Edit system settings of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.nimble_edit_system_settings import NimbleEditSystemSettings
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_edit_system_settings = NimbleEditSystemSettings(
        alert_settings=EditAlertSettings(
            alert_from_email_addr="bob@wikipedia.com",
            alert_min_level="warning",
            alert_to_email_addrs="bob@wikipedia.com,jason@wiki.com",
            send_alert_to_support=True,
        ),
        date_timezone_settings=EditDateTimezoneSettings(
            date=1598267193,
            ntp_server="0.abc.pool.ntp.org",
            timezone="America/Los_Angeles",
        ),
        dns_settings=EditDnsSettings(
            dns_servers=[
                IPAddressObject(
                    ip_addr="10.0.0.11",
                ),
            ],
            domain_name="example-1.com",
        ),
        isns_settings=EditIsnsSettings(
            isns_enabled=True,
            isns_port=1080,
            isns_server="isns-server.com",
        ),
        name="NimbleGroup55",
        proxy_settings=EditProxySettings(
            proxy_port=1234,
            proxy_server="example-1.com",
            proxy_username="usr1",
        ),
        security_settings=EditSecuritySettings(
            user_inactivity_timeout=1800,
        ),
        smtp_settings=EditSmtpMailSettings(
            smtp_port=25,
            smtp_server="example-1.com",
        ),
        snmp_settings=EditSnmpSettings(
            snmp_community="private",
            snmp_get_enabled=True,
            snmp_get_port=1080,
            snmp_sys_contact="System contact",
            snmp_sys_location="Location",
            snmp_trap_enabled=True,
            snmp_trap_host="snmphost-1.com",
            snmp_trap_port=1080,
        ),
        support_settings=EditSupportSettings(
            allow_analytics_gui=False,
            allow_support_tunnel=False,
            autosupport_enabled=True,
        ),
        syslogd_settings=EditSyslogdSettings(
            syslogd_enabled=True,
            syslogd_port=1080,
            syslogd_server="sysloghost-1.com",
            syslogd_servers=[
                NimbleSyslogdServerInfo(
                    syslog_port=1080,
                    syslog_server="sysloghost-1.com",
                ),
            ],
        ),
        system_parameters=EditSystemParameters(
            alarms_enabled=True,
            default_volume_limit=10,
            fc_enabled=True,
            group_target_enabled=True,
            iscsi_enabled=True,
            repl_throttle_list=[
                EditThrottle(
                    days="monday,tuesday",
                    description="Throttle one",
                    thr_at_time=10800,
                    thr_bandwidth=14,
                    thr_bandwidth_kbps=1400,
                    thr_bandwidth_limit_kbps=1400,
                    thr_until_time=14400,
                ),
            ],
            vss_validation_timeout=60,
        ),
    ) # NimbleEditSystemSettings | 

    # example passing only required values which don't have defaults set
    try:
        # Edit system settings of Nimble / Alletra 6K
        api_response = api_instance.device_type2_edit_system_settings(system_id, nimble_edit_system_settings)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_application_servers**
> ApplicationServersList device_type2_get_all_application_servers(system_id)

Get all application servers details by Nimble / Alletra 6K

Get all application servers details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.application_servers_list import ApplicationServersList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter application servers by Key. (optional)
    sort = "name desc" # str | oData query to sort application servers by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all application servers details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_application_servers(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_all_application_servers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all application servers details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_application_servers(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_network_settings**
> NimbleNetworkSettingsList device_type2_get_all_network_settings(system_id)

Get all network settings details by Nimble / Alletra 6K

Get all network settings details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.nimble_network_settings_list import NimbleNetworkSettingsList
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter network settings by Key. (optional)
    sort = "name desc" # str | oData query to sort network settings resource by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all network settings details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_network_settings(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_all_network_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all network settings details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_network_settings(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage group object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_application_server_by_id**
> ApplicationServerDetails device_type2_get_application_server_by_id(system_id, application_server_id)

Get details of Nimble / Alletra 6K application server identified by {applicationServerId}

Get details of Nimble / Alletra 6K application server identified by {applicationServerId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.application_server_details import ApplicationServerDetails
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    application_server_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of application server. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K application server identified by {applicationServerId}
        api_response = api_instance.device_type2_get_application_server_by_id(system_id, application_server_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_application_server_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K application server identified by {applicationServerId}
        api_response = api_instance.device_type2_get_application_server_by_id(system_id, application_server_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_network_setting_by_id**
> NimbleNetworkSettingsDetailsWithRequestUri device_type2_get_network_setting_by_id(system_id, network_setting_id)

Get details of Nimble / Alletra 6K network setting identified by {networkSettingId}

Get details of Nimble / Alletra 6K network setting identified by {networkSettingId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_network_settings_details_with_request_uri import NimbleNetworkSettingsDetailsWithRequestUri
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    network_setting_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | Identifier of network setting. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K network setting identified by {networkSettingId}
        api_response = api_instance.device_type2_get_network_setting_by_id(system_id, network_setting_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_network_setting_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K network setting identified by {networkSettingId}
        api_response = api_instance.device_type2_get_network_setting_by_id(system_id, network_setting_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | network settings object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_replication_partners**
> NimbleReplicationPartnersList device_type2_get_replication_partners(system_id)

Get all replication-partners details for Nimble / Alletra 6K

Get all replication-partners details for Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_replication_partners_list import NimbleReplicationPartnersList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter replication partners by Key. (optional)
    sort = "name desc" # str | oData query to sort replication partner resource by Key. (optional)
    include_indirect_partners = True # bool | Include indirect partners. Indirect partners are excluded by default. This parameter cannot be used with other query parameters. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all replication-partners details for Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_replication_partners(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_replication_partners: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all replication-partners details for Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_replication_partners(system_id, limit=limit, offset=offset, filter=filter, sort=sort, include_indirect_partners=include_indirect_partners, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_replication_partners_by_id**
> NimbleReplicationPartnerDetails device_type2_get_replication_partners_by_id(system_id, replicationpartner_id)

Get details of Nimble / Alletra 6K replication-partner identified by {replicationpartnerId}

Get details of Nimble / Alletra 6K replication-partner identified by {replicationpartnerId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_replication_partner_details import NimbleReplicationPartnerDetails
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    replicationpartner_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | Identifier of replicationpartner. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K replication-partner identified by {replicationpartnerId}
        api_response = api_instance.device_type2_get_replication_partners_by_id(system_id, replicationpartner_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_replication_partners_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K replication-partner identified by {replicationpartnerId}
        api_response = api_instance.device_type2_get_replication_partners_by_id(system_id, replicationpartner_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_witnesses**
> NimbleWitnessesList device_type2_get_witnesses(system_id)

Get all witness configuration details by Nimble / Alletra 6K

Get all witness configuration details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.nimble_witnesses_list import NimbleWitnessesList
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004007" # str | Lucene query to filter witnesses by Key. (optional)
    sort = "name desc" # str | oData query to sort witnesses resource by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all witness configuration details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_witnesses(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_witnesses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all witness configuration details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_witnesses(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_witnesses_by_id**
> NimbleWitnessDetails device_type2_get_witnesses_by_id(system_id, witness_id)

Get details of Nimble / Alletra 6K witness configuration identified by {witnessId}

Get details of Nimble / Alletra 6K witness configuration identified by {witnessId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.nimble_witness_details import NimbleWitnessDetails
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    witness_id = "2a0df0fe6f7dc7bb16000000000000000000004007" # str | Identifier of witness. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K witness configuration identified by {witnessId}
        api_response = api_instance.device_type2_get_witnesses_by_id(system_id, witness_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling SystemSettingsApi->device_type2_get_witnesses_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K witness configuration identified by {witnessId}
        api_response = api_instance.device_type2_get_witnesses_by_id(system_id, witness_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_pause_replication_partner**
> TaskResponse device_type2_pause_replication_partner(system_id, pause_resume_nimble_replication_partner_pair_input)

Pause the replication pair of Nimble / Alletra 6K

Pause the replication pair of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.pause_resume_nimble_replication_partner_pair_input import PauseResumeNimbleReplicationPartnerPairInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    pause_resume_nimble_replication_partner_pair_input = PauseResumeNimbleReplicationPartnerPairInput(
        replication_partners=[
            ReplicationPartnerPairAction(
                replication_partner_system_id="7a0ef0fe6f7dc7bb16000000000000000000001257",
                src_replication_id="3a0df0fe6f7dc7bb16000000000000000000003467",
                target_replication_id="1a0hf0fe6f7dc7bb16000000000000000000007835",
            ),
        ],
    ) # PauseResumeNimbleReplicationPartnerPairInput | 

    # example passing only required values which don't have defaults set
    try:
        # Pause the replication pair of Nimble / Alletra 6K
        api_response = api_instance.device_type2_pause_replication_partner(system_id, pause_resume_nimble_replication_partner_pair_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_application_server_by_id**
> TaskResponse device_type2_remove_application_server_by_id(system_id, application_server_id)

Remove application server identified by {applicationServerId} from Nimble / Alletra 6K

Remove application server identified by {applicationServerId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    application_server_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of application server. A 42 digit hexadecimal number.

    # example passing only required values which don't have defaults set
    try:
        # Remove application server identified by {applicationServerId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_application_server_by_id(system_id, application_server_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_replication_partner**
> TaskResponse device_type2_remove_replication_partner(system_id, remove_replication_partners)

Remove list of replication partner for Nimble / Alletra 6K

Remove list of replication partner for Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.remove_replication_partners import RemoveReplicationPartners
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    remove_replication_partners = RemoveReplicationPartners(
        replication_partners=[
            ReplicationPartnerPairAction(
                replication_partner_system_id="7a0ef0fe6f7dc7bb16000000000000000000001257",
                src_replication_id="3a0df0fe6f7dc7bb16000000000000000000003467",
                target_replication_id="1a0hf0fe6f7dc7bb16000000000000000000007835",
            ),
        ],
    ) # RemoveReplicationPartners | 

    # example passing only required values which don't have defaults set
    try:
        # Remove list of replication partner for Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_replication_partner(system_id, remove_replication_partners)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_witnesses_by_id**
> TaskResponse device_type2_remove_witnesses_by_id(system_id, witness_id)

Remove witness identified by {witnessId} from Nimble / Alletra 6K

Remove witness identified by {witnessId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    witness_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | Identifier of witness. A 42 digit hexadecimal number.

    # example passing only required values which don't have defaults set
    try:
        # Remove witness identified by {witnessId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_witnesses_by_id(system_id, witness_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_resume_replication_partner**
> TaskResponse device_type2_resume_replication_partner(system_id, pause_resume_nimble_replication_partner_pair_input)

Resume the replication pair of Nimble / Alletra 6K

Resume the replication pair of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.pause_resume_nimble_replication_partner_pair_input import PauseResumeNimbleReplicationPartnerPairInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    pause_resume_nimble_replication_partner_pair_input = PauseResumeNimbleReplicationPartnerPairInput(
        replication_partners=[
            ReplicationPartnerPairAction(
                replication_partner_system_id="7a0ef0fe6f7dc7bb16000000000000000000001257",
                src_replication_id="3a0df0fe6f7dc7bb16000000000000000000003467",
                target_replication_id="1a0hf0fe6f7dc7bb16000000000000000000007835",
            ),
        ],
    ) # PauseResumeNimbleReplicationPartnerPairInput | 

    # example passing only required values which don't have defaults set
    try:
        # Resume the replication pair of Nimble / Alletra 6K
        api_response = api_instance.device_type2_resume_replication_partner(system_id, pause_resume_nimble_replication_partner_pair_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_send_auto_support**
> TaskResponse device_type2_send_auto_support(system_id)

Send auto support information of Nimble / Alletra 6K identified by {systemId}

Send auto support information of Nimble / Alletra 6K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system

    # example passing only required values which don't have defaults set
    try:
        # Send auto support information of Nimble / Alletra 6K identified by {systemId}
        api_response = api_instance.device_type2_send_auto_support(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_test_replication_configuration**
> TaskResponseReplication device_type2_test_replication_configuration(system_id, pause_resume_nimble_replication_partner_pair_input)

Test the replication partner pair of Nimble / Alletra 6K

Test the replication partner pair of Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.task_response_replication import TaskResponseReplication
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.pause_resume_nimble_replication_partner_pair_input import PauseResumeNimbleReplicationPartnerPairInput
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    pause_resume_nimble_replication_partner_pair_input = PauseResumeNimbleReplicationPartnerPairInput(
        replication_partners=[
            ReplicationPartnerPairAction(
                replication_partner_system_id="7a0ef0fe6f7dc7bb16000000000000000000001257",
                src_replication_id="3a0df0fe6f7dc7bb16000000000000000000003467",
                target_replication_id="1a0hf0fe6f7dc7bb16000000000000000000007835",
            ),
        ],
    ) # PauseResumeNimbleReplicationPartnerPairInput | 

    # example passing only required values which don't have defaults set
    try:
        # Test the replication partner pair of Nimble / Alletra 6K
        api_response = api_instance.device_type2_test_replication_configuration(system_id, pause_resume_nimble_replication_partner_pair_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_test_witnesses_by_id**
> NimbleTestWitnessResponse device_type2_test_witnesses_by_id(system_id, witness_id)

Test and validate the witness configuration between the host identified by {witnessId} from Nimble / Alletra 6K identified by {systemId}

Test and validate the witness configuration between the host identified by {witnessId} from Nimble / Alletra 6K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_test_witness_response import NimbleTestWitnessResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    witness_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | Identifier of witness. A 42 digit hexadecimal number.

    # example passing only required values which don't have defaults set
    try:
        # Test and validate the witness configuration between the host identified by {witnessId} from Nimble / Alletra 6K identified by {systemId}
        api_response = api_instance.device_type2_test_witnesses_by_id(system_id, witness_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_settings_associate**
> TaskResponse mail_settings_associate(system_id, mailsettings_input)

Add SMTP/Mail server settigs

Add SMTP/Mail server settigs

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.mailsettings_input import MailsettingsInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    mailsettings_input = MailsettingsInput(
        mail_host_domain="hpe.com",
        mail_host_server="smtp1.hpe.com",
        port=25,
        sender_email_id="sender_email_id_example",
    ) # MailsettingsInput | 

    # example passing only required values which don't have defaults set
    try:
        # Add SMTP/Mail server settigs
        api_response = api_instance.mail_settings_associate(system_id, mailsettings_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_settings_delete**
> TaskResponse mail_settings_delete(system_id)

Delete SMTP/mail server settings

Delete SMTP/mail server settings

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system

    # example passing only required values which don't have defaults set
    try:
        # Delete SMTP/mail server settings
        api_response = api_instance.mail_settings_delete(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_settings_update**
> TaskResponse mail_settings_update(system_id, mailsettings_input)

Edit SMTP/Mail server settigs

Edit SMTP/Mail server settigs

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.mailsettings_input import MailsettingsInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    mailsettings_input = MailsettingsInput(
        mail_host_domain="hpe.com",
        mail_host_server="smtp1.hpe.com",
        port=25,
        sender_email_id="sender_email_id_example",
    ) # MailsettingsInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit SMTP/Mail server settigs
        api_response = api_instance.mail_settings_update(system_id, mailsettings_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_service_cim_update**
> TaskResponse network_service_cim_update(system_id, nw_cim_edit)

Edit CIM network service configuration

Edit CIM network service configuration

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.nw_cim_edit import NwCimEdit
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    nw_cim_edit = NwCimEdit(
        cim=None,
    ) # NwCimEdit | 

    # example passing only required values which don't have defaults set
    try:
        # Edit CIM network service configuration
        api_response = api_instance.network_service_cim_update(system_id, nw_cim_edit)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_service_snmp_mgr_create**
> TaskResponse network_service_snmp_mgr_create(system_id, nw_add_snmp_mgr)

Add SNMP Manager settings

Add SNMP Manager settings

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.nw_add_snmp_mgr import NwAddSnmpMgr
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    nw_add_snmp_mgr = NwAddSnmpMgr(
        snmp_config=[
            SnmpConfigParams(
                manager_ip="15.218.169.163",
                notify="STANDARD",
                port=162,
                retry=2,
                timeout_secs=162,
                user="user1",
                version=2,
            ),
        ],
    ) # NwAddSnmpMgr | 

    # example passing only required values which don't have defaults set
    try:
        # Add SNMP Manager settings
        api_response = api_instance.network_service_snmp_mgr_create(system_id, nw_add_snmp_mgr)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_service_snmp_mgr_delete**
> TaskResponse network_service_snmp_mgr_delete(system_id, id)

Delete SNMP manager settings identified by {id}

Delete SNMP manager settings identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | ID of the SNMP manager

    # example passing only required values which don't have defaults set
    try:
        # Delete SNMP manager settings identified by {id}
        api_response = api_instance.network_service_snmp_mgr_delete(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_service_snmp_mgr_update**
> TaskResponse network_service_snmp_mgr_update(system_id, id, nw_snmp_mgr_edit)

Edit SNMP Manager settings for the specified Id

Edit SNMP Manager settings for the specified Id

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nw_snmp_mgr_edit import NwSnmpMgrEdit
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | ID of the SNMP manager
    nw_snmp_mgr_edit = NwSnmpMgrEdit(
        manager_ip="15.218.169.163",
        notify="STANDARD",
        port=162,
        retry=2,
        timeout_secs=162,
        user="user1",
        version=2,
    ) # NwSnmpMgrEdit | 

    # example passing only required values which don't have defaults set
    try:
        # Edit SNMP Manager settings for the specified Id
        api_response = api_instance.network_service_snmp_mgr_update(system_id, id, nw_snmp_mgr_edit)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_settings_associate**
> TaskResponse network_settings_associate(system_id, edit_network_settings_input)

Post Network-Settings details for a storage system Primera / Alletra 9K

Post Network-Settings details for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from greenlake_data_services.model.edit_network_settings_input import EditNetworkSettingsInput
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    edit_network_settings_input = EditNetworkSettingsInput(
        dns_addresses=[
            "dns_addresses_example",
        ],
        ipv4_address="ipv4_address_example",
        ipv4_gateway="ipv4_gateway_example",
        ipv4_subnet_mask="ipv4_subnet_mask_example",
        ipv6_address="ipv6_address_example",
        ipv6_gateway="ipv6_gateway_example",
        ipv6_prefix_len="ipv6_prefix_len_example",
        proxy_params=EditNetworkSettingsInputProxyParams(
            authentication_required="authentication_required_example",
            proxy_password="proxy_password_example",
            proxy_port=1,
            proxy_protocol="proxy_protocol_example",
            proxy_server="proxy_server_example",
            proxy_user="proxy_user_example",
        ),
    ) # EditNetworkSettingsInput | 

    # example passing only required values which don't have defaults set
    try:
        # Post Network-Settings details for a storage system Primera / Alletra 9K
        api_response = api_instance.network_settings_associate(system_id, edit_network_settings_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_certificate**
> TaskResponse post_certificate(system_id, create_certificate_input)

Create certificate on storage system Primera / Alletra 9K identified by {systemId}

Create certificate on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.create_certificate_input import CreateCertificateInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    create_certificate_input = CreateCertificateInput(
        authority_chain="-----BEGIN CERTIFICATE REQUEST-----abc----END CERTIFICATE REQUEST-----",
        common_name="hpe.com CA - Intermediate",
        country="IN",
        days=365,
        key_length=2048,
        locality="BLR",
        organization="HPE",
        organization_unit="HPE Primera",
        province="Karnataka",
        service="QW_CLIENT",
        subject_alt_name=CertSubjectAltName(
            dns="7CE815P2BH",
            ip="15.213.65.129",
            email="abc@hpe.com",
        ),
        type="csr",
    ) # CreateCertificateInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create certificate on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.post_certificate(system_id, create_certificate_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_certificate**
> TaskResponse put_certificate(system_id, id, import_certificate_input)

Import certificate identified by {id} on storage system Primera / Alletra 9K identified by {systemId}

Import certificate identified by {id} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.import_certificate_input import ImportCertificateInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "99691e493067b2b2acf1774fc0ccc011" # str | ID of the certificate
    import_certificate_input = ImportCertificateInput(
        authority_chain="-----BEGIN CERTIFICATE REQUEST-----abc----END CERTIFICATE REQUEST----- \n-----BEGIN CERTIFICATE REQUEST-----pqr----END CERTIFICATE REQUEST-----",
        certificate="-----BEGIN CERTIFICATE REQUEST-----abc----END CERTIFICATE REQUEST-----",
    ) # ImportCertificateInput | 

    # example passing only required values which don't have defaults set
    try:
        # Import certificate identified by {id} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.put_certificate(system_id, id, import_certificate_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_certificates**
> TaskResponse remove_certificates(system_id, remove_certificates_input)

Delete certificates from storage system Primera / Alletra 9K identified by {systemId}

Delete certificates from storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.remove_certificates_input import RemoveCertificatesInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    remove_certificates_input = RemoveCertificatesInput(
        certificates=[
            RemoveCertificateInput(
                certificate="99691e493067b2b2acf1774fc0ccc011",
            ),
        ],
    ) # RemoveCertificatesInput | 

    # example passing only required values which don't have defaults set
    try:
        # Delete certificates from storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.remove_certificates(system_id, remove_certificates_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_settings_associate**
> TaskResponse support_settings_associate(system_id, support_settings_input)

Add support settings for a storage system Primera / Alletra 9K

Add support settings for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from greenlake_data_services.model.support_settings_input import SupportSettingsInput
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    support_settings_input = SupportSettingsInput(
        connect_to_hpe="connect_to_hpe_example",
        device_id="device_id_example",
        enterprise_server_url="enterprise_server_url_example",
        mini_insplore_enabled="mini_insplore_enabled_example",
        rap_forwarding="rap_forwarding_example",
        remote_access="DISABLE",
        rts_enabled="rts_enabled_example",
    ) # SupportSettingsInput | 

    # example passing only required values which don't have defaults set
    try:
        # Add support settings for a storage system Primera / Alletra 9K
        api_response = api_instance.support_settings_associate(system_id, support_settings_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_settings_update**
> TaskResponse support_settings_update(system_id, support_settings_input)

Edit support settings for a storage system Primera / Alletra 9K

Edit support settings for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from greenlake_data_services.model.support_settings_input import SupportSettingsInput
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    support_settings_input = SupportSettingsInput(
        connect_to_hpe="connect_to_hpe_example",
        device_id="device_id_example",
        enterprise_server_url="enterprise_server_url_example",
        mini_insplore_enabled="mini_insplore_enabled_example",
        rap_forwarding="rap_forwarding_example",
        remote_access="DISABLE",
        rts_enabled="rts_enabled_example",
    ) # SupportSettingsInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit support settings for a storage system Primera / Alletra 9K
        api_response = api_instance.support_settings_update(system_id, support_settings_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_associate**
> TaskResponse system_settings_associate(system_id, system_config_params_edit_input)

Edit system settings configuration

Edit system settings configuration

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.system_config_params_edit_input import SystemConfigParamsEditInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    system_config_params_edit_input = SystemConfigParamsEditInput(
        auth_mode=None,
        date_time="01/15/2020 10:00:00",
        installation_sites=None,
        name="Array1",
        ntp_addresses=[
            "ntp_addresses_example",
        ],
        remote_syslog_settings=None,
        srinfo=None,
        support_contact=ContactsEditDetails(
            company="HPE",
            company_code="HPE",
            country="US",
            fax="fax_id",
            first_name="john",
            id="67d09515-8526-9b02-c0c4-c1f443a39402",
            include_svc_alerts=False,
            last_name="kevin",
            notification_severities=[0,1,2,3,4,5],
            preferred_language="en",
            primary_email="kevin.john@hpe.com",
            primary_phone="98783456",
            receive_email=True,
            receive_grouped=True,
            secondary_email="winny.pooh@hpe.com",
            secondary_phone="23456789",
            system_id="7CE751P312",
        ),
        system_parameters=None,
        timezone="Asia/Calcutta",
    ) # SystemConfigParamsEditInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit system settings configuration
        api_response = api_instance.system_settings_associate(system_id, system_config_params_edit_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_update**
> TaskResponse system_settings_update(system_id, system_config_params_edit_input)

Edit system settings configuration

Edit system settings configuration

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import system_settings_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.system_config_params_edit_input import SystemConfigParamsEditInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_settings_api.SystemSettingsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    system_config_params_edit_input = SystemConfigParamsEditInput(
        auth_mode=None,
        date_time="01/15/2020 10:00:00",
        installation_sites=None,
        name="Array1",
        ntp_addresses=[
            "ntp_addresses_example",
        ],
        remote_syslog_settings=None,
        srinfo=None,
        support_contact=ContactsEditDetails(
            company="HPE",
            company_code="HPE",
            country="US",
            fax="fax_id",
            first_name="john",
            id="67d09515-8526-9b02-c0c4-c1f443a39402",
            include_svc_alerts=False,
            last_name="kevin",
            notification_severities=[0,1,2,3,4,5],
            preferred_language="en",
            primary_email="kevin.john@hpe.com",
            primary_phone="98783456",
            receive_email=True,
            receive_grouped=True,
            secondary_email="winny.pooh@hpe.com",
            secondary_phone="23456789",
            system_id="7CE751P312",
        ),
        system_parameters=None,
        timezone="Asia/Calcutta",
    ) # SystemConfigParamsEditInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit system settings configuration
        api_response = api_instance.system_settings_update(system_id, system_config_params_edit_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

