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


class GetCharactersCharacterIdStatsTravel(object):
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
        'acceleration_gate_activations': 'int',
        'align_to': 'int',
        'distance_warped_high_sec': 'int',
        'distance_warped_low_sec': 'int',
        'distance_warped_null_sec': 'int',
        'distance_warped_wormhole': 'int',
        'docks_high_sec': 'int',
        'docks_low_sec': 'int',
        'docks_null_sec': 'int',
        'jumps_stargate_high_sec': 'int',
        'jumps_stargate_low_sec': 'int',
        'jumps_stargate_null_sec': 'int',
        'jumps_wormhole': 'int',
        'warps_high_sec': 'int',
        'warps_low_sec': 'int',
        'warps_null_sec': 'int',
        'warps_to_bookmark': 'int',
        'warps_to_celestial': 'int',
        'warps_to_fleet_member': 'int',
        'warps_to_scan_result': 'int',
        'warps_wormhole': 'int'
    }

    attribute_map = {
        'acceleration_gate_activations': 'acceleration_gate_activations',
        'align_to': 'align_to',
        'distance_warped_high_sec': 'distance_warped_high_sec',
        'distance_warped_low_sec': 'distance_warped_low_sec',
        'distance_warped_null_sec': 'distance_warped_null_sec',
        'distance_warped_wormhole': 'distance_warped_wormhole',
        'docks_high_sec': 'docks_high_sec',
        'docks_low_sec': 'docks_low_sec',
        'docks_null_sec': 'docks_null_sec',
        'jumps_stargate_high_sec': 'jumps_stargate_high_sec',
        'jumps_stargate_low_sec': 'jumps_stargate_low_sec',
        'jumps_stargate_null_sec': 'jumps_stargate_null_sec',
        'jumps_wormhole': 'jumps_wormhole',
        'warps_high_sec': 'warps_high_sec',
        'warps_low_sec': 'warps_low_sec',
        'warps_null_sec': 'warps_null_sec',
        'warps_to_bookmark': 'warps_to_bookmark',
        'warps_to_celestial': 'warps_to_celestial',
        'warps_to_fleet_member': 'warps_to_fleet_member',
        'warps_to_scan_result': 'warps_to_scan_result',
        'warps_wormhole': 'warps_wormhole'
    }

    def __init__(self, acceleration_gate_activations=None, align_to=None, distance_warped_high_sec=None, distance_warped_low_sec=None, distance_warped_null_sec=None, distance_warped_wormhole=None, docks_high_sec=None, docks_low_sec=None, docks_null_sec=None, jumps_stargate_high_sec=None, jumps_stargate_low_sec=None, jumps_stargate_null_sec=None, jumps_wormhole=None, warps_high_sec=None, warps_low_sec=None, warps_null_sec=None, warps_to_bookmark=None, warps_to_celestial=None, warps_to_fleet_member=None, warps_to_scan_result=None, warps_wormhole=None):  # noqa: E501
        """GetCharactersCharacterIdStatsTravel - a model defined in Swagger"""  # noqa: E501

        self._acceleration_gate_activations = None
        self._align_to = None
        self._distance_warped_high_sec = None
        self._distance_warped_low_sec = None
        self._distance_warped_null_sec = None
        self._distance_warped_wormhole = None
        self._docks_high_sec = None
        self._docks_low_sec = None
        self._docks_null_sec = None
        self._jumps_stargate_high_sec = None
        self._jumps_stargate_low_sec = None
        self._jumps_stargate_null_sec = None
        self._jumps_wormhole = None
        self._warps_high_sec = None
        self._warps_low_sec = None
        self._warps_null_sec = None
        self._warps_to_bookmark = None
        self._warps_to_celestial = None
        self._warps_to_fleet_member = None
        self._warps_to_scan_result = None
        self._warps_wormhole = None
        self.discriminator = None

        if acceleration_gate_activations is not None:
            self.acceleration_gate_activations = acceleration_gate_activations
        if align_to is not None:
            self.align_to = align_to
        if distance_warped_high_sec is not None:
            self.distance_warped_high_sec = distance_warped_high_sec
        if distance_warped_low_sec is not None:
            self.distance_warped_low_sec = distance_warped_low_sec
        if distance_warped_null_sec is not None:
            self.distance_warped_null_sec = distance_warped_null_sec
        if distance_warped_wormhole is not None:
            self.distance_warped_wormhole = distance_warped_wormhole
        if docks_high_sec is not None:
            self.docks_high_sec = docks_high_sec
        if docks_low_sec is not None:
            self.docks_low_sec = docks_low_sec
        if docks_null_sec is not None:
            self.docks_null_sec = docks_null_sec
        if jumps_stargate_high_sec is not None:
            self.jumps_stargate_high_sec = jumps_stargate_high_sec
        if jumps_stargate_low_sec is not None:
            self.jumps_stargate_low_sec = jumps_stargate_low_sec
        if jumps_stargate_null_sec is not None:
            self.jumps_stargate_null_sec = jumps_stargate_null_sec
        if jumps_wormhole is not None:
            self.jumps_wormhole = jumps_wormhole
        if warps_high_sec is not None:
            self.warps_high_sec = warps_high_sec
        if warps_low_sec is not None:
            self.warps_low_sec = warps_low_sec
        if warps_null_sec is not None:
            self.warps_null_sec = warps_null_sec
        if warps_to_bookmark is not None:
            self.warps_to_bookmark = warps_to_bookmark
        if warps_to_celestial is not None:
            self.warps_to_celestial = warps_to_celestial
        if warps_to_fleet_member is not None:
            self.warps_to_fleet_member = warps_to_fleet_member
        if warps_to_scan_result is not None:
            self.warps_to_scan_result = warps_to_scan_result
        if warps_wormhole is not None:
            self.warps_wormhole = warps_wormhole

    @property
    def acceleration_gate_activations(self):
        """Gets the acceleration_gate_activations of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        acceleration_gate_activations integer  # noqa: E501

        :return: The acceleration_gate_activations of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._acceleration_gate_activations

    @acceleration_gate_activations.setter
    def acceleration_gate_activations(self, acceleration_gate_activations):
        """Sets the acceleration_gate_activations of this GetCharactersCharacterIdStatsTravel.

        acceleration_gate_activations integer  # noqa: E501

        :param acceleration_gate_activations: The acceleration_gate_activations of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._acceleration_gate_activations = acceleration_gate_activations

    @property
    def align_to(self):
        """Gets the align_to of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        align_to integer  # noqa: E501

        :return: The align_to of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._align_to

    @align_to.setter
    def align_to(self, align_to):
        """Sets the align_to of this GetCharactersCharacterIdStatsTravel.

        align_to integer  # noqa: E501

        :param align_to: The align_to of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._align_to = align_to

    @property
    def distance_warped_high_sec(self):
        """Gets the distance_warped_high_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        distance_warped_high_sec integer  # noqa: E501

        :return: The distance_warped_high_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._distance_warped_high_sec

    @distance_warped_high_sec.setter
    def distance_warped_high_sec(self, distance_warped_high_sec):
        """Sets the distance_warped_high_sec of this GetCharactersCharacterIdStatsTravel.

        distance_warped_high_sec integer  # noqa: E501

        :param distance_warped_high_sec: The distance_warped_high_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._distance_warped_high_sec = distance_warped_high_sec

    @property
    def distance_warped_low_sec(self):
        """Gets the distance_warped_low_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        distance_warped_low_sec integer  # noqa: E501

        :return: The distance_warped_low_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._distance_warped_low_sec

    @distance_warped_low_sec.setter
    def distance_warped_low_sec(self, distance_warped_low_sec):
        """Sets the distance_warped_low_sec of this GetCharactersCharacterIdStatsTravel.

        distance_warped_low_sec integer  # noqa: E501

        :param distance_warped_low_sec: The distance_warped_low_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._distance_warped_low_sec = distance_warped_low_sec

    @property
    def distance_warped_null_sec(self):
        """Gets the distance_warped_null_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        distance_warped_null_sec integer  # noqa: E501

        :return: The distance_warped_null_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._distance_warped_null_sec

    @distance_warped_null_sec.setter
    def distance_warped_null_sec(self, distance_warped_null_sec):
        """Sets the distance_warped_null_sec of this GetCharactersCharacterIdStatsTravel.

        distance_warped_null_sec integer  # noqa: E501

        :param distance_warped_null_sec: The distance_warped_null_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._distance_warped_null_sec = distance_warped_null_sec

    @property
    def distance_warped_wormhole(self):
        """Gets the distance_warped_wormhole of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        distance_warped_wormhole integer  # noqa: E501

        :return: The distance_warped_wormhole of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._distance_warped_wormhole

    @distance_warped_wormhole.setter
    def distance_warped_wormhole(self, distance_warped_wormhole):
        """Sets the distance_warped_wormhole of this GetCharactersCharacterIdStatsTravel.

        distance_warped_wormhole integer  # noqa: E501

        :param distance_warped_wormhole: The distance_warped_wormhole of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._distance_warped_wormhole = distance_warped_wormhole

    @property
    def docks_high_sec(self):
        """Gets the docks_high_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        docks_high_sec integer  # noqa: E501

        :return: The docks_high_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._docks_high_sec

    @docks_high_sec.setter
    def docks_high_sec(self, docks_high_sec):
        """Sets the docks_high_sec of this GetCharactersCharacterIdStatsTravel.

        docks_high_sec integer  # noqa: E501

        :param docks_high_sec: The docks_high_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._docks_high_sec = docks_high_sec

    @property
    def docks_low_sec(self):
        """Gets the docks_low_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        docks_low_sec integer  # noqa: E501

        :return: The docks_low_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._docks_low_sec

    @docks_low_sec.setter
    def docks_low_sec(self, docks_low_sec):
        """Sets the docks_low_sec of this GetCharactersCharacterIdStatsTravel.

        docks_low_sec integer  # noqa: E501

        :param docks_low_sec: The docks_low_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._docks_low_sec = docks_low_sec

    @property
    def docks_null_sec(self):
        """Gets the docks_null_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        docks_null_sec integer  # noqa: E501

        :return: The docks_null_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._docks_null_sec

    @docks_null_sec.setter
    def docks_null_sec(self, docks_null_sec):
        """Sets the docks_null_sec of this GetCharactersCharacterIdStatsTravel.

        docks_null_sec integer  # noqa: E501

        :param docks_null_sec: The docks_null_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._docks_null_sec = docks_null_sec

    @property
    def jumps_stargate_high_sec(self):
        """Gets the jumps_stargate_high_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        jumps_stargate_high_sec integer  # noqa: E501

        :return: The jumps_stargate_high_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._jumps_stargate_high_sec

    @jumps_stargate_high_sec.setter
    def jumps_stargate_high_sec(self, jumps_stargate_high_sec):
        """Sets the jumps_stargate_high_sec of this GetCharactersCharacterIdStatsTravel.

        jumps_stargate_high_sec integer  # noqa: E501

        :param jumps_stargate_high_sec: The jumps_stargate_high_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._jumps_stargate_high_sec = jumps_stargate_high_sec

    @property
    def jumps_stargate_low_sec(self):
        """Gets the jumps_stargate_low_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        jumps_stargate_low_sec integer  # noqa: E501

        :return: The jumps_stargate_low_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._jumps_stargate_low_sec

    @jumps_stargate_low_sec.setter
    def jumps_stargate_low_sec(self, jumps_stargate_low_sec):
        """Sets the jumps_stargate_low_sec of this GetCharactersCharacterIdStatsTravel.

        jumps_stargate_low_sec integer  # noqa: E501

        :param jumps_stargate_low_sec: The jumps_stargate_low_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._jumps_stargate_low_sec = jumps_stargate_low_sec

    @property
    def jumps_stargate_null_sec(self):
        """Gets the jumps_stargate_null_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        jumps_stargate_null_sec integer  # noqa: E501

        :return: The jumps_stargate_null_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._jumps_stargate_null_sec

    @jumps_stargate_null_sec.setter
    def jumps_stargate_null_sec(self, jumps_stargate_null_sec):
        """Sets the jumps_stargate_null_sec of this GetCharactersCharacterIdStatsTravel.

        jumps_stargate_null_sec integer  # noqa: E501

        :param jumps_stargate_null_sec: The jumps_stargate_null_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._jumps_stargate_null_sec = jumps_stargate_null_sec

    @property
    def jumps_wormhole(self):
        """Gets the jumps_wormhole of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        jumps_wormhole integer  # noqa: E501

        :return: The jumps_wormhole of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._jumps_wormhole

    @jumps_wormhole.setter
    def jumps_wormhole(self, jumps_wormhole):
        """Sets the jumps_wormhole of this GetCharactersCharacterIdStatsTravel.

        jumps_wormhole integer  # noqa: E501

        :param jumps_wormhole: The jumps_wormhole of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._jumps_wormhole = jumps_wormhole

    @property
    def warps_high_sec(self):
        """Gets the warps_high_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        warps_high_sec integer  # noqa: E501

        :return: The warps_high_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._warps_high_sec

    @warps_high_sec.setter
    def warps_high_sec(self, warps_high_sec):
        """Sets the warps_high_sec of this GetCharactersCharacterIdStatsTravel.

        warps_high_sec integer  # noqa: E501

        :param warps_high_sec: The warps_high_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._warps_high_sec = warps_high_sec

    @property
    def warps_low_sec(self):
        """Gets the warps_low_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        warps_low_sec integer  # noqa: E501

        :return: The warps_low_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._warps_low_sec

    @warps_low_sec.setter
    def warps_low_sec(self, warps_low_sec):
        """Sets the warps_low_sec of this GetCharactersCharacterIdStatsTravel.

        warps_low_sec integer  # noqa: E501

        :param warps_low_sec: The warps_low_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._warps_low_sec = warps_low_sec

    @property
    def warps_null_sec(self):
        """Gets the warps_null_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        warps_null_sec integer  # noqa: E501

        :return: The warps_null_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._warps_null_sec

    @warps_null_sec.setter
    def warps_null_sec(self, warps_null_sec):
        """Sets the warps_null_sec of this GetCharactersCharacterIdStatsTravel.

        warps_null_sec integer  # noqa: E501

        :param warps_null_sec: The warps_null_sec of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._warps_null_sec = warps_null_sec

    @property
    def warps_to_bookmark(self):
        """Gets the warps_to_bookmark of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        warps_to_bookmark integer  # noqa: E501

        :return: The warps_to_bookmark of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._warps_to_bookmark

    @warps_to_bookmark.setter
    def warps_to_bookmark(self, warps_to_bookmark):
        """Sets the warps_to_bookmark of this GetCharactersCharacterIdStatsTravel.

        warps_to_bookmark integer  # noqa: E501

        :param warps_to_bookmark: The warps_to_bookmark of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._warps_to_bookmark = warps_to_bookmark

    @property
    def warps_to_celestial(self):
        """Gets the warps_to_celestial of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        warps_to_celestial integer  # noqa: E501

        :return: The warps_to_celestial of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._warps_to_celestial

    @warps_to_celestial.setter
    def warps_to_celestial(self, warps_to_celestial):
        """Sets the warps_to_celestial of this GetCharactersCharacterIdStatsTravel.

        warps_to_celestial integer  # noqa: E501

        :param warps_to_celestial: The warps_to_celestial of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._warps_to_celestial = warps_to_celestial

    @property
    def warps_to_fleet_member(self):
        """Gets the warps_to_fleet_member of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        warps_to_fleet_member integer  # noqa: E501

        :return: The warps_to_fleet_member of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._warps_to_fleet_member

    @warps_to_fleet_member.setter
    def warps_to_fleet_member(self, warps_to_fleet_member):
        """Sets the warps_to_fleet_member of this GetCharactersCharacterIdStatsTravel.

        warps_to_fleet_member integer  # noqa: E501

        :param warps_to_fleet_member: The warps_to_fleet_member of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._warps_to_fleet_member = warps_to_fleet_member

    @property
    def warps_to_scan_result(self):
        """Gets the warps_to_scan_result of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        warps_to_scan_result integer  # noqa: E501

        :return: The warps_to_scan_result of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._warps_to_scan_result

    @warps_to_scan_result.setter
    def warps_to_scan_result(self, warps_to_scan_result):
        """Sets the warps_to_scan_result of this GetCharactersCharacterIdStatsTravel.

        warps_to_scan_result integer  # noqa: E501

        :param warps_to_scan_result: The warps_to_scan_result of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._warps_to_scan_result = warps_to_scan_result

    @property
    def warps_wormhole(self):
        """Gets the warps_wormhole of this GetCharactersCharacterIdStatsTravel.  # noqa: E501

        warps_wormhole integer  # noqa: E501

        :return: The warps_wormhole of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :rtype: int
        """
        return self._warps_wormhole

    @warps_wormhole.setter
    def warps_wormhole(self, warps_wormhole):
        """Sets the warps_wormhole of this GetCharactersCharacterIdStatsTravel.

        warps_wormhole integer  # noqa: E501

        :param warps_wormhole: The warps_wormhole of this GetCharactersCharacterIdStatsTravel.  # noqa: E501
        :type: int
        """

        self._warps_wormhole = warps_wormhole

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
        if not isinstance(other, GetCharactersCharacterIdStatsTravel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
