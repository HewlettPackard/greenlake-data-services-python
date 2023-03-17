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


class AlertContactsDetails(object):
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
        'company': 'str',
        'company_code': 'str',
        'console_uri': 'str',
        'country': 'str',
        'customer_id': 'str',
        'fax': 'str',
        'first_name': 'str',
        'generation': 'int',
        'id': 'str',
        'include_svc_alerts': 'bool',
        'last_name': 'str',
        'notification_severities': 'list[int]',
        'preferred_language': 'str',
        'primary_email': 'str',
        'primary_phone': 'str',
        'receive_email': 'bool',
        'receive_grouped': 'bool',
        'secondary_email': 'str',
        'secondary_phone': 'str',
        'system_id': 'str',
        'system_support_contact': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'company': 'company',
        'company_code': 'companyCode',
        'console_uri': 'consoleUri',
        'country': 'country',
        'customer_id': 'customerId',
        'fax': 'fax',
        'first_name': 'firstName',
        'generation': 'generation',
        'id': 'id',
        'include_svc_alerts': 'includeSvcAlerts',
        'last_name': 'lastName',
        'notification_severities': 'notificationSeverities',
        'preferred_language': 'preferredLanguage',
        'primary_email': 'primaryEmail',
        'primary_phone': 'primaryPhone',
        'receive_email': 'receiveEmail',
        'receive_grouped': 'receiveGrouped',
        'secondary_email': 'secondaryEmail',
        'secondary_phone': 'secondaryPhone',
        'system_id': 'systemId',
        'system_support_contact': 'systemSupportContact',
        'type': 'type'
    }

    def __init__(self, company=None, company_code=None, console_uri=None, country=None, customer_id=None, fax=None, first_name=None, generation=None, id=None, include_svc_alerts=None, last_name=None, notification_severities=None, preferred_language=None, primary_email=None, primary_phone=None, receive_email=None, receive_grouped=None, secondary_email=None, secondary_phone=None, system_id=None, system_support_contact=None, type=None):  # noqa: E501
        """AlertContactsDetails - a model defined in OpenAPI"""  # noqa: E501

        self._company = None
        self._company_code = None
        self._console_uri = None
        self._country = None
        self._customer_id = None
        self._fax = None
        self._first_name = None
        self._generation = None
        self._id = None
        self._include_svc_alerts = None
        self._last_name = None
        self._notification_severities = None
        self._preferred_language = None
        self._primary_email = None
        self._primary_phone = None
        self._receive_email = None
        self._receive_grouped = None
        self._secondary_email = None
        self._secondary_phone = None
        self._system_id = None
        self._system_support_contact = None
        self._type = None
        self.discriminator = None

        if company is not None:
            self.company = company
        if company_code is not None:
            self.company_code = company_code
        if console_uri is not None:
            self.console_uri = console_uri
        if country is not None:
            self.country = country
        if customer_id is not None:
            self.customer_id = customer_id
        if fax is not None:
            self.fax = fax
        if first_name is not None:
            self.first_name = first_name
        if generation is not None:
            self.generation = generation
        if id is not None:
            self.id = id
        if include_svc_alerts is not None:
            self.include_svc_alerts = include_svc_alerts
        if last_name is not None:
            self.last_name = last_name
        if notification_severities is not None:
            self.notification_severities = notification_severities
        if preferred_language is not None:
            self.preferred_language = preferred_language
        if primary_email is not None:
            self.primary_email = primary_email
        if primary_phone is not None:
            self.primary_phone = primary_phone
        if receive_email is not None:
            self.receive_email = receive_email
        if receive_grouped is not None:
            self.receive_grouped = receive_grouped
        if secondary_email is not None:
            self.secondary_email = secondary_email
        if secondary_phone is not None:
            self.secondary_phone = secondary_phone
        if system_id is not None:
            self.system_id = system_id
        if system_support_contact is not None:
            self.system_support_contact = system_support_contact
        if type is not None:
            self.type = type

    @property
    def company(self):
        """Gets the company of this AlertContactsDetails.  # noqa: E501

        Company  # noqa: E501

        :return: The company of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this AlertContactsDetails.

        Company  # noqa: E501

        :param company: The company of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def company_code(self):
        """Gets the company_code of this AlertContactsDetails.  # noqa: E501

        Company code  # noqa: E501

        :return: The company_code of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._company_code

    @company_code.setter
    def company_code(self, company_code):
        """Sets the company_code of this AlertContactsDetails.

        Company code  # noqa: E501

        :param company_code: The company_code of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._company_code = company_code

    @property
    def console_uri(self):
        """Gets the console_uri of this AlertContactsDetails.  # noqa: E501

        consoleUri for detailed storage object  # noqa: E501

        :return: The console_uri of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this AlertContactsDetails.

        consoleUri for detailed storage object  # noqa: E501

        :param console_uri: The console_uri of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def country(self):
        """Gets the country of this AlertContactsDetails.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AlertContactsDetails.

        Country  # noqa: E501

        :param country: The country of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def customer_id(self):
        """Gets the customer_id of this AlertContactsDetails.  # noqa: E501

        The customer application identifier  # noqa: E501

        :return: The customer_id of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AlertContactsDetails.

        The customer application identifier  # noqa: E501

        :param customer_id: The customer_id of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def fax(self):
        """Gets the fax of this AlertContactsDetails.  # noqa: E501

        Fax number  # noqa: E501

        :return: The fax of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this AlertContactsDetails.

        Fax number  # noqa: E501

        :param fax: The fax of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def first_name(self):
        """Gets the first_name of this AlertContactsDetails.  # noqa: E501

        First name  # noqa: E501

        :return: The first_name of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AlertContactsDetails.

        First name  # noqa: E501

        :param first_name: The first_name of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def generation(self):
        """Gets the generation of this AlertContactsDetails.  # noqa: E501

        A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.   # noqa: E501

        :return: The generation of this AlertContactsDetails.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this AlertContactsDetails.

        A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.   # noqa: E501

        :param generation: The generation of this AlertContactsDetails.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def id(self):
        """Gets the id of this AlertContactsDetails.  # noqa: E501

        Unique Identifier of the contact  # noqa: E501

        :return: The id of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertContactsDetails.

        Unique Identifier of the contact  # noqa: E501

        :param id: The id of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def include_svc_alerts(self):
        """Gets the include_svc_alerts of this AlertContactsDetails.  # noqa: E501

        Email sent to contact shall include service alert  # noqa: E501

        :return: The include_svc_alerts of this AlertContactsDetails.  # noqa: E501
        :rtype: bool
        """
        return self._include_svc_alerts

    @include_svc_alerts.setter
    def include_svc_alerts(self, include_svc_alerts):
        """Sets the include_svc_alerts of this AlertContactsDetails.

        Email sent to contact shall include service alert  # noqa: E501

        :param include_svc_alerts: The include_svc_alerts of this AlertContactsDetails.  # noqa: E501
        :type: bool
        """

        self._include_svc_alerts = include_svc_alerts

    @property
    def last_name(self):
        """Gets the last_name of this AlertContactsDetails.  # noqa: E501

        Last name  # noqa: E501

        :return: The last_name of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AlertContactsDetails.

        Last name  # noqa: E501

        :param last_name: The last_name of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def notification_severities(self):
        """Gets the notification_severities of this AlertContactsDetails.  # noqa: E501

        Severities of notifications the contact will be notificated. An array of number: 0 - Fatal, 1 - Critical, 2 - Major, 3 - Minor, 4 - Degraded, 5 - Info, 6 - Debug  # noqa: E501

        :return: The notification_severities of this AlertContactsDetails.  # noqa: E501
        :rtype: list[int]
        """
        return self._notification_severities

    @notification_severities.setter
    def notification_severities(self, notification_severities):
        """Sets the notification_severities of this AlertContactsDetails.

        Severities of notifications the contact will be notificated. An array of number: 0 - Fatal, 1 - Critical, 2 - Major, 3 - Minor, 4 - Degraded, 5 - Info, 6 - Debug  # noqa: E501

        :param notification_severities: The notification_severities of this AlertContactsDetails.  # noqa: E501
        :type: list[int]
        """

        self._notification_severities = notification_severities

    @property
    def preferred_language(self):
        """Gets the preferred_language of this AlertContactsDetails.  # noqa: E501

        Preferred language when being contacted or emailed  # noqa: E501

        :return: The preferred_language of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._preferred_language

    @preferred_language.setter
    def preferred_language(self, preferred_language):
        """Sets the preferred_language of this AlertContactsDetails.

        Preferred language when being contacted or emailed  # noqa: E501

        :param preferred_language: The preferred_language of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._preferred_language = preferred_language

    @property
    def primary_email(self):
        """Gets the primary_email of this AlertContactsDetails.  # noqa: E501

        Primary email address  # noqa: E501

        :return: The primary_email of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._primary_email

    @primary_email.setter
    def primary_email(self, primary_email):
        """Sets the primary_email of this AlertContactsDetails.

        Primary email address  # noqa: E501

        :param primary_email: The primary_email of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._primary_email = primary_email

    @property
    def primary_phone(self):
        """Gets the primary_phone of this AlertContactsDetails.  # noqa: E501

        Primary phone  # noqa: E501

        :return: The primary_phone of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._primary_phone

    @primary_phone.setter
    def primary_phone(self, primary_phone):
        """Sets the primary_phone of this AlertContactsDetails.

        Primary phone  # noqa: E501

        :param primary_phone: The primary_phone of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._primary_phone = primary_phone

    @property
    def receive_email(self):
        """Gets the receive_email of this AlertContactsDetails.  # noqa: E501

        Contact will receive email notifications. This is a deprecated field and will always pass true to be inline with UI.  # noqa: E501

        :return: The receive_email of this AlertContactsDetails.  # noqa: E501
        :rtype: bool
        """
        return self._receive_email

    @receive_email.setter
    def receive_email(self, receive_email):
        """Sets the receive_email of this AlertContactsDetails.

        Contact will receive email notifications. This is a deprecated field and will always pass true to be inline with UI.  # noqa: E501

        :param receive_email: The receive_email of this AlertContactsDetails.  # noqa: E501
        :type: bool
        """

        self._receive_email = receive_email

    @property
    def receive_grouped(self):
        """Gets the receive_grouped of this AlertContactsDetails.  # noqa: E501

        Contact will receive grouped low urgency email notifications  # noqa: E501

        :return: The receive_grouped of this AlertContactsDetails.  # noqa: E501
        :rtype: bool
        """
        return self._receive_grouped

    @receive_grouped.setter
    def receive_grouped(self, receive_grouped):
        """Sets the receive_grouped of this AlertContactsDetails.

        Contact will receive grouped low urgency email notifications  # noqa: E501

        :param receive_grouped: The receive_grouped of this AlertContactsDetails.  # noqa: E501
        :type: bool
        """

        self._receive_grouped = receive_grouped

    @property
    def secondary_email(self):
        """Gets the secondary_email of this AlertContactsDetails.  # noqa: E501

        Secondary email address  # noqa: E501

        :return: The secondary_email of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._secondary_email

    @secondary_email.setter
    def secondary_email(self, secondary_email):
        """Sets the secondary_email of this AlertContactsDetails.

        Secondary email address  # noqa: E501

        :param secondary_email: The secondary_email of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._secondary_email = secondary_email

    @property
    def secondary_phone(self):
        """Gets the secondary_phone of this AlertContactsDetails.  # noqa: E501

        Secondary phone  # noqa: E501

        :return: The secondary_phone of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._secondary_phone

    @secondary_phone.setter
    def secondary_phone(self, secondary_phone):
        """Sets the secondary_phone of this AlertContactsDetails.

        Secondary phone  # noqa: E501

        :param secondary_phone: The secondary_phone of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._secondary_phone = secondary_phone

    @property
    def system_id(self):
        """Gets the system_id of this AlertContactsDetails.  # noqa: E501

        SystemId/serialNumber of the array.  # noqa: E501

        :return: The system_id of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this AlertContactsDetails.

        SystemId/serialNumber of the array.  # noqa: E501

        :param system_id: The system_id of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def system_support_contact(self):
        """Gets the system_support_contact of this AlertContactsDetails.  # noqa: E501

        Contact will be called for any system issues  # noqa: E501

        :return: The system_support_contact of this AlertContactsDetails.  # noqa: E501
        :rtype: bool
        """
        return self._system_support_contact

    @system_support_contact.setter
    def system_support_contact(self, system_support_contact):
        """Sets the system_support_contact of this AlertContactsDetails.

        Contact will be called for any system issues  # noqa: E501

        :param system_support_contact: The system_support_contact of this AlertContactsDetails.  # noqa: E501
        :type: bool
        """

        self._system_support_contact = system_support_contact

    @property
    def type(self):
        """Gets the type of this AlertContactsDetails.  # noqa: E501

        The type of resource  # noqa: E501

        :return: The type of this AlertContactsDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlertContactsDetails.

        The type of resource  # noqa: E501

        :param type: The type of this AlertContactsDetails.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, AlertContactsDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other