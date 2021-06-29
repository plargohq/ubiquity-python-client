"""
    Ubiquity REST API

    Ubiquity provides a RESTful and uniform way to access blockchain resources, with a rich and reusable model across multiple cryptocurrencies.  [Documentation](https://app.blockdaemon.com/docs/ubiquity)  ### Protocols #### Mainnet The following protocols are currently supported: * bitcoin * ethereum * polkadot * xrp * algorand * stellar * dogecoin  #### Testnet * bitcoin/testnet * ethereum/ropsten * dogecoin/testnet  ##### Pagination Certain resources contain a lot of data, more than what's practical to return for a single request. With the help of pagination, the data is split across multiple responses. Each response returns a subset of the items requested and a continuation token.  To get the next batch of items, copy the returned continuation token to the continuation query parameter and repeat the request with the new URL. In case no continuation token is returned, there is no more data available.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@blockdaemon.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ubiquity.ubiquity_openapi_client.model_utils import (  # noqa: F401
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
)
from ..model_utils import OpenApiModel
from ubiquity.ubiquity_openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from ubiquity.ubiquity_openapi_client.model.report_field_meta import ReportFieldMeta
    globals()['ReportFieldMeta'] = ReportFieldMeta


class ReportField(ModelNormal):
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
            'protocol': (str,),  # noqa: E501
            'address': (str,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'event_id': (str,),  # noqa: E501
            'block': (int,),  # noqa: E501
            'timestamp': (int,),  # noqa: E501
            'hash': (str,),  # noqa: E501
            'action': (str,),  # noqa: E501
            'value': (str,),  # noqa: E501
            'sender_address': (str,),  # noqa: E501
            'fee': (str,),  # noqa: E501
            'decimals': (int,),  # noqa: E501
            'meta': (ReportFieldMeta,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'protocol': 'protocol',  # noqa: E501
        'address': 'address',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'event_id': 'event_id',  # noqa: E501
        'block': 'block',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'hash': 'hash',  # noqa: E501
        'action': 'action',  # noqa: E501
        'value': 'value',  # noqa: E501
        'sender_address': 'sender_address',  # noqa: E501
        'fee': 'fee',  # noqa: E501
        'decimals': 'decimals',  # noqa: E501
        'meta': 'meta',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, protocol, address, currency, event_id, block, timestamp, hash, action, value, sender_address, fee, decimals, *args, **kwargs):  # noqa: E501
        """ReportField - a model defined in OpenAPI

        Args:
            protocol (str): The protocol the address relates to
            address (str): The wallet/account the transaction occurred
            currency (str): The currency symbol
            event_id (str): The ID of the event within a transaction
            block (int): The block number the transaction occurred on
            timestamp (int): The unix timestamp when the transaction was added to a block
            hash (str): The transaction ID
            action (str): The action type e.g. Transfer, Deposit, Staking Reward etc..
            value (str): The amount of currency involved in the transaction (smallest unit)
            sender_address (str): The address where the funds originated
            fee (str): How much was charged as a fee for processing the transaction
            decimals (int): The number of decimals in one coin, used to convert smallest unit to 1 whole coin if needed

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
            meta (ReportFieldMeta): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
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

        self.protocol = protocol
        self.address = address
        self.currency = currency
        self.event_id = event_id
        self.block = block
        self.timestamp = timestamp
        self.hash = hash
        self.action = action
        self.value = value
        self.sender_address = sender_address
        self.fee = fee
        self.decimals = decimals
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
    def __init__(self, protocol, address, currency, event_id, block, timestamp, hash, action, value, sender_address, fee, decimals, *args, **kwargs):  # noqa: E501
        """ReportField - a model defined in OpenAPI

        Args:
            protocol (str): The protocol the address relates to
            address (str): The wallet/account the transaction occurred
            currency (str): The currency symbol
            event_id (str): The ID of the event within a transaction
            block (int): The block number the transaction occurred on
            timestamp (int): The unix timestamp when the transaction was added to a block
            hash (str): The transaction ID
            action (str): The action type e.g. Transfer, Deposit, Staking Reward etc..
            value (str): The amount of currency involved in the transaction (smallest unit)
            sender_address (str): The address where the funds originated
            fee (str): How much was charged as a fee for processing the transaction
            decimals (int): The number of decimals in one coin, used to convert smallest unit to 1 whole coin if needed

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
            meta (ReportFieldMeta): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
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

        self.protocol = protocol
        self.address = address
        self.currency = currency
        self.event_id = event_id
        self.block = block
        self.timestamp = timestamp
        self.hash = hash
        self.action = action
        self.value = value
        self.sender_address = sender_address
        self.fee = fee
        self.decimals = decimals
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
