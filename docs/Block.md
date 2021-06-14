# Block


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Block number | [optional] 
**id** | **str** | Block hash | [optional] 
**parent_id** | **str** | Parent block hash | [optional] 
**date** | **int** | Unix timestamp | [optional] 
**tx_ids** | **[str]** | Complete list of transaction IDs | [optional] 
**txs** | [**[Tx]**](Tx.md) | Partial list of normalized transactions (not filtered or unknown model) | [optional] 
**supply** | [**{str: (Supply,)}**](Supply.md) | Coin supplies with asset paths as keys | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


