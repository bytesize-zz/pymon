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


class GetCorporationsCorporationIdWallets200Ok(object):
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
        'division': 'int',
        'balance': 'float'
    }

    attribute_map = {
        'division': 'division',
        'balance': 'balance'
    }

    def __init__(self, division=None, balance=None):  # noqa: E501
        """GetCorporationsCorporationIdWallets200Ok - a model defined in Swagger"""  # noqa: E501

        self._division = None
        self._balance = None
        self.discriminator = None

        self.division = division
        self.balance = balance

    @property
    def division(self):
        """Gets the division of this GetCorporationsCorporationIdWallets200Ok.  # noqa: E501

        division integer  # noqa: E501

        :return: The division of this GetCorporationsCorporationIdWallets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._division

    @division.setter
    def division(self, division):
        """Sets the division of this GetCorporationsCorporationIdWallets200Ok.

        division integer  # noqa: E501

        :param division: The division of this GetCorporationsCorporationIdWallets200Ok.  # noqa: E501
        :type: int
        """
        if division is None:
            raise ValueError("Invalid value for `division`, must not be `None`")  # noqa: E501
        if division is not None and division > 7:  # noqa: E501
            raise ValueError("Invalid value for `division`, must be a value less than or equal to `7`")  # noqa: E501
        if division is not None and division < 1:  # noqa: E501
            raise ValueError("Invalid value for `division`, must be a value greater than or equal to `1`")  # noqa: E501

        self._division = division

    @property
    def balance(self):
        """Gets the balance of this GetCorporationsCorporationIdWallets200Ok.  # noqa: E501

        balance number  # noqa: E501

        :return: The balance of this GetCorporationsCorporationIdWallets200Ok.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this GetCorporationsCorporationIdWallets200Ok.

        balance number  # noqa: E501

        :param balance: The balance of this GetCorporationsCorporationIdWallets200Ok.  # noqa: E501
        :type: float
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

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
        if not isinstance(other, GetCorporationsCorporationIdWallets200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other