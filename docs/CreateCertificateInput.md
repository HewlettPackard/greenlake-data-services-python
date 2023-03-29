# CreateCertificateInput

Create Certificate input.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** | Name of service the certificate is for. | 
**type** | **str** | Type of certificate to create. | 
**authority_chain** | **str** | The authority chain for Quorum Witness server certificate. | [optional] 
**common_name** | **str** | CommonName for the certificate. | [optional] 
**country** | **str** | Two-letter code for the country where organization is located. | [optional] 
**days** | **int** | Number of days valid for the certificate. | [optional] 
**key_length** | **int** | Key length for the certificate. | [optional] 
**locality** | **str** | Locality where organization is located. | [optional] 
**organization** | **str** | Organization for the certificate | [optional] 
**organization_unit** | **str** | Division of organization handling the certificate. | [optional] 
**province** | **str** | Province where organization is located. | [optional] 
**subject_alt_name** | [**CertSubjectAltName**](CertSubjectAltName.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


