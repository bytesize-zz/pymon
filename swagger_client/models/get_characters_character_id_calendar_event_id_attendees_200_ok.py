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


class GetCharactersCharacterIdCalendarEventIdAttendees200Ok(object):
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
        'event_response': 'str'
    }

    attribute_map = {
        'character_id': 'character_id',
        'event_response': 'event_response'
    }

    def __init__(self, character_id=None, event_response=None):  # noqa: E501
        """GetCharactersCharacterIdCalendarEventIdAttendees200Ok - a model defined in Swagger"""  # noqa: E501

        self._character_id = None
        self._event_response = None
        self.discriminator = None

        if character_id is not None:
            self.character_id = character_id
        if event_response is not None:
            self.event_response = event_response

    @property
    def character_id(self):
        """Gets the character_id of this GetCharactersCharacterIdCalendarEventIdAttendees200Ok.  # noqa: E501

        character_id integer  # noqa: E501

        :return: The character_id of this GetCharactersCharacterIdCalendarEventIdAttendees200Ok.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this GetCharactersCharacterIdCalendarEventIdAttendees200Ok.

        character_id integer  # noqa: E501

        :param character_id: The character_id of this GetCharactersCharacterIdCalendarEventIdAttendees200Ok.  # noqa: E501
        :type: int
        """

        self._character_id = character_id

    @property
    def event_response(self):
        """Gets the event_response of this GetCharactersCharacterIdCalendarEventIdAttendees200Ok.  # noqa: E501

        event_response string  # noqa: E501

        :return: The event_response of this GetCharactersCharacterIdCalendarEventIdAttendees200Ok.  # noqa: E501
        :rtype: str
        """
        return self._event_response

    @event_response.setter
    def event_response(self, event_response):
        """Sets the event_response of this GetCharactersCharacterIdCalendarEventIdAttendees200Ok.

        event_response string  # noqa: E501

        :param event_response: The event_response of this GetCharactersCharacterIdCalendarEventIdAttendees200Ok.  # noqa: E501
        :type: str
        """
        allowed_values = ["declined", "not_responded", "accepted", "tentative"]  # noqa: E501
        if event_response not in allowed_values:
            raise ValueError(
                "Invalid value for `event_response` ({0}), must be one of {1}"  # noqa: E501
                .format(event_response, allowed_values)
            )

        self._event_response = event_response

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
        if not isinstance(other, GetCharactersCharacterIdCalendarEventIdAttendees200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other