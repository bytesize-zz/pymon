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

from swagger_client.models.post_characters_character_id_mail_recipient import PostCharactersCharacterIdMailRecipient  # noqa: F401,E501


class PostCharactersCharacterIdMailMail(object):
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
        'recipients': 'list[PostCharactersCharacterIdMailRecipient]',
        'subject': 'str',
        'body': 'str',
        'approved_cost': 'int'
    }

    attribute_map = {
        'recipients': 'recipients',
        'subject': 'subject',
        'body': 'body',
        'approved_cost': 'approved_cost'
    }

    def __init__(self, recipients=None, subject=None, body=None, approved_cost=0):  # noqa: E501
        """PostCharactersCharacterIdMailMail - a model defined in Swagger"""  # noqa: E501

        self._recipients = None
        self._subject = None
        self._body = None
        self._approved_cost = None
        self.discriminator = None

        self.recipients = recipients
        self.subject = subject
        self.body = body
        if approved_cost is not None:
            self.approved_cost = approved_cost

    @property
    def recipients(self):
        """Gets the recipients of this PostCharactersCharacterIdMailMail.  # noqa: E501

        recipients array  # noqa: E501

        :return: The recipients of this PostCharactersCharacterIdMailMail.  # noqa: E501
        :rtype: list[PostCharactersCharacterIdMailRecipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this PostCharactersCharacterIdMailMail.

        recipients array  # noqa: E501

        :param recipients: The recipients of this PostCharactersCharacterIdMailMail.  # noqa: E501
        :type: list[PostCharactersCharacterIdMailRecipient]
        """
        if recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")  # noqa: E501

        self._recipients = recipients

    @property
    def subject(self):
        """Gets the subject of this PostCharactersCharacterIdMailMail.  # noqa: E501

        subject string  # noqa: E501

        :return: The subject of this PostCharactersCharacterIdMailMail.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PostCharactersCharacterIdMailMail.

        subject string  # noqa: E501

        :param subject: The subject of this PostCharactersCharacterIdMailMail.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501
        if subject is not None and len(subject) > 1000:
            raise ValueError("Invalid value for `subject`, length must be less than or equal to `1000`")  # noqa: E501

        self._subject = subject

    @property
    def body(self):
        """Gets the body of this PostCharactersCharacterIdMailMail.  # noqa: E501

        body string  # noqa: E501

        :return: The body of this PostCharactersCharacterIdMailMail.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this PostCharactersCharacterIdMailMail.

        body string  # noqa: E501

        :param body: The body of this PostCharactersCharacterIdMailMail.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501
        if body is not None and len(body) > 10000:
            raise ValueError("Invalid value for `body`, length must be less than or equal to `10000`")  # noqa: E501

        self._body = body

    @property
    def approved_cost(self):
        """Gets the approved_cost of this PostCharactersCharacterIdMailMail.  # noqa: E501

        approved_cost integer  # noqa: E501

        :return: The approved_cost of this PostCharactersCharacterIdMailMail.  # noqa: E501
        :rtype: int
        """
        return self._approved_cost

    @approved_cost.setter
    def approved_cost(self, approved_cost):
        """Sets the approved_cost of this PostCharactersCharacterIdMailMail.

        approved_cost integer  # noqa: E501

        :param approved_cost: The approved_cost of this PostCharactersCharacterIdMailMail.  # noqa: E501
        :type: int
        """

        self._approved_cost = approved_cost

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
        if not isinstance(other, PostCharactersCharacterIdMailMail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
