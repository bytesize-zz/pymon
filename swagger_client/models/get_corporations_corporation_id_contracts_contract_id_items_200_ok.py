# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 0.7.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetCorporationsCorporationIdContractsContractIdItems200Ok(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'record_id': 'int',
        'type_id': 'int',
        'quantity': 'int',
        'raw_quantity': 'int',
        'is_singleton': 'bool',
        'is_included': 'bool'
    }

    attribute_map = {
        'record_id': 'record_id',
        'type_id': 'type_id',
        'quantity': 'quantity',
        'raw_quantity': 'raw_quantity',
        'is_singleton': 'is_singleton',
        'is_included': 'is_included'
    }

    def __init__(self, record_id=None, type_id=None, quantity=None, raw_quantity=None, is_singleton=None, is_included=None):  # noqa: E501
        """GetCorporationsCorporationIdContractsContractIdItems200Ok - a model defined in Swagger"""  # noqa: E501

        self._record_id = None
        self._type_id = None
        self._quantity = None
        self._raw_quantity = None
        self._is_singleton = None
        self._is_included = None
        self.discriminator = None

        self.record_id = record_id
        self.type_id = type_id
        self.quantity = quantity
        if raw_quantity is not None:
            self.raw_quantity = raw_quantity
        self.is_singleton = is_singleton
        self.is_included = is_included

    @property
    def record_id(self):
        """Gets the record_id of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501

        Unique ID for the item  # noqa: E501

        :return: The record_id of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501
        :rtype: int
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this GetCorporationsCorporationIdContractsContractIdItems200Ok.

        Unique ID for the item  # noqa: E501

        :param record_id: The record_id of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501
        :type: int
        """
        if record_id is None:
            raise ValueError("Invalid value for `record_id`, must not be `None`")  # noqa: E501

        self._record_id = record_id

    @property
    def type_id(self):
        """Gets the type_id of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501

        Type ID for item  # noqa: E501

        :return: The type_id of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCorporationsCorporationIdContractsContractIdItems200Ok.

        Type ID for item  # noqa: E501

        :param type_id: The type_id of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def quantity(self):
        """Gets the quantity of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501

        Number of items in the stack  # noqa: E501

        :return: The quantity of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this GetCorporationsCorporationIdContractsContractIdItems200Ok.

        Number of items in the stack  # noqa: E501

        :param quantity: The quantity of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def raw_quantity(self):
        """Gets the raw_quantity of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501

        -1 indicates that the item is a singleton (non-stackable). If the item happens to be a Blueprint, -1 is an Original and -2 is a Blueprint Copy  # noqa: E501

        :return: The raw_quantity of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501
        :rtype: int
        """
        return self._raw_quantity

    @raw_quantity.setter
    def raw_quantity(self, raw_quantity):
        """Sets the raw_quantity of this GetCorporationsCorporationIdContractsContractIdItems200Ok.

        -1 indicates that the item is a singleton (non-stackable). If the item happens to be a Blueprint, -1 is an Original and -2 is a Blueprint Copy  # noqa: E501

        :param raw_quantity: The raw_quantity of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501
        :type: int
        """

        self._raw_quantity = raw_quantity

    @property
    def is_singleton(self):
        """Gets the is_singleton of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501

        is_singleton boolean  # noqa: E501

        :return: The is_singleton of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._is_singleton

    @is_singleton.setter
    def is_singleton(self, is_singleton):
        """Sets the is_singleton of this GetCorporationsCorporationIdContractsContractIdItems200Ok.

        is_singleton boolean  # noqa: E501

        :param is_singleton: The is_singleton of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501
        :type: bool
        """
        if is_singleton is None:
            raise ValueError("Invalid value for `is_singleton`, must not be `None`")  # noqa: E501

        self._is_singleton = is_singleton

    @property
    def is_included(self):
        """Gets the is_included of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501

        true if the contract issuer has submitted this item with the contract, false if the isser is asking for this item in the contract.  # noqa: E501

        :return: The is_included of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._is_included

    @is_included.setter
    def is_included(self, is_included):
        """Sets the is_included of this GetCorporationsCorporationIdContractsContractIdItems200Ok.

        true if the contract issuer has submitted this item with the contract, false if the isser is asking for this item in the contract.  # noqa: E501

        :param is_included: The is_included of this GetCorporationsCorporationIdContractsContractIdItems200Ok.  # noqa: E501
        :type: bool
        """
        if is_included is None:
            raise ValueError("Invalid value for `is_included`, must not be `None`")  # noqa: E501

        self._is_included = is_included

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetCorporationsCorporationIdContractsContractIdItems200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
