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

from swagger_client.models.get_characters_character_id_mail_labels_label import GetCharactersCharacterIdMailLabelsLabel  # noqa: F401,E501


class GetCharactersCharacterIdMailLabelsOk(object):
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
        'total_unread_count': 'int',
        'labels': 'list[GetCharactersCharacterIdMailLabelsLabel]'
    }

    attribute_map = {
        'total_unread_count': 'total_unread_count',
        'labels': 'labels'
    }

    def __init__(self, total_unread_count=None, labels=None):  # noqa: E501
        """GetCharactersCharacterIdMailLabelsOk - a model defined in Swagger"""  # noqa: E501

        self._total_unread_count = None
        self._labels = None
        self.discriminator = None

        if total_unread_count is not None:
            self.total_unread_count = total_unread_count
        if labels is not None:
            self.labels = labels

    @property
    def total_unread_count(self):
        """Gets the total_unread_count of this GetCharactersCharacterIdMailLabelsOk.  # noqa: E501

        total_unread_count integer  # noqa: E501

        :return: The total_unread_count of this GetCharactersCharacterIdMailLabelsOk.  # noqa: E501
        :rtype: int
        """
        return self._total_unread_count

    @total_unread_count.setter
    def total_unread_count(self, total_unread_count):
        """Sets the total_unread_count of this GetCharactersCharacterIdMailLabelsOk.

        total_unread_count integer  # noqa: E501

        :param total_unread_count: The total_unread_count of this GetCharactersCharacterIdMailLabelsOk.  # noqa: E501
        :type: int
        """
        if total_unread_count is not None and total_unread_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `total_unread_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_unread_count = total_unread_count

    @property
    def labels(self):
        """Gets the labels of this GetCharactersCharacterIdMailLabelsOk.  # noqa: E501

        labels array  # noqa: E501

        :return: The labels of this GetCharactersCharacterIdMailLabelsOk.  # noqa: E501
        :rtype: list[GetCharactersCharacterIdMailLabelsLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this GetCharactersCharacterIdMailLabelsOk.

        labels array  # noqa: E501

        :param labels: The labels of this GetCharactersCharacterIdMailLabelsOk.  # noqa: E501
        :type: list[GetCharactersCharacterIdMailLabelsLabel]
        """

        self._labels = labels

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
        if not isinstance(other, GetCharactersCharacterIdMailLabelsOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other