# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    OpenAPI spec version: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class NimbleErrorWithArguments(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'code': 'int',
        'severity': 'str',
        'text': 'str'
    }

    attribute_map = {
        'code': 'code',
        'severity': 'severity',
        'text': 'text'
    }

    def __init__(self, code=None, severity=None, text=None):  # noqa: E501
        """NimbleErrorWithArguments - a model defined in OpenAPI"""  # noqa: E501

        self._code = None
        self._severity = None
        self._text = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if severity is not None:
            self.severity = severity
        if text is not None:
            self.text = text

    @property
    def code(self):
        """Gets the code of this NimbleErrorWithArguments.  # noqa: E501

        Error code.  # noqa: E501

        :return: The code of this NimbleErrorWithArguments.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this NimbleErrorWithArguments.

        Error code.  # noqa: E501

        :param code: The code of this NimbleErrorWithArguments.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def severity(self):
        """Gets the severity of this NimbleErrorWithArguments.  # noqa: E501


        :return: The severity of this NimbleErrorWithArguments.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this NimbleErrorWithArguments.


        :param severity: The severity of this NimbleErrorWithArguments.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def text(self):
        """Gets the text of this NimbleErrorWithArguments.  # noqa: E501

        Full error message with argument populated.  # noqa: E501

        :return: The text of this NimbleErrorWithArguments.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this NimbleErrorWithArguments.

        Full error message with argument populated.  # noqa: E501

        :param text: The text of this NimbleErrorWithArguments.  # noqa: E501
        :type: str
        """

        self._text = text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, NimbleErrorWithArguments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other