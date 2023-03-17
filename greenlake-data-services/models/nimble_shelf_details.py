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


class NimbleShelfDetails(object):
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
        'associated_links': 'AssociatedLinks',
        'chassis_sensors': 'list[NimbleNsShelfSensor]',
        'chassis_type': 'str',
        'console_uri': 'str',
        'ctrlrs': 'list[NimbleNsShelfCtrlr]',
        'customer_id': 'str',
        'disk_sets': 'list[NimbleNsDiskSetAttr]',
        'fan_overall_status': 'str',
        'generation': 'int',
        'model_ext': 'str',
        'psu_overall_status': 'str',
        'resource_uri': 'str',
        'temp_overall_status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'associated_links': 'associated_links',
        'chassis_sensors': 'chassis_sensors',
        'chassis_type': 'chassis_type',
        'console_uri': 'consoleUri',
        'ctrlrs': 'ctrlrs',
        'customer_id': 'customerId',
        'disk_sets': 'disk_sets',
        'fan_overall_status': 'fan_overall_status',
        'generation': 'generation',
        'model_ext': 'model_ext',
        'psu_overall_status': 'psu_overall_status',
        'resource_uri': 'resourceUri',
        'temp_overall_status': 'temp_overall_status',
        'type': 'type'
    }

    def __init__(self, associated_links=None, chassis_sensors=None, chassis_type=None, console_uri=None, ctrlrs=None, customer_id=None, disk_sets=None, fan_overall_status=None, generation=None, model_ext=None, psu_overall_status=None, resource_uri=None, temp_overall_status=None, type=None):  # noqa: E501
        """NimbleShelfDetails - a model defined in OpenAPI"""  # noqa: E501

        self._associated_links = None
        self._chassis_sensors = None
        self._chassis_type = None
        self._console_uri = None
        self._ctrlrs = None
        self._customer_id = None
        self._disk_sets = None
        self._fan_overall_status = None
        self._generation = None
        self._model_ext = None
        self._psu_overall_status = None
        self._resource_uri = None
        self._temp_overall_status = None
        self._type = None
        self.discriminator = None

        if associated_links is not None:
            self.associated_links = associated_links
        if chassis_sensors is not None:
            self.chassis_sensors = chassis_sensors
        if chassis_type is not None:
            self.chassis_type = chassis_type
        if console_uri is not None:
            self.console_uri = console_uri
        if ctrlrs is not None:
            self.ctrlrs = ctrlrs
        if customer_id is not None:
            self.customer_id = customer_id
        if disk_sets is not None:
            self.disk_sets = disk_sets
        if fan_overall_status is not None:
            self.fan_overall_status = fan_overall_status
        if generation is not None:
            self.generation = generation
        if model_ext is not None:
            self.model_ext = model_ext
        if psu_overall_status is not None:
            self.psu_overall_status = psu_overall_status
        if resource_uri is not None:
            self.resource_uri = resource_uri
        if temp_overall_status is not None:
            self.temp_overall_status = temp_overall_status
        if type is not None:
            self.type = type

    @property
    def associated_links(self):
        """Gets the associated_links of this NimbleShelfDetails.  # noqa: E501


        :return: The associated_links of this NimbleShelfDetails.  # noqa: E501
        :rtype: AssociatedLinks
        """
        return self._associated_links

    @associated_links.setter
    def associated_links(self, associated_links):
        """Sets the associated_links of this NimbleShelfDetails.


        :param associated_links: The associated_links of this NimbleShelfDetails.  # noqa: E501
        :type: AssociatedLinks
        """

        self._associated_links = associated_links

    @property
    def chassis_sensors(self):
        """Gets the chassis_sensors of this NimbleShelfDetails.  # noqa: E501

        List of chassis sensor readings.  # noqa: E501

        :return: The chassis_sensors of this NimbleShelfDetails.  # noqa: E501
        :rtype: list[NimbleNsShelfSensor]
        """
        return self._chassis_sensors

    @chassis_sensors.setter
    def chassis_sensors(self, chassis_sensors):
        """Sets the chassis_sensors of this NimbleShelfDetails.

        List of chassis sensor readings.  # noqa: E501

        :param chassis_sensors: The chassis_sensors of this NimbleShelfDetails.  # noqa: E501
        :type: list[NimbleNsShelfSensor]
        """

        self._chassis_sensors = chassis_sensors

    @property
    def chassis_type(self):
        """Gets the chassis_type of this NimbleShelfDetails.  # noqa: E501

        Chassis type. Possible values: 'chassis_unknown', 'chassis_3u16', 'chassis_4u24', 'chassis_nmbl_2u12', 'chassis_nmbl_4u24'  # noqa: E501

        :return: The chassis_type of this NimbleShelfDetails.  # noqa: E501
        :rtype: str
        """
        return self._chassis_type

    @chassis_type.setter
    def chassis_type(self, chassis_type):
        """Sets the chassis_type of this NimbleShelfDetails.

        Chassis type. Possible values: 'chassis_unknown', 'chassis_3u16', 'chassis_4u24', 'chassis_nmbl_2u12', 'chassis_nmbl_4u24'  # noqa: E501

        :param chassis_type: The chassis_type of this NimbleShelfDetails.  # noqa: E501
        :type: str
        """

        self._chassis_type = chassis_type

    @property
    def console_uri(self):
        """Gets the console_uri of this NimbleShelfDetails.  # noqa: E501

        consoleUri for detailed storage object  # noqa: E501

        :return: The console_uri of this NimbleShelfDetails.  # noqa: E501
        :rtype: str
        """
        return self._console_uri

    @console_uri.setter
    def console_uri(self, console_uri):
        """Sets the console_uri of this NimbleShelfDetails.

        consoleUri for detailed storage object  # noqa: E501

        :param console_uri: The console_uri of this NimbleShelfDetails.  # noqa: E501
        :type: str
        """

        self._console_uri = console_uri

    @property
    def ctrlrs(self):
        """Gets the ctrlrs of this NimbleShelfDetails.  # noqa: E501

        List of ctrlr info.  # noqa: E501

        :return: The ctrlrs of this NimbleShelfDetails.  # noqa: E501
        :rtype: list[NimbleNsShelfCtrlr]
        """
        return self._ctrlrs

    @ctrlrs.setter
    def ctrlrs(self, ctrlrs):
        """Sets the ctrlrs of this NimbleShelfDetails.

        List of ctrlr info.  # noqa: E501

        :param ctrlrs: The ctrlrs of this NimbleShelfDetails.  # noqa: E501
        :type: list[NimbleNsShelfCtrlr]
        """

        self._ctrlrs = ctrlrs

    @property
    def customer_id(self):
        """Gets the customer_id of this NimbleShelfDetails.  # noqa: E501

        customerId  # noqa: E501

        :return: The customer_id of this NimbleShelfDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this NimbleShelfDetails.

        customerId  # noqa: E501

        :param customer_id: The customer_id of this NimbleShelfDetails.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def disk_sets(self):
        """Gets the disk_sets of this NimbleShelfDetails.  # noqa: E501

        Attributes for the disk sets in this shelf.  # noqa: E501

        :return: The disk_sets of this NimbleShelfDetails.  # noqa: E501
        :rtype: list[NimbleNsDiskSetAttr]
        """
        return self._disk_sets

    @disk_sets.setter
    def disk_sets(self, disk_sets):
        """Sets the disk_sets of this NimbleShelfDetails.

        Attributes for the disk sets in this shelf.  # noqa: E501

        :param disk_sets: The disk_sets of this NimbleShelfDetails.  # noqa: E501
        :type: list[NimbleNsDiskSetAttr]
        """

        self._disk_sets = disk_sets

    @property
    def fan_overall_status(self):
        """Gets the fan_overall_status of this NimbleShelfDetails.  # noqa: E501

        The overall status for the fans on both controllers. Possible values: 'OK', 'Alerted', 'Failed', 'Missing'.  # noqa: E501

        :return: The fan_overall_status of this NimbleShelfDetails.  # noqa: E501
        :rtype: str
        """
        return self._fan_overall_status

    @fan_overall_status.setter
    def fan_overall_status(self, fan_overall_status):
        """Sets the fan_overall_status of this NimbleShelfDetails.

        The overall status for the fans on both controllers. Possible values: 'OK', 'Alerted', 'Failed', 'Missing'.  # noqa: E501

        :param fan_overall_status: The fan_overall_status of this NimbleShelfDetails.  # noqa: E501
        :type: str
        """

        self._fan_overall_status = fan_overall_status

    @property
    def generation(self):
        """Gets the generation of this NimbleShelfDetails.  # noqa: E501

        generation  # noqa: E501

        :return: The generation of this NimbleShelfDetails.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this NimbleShelfDetails.

        generation  # noqa: E501

        :param generation: The generation of this NimbleShelfDetails.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def model_ext(self):
        """Gets the model_ext of this NimbleShelfDetails.  # noqa: E501

        Extended model of the shelf or head unit.  # noqa: E501

        :return: The model_ext of this NimbleShelfDetails.  # noqa: E501
        :rtype: str
        """
        return self._model_ext

    @model_ext.setter
    def model_ext(self, model_ext):
        """Sets the model_ext of this NimbleShelfDetails.

        Extended model of the shelf or head unit.  # noqa: E501

        :param model_ext: The model_ext of this NimbleShelfDetails.  # noqa: E501
        :type: str
        """

        self._model_ext = model_ext

    @property
    def psu_overall_status(self):
        """Gets the psu_overall_status of this NimbleShelfDetails.  # noqa: E501

        The overall status for the PSUs. Possible values: 'OK', 'Alerted', 'Failed', 'Missing'.  # noqa: E501

        :return: The psu_overall_status of this NimbleShelfDetails.  # noqa: E501
        :rtype: str
        """
        return self._psu_overall_status

    @psu_overall_status.setter
    def psu_overall_status(self, psu_overall_status):
        """Sets the psu_overall_status of this NimbleShelfDetails.

        The overall status for the PSUs. Possible values: 'OK', 'Alerted', 'Failed', 'Missing'.  # noqa: E501

        :param psu_overall_status: The psu_overall_status of this NimbleShelfDetails.  # noqa: E501
        :type: str
        """

        self._psu_overall_status = psu_overall_status

    @property
    def resource_uri(self):
        """Gets the resource_uri of this NimbleShelfDetails.  # noqa: E501


        :return: The resource_uri of this NimbleShelfDetails.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this NimbleShelfDetails.


        :param resource_uri: The resource_uri of this NimbleShelfDetails.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

    @property
    def temp_overall_status(self):
        """Gets the temp_overall_status of this NimbleShelfDetails.  # noqa: E501

        The overall status for the temperature on both controllers. Possible values: 'OK', 'Alerted', 'Failed', 'Missing'.  # noqa: E501

        :return: The temp_overall_status of this NimbleShelfDetails.  # noqa: E501
        :rtype: str
        """
        return self._temp_overall_status

    @temp_overall_status.setter
    def temp_overall_status(self, temp_overall_status):
        """Sets the temp_overall_status of this NimbleShelfDetails.

        The overall status for the temperature on both controllers. Possible values: 'OK', 'Alerted', 'Failed', 'Missing'.  # noqa: E501

        :param temp_overall_status: The temp_overall_status of this NimbleShelfDetails.  # noqa: E501
        :type: str
        """

        self._temp_overall_status = temp_overall_status

    @property
    def type(self):
        """Gets the type of this NimbleShelfDetails.  # noqa: E501

        type  # noqa: E501

        :return: The type of this NimbleShelfDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NimbleShelfDetails.

        type  # noqa: E501

        :param type: The type of this NimbleShelfDetails.  # noqa: E501
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
        if not isinstance(other, NimbleShelfDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
