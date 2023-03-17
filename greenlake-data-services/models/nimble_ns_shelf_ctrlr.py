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


class NimbleNsShelfCtrlr(object):
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
        'cached_serial': 'str',
        'ctrlr_attrset_list': 'list[NimbleNsShelfCtrlrAttrSet]',
        'ctrlr_hw_model': 'str',
        'ctrlr_sensor_last_run': 'int',
        'ctrlr_sensors': 'list[NimbleNsShelfSensor]',
        'ctrlr_side': 'str',
        'enc_loc_id': 'int',
        'exp_sas_addr': 'str',
        'extra_attributes': 'list[str]',
        'fan_overall_status': 'str',
        'hw_master_state': 'str',
        'hw_mship_failure': 'bool',
        'identify_status': 'bool',
        'port_info': 'list[NimbleNsShelfPortInfo]',
        'psu_overall_status': 'str',
        'sw_master_state': 'str',
        'temp_overall_status': 'str'
    }

    attribute_map = {
        'cached_serial': 'cached_serial',
        'ctrlr_attrset_list': 'ctrlr_attrset_list',
        'ctrlr_hw_model': 'ctrlr_hw_model',
        'ctrlr_sensor_last_run': 'ctrlr_sensor_last_run',
        'ctrlr_sensors': 'ctrlr_sensors',
        'ctrlr_side': 'ctrlr_side',
        'enc_loc_id': 'enc_loc_id',
        'exp_sas_addr': 'exp_sas_addr',
        'extra_attributes': 'extra_attributes',
        'fan_overall_status': 'fan_overall_status',
        'hw_master_state': 'hw_master_state',
        'hw_mship_failure': 'hw_mship_failure',
        'identify_status': 'identify_status',
        'port_info': 'port_info',
        'psu_overall_status': 'psu_overall_status',
        'sw_master_state': 'sw_master_state',
        'temp_overall_status': 'temp_overall_status'
    }

    def __init__(self, cached_serial=None, ctrlr_attrset_list=None, ctrlr_hw_model=None, ctrlr_sensor_last_run=None, ctrlr_sensors=None, ctrlr_side=None, enc_loc_id=None, exp_sas_addr=None, extra_attributes=None, fan_overall_status=None, hw_master_state=None, hw_mship_failure=None, identify_status=None, port_info=None, psu_overall_status=None, sw_master_state=None, temp_overall_status=None):  # noqa: E501
        """NimbleNsShelfCtrlr - a model defined in OpenAPI"""  # noqa: E501

        self._cached_serial = None
        self._ctrlr_attrset_list = None
        self._ctrlr_hw_model = None
        self._ctrlr_sensor_last_run = None
        self._ctrlr_sensors = None
        self._ctrlr_side = None
        self._enc_loc_id = None
        self._exp_sas_addr = None
        self._extra_attributes = None
        self._fan_overall_status = None
        self._hw_master_state = None
        self._hw_mship_failure = None
        self._identify_status = None
        self._port_info = None
        self._psu_overall_status = None
        self._sw_master_state = None
        self._temp_overall_status = None
        self.discriminator = None

        if cached_serial is not None:
            self.cached_serial = cached_serial
        if ctrlr_attrset_list is not None:
            self.ctrlr_attrset_list = ctrlr_attrset_list
        if ctrlr_hw_model is not None:
            self.ctrlr_hw_model = ctrlr_hw_model
        if ctrlr_sensor_last_run is not None:
            self.ctrlr_sensor_last_run = ctrlr_sensor_last_run
        if ctrlr_sensors is not None:
            self.ctrlr_sensors = ctrlr_sensors
        if ctrlr_side is not None:
            self.ctrlr_side = ctrlr_side
        if enc_loc_id is not None:
            self.enc_loc_id = enc_loc_id
        if exp_sas_addr is not None:
            self.exp_sas_addr = exp_sas_addr
        if extra_attributes is not None:
            self.extra_attributes = extra_attributes
        if fan_overall_status is not None:
            self.fan_overall_status = fan_overall_status
        if hw_master_state is not None:
            self.hw_master_state = hw_master_state
        if hw_mship_failure is not None:
            self.hw_mship_failure = hw_mship_failure
        if identify_status is not None:
            self.identify_status = identify_status
        if port_info is not None:
            self.port_info = port_info
        if psu_overall_status is not None:
            self.psu_overall_status = psu_overall_status
        if sw_master_state is not None:
            self.sw_master_state = sw_master_state
        if temp_overall_status is not None:
            self.temp_overall_status = temp_overall_status

    @property
    def cached_serial(self):
        """Gets the cached_serial of this NimbleNsShelfCtrlr.  # noqa: E501

        CachedSerial - Cached serial.  # noqa: E501

        :return: The cached_serial of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: str
        """
        return self._cached_serial

    @cached_serial.setter
    def cached_serial(self, cached_serial):
        """Sets the cached_serial of this NimbleNsShelfCtrlr.

        CachedSerial - Cached serial.  # noqa: E501

        :param cached_serial: The cached_serial of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: str
        """

        self._cached_serial = cached_serial

    @property
    def ctrlr_attrset_list(self):
        """Gets the ctrlr_attrset_list of this NimbleNsShelfCtrlr.  # noqa: E501

        List of ctrlr attribute set for each logical controller.  # noqa: E501

        :return: The ctrlr_attrset_list of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: list[NimbleNsShelfCtrlrAttrSet]
        """
        return self._ctrlr_attrset_list

    @ctrlr_attrset_list.setter
    def ctrlr_attrset_list(self, ctrlr_attrset_list):
        """Sets the ctrlr_attrset_list of this NimbleNsShelfCtrlr.

        List of ctrlr attribute set for each logical controller.  # noqa: E501

        :param ctrlr_attrset_list: The ctrlr_attrset_list of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: list[NimbleNsShelfCtrlrAttrSet]
        """

        self._ctrlr_attrset_list = ctrlr_attrset_list

    @property
    def ctrlr_hw_model(self):
        """Gets the ctrlr_hw_model of this NimbleNsShelfCtrlr.  # noqa: E501

        Controller hardware model. Possible values:'head_x9', 'head_x8', 'head_gen5_2u', 'es2_4u', 'head_vmware', 'es1_3u', 'head_x9_2u', 'head_x10', 'head_gen5', 'es3_4u', 'unknown'.  # noqa: E501

        :return: The ctrlr_hw_model of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: str
        """
        return self._ctrlr_hw_model

    @ctrlr_hw_model.setter
    def ctrlr_hw_model(self, ctrlr_hw_model):
        """Sets the ctrlr_hw_model of this NimbleNsShelfCtrlr.

        Controller hardware model. Possible values:'head_x9', 'head_x8', 'head_gen5_2u', 'es2_4u', 'head_vmware', 'es1_3u', 'head_x9_2u', 'head_x10', 'head_gen5', 'es3_4u', 'unknown'.  # noqa: E501

        :param ctrlr_hw_model: The ctrlr_hw_model of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: str
        """

        self._ctrlr_hw_model = ctrlr_hw_model

    @property
    def ctrlr_sensor_last_run(self):
        """Gets the ctrlr_sensor_last_run of this NimbleNsShelfCtrlr.  # noqa: E501

        The time of last valid sensor reading, in epoch seconds.  # noqa: E501

        :return: The ctrlr_sensor_last_run of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: int
        """
        return self._ctrlr_sensor_last_run

    @ctrlr_sensor_last_run.setter
    def ctrlr_sensor_last_run(self, ctrlr_sensor_last_run):
        """Sets the ctrlr_sensor_last_run of this NimbleNsShelfCtrlr.

        The time of last valid sensor reading, in epoch seconds.  # noqa: E501

        :param ctrlr_sensor_last_run: The ctrlr_sensor_last_run of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: int
        """

        self._ctrlr_sensor_last_run = ctrlr_sensor_last_run

    @property
    def ctrlr_sensors(self):
        """Gets the ctrlr_sensors of this NimbleNsShelfCtrlr.  # noqa: E501

        The list of individual sensor reading in this controller.  # noqa: E501

        :return: The ctrlr_sensors of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: list[NimbleNsShelfSensor]
        """
        return self._ctrlr_sensors

    @ctrlr_sensors.setter
    def ctrlr_sensors(self, ctrlr_sensors):
        """Sets the ctrlr_sensors of this NimbleNsShelfCtrlr.

        The list of individual sensor reading in this controller.  # noqa: E501

        :param ctrlr_sensors: The ctrlr_sensors of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: list[NimbleNsShelfSensor]
        """

        self._ctrlr_sensors = ctrlr_sensors

    @property
    def ctrlr_side(self):
        """Gets the ctrlr_side of this NimbleNsShelfCtrlr.  # noqa: E501

        Position of this controller in the chassis. Possible values:'A', 'B', 'unknown'.  # noqa: E501

        :return: The ctrlr_side of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: str
        """
        return self._ctrlr_side

    @ctrlr_side.setter
    def ctrlr_side(self, ctrlr_side):
        """Sets the ctrlr_side of this NimbleNsShelfCtrlr.

        Position of this controller in the chassis. Possible values:'A', 'B', 'unknown'.  # noqa: E501

        :param ctrlr_side: The ctrlr_side of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: str
        """

        self._ctrlr_side = ctrlr_side

    @property
    def enc_loc_id(self):
        """Gets the enc_loc_id of this NimbleNsShelfCtrlr.  # noqa: E501

        Location ID based on SAS topology.  # noqa: E501

        :return: The enc_loc_id of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: int
        """
        return self._enc_loc_id

    @enc_loc_id.setter
    def enc_loc_id(self, enc_loc_id):
        """Sets the enc_loc_id of this NimbleNsShelfCtrlr.

        Location ID based on SAS topology.  # noqa: E501

        :param enc_loc_id: The enc_loc_id of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: int
        """

        self._enc_loc_id = enc_loc_id

    @property
    def exp_sas_addr(self):
        """Gets the exp_sas_addr of this NimbleNsShelfCtrlr.  # noqa: E501

        Expander SAS address.  # noqa: E501

        :return: The exp_sas_addr of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: str
        """
        return self._exp_sas_addr

    @exp_sas_addr.setter
    def exp_sas_addr(self, exp_sas_addr):
        """Sets the exp_sas_addr of this NimbleNsShelfCtrlr.

        Expander SAS address.  # noqa: E501

        :param exp_sas_addr: The exp_sas_addr of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: str
        """

        self._exp_sas_addr = exp_sas_addr

    @property
    def extra_attributes(self):
        """Gets the extra_attributes of this NimbleNsShelfCtrlr.  # noqa: E501

        Extra attributes as attribute value pairs.  # noqa: E501

        :return: The extra_attributes of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: list[str]
        """
        return self._extra_attributes

    @extra_attributes.setter
    def extra_attributes(self, extra_attributes):
        """Sets the extra_attributes of this NimbleNsShelfCtrlr.

        Extra attributes as attribute value pairs.  # noqa: E501

        :param extra_attributes: The extra_attributes of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: list[str]
        """

        self._extra_attributes = extra_attributes

    @property
    def fan_overall_status(self):
        """Gets the fan_overall_status of this NimbleNsShelfCtrlr.  # noqa: E501

        The overall status for the fans on this controller. Possible values:'Missing', 'Failed', 'OK', 'Alerted'.  # noqa: E501

        :return: The fan_overall_status of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: str
        """
        return self._fan_overall_status

    @fan_overall_status.setter
    def fan_overall_status(self, fan_overall_status):
        """Sets the fan_overall_status of this NimbleNsShelfCtrlr.

        The overall status for the fans on this controller. Possible values:'Missing', 'Failed', 'OK', 'Alerted'.  # noqa: E501

        :param fan_overall_status: The fan_overall_status of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: str
        """

        self._fan_overall_status = fan_overall_status

    @property
    def hw_master_state(self):
        """Gets the hw_master_state of this NimbleNsShelfCtrlr.  # noqa: E501

        SES device hardware mastership state. Possible values:'not master', 'failed', 'unknown', 'master'.  # noqa: E501

        :return: The hw_master_state of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: str
        """
        return self._hw_master_state

    @hw_master_state.setter
    def hw_master_state(self, hw_master_state):
        """Sets the hw_master_state of this NimbleNsShelfCtrlr.

        SES device hardware mastership state. Possible values:'not master', 'failed', 'unknown', 'master'.  # noqa: E501

        :param hw_master_state: The hw_master_state of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: str
        """

        self._hw_master_state = hw_master_state

    @property
    def hw_mship_failure(self):
        """Gets the hw_mship_failure of this NimbleNsShelfCtrlr.  # noqa: E501

        SES device hardware mastership failure.  # noqa: E501

        :return: The hw_mship_failure of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: bool
        """
        return self._hw_mship_failure

    @hw_mship_failure.setter
    def hw_mship_failure(self, hw_mship_failure):
        """Sets the hw_mship_failure of this NimbleNsShelfCtrlr.

        SES device hardware mastership failure.  # noqa: E501

        :param hw_mship_failure: The hw_mship_failure of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: bool
        """

        self._hw_mship_failure = hw_mship_failure

    @property
    def identify_status(self):
        """Gets the identify_status of this NimbleNsShelfCtrlr.  # noqa: E501

        Status of chassis identifier.  # noqa: E501

        :return: The identify_status of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: bool
        """
        return self._identify_status

    @identify_status.setter
    def identify_status(self, identify_status):
        """Sets the identify_status of this NimbleNsShelfCtrlr.

        Status of chassis identifier.  # noqa: E501

        :param identify_status: The identify_status of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: bool
        """

        self._identify_status = identify_status

    @property
    def port_info(self):
        """Gets the port_info of this NimbleNsShelfCtrlr.  # noqa: E501

        Port info for each SAS port.  # noqa: E501

        :return: The port_info of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: list[NimbleNsShelfPortInfo]
        """
        return self._port_info

    @port_info.setter
    def port_info(self, port_info):
        """Sets the port_info of this NimbleNsShelfCtrlr.

        Port info for each SAS port.  # noqa: E501

        :param port_info: The port_info of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: list[NimbleNsShelfPortInfo]
        """

        self._port_info = port_info

    @property
    def psu_overall_status(self):
        """Gets the psu_overall_status of this NimbleNsShelfCtrlr.  # noqa: E501

        The overall status for the PSU on this controller.. Possible values: 'OK', 'Alerted', 'Failed', 'Missing'.  # noqa: E501

        :return: The psu_overall_status of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: str
        """
        return self._psu_overall_status

    @psu_overall_status.setter
    def psu_overall_status(self, psu_overall_status):
        """Sets the psu_overall_status of this NimbleNsShelfCtrlr.

        The overall status for the PSU on this controller.. Possible values: 'OK', 'Alerted', 'Failed', 'Missing'.  # noqa: E501

        :param psu_overall_status: The psu_overall_status of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: str
        """

        self._psu_overall_status = psu_overall_status

    @property
    def sw_master_state(self):
        """Gets the sw_master_state of this NimbleNsShelfCtrlr.  # noqa: E501

        SES device software mastership state. Possible values:'not master', 'want master', 'unknown', 'master', 'release master'.  # noqa: E501

        :return: The sw_master_state of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: str
        """
        return self._sw_master_state

    @sw_master_state.setter
    def sw_master_state(self, sw_master_state):
        """Sets the sw_master_state of this NimbleNsShelfCtrlr.

        SES device software mastership state. Possible values:'not master', 'want master', 'unknown', 'master', 'release master'.  # noqa: E501

        :param sw_master_state: The sw_master_state of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: str
        """

        self._sw_master_state = sw_master_state

    @property
    def temp_overall_status(self):
        """Gets the temp_overall_status of this NimbleNsShelfCtrlr.  # noqa: E501

        The overall status for the temperature of this controller.  Possible values:'Missing', 'Failed', 'OK', 'Alerted'.  # noqa: E501

        :return: The temp_overall_status of this NimbleNsShelfCtrlr.  # noqa: E501
        :rtype: str
        """
        return self._temp_overall_status

    @temp_overall_status.setter
    def temp_overall_status(self, temp_overall_status):
        """Sets the temp_overall_status of this NimbleNsShelfCtrlr.

        The overall status for the temperature of this controller.  Possible values:'Missing', 'Failed', 'OK', 'Alerted'.  # noqa: E501

        :param temp_overall_status: The temp_overall_status of this NimbleNsShelfCtrlr.  # noqa: E501
        :type: str
        """

        self._temp_overall_status = temp_overall_status

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
        if not isinstance(other, NimbleNsShelfCtrlr):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
