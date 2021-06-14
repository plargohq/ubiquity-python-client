# Tx


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique transaction identifier | [optional] 
**slip44** | **int** | SLIP-44 coin ID | [optional] 
**addresses** | **[str], none_type** | List of involved addresses (excluding contracts) | [optional] 
**assets** | **[str], none_type** | List of moved assets by asset path | [optional] 
**date** | **int** | Unix timestamp | [optional] 
**height** | **int, none_type** | Number of block if mined, otherwise omitted. | [optional] 
**block_id** | **str, none_type** | ID of block if mined, otherwise omitted. | [optional] 
**status** | **str** | Result status of the transaction. | [optional] 
**tags** | **[str], none_type** | List of tags for this transaction | [optional] 
**operations** | [**{str: (Operation,)}**](Operation.md) | Operations in this transaction (opaque keys). | [optional] 
**effects** | [**{str: (Effect,)}**](Effect.md) | Effects by address, if supported | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


