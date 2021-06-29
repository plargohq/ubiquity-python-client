# ReportField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The protocol the address relates to | 
**address** | **str** | The wallet/account the transaction occurred | 
**currency** | **str** | The currency symbol | 
**event_id** | **str** | The ID of the event within a transaction | 
**block** | **int** | The block number the transaction occurred on | 
**timestamp** | **int** | The unix timestamp when the transaction was added to a block | 
**hash** | **str** | The transaction ID | 
**action** | **str** | The action type e.g. Transfer, Deposit, Staking Reward etc.. | 
**value** | **str** | The amount of currency involved in the transaction (smallest unit) | 
**sender_address** | **str** | The address where the funds originated | 
**fee** | **str** | How much was charged as a fee for processing the transaction | 
**decimals** | **int** | The number of decimals in one coin, used to convert smallest unit to 1 whole coin if needed | 
**meta** | [**ReportFieldMeta**](ReportFieldMeta.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


