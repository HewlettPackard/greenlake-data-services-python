# EncryptionSettings

How encryption is configured for this group. Group encryption settings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cipher** | **str, none_type** | Type of encryption cipher used. Possible values: &#39;aes_256_xts&#39;, &#39;none&#39;. | [optional] 
**encryption_active** | **bool, none_type** | Is encryption active (output only). | [optional] 
**encryption_key_manager** | **str, none_type** | Is the master key on local or external key manager (output only). Possible values: &#39;external&#39;, &#39;local&#39;. | [optional] 
**master_key_set** | **bool, none_type** | Is the master key set (output only). | [optional] 
**mode** | **str, none_type** | Mode of encryption. Possible values: &#39;available&#39;, &#39;none&#39;, &#39;secure&#39;. | [optional] 
**scope** | **str, none_type** | Encryption scope. Possible values: &#39;volume&#39;, &#39;pool&#39;, &#39;none&#39;, &#39;group&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


