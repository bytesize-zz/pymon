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

from swagger_client.models.get_characters_character_id_wallet_journal_extra_info import GetCharactersCharacterIdWalletJournalExtraInfo  # noqa: F401,E501


class GetCharactersCharacterIdWalletJournal200Ok(object):
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
        'date': 'datetime',
        'ref_id': 'int',
        'ref_type': 'str',
        'first_party_id': 'int',
        'first_party_type': 'str',
        'second_party_id': 'int',
        'second_party_type': 'str',
        'amount': 'float',
        'balance': 'float',
        'reason': 'str',
        'tax_receiver_id': 'int',
        'tax': 'float',
        'extra_info': 'GetCharactersCharacterIdWalletJournalExtraInfo'
    }

    attribute_map = {
        'date': 'date',
        'ref_id': 'ref_id',
        'ref_type': 'ref_type',
        'first_party_id': 'first_party_id',
        'first_party_type': 'first_party_type',
        'second_party_id': 'second_party_id',
        'second_party_type': 'second_party_type',
        'amount': 'amount',
        'balance': 'balance',
        'reason': 'reason',
        'tax_receiver_id': 'tax_receiver_id',
        'tax': 'tax',
        'extra_info': 'extra_info'
    }

    def __init__(self, date=None, ref_id=None, ref_type=None, first_party_id=None, first_party_type=None, second_party_id=None, second_party_type=None, amount=None, balance=None, reason=None, tax_receiver_id=None, tax=None, extra_info=None):  # noqa: E501
        """GetCharactersCharacterIdWalletJournal200Ok - a model defined in Swagger"""  # noqa: E501

        self._date = None
        self._ref_id = None
        self._ref_type = None
        self._first_party_id = None
        self._first_party_type = None
        self._second_party_id = None
        self._second_party_type = None
        self._amount = None
        self._balance = None
        self._reason = None
        self._tax_receiver_id = None
        self._tax = None
        self._extra_info = None
        self.discriminator = None

        self.date = date
        self.ref_id = ref_id
        self.ref_type = ref_type
        if first_party_id is not None:
            self.first_party_id = first_party_id
        if first_party_type is not None:
            self.first_party_type = first_party_type
        if second_party_id is not None:
            self.second_party_id = second_party_id
        if second_party_type is not None:
            self.second_party_type = second_party_type
        if amount is not None:
            self.amount = amount
        if balance is not None:
            self.balance = balance
        if reason is not None:
            self.reason = reason
        if tax_receiver_id is not None:
            self.tax_receiver_id = tax_receiver_id
        if tax is not None:
            self.tax = tax
        if extra_info is not None:
            self.extra_info = extra_info

    @property
    def date(self):
        """Gets the date of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501

        Date and time of transaction  # noqa: E501

        :return: The date of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this GetCharactersCharacterIdWalletJournal200Ok.

        Date and time of transaction  # noqa: E501

        :param date: The date of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: datetime
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def ref_id(self):
        """Gets the ref_id of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501

        Unique journal reference ID  # noqa: E501

        :return: The ref_id of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: int
        """
        return self._ref_id

    @ref_id.setter
    def ref_id(self, ref_id):
        """Sets the ref_id of this GetCharactersCharacterIdWalletJournal200Ok.

        Unique journal reference ID  # noqa: E501

        :param ref_id: The ref_id of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: int
        """
        if ref_id is None:
            raise ValueError("Invalid value for `ref_id`, must not be `None`")  # noqa: E501

        self._ref_id = ref_id

    @property
    def ref_type(self):
        """Gets the ref_type of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501

        Transaction type, different type of transaction will populate different fields in `extra_info` Note: If you have an existing XML API application that is using ref_types, you will need to know which string ESI ref_type maps to which integer. You can use the following gist to see string->int mappings: https://gist.github.com/ccp-zoetrope/c03db66d90c2148724c06171bc52e0ec  # noqa: E501

        :return: The ref_type of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: str
        """
        return self._ref_type

    @ref_type.setter
    def ref_type(self, ref_type):
        """Sets the ref_type of this GetCharactersCharacterIdWalletJournal200Ok.

        Transaction type, different type of transaction will populate different fields in `extra_info` Note: If you have an existing XML API application that is using ref_types, you will need to know which string ESI ref_type maps to which integer. You can use the following gist to see string->int mappings: https://gist.github.com/ccp-zoetrope/c03db66d90c2148724c06171bc52e0ec  # noqa: E501

        :param ref_type: The ref_type of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: str
        """
        if ref_type is None:
            raise ValueError("Invalid value for `ref_type`, must not be `None`")  # noqa: E501
        allowed_values = ["acceleration_gate_fee", "advertisement_listing_fee", "agent_donation", "agent_location_services", "agent_miscellaneous", "agent_mission_collateral_paid", "agent_mission_collateral_refunded", "agent_mission_reward", "agent_mission_reward_corporation_tax", "agent_mission_time_bonus_reward", "agent_mission_time_bonus_reward_corporation_tax", "agent_security_services", "agent_services_rendered", "agents_preward", "alliance_maintainance_fee", "alliance_registration_fee", "asset_safety_recovery_tax", "bounty", "bounty_prize", "bounty_prize_corporation_tax", "bounty_prizes", "bounty_reimbursement", "bounty_surcharge", "brokers_fee", "clone_activation", "clone_transfer", "contraband_fine", "contract_auction_bid", "contract_auction_bid_corp", "contract_auction_bid_refund", "contract_auction_sold", "contract_brokers_fee", "contract_brokers_fee_corp", "contract_collateral", "contract_collateral_deposited_corp", "contract_collateral_payout", "contract_collateral_refund", "contract_deposit", "contract_deposit_corp", "contract_deposit_refund", "contract_deposit_sales_tax", "contract_price", "contract_price_payment_corp", "contract_reversal", "contract_reward", "contract_reward_deposited", "contract_reward_deposited_corp", "contract_reward_refund", "contract_sales_tax", "copying", "corporate_reward_payout", "corporate_reward_tax", "corporation_account_withdrawal", "corporation_bulk_payment", "corporation_dividend_payment", "corporation_liquidation", "corporation_logo_change_cost", "corporation_payment", "corporation_registration_fee", "courier_mission_escrow", "cspa", "cspaofflinerefund", "datacore_fee", "dna_modification_fee", "docking_fee", "duel_wager_escrow", "duel_wager_payment", "duel_wager_refund", "factory_slot_rental_fee", "gm_cash_transfer", "industry_job_tax", "infrastructure_hub_maintenance", "inheritance", "insurance", "jump_clone_activation_fee", "jump_clone_installation_fee", "kill_right_fee", "lp_store", "manufacturing", "market_escrow", "market_fine_paid", "market_transaction", "medal_creation", "medal_issued", "mission_completion", "mission_cost", "mission_expiration", "mission_reward", "office_rental_fee", "operation_bonus", "opportunity_reward", "planetary_construction", "planetary_export_tax", "planetary_import_tax", "player_donation", "player_trading", "project_discovery_reward", "project_discovery_tax", "reaction", "release_of_impounded_property", "repair_bill", "reprocessing_tax", "researching_material_productivity", "researching_technology", "researching_time_productivity", "resource_wars_reward", "reverse_engineering", "security_processing_fee", "shares", "sovereignity_bill", "store_purchase", "store_purchase_refund", "transaction_tax", "upkeep_adjustment_fee", "war_ally_contract", "war_fee", "war_fee_surrender"]  # noqa: E501
        if ref_type not in allowed_values:
            raise ValueError(
                "Invalid value for `ref_type` ({0}), must be one of {1}"  # noqa: E501
                .format(ref_type, allowed_values)
            )

        self._ref_type = ref_type

    @property
    def first_party_id(self):
        """Gets the first_party_id of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501

        first_party_id integer  # noqa: E501

        :return: The first_party_id of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: int
        """
        return self._first_party_id

    @first_party_id.setter
    def first_party_id(self, first_party_id):
        """Sets the first_party_id of this GetCharactersCharacterIdWalletJournal200Ok.

        first_party_id integer  # noqa: E501

        :param first_party_id: The first_party_id of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: int
        """

        self._first_party_id = first_party_id

    @property
    def first_party_type(self):
        """Gets the first_party_type of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501

        first_party_type string  # noqa: E501

        :return: The first_party_type of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: str
        """
        return self._first_party_type

    @first_party_type.setter
    def first_party_type(self, first_party_type):
        """Sets the first_party_type of this GetCharactersCharacterIdWalletJournal200Ok.

        first_party_type string  # noqa: E501

        :param first_party_type: The first_party_type of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: str
        """
        allowed_values = ["character", "corporation", "alliance", "faction", "system"]  # noqa: E501
        if first_party_type not in allowed_values:
            raise ValueError(
                "Invalid value for `first_party_type` ({0}), must be one of {1}"  # noqa: E501
                .format(first_party_type, allowed_values)
            )

        self._first_party_type = first_party_type

    @property
    def second_party_id(self):
        """Gets the second_party_id of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501

        second_party_id integer  # noqa: E501

        :return: The second_party_id of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: int
        """
        return self._second_party_id

    @second_party_id.setter
    def second_party_id(self, second_party_id):
        """Sets the second_party_id of this GetCharactersCharacterIdWalletJournal200Ok.

        second_party_id integer  # noqa: E501

        :param second_party_id: The second_party_id of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: int
        """

        self._second_party_id = second_party_id

    @property
    def second_party_type(self):
        """Gets the second_party_type of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501

        second_party_type string  # noqa: E501

        :return: The second_party_type of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: str
        """
        return self._second_party_type

    @second_party_type.setter
    def second_party_type(self, second_party_type):
        """Sets the second_party_type of this GetCharactersCharacterIdWalletJournal200Ok.

        second_party_type string  # noqa: E501

        :param second_party_type: The second_party_type of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: str
        """
        allowed_values = ["character", "corporation", "alliance", "faction", "system"]  # noqa: E501
        if second_party_type not in allowed_values:
            raise ValueError(
                "Invalid value for `second_party_type` ({0}), must be one of {1}"  # noqa: E501
                .format(second_party_type, allowed_values)
            )

        self._second_party_type = second_party_type

    @property
    def amount(self):
        """Gets the amount of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501

        Transaction amount. Positive when value transferred to the first party. Negative otherwise  # noqa: E501

        :return: The amount of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetCharactersCharacterIdWalletJournal200Ok.

        Transaction amount. Positive when value transferred to the first party. Negative otherwise  # noqa: E501

        :param amount: The amount of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def balance(self):
        """Gets the balance of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501

        Wallet balance after transaction occurred  # noqa: E501

        :return: The balance of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this GetCharactersCharacterIdWalletJournal200Ok.

        Wallet balance after transaction occurred  # noqa: E501

        :param balance: The balance of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def reason(self):
        """Gets the reason of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501

        reason string  # noqa: E501

        :return: The reason of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this GetCharactersCharacterIdWalletJournal200Ok.

        reason string  # noqa: E501

        :param reason: The reason of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def tax_receiver_id(self):
        """Gets the tax_receiver_id of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501

        the corporation ID receiving any tax paid  # noqa: E501

        :return: The tax_receiver_id of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: int
        """
        return self._tax_receiver_id

    @tax_receiver_id.setter
    def tax_receiver_id(self, tax_receiver_id):
        """Sets the tax_receiver_id of this GetCharactersCharacterIdWalletJournal200Ok.

        the corporation ID receiving any tax paid  # noqa: E501

        :param tax_receiver_id: The tax_receiver_id of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: int
        """

        self._tax_receiver_id = tax_receiver_id

    @property
    def tax(self):
        """Gets the tax of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501

        Tax amount received for tax related transactions  # noqa: E501

        :return: The tax of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this GetCharactersCharacterIdWalletJournal200Ok.

        Tax amount received for tax related transactions  # noqa: E501

        :param tax: The tax of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: float
        """

        self._tax = tax

    @property
    def extra_info(self):
        """Gets the extra_info of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501


        :return: The extra_info of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :rtype: GetCharactersCharacterIdWalletJournalExtraInfo
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this GetCharactersCharacterIdWalletJournal200Ok.


        :param extra_info: The extra_info of this GetCharactersCharacterIdWalletJournal200Ok.  # noqa: E501
        :type: GetCharactersCharacterIdWalletJournalExtraInfo
        """

        self._extra_info = extra_info

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
        if not isinstance(other, GetCharactersCharacterIdWalletJournal200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
