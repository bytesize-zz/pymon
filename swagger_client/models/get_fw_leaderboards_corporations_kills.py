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

from swagger_client.models.get_fw_leaderboards_corporations_active_total import GetFwLeaderboardsCorporationsActiveTotal  # noqa: F401,E501
from swagger_client.models.get_fw_leaderboards_corporations_last_week import GetFwLeaderboardsCorporationsLastWeek  # noqa: F401,E501
from swagger_client.models.get_fw_leaderboards_corporations_yesterday import GetFwLeaderboardsCorporationsYesterday  # noqa: F401,E501


class GetFwLeaderboardsCorporationsKills(object):
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
        'yesterday': 'list[GetFwLeaderboardsCorporationsYesterday]',
        'last_week': 'list[GetFwLeaderboardsCorporationsLastWeek]',
        'active_total': 'list[GetFwLeaderboardsCorporationsActiveTotal]'
    }

    attribute_map = {
        'yesterday': 'yesterday',
        'last_week': 'last_week',
        'active_total': 'active_total'
    }

    def __init__(self, yesterday=None, last_week=None, active_total=None):  # noqa: E501
        """GetFwLeaderboardsCorporationsKills - a model defined in Swagger"""  # noqa: E501

        self._yesterday = None
        self._last_week = None
        self._active_total = None
        self.discriminator = None

        self.yesterday = yesterday
        self.last_week = last_week
        self.active_total = active_total

    @property
    def yesterday(self):
        """Gets the yesterday of this GetFwLeaderboardsCorporationsKills.  # noqa: E501

        Top 10 ranking of corporations by kills in the past day  # noqa: E501

        :return: The yesterday of this GetFwLeaderboardsCorporationsKills.  # noqa: E501
        :rtype: list[GetFwLeaderboardsCorporationsYesterday]
        """
        return self._yesterday

    @yesterday.setter
    def yesterday(self, yesterday):
        """Sets the yesterday of this GetFwLeaderboardsCorporationsKills.

        Top 10 ranking of corporations by kills in the past day  # noqa: E501

        :param yesterday: The yesterday of this GetFwLeaderboardsCorporationsKills.  # noqa: E501
        :type: list[GetFwLeaderboardsCorporationsYesterday]
        """
        if yesterday is None:
            raise ValueError("Invalid value for `yesterday`, must not be `None`")  # noqa: E501

        self._yesterday = yesterday

    @property
    def last_week(self):
        """Gets the last_week of this GetFwLeaderboardsCorporationsKills.  # noqa: E501

        Top 10 ranking of corporations by kills in the past week  # noqa: E501

        :return: The last_week of this GetFwLeaderboardsCorporationsKills.  # noqa: E501
        :rtype: list[GetFwLeaderboardsCorporationsLastWeek]
        """
        return self._last_week

    @last_week.setter
    def last_week(self, last_week):
        """Sets the last_week of this GetFwLeaderboardsCorporationsKills.

        Top 10 ranking of corporations by kills in the past week  # noqa: E501

        :param last_week: The last_week of this GetFwLeaderboardsCorporationsKills.  # noqa: E501
        :type: list[GetFwLeaderboardsCorporationsLastWeek]
        """
        if last_week is None:
            raise ValueError("Invalid value for `last_week`, must not be `None`")  # noqa: E501

        self._last_week = last_week

    @property
    def active_total(self):
        """Gets the active_total of this GetFwLeaderboardsCorporationsKills.  # noqa: E501

        Top 10 ranking of corporations active in faction warfare by total kills. A corporation is considered \"active\" if they have participated in faction warfare in the past 14 days.  # noqa: E501

        :return: The active_total of this GetFwLeaderboardsCorporationsKills.  # noqa: E501
        :rtype: list[GetFwLeaderboardsCorporationsActiveTotal]
        """
        return self._active_total

    @active_total.setter
    def active_total(self, active_total):
        """Sets the active_total of this GetFwLeaderboardsCorporationsKills.

        Top 10 ranking of corporations active in faction warfare by total kills. A corporation is considered \"active\" if they have participated in faction warfare in the past 14 days.  # noqa: E501

        :param active_total: The active_total of this GetFwLeaderboardsCorporationsKills.  # noqa: E501
        :type: list[GetFwLeaderboardsCorporationsActiveTotal]
        """
        if active_total is None:
            raise ValueError("Invalid value for `active_total`, must not be `None`")  # noqa: E501

        self._active_total = active_total

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
        if not isinstance(other, GetFwLeaderboardsCorporationsKills):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
