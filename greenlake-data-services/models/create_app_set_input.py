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


class CreateAppSetInput(object):
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
        'app_set_business_unit': 'str',
        'app_set_comments': 'str',
        'app_set_importance': 'str',
        'app_set_name': 'str',
        'app_set_type': 'object',
        'custom_app_type': 'str',
        'members': 'list[str]'
    }

    attribute_map = {
        'app_set_business_unit': 'appSetBusinessUnit',
        'app_set_comments': 'appSetComments',
        'app_set_importance': 'appSetImportance',
        'app_set_name': 'appSetName',
        'app_set_type': 'appSetType',
        'custom_app_type': 'customAppType',
        'members': 'members'
    }

    def __init__(self, app_set_business_unit=None, app_set_comments=None, app_set_importance=None, app_set_name=None, app_set_type=None, custom_app_type=None, members=None):  # noqa: E501
        """CreateAppSetInput - a model defined in OpenAPI"""  # noqa: E501

        self._app_set_business_unit = None
        self._app_set_comments = None
        self._app_set_importance = None
        self._app_set_name = None
        self._app_set_type = None
        self._custom_app_type = None
        self._members = None
        self.discriminator = None

        if app_set_business_unit is not None:
            self.app_set_business_unit = app_set_business_unit
        if app_set_comments is not None:
            self.app_set_comments = app_set_comments
        if app_set_importance is not None:
            self.app_set_importance = app_set_importance
        self.app_set_name = app_set_name
        self.app_set_type = app_set_type
        if custom_app_type is not None:
            self.custom_app_type = custom_app_type
        if members is not None:
            self.members = members

    @property
    def app_set_business_unit(self):
        """Gets the app_set_business_unit of this CreateAppSetInput.  # noqa: E501

        App set business unit  # noqa: E501

        :return: The app_set_business_unit of this CreateAppSetInput.  # noqa: E501
        :rtype: str
        """
        return self._app_set_business_unit

    @app_set_business_unit.setter
    def app_set_business_unit(self, app_set_business_unit):
        """Sets the app_set_business_unit of this CreateAppSetInput.

        App set business unit  # noqa: E501

        :param app_set_business_unit: The app_set_business_unit of this CreateAppSetInput.  # noqa: E501
        :type: str
        """

        self._app_set_business_unit = app_set_business_unit

    @property
    def app_set_comments(self):
        """Gets the app_set_comments of this CreateAppSetInput.  # noqa: E501

        App set comments  # noqa: E501

        :return: The app_set_comments of this CreateAppSetInput.  # noqa: E501
        :rtype: str
        """
        return self._app_set_comments

    @app_set_comments.setter
    def app_set_comments(self, app_set_comments):
        """Sets the app_set_comments of this CreateAppSetInput.

        App set comments  # noqa: E501

        :param app_set_comments: The app_set_comments of this CreateAppSetInput.  # noqa: E501
        :type: str
        """

        self._app_set_comments = app_set_comments

    @property
    def app_set_importance(self):
        """Gets the app_set_importance of this CreateAppSetInput.  # noqa: E501

        App set importance  # noqa: E501

        :return: The app_set_importance of this CreateAppSetInput.  # noqa: E501
        :rtype: str
        """
        return self._app_set_importance

    @app_set_importance.setter
    def app_set_importance(self, app_set_importance):
        """Sets the app_set_importance of this CreateAppSetInput.

        App set importance  # noqa: E501

        :param app_set_importance: The app_set_importance of this CreateAppSetInput.  # noqa: E501
        :type: str
        """

        self._app_set_importance = app_set_importance

    @property
    def app_set_name(self):
        """Gets the app_set_name of this CreateAppSetInput.  # noqa: E501

        App set name  # noqa: E501

        :return: The app_set_name of this CreateAppSetInput.  # noqa: E501
        :rtype: str
        """
        return self._app_set_name

    @app_set_name.setter
    def app_set_name(self, app_set_name):
        """Sets the app_set_name of this CreateAppSetInput.

        App set name  # noqa: E501

        :param app_set_name: The app_set_name of this CreateAppSetInput.  # noqa: E501
        :type: str
        """
        if app_set_name is None:
            raise ValueError("Invalid value for `app_set_name`, must not be `None`")  # noqa: E501

        self._app_set_name = app_set_name

    @property
    def app_set_type(self):
        """Gets the app_set_type of this CreateAppSetInput.  # noqa: E501


        :return: The app_set_type of this CreateAppSetInput.  # noqa: E501
        :rtype: object
        """
        return self._app_set_type

    @app_set_type.setter
    def app_set_type(self, app_set_type):
        """Sets the app_set_type of this CreateAppSetInput.


        :param app_set_type: The app_set_type of this CreateAppSetInput.  # noqa: E501
        :type: object
        """
        if app_set_type is None:
            raise ValueError("Invalid value for `app_set_type`, must not be `None`")  # noqa: E501

        self._app_set_type = app_set_type

    @property
    def custom_app_type(self):
        """Gets the custom_app_type of this CreateAppSetInput.  # noqa: E501

        App set name for Custom workloads when appSetType=CUSTOM  # noqa: E501

        :return: The custom_app_type of this CreateAppSetInput.  # noqa: E501
        :rtype: str
        """
        return self._custom_app_type

    @custom_app_type.setter
    def custom_app_type(self, custom_app_type):
        """Sets the custom_app_type of this CreateAppSetInput.

        App set name for Custom workloads when appSetType=CUSTOM  # noqa: E501

        :param custom_app_type: The custom_app_type of this CreateAppSetInput.  # noqa: E501
        :type: str
        """

        self._custom_app_type = custom_app_type

    @property
    def members(self):
        """Gets the members of this CreateAppSetInput.  # noqa: E501

        volumes list  # noqa: E501

        :return: The members of this CreateAppSetInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this CreateAppSetInput.

        volumes list  # noqa: E501

        :param members: The members of this CreateAppSetInput.  # noqa: E501
        :type: list[str]
        """

        self._members = members

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
        if not isinstance(other, CreateAppSetInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other