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


class GetIncursions200Ok(object):
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
        'type': 'str',
        'state': 'str',
        'influence': 'float',
        'has_boss': 'bool',
        'faction_id': 'int',
        'constellation_id': 'int',
        'staging_solar_system_id': 'int',
        'infested_solar_systems': 'list[int]'
    }

    attribute_map = {
        'type': 'type',
        'state': 'state',
        'influence': 'influence',
        'has_boss': 'has_boss',
        'faction_id': 'faction_id',
        'constellation_id': 'constellation_id',
        'staging_solar_system_id': 'staging_solar_system_id',
        'infested_solar_systems': 'infested_solar_systems'
    }

    def __init__(self, type=None, state=None, influence=None, has_boss=None, faction_id=None, constellation_id=None, staging_solar_system_id=None, infested_solar_systems=None):  # noqa: E501
        """GetIncursions200Ok - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._state = None
        self._influence = None
        self._has_boss = None
        self._faction_id = None
        self._constellation_id = None
        self._staging_solar_system_id = None
        self._infested_solar_systems = None
        self.discriminator = None

        self.type = type
        self.state = state
        self.influence = influence
        self.has_boss = has_boss
        self.faction_id = faction_id
        self.constellation_id = constellation_id
        self.staging_solar_system_id = staging_solar_system_id
        self.infested_solar_systems = infested_solar_systems

    @property
    def type(self):
        """Gets the type of this GetIncursions200Ok.  # noqa: E501

        The type of this incursion  # noqa: E501

        :return: The type of this GetIncursions200Ok.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetIncursions200Ok.

        The type of this incursion  # noqa: E501

        :param type: The type of this GetIncursions200Ok.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def state(self):
        """Gets the state of this GetIncursions200Ok.  # noqa: E501

        The state of this incursion  # noqa: E501

        :return: The state of this GetIncursions200Ok.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GetIncursions200Ok.

        The state of this incursion  # noqa: E501

        :param state: The state of this GetIncursions200Ok.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["withdrawing", "mobilizing", "established"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def influence(self):
        """Gets the influence of this GetIncursions200Ok.  # noqa: E501

        Influence of this incursion as a float from 0 to 1  # noqa: E501

        :return: The influence of this GetIncursions200Ok.  # noqa: E501
        :rtype: float
        """
        return self._influence

    @influence.setter
    def influence(self, influence):
        """Sets the influence of this GetIncursions200Ok.

        Influence of this incursion as a float from 0 to 1  # noqa: E501

        :param influence: The influence of this GetIncursions200Ok.  # noqa: E501
        :type: float
        """
        if influence is None:
            raise ValueError("Invalid value for `influence`, must not be `None`")  # noqa: E501

        self._influence = influence

    @property
    def has_boss(self):
        """Gets the has_boss of this GetIncursions200Ok.  # noqa: E501

        Whether the final encounter has boss or not  # noqa: E501

        :return: The has_boss of this GetIncursions200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._has_boss

    @has_boss.setter
    def has_boss(self, has_boss):
        """Sets the has_boss of this GetIncursions200Ok.

        Whether the final encounter has boss or not  # noqa: E501

        :param has_boss: The has_boss of this GetIncursions200Ok.  # noqa: E501
        :type: bool
        """
        if has_boss is None:
            raise ValueError("Invalid value for `has_boss`, must not be `None`")  # noqa: E501

        self._has_boss = has_boss

    @property
    def faction_id(self):
        """Gets the faction_id of this GetIncursions200Ok.  # noqa: E501

        The attacking faction's id  # noqa: E501

        :return: The faction_id of this GetIncursions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """Sets the faction_id of this GetIncursions200Ok.

        The attacking faction's id  # noqa: E501

        :param faction_id: The faction_id of this GetIncursions200Ok.  # noqa: E501
        :type: int
        """
        if faction_id is None:
            raise ValueError("Invalid value for `faction_id`, must not be `None`")  # noqa: E501

        self._faction_id = faction_id

    @property
    def constellation_id(self):
        """Gets the constellation_id of this GetIncursions200Ok.  # noqa: E501

        The constellation id in which this incursion takes place  # noqa: E501

        :return: The constellation_id of this GetIncursions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._constellation_id

    @constellation_id.setter
    def constellation_id(self, constellation_id):
        """Sets the constellation_id of this GetIncursions200Ok.

        The constellation id in which this incursion takes place  # noqa: E501

        :param constellation_id: The constellation_id of this GetIncursions200Ok.  # noqa: E501
        :type: int
        """
        if constellation_id is None:
            raise ValueError("Invalid value for `constellation_id`, must not be `None`")  # noqa: E501

        self._constellation_id = constellation_id

    @property
    def staging_solar_system_id(self):
        """Gets the staging_solar_system_id of this GetIncursions200Ok.  # noqa: E501

        Staging solar system for this incursion  # noqa: E501

        :return: The staging_solar_system_id of this GetIncursions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._staging_solar_system_id

    @staging_solar_system_id.setter
    def staging_solar_system_id(self, staging_solar_system_id):
        """Sets the staging_solar_system_id of this GetIncursions200Ok.

        Staging solar system for this incursion  # noqa: E501

        :param staging_solar_system_id: The staging_solar_system_id of this GetIncursions200Ok.  # noqa: E501
        :type: int
        """
        if staging_solar_system_id is None:
            raise ValueError("Invalid value for `staging_solar_system_id`, must not be `None`")  # noqa: E501

        self._staging_solar_system_id = staging_solar_system_id

    @property
    def infested_solar_systems(self):
        """Gets the infested_solar_systems of this GetIncursions200Ok.  # noqa: E501

        A list of infested solar system ids that are a part of this incursion  # noqa: E501

        :return: The infested_solar_systems of this GetIncursions200Ok.  # noqa: E501
        :rtype: list[int]
        """
        return self._infested_solar_systems

    @infested_solar_systems.setter
    def infested_solar_systems(self, infested_solar_systems):
        """Sets the infested_solar_systems of this GetIncursions200Ok.

        A list of infested solar system ids that are a part of this incursion  # noqa: E501

        :param infested_solar_systems: The infested_solar_systems of this GetIncursions200Ok.  # noqa: E501
        :type: list[int]
        """
        if infested_solar_systems is None:
            raise ValueError("Invalid value for `infested_solar_systems`, must not be `None`")  # noqa: E501

        self._infested_solar_systems = infested_solar_systems

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
        if not isinstance(other, GetIncursions200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
