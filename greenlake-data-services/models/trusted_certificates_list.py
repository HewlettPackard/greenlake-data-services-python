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


class TrustedCertificatesList(object):
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
        'commonname': 'str',
        'detail': 'TrustedCertificateDetailsDetail',
        'domain': 'str',
        'enddate': 'TrustedCertificateDetailsEnddate',
        'fingerprint': 'str',
        'hash': 'str',
        'id': 'str',
        'issuer': 'str',
        'isvalid': 'bool',
        'key_usage': 'str',
        'pem': 'str',
        'serial': 'str',
        'signaturetype': 'str',
        'startdate': 'TrustedCertificateDetailsStartdate',
        'subject': 'str',
        'system_id': 'str',
        'type': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'commonname': 'commonname',
        'detail': 'detail',
        'domain': 'domain',
        'enddate': 'enddate',
        'fingerprint': 'fingerprint',
        'hash': 'hash',
        'id': 'id',
        'issuer': 'issuer',
        'isvalid': 'isvalid',
        'key_usage': 'keyUsage',
        'pem': 'pem',
        'serial': 'serial',
        'signaturetype': 'signaturetype',
        'startdate': 'startdate',
        'subject': 'subject',
        'system_id': 'systemId',
        'type': 'type',
        'uri': 'uri'
    }

    def __init__(self, commonname=None, detail=None, domain=None, enddate=None, fingerprint=None, hash=None, id=None, issuer=None, isvalid=None, key_usage=None, pem=None, serial=None, signaturetype=None, startdate=None, subject=None, system_id=None, type=None, uri=None):  # noqa: E501
        """TrustedCertificatesList - a model defined in OpenAPI"""  # noqa: E501

        self._commonname = None
        self._detail = None
        self._domain = None
        self._enddate = None
        self._fingerprint = None
        self._hash = None
        self._id = None
        self._issuer = None
        self._isvalid = None
        self._key_usage = None
        self._pem = None
        self._serial = None
        self._signaturetype = None
        self._startdate = None
        self._subject = None
        self._system_id = None
        self._type = None
        self._uri = None
        self.discriminator = None

        if commonname is not None:
            self.commonname = commonname
        if detail is not None:
            self.detail = detail
        if domain is not None:
            self.domain = domain
        if enddate is not None:
            self.enddate = enddate
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if hash is not None:
            self.hash = hash
        if id is not None:
            self.id = id
        if issuer is not None:
            self.issuer = issuer
        if isvalid is not None:
            self.isvalid = isvalid
        if key_usage is not None:
            self.key_usage = key_usage
        if pem is not None:
            self.pem = pem
        if serial is not None:
            self.serial = serial
        if signaturetype is not None:
            self.signaturetype = signaturetype
        if startdate is not None:
            self.startdate = startdate
        if subject is not None:
            self.subject = subject
        if system_id is not None:
            self.system_id = system_id
        if type is not None:
            self.type = type
        if uri is not None:
            self.uri = uri

    @property
    def commonname(self):
        """Gets the commonname of this TrustedCertificatesList.  # noqa: E501

        Displayname of the resource  # noqa: E501

        :return: The commonname of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._commonname

    @commonname.setter
    def commonname(self, commonname):
        """Sets the commonname of this TrustedCertificatesList.

        Displayname of the resource  # noqa: E501

        :param commonname: The commonname of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._commonname = commonname

    @property
    def detail(self):
        """Gets the detail of this TrustedCertificatesList.  # noqa: E501


        :return: The detail of this TrustedCertificatesList.  # noqa: E501
        :rtype: TrustedCertificateDetailsDetail
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this TrustedCertificatesList.


        :param detail: The detail of this TrustedCertificatesList.  # noqa: E501
        :type: TrustedCertificateDetailsDetail
        """

        self._detail = detail

    @property
    def domain(self):
        """Gets the domain of this TrustedCertificatesList.  # noqa: E501

        Domain of the resource  # noqa: E501

        :return: The domain of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this TrustedCertificatesList.

        Domain of the resource  # noqa: E501

        :param domain: The domain of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def enddate(self):
        """Gets the enddate of this TrustedCertificatesList.  # noqa: E501


        :return: The enddate of this TrustedCertificatesList.  # noqa: E501
        :rtype: TrustedCertificateDetailsEnddate
        """
        return self._enddate

    @enddate.setter
    def enddate(self, enddate):
        """Sets the enddate of this TrustedCertificatesList.


        :param enddate: The enddate of this TrustedCertificatesList.  # noqa: E501
        :type: TrustedCertificateDetailsEnddate
        """

        self._enddate = enddate

    @property
    def fingerprint(self):
        """Gets the fingerprint of this TrustedCertificatesList.  # noqa: E501

        Fingerprint of the resource  # noqa: E501

        :return: The fingerprint of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this TrustedCertificatesList.

        Fingerprint of the resource  # noqa: E501

        :param fingerprint: The fingerprint of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def hash(self):
        """Gets the hash of this TrustedCertificatesList.  # noqa: E501

        Hash of the resource  # noqa: E501

        :return: The hash of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this TrustedCertificatesList.

        Hash of the resource  # noqa: E501

        :param hash: The hash of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def id(self):
        """Gets the id of this TrustedCertificatesList.  # noqa: E501

        Unique Identifier of the resource  # noqa: E501

        :return: The id of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrustedCertificatesList.

        Unique Identifier of the resource  # noqa: E501

        :param id: The id of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def issuer(self):
        """Gets the issuer of this TrustedCertificatesList.  # noqa: E501

        Issuer of the resource  # noqa: E501

        :return: The issuer of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this TrustedCertificatesList.

        Issuer of the resource  # noqa: E501

        :param issuer: The issuer of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def isvalid(self):
        """Gets the isvalid of this TrustedCertificatesList.  # noqa: E501

        validity of the resource  # noqa: E501

        :return: The isvalid of this TrustedCertificatesList.  # noqa: E501
        :rtype: bool
        """
        return self._isvalid

    @isvalid.setter
    def isvalid(self, isvalid):
        """Sets the isvalid of this TrustedCertificatesList.

        validity of the resource  # noqa: E501

        :param isvalid: The isvalid of this TrustedCertificatesList.  # noqa: E501
        :type: bool
        """

        self._isvalid = isvalid

    @property
    def key_usage(self):
        """Gets the key_usage of this TrustedCertificatesList.  # noqa: E501

        key usage of the resource  # noqa: E501

        :return: The key_usage of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._key_usage

    @key_usage.setter
    def key_usage(self, key_usage):
        """Sets the key_usage of this TrustedCertificatesList.

        key usage of the resource  # noqa: E501

        :param key_usage: The key_usage of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._key_usage = key_usage

    @property
    def pem(self):
        """Gets the pem of this TrustedCertificatesList.  # noqa: E501

        trusted certificate pem  # noqa: E501

        :return: The pem of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._pem

    @pem.setter
    def pem(self, pem):
        """Sets the pem of this TrustedCertificatesList.

        trusted certificate pem  # noqa: E501

        :param pem: The pem of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._pem = pem

    @property
    def serial(self):
        """Gets the serial of this TrustedCertificatesList.  # noqa: E501

        Serial of the resource  # noqa: E501

        :return: The serial of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this TrustedCertificatesList.

        Serial of the resource  # noqa: E501

        :param serial: The serial of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def signaturetype(self):
        """Gets the signaturetype of this TrustedCertificatesList.  # noqa: E501

        Signature type of the resource  # noqa: E501

        :return: The signaturetype of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._signaturetype

    @signaturetype.setter
    def signaturetype(self, signaturetype):
        """Sets the signaturetype of this TrustedCertificatesList.

        Signature type of the resource  # noqa: E501

        :param signaturetype: The signaturetype of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._signaturetype = signaturetype

    @property
    def startdate(self):
        """Gets the startdate of this TrustedCertificatesList.  # noqa: E501


        :return: The startdate of this TrustedCertificatesList.  # noqa: E501
        :rtype: TrustedCertificateDetailsStartdate
        """
        return self._startdate

    @startdate.setter
    def startdate(self, startdate):
        """Sets the startdate of this TrustedCertificatesList.


        :param startdate: The startdate of this TrustedCertificatesList.  # noqa: E501
        :type: TrustedCertificateDetailsStartdate
        """

        self._startdate = startdate

    @property
    def subject(self):
        """Gets the subject of this TrustedCertificatesList.  # noqa: E501

        Subject of the resource  # noqa: E501

        :return: The subject of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this TrustedCertificatesList.

        Subject of the resource  # noqa: E501

        :param subject: The subject of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def system_id(self):
        """Gets the system_id of this TrustedCertificatesList.  # noqa: E501

        SystemID of the array  # noqa: E501

        :return: The system_id of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this TrustedCertificatesList.

        SystemID of the array  # noqa: E501

        :param system_id: The system_id of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def type(self):
        """Gets the type of this TrustedCertificatesList.  # noqa: E501

        The type of resource.  # noqa: E501

        :return: The type of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TrustedCertificatesList.

        The type of resource.  # noqa: E501

        :param type: The type of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uri(self):
        """Gets the uri of this TrustedCertificatesList.  # noqa: E501

        URI of the resource  # noqa: E501

        :return: The uri of this TrustedCertificatesList.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this TrustedCertificatesList.

        URI of the resource  # noqa: E501

        :param uri: The uri of this TrustedCertificatesList.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if not isinstance(other, TrustedCertificatesList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
