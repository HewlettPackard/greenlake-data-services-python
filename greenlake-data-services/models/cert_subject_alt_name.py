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


class CertSubjectAltName(object):
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
        'dns': 'str',
        'ip': 'str',
        'email': 'str'
    }

    attribute_map = {
        'dns': 'DNS',
        'ip': 'IP',
        'email': 'email'
    }

    def __init__(self, dns=None, ip=None, email=None):  # noqa: E501
        """CertSubjectAltName - a model defined in OpenAPI"""  # noqa: E501

        self._dns = None
        self._ip = None
        self._email = None
        self.discriminator = None

        if dns is not None:
            self.dns = dns
        if ip is not None:
            self.ip = ip
        if email is not None:
            self.email = email

    @property
    def dns(self):
        """Gets the dns of this CertSubjectAltName.  # noqa: E501

        DNS for Subject Alternative Name for the certificate  # noqa: E501

        :return: The dns of this CertSubjectAltName.  # noqa: E501
        :rtype: str
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this CertSubjectAltName.

        DNS for Subject Alternative Name for the certificate  # noqa: E501

        :param dns: The dns of this CertSubjectAltName.  # noqa: E501
        :type: str
        """

        self._dns = dns

    @property
    def ip(self):
        """Gets the ip of this CertSubjectAltName.  # noqa: E501

        IP Address for Subject Alternative Name for the certificate  # noqa: E501

        :return: The ip of this CertSubjectAltName.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this CertSubjectAltName.

        IP Address for Subject Alternative Name for the certificate  # noqa: E501

        :param ip: The ip of this CertSubjectAltName.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def email(self):
        """Gets the email of this CertSubjectAltName.  # noqa: E501

        Email for Subject Alternative Name for the certificate  # noqa: E501

        :return: The email of this CertSubjectAltName.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CertSubjectAltName.

        Email for Subject Alternative Name for the certificate  # noqa: E501

        :param email: The email of this CertSubjectAltName.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if not isinstance(other, CertSubjectAltName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other