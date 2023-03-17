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


class RemoveTrustedCertificateInput(object):
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
        'trusted_certificate': 'str'
    }

    attribute_map = {
        'trusted_certificate': 'trustedCertificate'
    }

    def __init__(self, trusted_certificate=None):  # noqa: E501
        """RemoveTrustedCertificateInput - a model defined in OpenAPI"""  # noqa: E501

        self._trusted_certificate = None
        self.discriminator = None

        self.trusted_certificate = trusted_certificate

    @property
    def trusted_certificate(self):
        """Gets the trusted_certificate of this RemoveTrustedCertificateInput.  # noqa: E501

        ID of certificate to be deleted  # noqa: E501

        :return: The trusted_certificate of this RemoveTrustedCertificateInput.  # noqa: E501
        :rtype: str
        """
        return self._trusted_certificate

    @trusted_certificate.setter
    def trusted_certificate(self, trusted_certificate):
        """Sets the trusted_certificate of this RemoveTrustedCertificateInput.

        ID of certificate to be deleted  # noqa: E501

        :param trusted_certificate: The trusted_certificate of this RemoveTrustedCertificateInput.  # noqa: E501
        :type: str
        """
        if trusted_certificate is None:
            raise ValueError("Invalid value for `trusted_certificate`, must not be `None`")  # noqa: E501

        self._trusted_certificate = trusted_certificate

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
        if not isinstance(other, RemoveTrustedCertificateInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
