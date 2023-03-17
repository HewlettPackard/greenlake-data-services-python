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


class EditProxySettings(object):
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
        'proxy_port': 'int',
        'proxy_server': 'str',
        'proxy_username': 'str'
    }

    attribute_map = {
        'proxy_port': 'proxy_port',
        'proxy_server': 'proxy_server',
        'proxy_username': 'proxy_username'
    }

    def __init__(self, proxy_port=None, proxy_server=None, proxy_username=None):  # noqa: E501
        """EditProxySettings - a model defined in OpenAPI"""  # noqa: E501

        self._proxy_port = None
        self._proxy_server = None
        self._proxy_username = None
        self.discriminator = None

        if proxy_port is not None:
            self.proxy_port = proxy_port
        if proxy_server is not None:
            self.proxy_server = proxy_server
        if proxy_username is not None:
            self.proxy_username = proxy_username

    @property
    def proxy_port(self):
        """Gets the proxy_port of this EditProxySettings.  # noqa: E501

        Proxy Port of HTTP Proxy Server. Integer value between 0-65535 representing TCP/IP port.  # noqa: E501

        :return: The proxy_port of this EditProxySettings.  # noqa: E501
        :rtype: int
        """
        return self._proxy_port

    @proxy_port.setter
    def proxy_port(self, proxy_port):
        """Sets the proxy_port of this EditProxySettings.

        Proxy Port of HTTP Proxy Server. Integer value between 0-65535 representing TCP/IP port.  # noqa: E501

        :param proxy_port: The proxy_port of this EditProxySettings.  # noqa: E501
        :type: int
        """

        self._proxy_port = proxy_port

    @property
    def proxy_server(self):
        """Gets the proxy_server of this EditProxySettings.  # noqa: E501

        Hostname or IP Address of HTTP Proxy Server. Setting this attribute to an empty string will unset all proxy settings. String of alphanumeric characters, can be an empty string, or valid range must be from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character.  # noqa: E501

        :return: The proxy_server of this EditProxySettings.  # noqa: E501
        :rtype: str
        """
        return self._proxy_server

    @proxy_server.setter
    def proxy_server(self, proxy_server):
        """Sets the proxy_server of this EditProxySettings.

        Hostname or IP Address of HTTP Proxy Server. Setting this attribute to an empty string will unset all proxy settings. String of alphanumeric characters, can be an empty string, or valid range must be from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character.  # noqa: E501

        :param proxy_server: The proxy_server of this EditProxySettings.  # noqa: E501
        :type: str
        """

        self._proxy_server = proxy_server

    @property
    def proxy_username(self):
        """Gets the proxy_username of this EditProxySettings.  # noqa: E501

        Username to authenticate with HTTP Proxy Server. HTTP proxy server username, string up to 255 characters, special characters ([, ], `, ;, ampersand, tab, space, newline) are not allowed.  # noqa: E501

        :return: The proxy_username of this EditProxySettings.  # noqa: E501
        :rtype: str
        """
        return self._proxy_username

    @proxy_username.setter
    def proxy_username(self, proxy_username):
        """Sets the proxy_username of this EditProxySettings.

        Username to authenticate with HTTP Proxy Server. HTTP proxy server username, string up to 255 characters, special characters ([, ], `, ;, ampersand, tab, space, newline) are not allowed.  # noqa: E501

        :param proxy_username: The proxy_username of this EditProxySettings.  # noqa: E501
        :type: str
        """

        self._proxy_username = proxy_username

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
        if not isinstance(other, EditProxySettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other