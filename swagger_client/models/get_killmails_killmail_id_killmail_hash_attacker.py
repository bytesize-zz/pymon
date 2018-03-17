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


class GetKillmailsKillmailIdKillmailHashAttacker(object):
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
        'character_id': 'int',
        'corporation_id': 'int',
        'alliance_id': 'int',
        'faction_id': 'int',
        'security_status': 'float',
        'final_blow': 'bool',
        'damage_done': 'int',
        'ship_type_id': 'int',
        'weapon_type_id': 'int'
    }

    attribute_map = {
        'character_id': 'character_id',
        'corporation_id': 'corporation_id',
        'alliance_id': 'alliance_id',
        'faction_id': 'faction_id',
        'security_status': 'security_status',
        'final_blow': 'final_blow',
        'damage_done': 'damage_done',
        'ship_type_id': 'ship_type_id',
        'weapon_type_id': 'weapon_type_id'
    }

    def __init__(self, character_id=None, corporation_id=None, alliance_id=None, faction_id=None, security_status=None, final_blow=None, damage_done=None, ship_type_id=None, weapon_type_id=None):  # noqa: E501
        """GetKillmailsKillmailIdKillmailHashAttacker - a model defined in Swagger"""  # noqa: E501

        self._character_id = None
        self._corporation_id = None
        self._alliance_id = None
        self._faction_id = None
        self._security_status = None
        self._final_blow = None
        self._damage_done = None
        self._ship_type_id = None
        self._weapon_type_id = None
        self.discriminator = None

        if character_id is not None:
            self.character_id = character_id
        if corporation_id is not None:
            self.corporation_id = corporation_id
        if alliance_id is not None:
            self.alliance_id = alliance_id
        if faction_id is not None:
            self.faction_id = faction_id
        self.security_status = security_status
        self.final_blow = final_blow
        self.damage_done = damage_done
        if ship_type_id is not None:
            self.ship_type_id = ship_type_id
        if weapon_type_id is not None:
            self.weapon_type_id = weapon_type_id

    @property
    def character_id(self):
        """Gets the character_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501

        character_id integer  # noqa: E501

        :return: The character_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this GetKillmailsKillmailIdKillmailHashAttacker.

        character_id integer  # noqa: E501

        :param character_id: The character_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :type: int
        """

        self._character_id = character_id

    @property
    def corporation_id(self):
        """Gets the corporation_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501

        corporation_id integer  # noqa: E501

        :return: The corporation_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """Sets the corporation_id of this GetKillmailsKillmailIdKillmailHashAttacker.

        corporation_id integer  # noqa: E501

        :param corporation_id: The corporation_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :type: int
        """

        self._corporation_id = corporation_id

    @property
    def alliance_id(self):
        """Gets the alliance_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501

        alliance_id integer  # noqa: E501

        :return: The alliance_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """Sets the alliance_id of this GetKillmailsKillmailIdKillmailHashAttacker.

        alliance_id integer  # noqa: E501

        :param alliance_id: The alliance_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :type: int
        """

        self._alliance_id = alliance_id

    @property
    def faction_id(self):
        """Gets the faction_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501

        faction_id integer  # noqa: E501

        :return: The faction_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """Sets the faction_id of this GetKillmailsKillmailIdKillmailHashAttacker.

        faction_id integer  # noqa: E501

        :param faction_id: The faction_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :type: int
        """

        self._faction_id = faction_id

    @property
    def security_status(self):
        """Gets the security_status of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501

        Security status for the attacker   # noqa: E501

        :return: The security_status of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :rtype: float
        """
        return self._security_status

    @security_status.setter
    def security_status(self, security_status):
        """Sets the security_status of this GetKillmailsKillmailIdKillmailHashAttacker.

        Security status for the attacker   # noqa: E501

        :param security_status: The security_status of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :type: float
        """
        if security_status is None:
            raise ValueError("Invalid value for `security_status`, must not be `None`")  # noqa: E501

        self._security_status = security_status

    @property
    def final_blow(self):
        """Gets the final_blow of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501

        Was the attacker the one to achieve the final blow   # noqa: E501

        :return: The final_blow of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :rtype: bool
        """
        return self._final_blow

    @final_blow.setter
    def final_blow(self, final_blow):
        """Sets the final_blow of this GetKillmailsKillmailIdKillmailHashAttacker.

        Was the attacker the one to achieve the final blow   # noqa: E501

        :param final_blow: The final_blow of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :type: bool
        """
        if final_blow is None:
            raise ValueError("Invalid value for `final_blow`, must not be `None`")  # noqa: E501

        self._final_blow = final_blow

    @property
    def damage_done(self):
        """Gets the damage_done of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501

        damage_done integer  # noqa: E501

        :return: The damage_done of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :rtype: int
        """
        return self._damage_done

    @damage_done.setter
    def damage_done(self, damage_done):
        """Sets the damage_done of this GetKillmailsKillmailIdKillmailHashAttacker.

        damage_done integer  # noqa: E501

        :param damage_done: The damage_done of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :type: int
        """
        if damage_done is None:
            raise ValueError("Invalid value for `damage_done`, must not be `None`")  # noqa: E501

        self._damage_done = damage_done

    @property
    def ship_type_id(self):
        """Gets the ship_type_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501

        What ship was the attacker flying   # noqa: E501

        :return: The ship_type_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :rtype: int
        """
        return self._ship_type_id

    @ship_type_id.setter
    def ship_type_id(self, ship_type_id):
        """Sets the ship_type_id of this GetKillmailsKillmailIdKillmailHashAttacker.

        What ship was the attacker flying   # noqa: E501

        :param ship_type_id: The ship_type_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :type: int
        """

        self._ship_type_id = ship_type_id

    @property
    def weapon_type_id(self):
        """Gets the weapon_type_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501

        What weapon was used by the attacker for the kill   # noqa: E501

        :return: The weapon_type_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :rtype: int
        """
        return self._weapon_type_id

    @weapon_type_id.setter
    def weapon_type_id(self, weapon_type_id):
        """Sets the weapon_type_id of this GetKillmailsKillmailIdKillmailHashAttacker.

        What weapon was used by the attacker for the kill   # noqa: E501

        :param weapon_type_id: The weapon_type_id of this GetKillmailsKillmailIdKillmailHashAttacker.  # noqa: E501
        :type: int
        """

        self._weapon_type_id = weapon_type_id

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
        if not isinstance(other, GetKillmailsKillmailIdKillmailHashAttacker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
