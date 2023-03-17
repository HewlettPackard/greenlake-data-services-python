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


class CreateCertificateInput(object):
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
        'authority_chain': 'str',
        'common_name': 'str',
        'country': 'str',
        'days': 'int',
        'key_length': 'int',
        'locality': 'str',
        'organization': 'str',
        'organization_unit': 'str',
        'province': 'str',
        'service': 'str',
        'subject_alt_name': 'CertSubjectAltName',
        'type': 'str'
    }

    attribute_map = {
        'authority_chain': 'authorityChain',
        'common_name': 'commonName',
        'country': 'country',
        'days': 'days',
        'key_length': 'keyLength',
        'locality': 'locality',
        'organization': 'organization',
        'organization_unit': 'organizationUnit',
        'province': 'province',
        'service': 'service',
        'subject_alt_name': 'subjectAltName',
        'type': 'type'
    }

    def __init__(self, authority_chain=None, common_name=None, country=None, days=None, key_length=None, locality=None, organization=None, organization_unit=None, province=None, service=None, subject_alt_name=None, type=None):  # noqa: E501
        """CreateCertificateInput - a model defined in OpenAPI"""  # noqa: E501

        self._authority_chain = None
        self._common_name = None
        self._country = None
        self._days = None
        self._key_length = None
        self._locality = None
        self._organization = None
        self._organization_unit = None
        self._province = None
        self._service = None
        self._subject_alt_name = None
        self._type = None
        self.discriminator = None

        if authority_chain is not None:
            self.authority_chain = authority_chain
        if common_name is not None:
            self.common_name = common_name
        if country is not None:
            self.country = country
        if days is not None:
            self.days = days
        if key_length is not None:
            self.key_length = key_length
        if locality is not None:
            self.locality = locality
        if organization is not None:
            self.organization = organization
        if organization_unit is not None:
            self.organization_unit = organization_unit
        if province is not None:
            self.province = province
        self.service = service
        if subject_alt_name is not None:
            self.subject_alt_name = subject_alt_name
        self.type = type

    @property
    def authority_chain(self):
        """Gets the authority_chain of this CreateCertificateInput.  # noqa: E501

        The authority chain for Quorum Witness server certificate.  # noqa: E501

        :return: The authority_chain of this CreateCertificateInput.  # noqa: E501
        :rtype: str
        """
        return self._authority_chain

    @authority_chain.setter
    def authority_chain(self, authority_chain):
        """Sets the authority_chain of this CreateCertificateInput.

        The authority chain for Quorum Witness server certificate.  # noqa: E501

        :param authority_chain: The authority_chain of this CreateCertificateInput.  # noqa: E501
        :type: str
        """

        self._authority_chain = authority_chain

    @property
    def common_name(self):
        """Gets the common_name of this CreateCertificateInput.  # noqa: E501

        CommonName for the certificate.  # noqa: E501

        :return: The common_name of this CreateCertificateInput.  # noqa: E501
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this CreateCertificateInput.

        CommonName for the certificate.  # noqa: E501

        :param common_name: The common_name of this CreateCertificateInput.  # noqa: E501
        :type: str
        """

        self._common_name = common_name

    @property
    def country(self):
        """Gets the country of this CreateCertificateInput.  # noqa: E501

        Two-letter code for the country where organization is located.  # noqa: E501

        :return: The country of this CreateCertificateInput.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreateCertificateInput.

        Two-letter code for the country where organization is located.  # noqa: E501

        :param country: The country of this CreateCertificateInput.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def days(self):
        """Gets the days of this CreateCertificateInput.  # noqa: E501

        Number of days valid for the certificate.  # noqa: E501

        :return: The days of this CreateCertificateInput.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this CreateCertificateInput.

        Number of days valid for the certificate.  # noqa: E501

        :param days: The days of this CreateCertificateInput.  # noqa: E501
        :type: int
        """

        self._days = days

    @property
    def key_length(self):
        """Gets the key_length of this CreateCertificateInput.  # noqa: E501

        Key length for the certificate.  # noqa: E501

        :return: The key_length of this CreateCertificateInput.  # noqa: E501
        :rtype: int
        """
        return self._key_length

    @key_length.setter
    def key_length(self, key_length):
        """Sets the key_length of this CreateCertificateInput.

        Key length for the certificate.  # noqa: E501

        :param key_length: The key_length of this CreateCertificateInput.  # noqa: E501
        :type: int
        """

        self._key_length = key_length

    @property
    def locality(self):
        """Gets the locality of this CreateCertificateInput.  # noqa: E501

        Locality where organization is located.  # noqa: E501

        :return: The locality of this CreateCertificateInput.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this CreateCertificateInput.

        Locality where organization is located.  # noqa: E501

        :param locality: The locality of this CreateCertificateInput.  # noqa: E501
        :type: str
        """

        self._locality = locality

    @property
    def organization(self):
        """Gets the organization of this CreateCertificateInput.  # noqa: E501

        Organization for the certificate  # noqa: E501

        :return: The organization of this CreateCertificateInput.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this CreateCertificateInput.

        Organization for the certificate  # noqa: E501

        :param organization: The organization of this CreateCertificateInput.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def organization_unit(self):
        """Gets the organization_unit of this CreateCertificateInput.  # noqa: E501

        Division of organization handling the certificate.  # noqa: E501

        :return: The organization_unit of this CreateCertificateInput.  # noqa: E501
        :rtype: str
        """
        return self._organization_unit

    @organization_unit.setter
    def organization_unit(self, organization_unit):
        """Sets the organization_unit of this CreateCertificateInput.

        Division of organization handling the certificate.  # noqa: E501

        :param organization_unit: The organization_unit of this CreateCertificateInput.  # noqa: E501
        :type: str
        """

        self._organization_unit = organization_unit

    @property
    def province(self):
        """Gets the province of this CreateCertificateInput.  # noqa: E501

        Province where organization is located.  # noqa: E501

        :return: The province of this CreateCertificateInput.  # noqa: E501
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this CreateCertificateInput.

        Province where organization is located.  # noqa: E501

        :param province: The province of this CreateCertificateInput.  # noqa: E501
        :type: str
        """

        self._province = province

    @property
    def service(self):
        """Gets the service of this CreateCertificateInput.  # noqa: E501

        Name of service the certificate is for.  # noqa: E501

        :return: The service of this CreateCertificateInput.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this CreateCertificateInput.

        Name of service the certificate is for.  # noqa: E501

        :param service: The service of this CreateCertificateInput.  # noqa: E501
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501
        allowed_values = ["QW_CLIENT", "QW_SERVER", "WSAPI", "CLI", "CIM", "VASA", "EKM_CLIENT", "SYSLOG_GEN_CLIENT", "SYSLOG_SEC_CLIENT", "UNIFIED_SERVER"]  # noqa: E501
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"  # noqa: E501
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def subject_alt_name(self):
        """Gets the subject_alt_name of this CreateCertificateInput.  # noqa: E501


        :return: The subject_alt_name of this CreateCertificateInput.  # noqa: E501
        :rtype: CertSubjectAltName
        """
        return self._subject_alt_name

    @subject_alt_name.setter
    def subject_alt_name(self, subject_alt_name):
        """Sets the subject_alt_name of this CreateCertificateInput.


        :param subject_alt_name: The subject_alt_name of this CreateCertificateInput.  # noqa: E501
        :type: CertSubjectAltName
        """

        self._subject_alt_name = subject_alt_name

    @property
    def type(self):
        """Gets the type of this CreateCertificateInput.  # noqa: E501

        Type of certificate to create.  # noqa: E501

        :return: The type of this CreateCertificateInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateCertificateInput.

        Type of certificate to create.  # noqa: E501

        :param type: The type of this CreateCertificateInput.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, CreateCertificateInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other