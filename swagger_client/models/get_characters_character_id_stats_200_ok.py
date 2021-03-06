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

from swagger_client.models.get_characters_character_id_stats_character import GetCharactersCharacterIdStatsCharacter  # noqa: F401,E501
from swagger_client.models.get_characters_character_id_stats_combat import GetCharactersCharacterIdStatsCombat  # noqa: F401,E501
from swagger_client.models.get_characters_character_id_stats_industry import GetCharactersCharacterIdStatsIndustry  # noqa: F401,E501
from swagger_client.models.get_characters_character_id_stats_inventory import GetCharactersCharacterIdStatsInventory  # noqa: F401,E501
from swagger_client.models.get_characters_character_id_stats_isk import GetCharactersCharacterIdStatsIsk  # noqa: F401,E501
from swagger_client.models.get_characters_character_id_stats_market import GetCharactersCharacterIdStatsMarket  # noqa: F401,E501
from swagger_client.models.get_characters_character_id_stats_mining import GetCharactersCharacterIdStatsMining  # noqa: F401,E501
from swagger_client.models.get_characters_character_id_stats_module import GetCharactersCharacterIdStatsModule  # noqa: F401,E501
from swagger_client.models.get_characters_character_id_stats_orbital import GetCharactersCharacterIdStatsOrbital  # noqa: F401,E501
from swagger_client.models.get_characters_character_id_stats_pve import GetCharactersCharacterIdStatsPve  # noqa: F401,E501
from swagger_client.models.get_characters_character_id_stats_social import GetCharactersCharacterIdStatsSocial  # noqa: F401,E501
from swagger_client.models.get_characters_character_id_stats_travel import GetCharactersCharacterIdStatsTravel  # noqa: F401,E501


