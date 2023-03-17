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


class NimbleNsDiskSetAttr(object):
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
        'ave_mb_ps': 'int',
        'ave_segment_ps': 'int',
        'ave_ttc': 'int',
        'driveset': 'int',
        'is_capacity_valid': 'bool',
        'is_flash_shelf': 'bool',
        'pause_state': 'int',
        'pct_completion': 'int',
        'raw_cache_capacity': 'int',
        'raw_capacity': 'int',
        'sw_state': 'str',
        'usable_cache_capacity': 'int',
        'usable_capacity': 'int'
    }

    attribute_map = {
        'ave_mb_ps': 'ave_mb_ps',
        'ave_segment_ps': 'ave_segment_ps',
        'ave_ttc': 'ave_ttc',
        'driveset': 'driveset',
        'is_capacity_valid': 'is_capacity_valid',
        'is_flash_shelf': 'is_flash_shelf',
        'pause_state': 'pause_state',
        'pct_completion': 'pct_completion',
        'raw_cache_capacity': 'raw_cache_capacity',
        'raw_capacity': 'raw_capacity',
        'sw_state': 'sw_state',
        'usable_cache_capacity': 'usable_cache_capacity',
        'usable_capacity': 'usable_capacity'
    }

    def __init__(self, ave_mb_ps=None, ave_segment_ps=None, ave_ttc=None, driveset=None, is_capacity_valid=None, is_flash_shelf=None, pause_state=None, pct_completion=None, raw_cache_capacity=None, raw_capacity=None, sw_state=None, usable_cache_capacity=None, usable_capacity=None):  # noqa: E501
        """NimbleNsDiskSetAttr - a model defined in OpenAPI"""  # noqa: E501

        self._ave_mb_ps = None
        self._ave_segment_ps = None
        self._ave_ttc = None
        self._driveset = None
        self._is_capacity_valid = None
        self._is_flash_shelf = None
        self._pause_state = None
        self._pct_completion = None
        self._raw_cache_capacity = None
        self._raw_capacity = None
        self._sw_state = None
        self._usable_cache_capacity = None
        self._usable_capacity = None
        self.discriminator = None

        if ave_mb_ps is not None:
            self.ave_mb_ps = ave_mb_ps
        if ave_segment_ps is not None:
            self.ave_segment_ps = ave_segment_ps
        if ave_ttc is not None:
            self.ave_ttc = ave_ttc
        if driveset is not None:
            self.driveset = driveset
        if is_capacity_valid is not None:
            self.is_capacity_valid = is_capacity_valid
        if is_flash_shelf is not None:
            self.is_flash_shelf = is_flash_shelf
        if pause_state is not None:
            self.pause_state = pause_state
        if pct_completion is not None:
            self.pct_completion = pct_completion
        if raw_cache_capacity is not None:
            self.raw_cache_capacity = raw_cache_capacity
        if raw_capacity is not None:
            self.raw_capacity = raw_capacity
        if sw_state is not None:
            self.sw_state = sw_state
        if usable_cache_capacity is not None:
            self.usable_cache_capacity = usable_cache_capacity
        if usable_capacity is not None:
            self.usable_capacity = usable_capacity

    @property
    def ave_mb_ps(self):
        """Gets the ave_mb_ps of this NimbleNsDiskSetAttr.  # noqa: E501

        Average evacuation speed in MB/s; valid only when sw_state is evacuating, ie. evacuation is underway.  # noqa: E501

        :return: The ave_mb_ps of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: int
        """
        return self._ave_mb_ps

    @ave_mb_ps.setter
    def ave_mb_ps(self, ave_mb_ps):
        """Sets the ave_mb_ps of this NimbleNsDiskSetAttr.

        Average evacuation speed in MB/s; valid only when sw_state is evacuating, ie. evacuation is underway.  # noqa: E501

        :param ave_mb_ps: The ave_mb_ps of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: int
        """

        self._ave_mb_ps = ave_mb_ps

    @property
    def ave_segment_ps(self):
        """Gets the ave_segment_ps of this NimbleNsDiskSetAttr.  # noqa: E501

        Average evacuation speed in segments/sec; valid only when sw_state is evacuating, ie. evacuation is underway.  # noqa: E501

        :return: The ave_segment_ps of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: int
        """
        return self._ave_segment_ps

    @ave_segment_ps.setter
    def ave_segment_ps(self, ave_segment_ps):
        """Sets the ave_segment_ps of this NimbleNsDiskSetAttr.

        Average evacuation speed in segments/sec; valid only when sw_state is evacuating, ie. evacuation is underway.  # noqa: E501

        :param ave_segment_ps: The ave_segment_ps of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: int
        """

        self._ave_segment_ps = ave_segment_ps

    @property
    def ave_ttc(self):
        """Gets the ave_ttc of this NimbleNsDiskSetAttr.  # noqa: E501

        Average time to complete in seconds; valid only when sw_state is evacuating, ie. evacuation is underway.  # noqa: E501

        :return: The ave_ttc of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: int
        """
        return self._ave_ttc

    @ave_ttc.setter
    def ave_ttc(self, ave_ttc):
        """Sets the ave_ttc of this NimbleNsDiskSetAttr.

        Average time to complete in seconds; valid only when sw_state is evacuating, ie. evacuation is underway.  # noqa: E501

        :param ave_ttc: The ave_ttc of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: int
        """

        self._ave_ttc = ave_ttc

    @property
    def driveset(self):
        """Gets the driveset of this NimbleNsDiskSetAttr.  # noqa: E501

        Driveset index for this shelf.  # noqa: E501

        :return: The driveset of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: int
        """
        return self._driveset

    @driveset.setter
    def driveset(self, driveset):
        """Sets the driveset of this NimbleNsDiskSetAttr.

        Driveset index for this shelf.  # noqa: E501

        :param driveset: The driveset of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: int
        """

        self._driveset = driveset

    @property
    def is_capacity_valid(self):
        """Gets the is_capacity_valid of this NimbleNsDiskSetAttr.  # noqa: E501

        Is the capacity fields in this data struct valid.  # noqa: E501

        :return: The is_capacity_valid of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: bool
        """
        return self._is_capacity_valid

    @is_capacity_valid.setter
    def is_capacity_valid(self, is_capacity_valid):
        """Sets the is_capacity_valid of this NimbleNsDiskSetAttr.

        Is the capacity fields in this data struct valid.  # noqa: E501

        :param is_capacity_valid: The is_capacity_valid of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: bool
        """

        self._is_capacity_valid = is_capacity_valid

    @property
    def is_flash_shelf(self):
        """Gets the is_flash_shelf of this NimbleNsDiskSetAttr.  # noqa: E501

        Is this a all-flash-shelf.  # noqa: E501

        :return: The is_flash_shelf of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: bool
        """
        return self._is_flash_shelf

    @is_flash_shelf.setter
    def is_flash_shelf(self, is_flash_shelf):
        """Sets the is_flash_shelf of this NimbleNsDiskSetAttr.

        Is this a all-flash-shelf.  # noqa: E501

        :param is_flash_shelf: The is_flash_shelf of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: bool
        """

        self._is_flash_shelf = is_flash_shelf

    @property
    def pause_state(self):
        """Gets the pause_state of this NimbleNsDiskSetAttr.  # noqa: E501

        State of evacuation, paused or in-progress; valid only when sw_state is evacuating, ie. evacuation is underway.  # noqa: E501

        :return: The pause_state of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: int
        """
        return self._pause_state

    @pause_state.setter
    def pause_state(self, pause_state):
        """Sets the pause_state of this NimbleNsDiskSetAttr.

        State of evacuation, paused or in-progress; valid only when sw_state is evacuating, ie. evacuation is underway.  # noqa: E501

        :param pause_state: The pause_state of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: int
        """

        self._pause_state = pause_state

    @property
    def pct_completion(self):
        """Gets the pct_completion of this NimbleNsDiskSetAttr.  # noqa: E501

        Evacuation percent completion; valid only when sw_state is evacuating, ie. evacuation is underway.  # noqa: E501

        :return: The pct_completion of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: int
        """
        return self._pct_completion

    @pct_completion.setter
    def pct_completion(self, pct_completion):
        """Sets the pct_completion of this NimbleNsDiskSetAttr.

        Evacuation percent completion; valid only when sw_state is evacuating, ie. evacuation is underway.  # noqa: E501

        :param pct_completion: The pct_completion of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: int
        """

        self._pct_completion = pct_completion

    @property
    def raw_cache_capacity(self):
        """Gets the raw_cache_capacity of this NimbleNsDiskSetAttr.  # noqa: E501

        Raw cache capacity for this shelf.  # noqa: E501

        :return: The raw_cache_capacity of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: int
        """
        return self._raw_cache_capacity

    @raw_cache_capacity.setter
    def raw_cache_capacity(self, raw_cache_capacity):
        """Sets the raw_cache_capacity of this NimbleNsDiskSetAttr.

        Raw cache capacity for this shelf.  # noqa: E501

        :param raw_cache_capacity: The raw_cache_capacity of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: int
        """

        self._raw_cache_capacity = raw_cache_capacity

    @property
    def raw_capacity(self):
        """Gets the raw_capacity of this NimbleNsDiskSetAttr.  # noqa: E501

        Hdd raw capacity for this shelf.  # noqa: E501

        :return: The raw_capacity of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: int
        """
        return self._raw_capacity

    @raw_capacity.setter
    def raw_capacity(self, raw_capacity):
        """Sets the raw_capacity of this NimbleNsDiskSetAttr.

        Hdd raw capacity for this shelf.  # noqa: E501

        :param raw_capacity: The raw_capacity of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: int
        """

        self._raw_capacity = raw_capacity

    @property
    def sw_state(self):
        """Gets the sw_state of this NimbleNsDiskSetAttr.  # noqa: E501

        Software state. Possible values:'available', 'online', 'foreign', 'unknown'.  # noqa: E501

        :return: The sw_state of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: str
        """
        return self._sw_state

    @sw_state.setter
    def sw_state(self, sw_state):
        """Sets the sw_state of this NimbleNsDiskSetAttr.

        Software state. Possible values:'available', 'online', 'foreign', 'unknown'.  # noqa: E501

        :param sw_state: The sw_state of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: str
        """

        self._sw_state = sw_state

    @property
    def usable_cache_capacity(self):
        """Gets the usable_cache_capacity of this NimbleNsDiskSetAttr.  # noqa: E501

        Estimated usable cache capacity for this shelf.  # noqa: E501

        :return: The usable_cache_capacity of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: int
        """
        return self._usable_cache_capacity

    @usable_cache_capacity.setter
    def usable_cache_capacity(self, usable_cache_capacity):
        """Sets the usable_cache_capacity of this NimbleNsDiskSetAttr.

        Estimated usable cache capacity for this shelf.  # noqa: E501

        :param usable_cache_capacity: The usable_cache_capacity of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: int
        """

        self._usable_cache_capacity = usable_cache_capacity

    @property
    def usable_capacity(self):
        """Gets the usable_capacity of this NimbleNsDiskSetAttr.  # noqa: E501

        Estimated usable capacity for this shelf.  # noqa: E501

        :return: The usable_capacity of this NimbleNsDiskSetAttr.  # noqa: E501
        :rtype: int
        """
        return self._usable_capacity

    @usable_capacity.setter
    def usable_capacity(self, usable_capacity):
        """Sets the usable_capacity of this NimbleNsDiskSetAttr.

        Estimated usable capacity for this shelf.  # noqa: E501

        :param usable_capacity: The usable_capacity of this NimbleNsDiskSetAttr.  # noqa: E501
        :type: int
        """

        self._usable_capacity = usable_capacity

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
        if not isinstance(other, NimbleNsDiskSetAttr):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
