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


class GetCharactersCharacterIdLoyaltyPoints200Ok(object):
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
        'corporation_id': 'int',
        'loyalty_points': 'int'
    }

    attribute_map = {
        'corporation_id': 'corporation_id',
        'loyalty_points': 'loyalty_points'
    }

    def __init__(self, corporation_id=None, loyalty_points=None):  # noqa: E501
        """GetCharactersCharacterIdLoyaltyPoints200Ok - a model defined in Swagger"""  # noqa: E501

        self._corporation_id = None
        self._loyalty_points = None
        self.discriminator = None

        self.corporation_id = corporation_id
        self.loyalty_points = loyalty_points

    @property
    def corporation_id(self):
        """Gets the corporation_id of this GetCharactersCharacterIdLoyaltyPoints200Ok.  # noqa: E501

        corporation_id integer  # noqa: E501

        :return: The corporation_id of this GetCharactersCharacterIdLoyaltyPoints200Ok.  # noqa: E501
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """Sets the corporation_id of this GetCharactersCharacterIdLoyaltyPoints200Ok.

        corporation_id integer  # noqa: E501

        :param corporation_id: The corporation_id of this GetCharactersCharacterIdLoyaltyPoints200Ok.  # noqa: E501
        :type: int
        """
        if corporation_id is None:
            raise ValueError("Invalid value for `corporation_id`, must not be `None`")  # noqa: E501

        self._corporation_id = corporation_id

    @property
    def loyalty_points(self):
        """Gets the loyalty_points of this GetCharactersCharacterIdLoyaltyPoints200Ok.  # noqa: E501

        loyalty_points integer  # noqa: E501

        :return: The loyalty_points of this GetCharactersCharacterIdLoyaltyPoints200Ok.  # noqa: E501
        :rtype: int
        """
        return self._loyalty_points

    @loyalty_points.setter
    def loyalty_points(self, loyalty_points):
        """Sets the loyalty_points of this GetCharactersCharacterIdLoyaltyPoints200Ok.

        loyalty_points integer  # noqa: E501

        :param loyalty_points: The loyalty_points of this GetCharactersCharacterIdLoyaltyPoints200Ok.  # noqa: E501
        :type: int
        """
        if loyalty_points is None:
            raise ValueError("Invalid value for `loyalty_points`, must not be `None`")  # noqa: E501

        self._loyalty_points = loyalty_points

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
        if not isinstance(other, GetCharactersCharacterIdLoyaltyPoints200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