class GetCharactersCharacterIdStats200Ok(object):
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
        'year': 'int',
        'character': 'GetCharactersCharacterIdStatsCharacter',
        'combat': 'GetCharactersCharacterIdStatsCombat',
        'industry': 'GetCharactersCharacterIdStatsIndustry',
        'inventory': 'GetCharactersCharacterIdStatsInventory',
        'isk': 'GetCharactersCharacterIdStatsIsk',
        'market': 'GetCharactersCharacterIdStatsMarket',
        'mining': 'GetCharactersCharacterIdStatsMining',
        'module': 'GetCharactersCharacterIdStatsModule',
        'orbital': 'GetCharactersCharacterIdStatsOrbital',
        'pve': 'GetCharactersCharacterIdStatsPve',
        'social': 'GetCharactersCharacterIdStatsSocial',
        'travel': 'GetCharactersCharacterIdStatsTravel'
    }

    attribute_map = {
        'year': 'year',
        'character': 'character',
        'combat': 'combat',
        'industry': 'industry',
        'inventory': 'inventory',
        'isk': 'isk',
        'market': 'market',
        'mining': 'mining',
        'module': 'module',
        'orbital': 'orbital',
        'pve': 'pve',
        'social': 'social',
        'travel': 'travel'
    }

    def __init__(self, year=None, character=None, combat=None, industry=None, inventory=None, isk=None, market=None, mining=None, module=None, orbital=None, pve=None, social=None, travel=None):  # noqa: E501
        """GetCharactersCharacterIdStats200Ok - a model defined in Swagger"""  # noqa: E501

        self._year = None
        self._character = None
        self._combat = None
        self._industry = None
        self._inventory = None
        self._isk = None
        self._market = None
        self._mining = None
        self._module = None
        self._orbital = None
        self._pve = None
        self._social = None
        self._travel = None
        self.discriminator = None

        self.year = year
        if character is not None:
            self.character = character
        if combat is not None:
            self.combat = combat
        if industry is not None:
            self.industry = industry
        if inventory is not None:
            self.inventory = inventory
        if isk is not None:
            self.isk = isk
        if market is not None:
            self.market = market
        if mining is not None:
            self.mining = mining
        if module is not None:
            self.module = module
        if orbital is not None:
            self.orbital = orbital
        if pve is not None:
            self.pve = pve
        if social is not None:
            self.social = social
        if travel is not None:
            self.travel = travel

    @property
    def year(self):
        """Gets the year of this GetCharactersCharacterIdStats200Ok.  # noqa: E501

        Gregorian year for this set of aggregates  # noqa: E501

        :return: The year of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this GetCharactersCharacterIdStats200Ok.

        Gregorian year for this set of aggregates  # noqa: E501

        :param year: The year of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def character(self):
        """Gets the character of this GetCharactersCharacterIdStats200Ok.  # noqa: E501


        :return: The character of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdStatsCharacter
        """
        return self._character

    @character.setter
    def character(self, character):
        """Sets the character of this GetCharactersCharacterIdStats200Ok.


        :param character: The character of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdStatsCharacter
        """

        self._character = character

    @property
    def combat(self):
        """Gets the combat of this GetCharactersCharacterIdStats200Ok.  # noqa: E501


        :return: The combat of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdStatsCombat
        """
        return self._combat

    @combat.setter
    def combat(self, combat):
        """Sets the combat of this GetCharactersCharacterIdStats200Ok.


        :param combat: The combat of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdStatsCombat
        """

        self._combat = combat

    @property
    def industry(self):
        """Gets the industry of this GetCharactersCharacterIdStats200Ok.  # noqa: E501


        :return: The industry of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdStatsIndustry
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this GetCharactersCharacterIdStats200Ok.


        :param industry: The industry of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdStatsIndustry
        """

        self._industry = industry

    @property
    def inventory(self):
        """Gets the inventory of this GetCharactersCharacterIdStats200Ok.  # noqa: E501


        :return: The inventory of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdStatsInventory
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """Sets the inventory of this GetCharactersCharacterIdStats200Ok.


        :param inventory: The inventory of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdStatsInventory
        """

        self._inventory = inventory

    @property
    def isk(self):
        """Gets the isk of this GetCharactersCharacterIdStats200Ok.  # noqa: E501


        :return: The isk of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdStatsIsk
        """
        return self._isk

    @isk.setter
    def isk(self, isk):
        """Sets the isk of this GetCharactersCharacterIdStats200Ok.


        :param isk: The isk of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdStatsIsk
        """

        self._isk = isk

    @property
    def market(self):
        """Gets the market of this GetCharactersCharacterIdStats200Ok.  # noqa: E501


        :return: The market of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdStatsMarket
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this GetCharactersCharacterIdStats200Ok.


        :param market: The market of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdStatsMarket
        """

        self._market = market

    @property
    def mining(self):
        """Gets the mining of this GetCharactersCharacterIdStats200Ok.  # noqa: E501


        :return: The mining of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdStatsMining
        """
        return self._mining

    @mining.setter
    def mining(self, mining):
        """Sets the mining of this GetCharactersCharacterIdStats200Ok.


        :param mining: The mining of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdStatsMining
        """

        self._mining = mining

    @property
    def module(self):
        """Gets the module of this GetCharactersCharacterIdStats200Ok.  # noqa: E501


        :return: The module of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdStatsModule
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this GetCharactersCharacterIdStats200Ok.


        :param module: The module of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdStatsModule
        """

        self._module = module

    @property
    def orbital(self):
        """Gets the orbital of this GetCharactersCharacterIdStats200Ok.  # noqa: E501


        :return: The orbital of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdStatsOrbital
        """
        return self._orbital

    @orbital.setter
    def orbital(self, orbital):
        """Sets the orbital of this GetCharactersCharacterIdStats200Ok.


        :param orbital: The orbital of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdStatsOrbital
        """

        self._orbital = orbital

    @property
    def pve(self):
        """Gets the pve of this GetCharactersCharacterIdStats200Ok.  # noqa: E501


        :return: The pve of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdStatsPve
        """
        return self._pve

    @pve.setter
    def pve(self, pve):
        """Sets the pve of this GetCharactersCharacterIdStats200Ok.


        :param pve: The pve of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdStatsPve
        """

        self._pve = pve

    @property
    def social(self):
        """Gets the social of this GetCharactersCharacterIdStats200Ok.  # noqa: E501


        :return: The social of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdStatsSocial
        """
        return self._social

    @social.setter
    def social(self, social):
        """Sets the social of this GetCharactersCharacterIdStats200Ok.


        :param social: The social of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdStatsSocial
        """

        self._social = social

    @property
    def travel(self):
        """Gets the travel of this GetCharactersCharacterIdStats200Ok.  # noqa: E501


        :return: The travel of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdStatsTravel
        """
        return self._travel

    @travel.setter
    def travel(self, travel):
        """Sets the travel of this GetCharactersCharacterIdStats200Ok.


        :param travel: The travel of this GetCharactersCharacterIdStats200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdStatsTravel
        """

        self._travel = travel

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
        if not isinstance(other, GetCharactersCharacterIdStats200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
