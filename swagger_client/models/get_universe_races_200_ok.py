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


class GetUniverseRaces200Ok(object):
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
        'race_id': 'int',
        'name': 'str',
        'description': 'str',
        'alliance_id': 'int'
    }

    attribute_map = {
        'race_id': 'race_id',
        'name': 'name',
        'description': 'description',
        'alliance_id': 'alliance_id'
    }

    def __init__(self, race_id=None, name=None, description=None, alliance_id=None):  # noqa: E501
        """GetUniverseRaces200Ok - a model defined in Swagger"""  # noqa: E501

        self._race_id = None
        self._name = None
        self._description = None
        self._alliance_id = None
        self.discriminator = None

        self.race_id = race_id
        self.name = name
        self.description = description
        self.alliance_id = alliance_id

    @property
    def race_id(self):
        """Gets the race_id of this GetUniverseRaces200Ok.  # noqa: E501

        race_id integer  # noqa: E501

        :return: The race_id of this GetUniverseRaces200Ok.  # noqa: E501
        :rtype: int
        """
        return self._race_id

    @race_id.setter
    def race_id(self, race_id):
        """Sets the race_id of this GetUniverseRaces200Ok.

        race_id integer  # noqa: E501

        :param race_id: The race_id of this GetUniverseRaces200Ok.  # noqa: E501
        :type: int
        """
        if race_id is None:
            raise ValueError("Invalid value for `race_id`, must not be `None`")  # noqa: E501

        self._race_id = race_id

    @property
    def name(self):
        """Gets the name of this GetUniverseRaces200Ok.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetUniverseRaces200Ok.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUniverseRaces200Ok.

        name string  # noqa: E501

        :param name: The name of this GetUniverseRaces200Ok.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this GetUniverseRaces200Ok.  # noqa: E501

        description string  # noqa: E501

        :return: The description of this GetUniverseRaces200Ok.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetUniverseRaces200Ok.

        description string  # noqa: E501

        :param description: The description of this GetUniverseRaces200Ok.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def alliance_id(self):
        """Gets the alliance_id of this GetUniverseRaces200Ok.  # noqa: E501

        The alliance generally associated with this race  # noqa: E501

        :return: The alliance_id of this GetUniverseRaces200Ok.  # noqa: E501
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """Sets the alliance_id of this GetUniverseRaces200Ok.

        The alliance generally associated with this race  # noqa: E501

        :param alliance_id: The alliance_id of this GetUniverseRaces200Ok.  # noqa: E501
        :type: int
        """
        if alliance_id is None:
            raise ValueError("Invalid value for `alliance_id`, must not be `None`")  # noqa: E501

        self._alliance_id = alliance_id

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
        if not isinstance(other, GetUniverseRaces200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other