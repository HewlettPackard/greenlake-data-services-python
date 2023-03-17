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


class EditThrottle(object):
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
        'days': 'str',
        'description': 'str',
        'thr_at_time': 'int',
        'thr_bandwidth': 'int',
        'thr_bandwidth_kbps': 'int',
        'thr_bandwidth_limit_kbps': 'int',
        'thr_until_time': 'int'
    }

    attribute_map = {
        'days': 'days',
        'description': 'description',
        'thr_at_time': 'thr_at_time',
        'thr_bandwidth': 'thr_bandwidth',
        'thr_bandwidth_kbps': 'thr_bandwidth_kbps',
        'thr_bandwidth_limit_kbps': 'thr_bandwidth_limit_kbps',
        'thr_until_time': 'thr_until_time'
    }

    def __init__(self, days=None, description=None, thr_at_time=None, thr_bandwidth=None, thr_bandwidth_kbps=None, thr_bandwidth_limit_kbps=None, thr_until_time=None):  # noqa: E501
        """EditThrottle - a model defined in OpenAPI"""  # noqa: E501

        self._days = None
        self._description = None
        self._thr_at_time = None
        self._thr_bandwidth = None
        self._thr_bandwidth_kbps = None
        self._thr_bandwidth_limit_kbps = None
        self._thr_until_time = None
        self.discriminator = None

        if days is not None:
            self.days = days
        if description is not None:
            self.description = description
        if thr_at_time is not None:
            self.thr_at_time = thr_at_time
        if thr_bandwidth is not None:
            self.thr_bandwidth = thr_bandwidth
        if thr_bandwidth_kbps is not None:
            self.thr_bandwidth_kbps = thr_bandwidth_kbps
        if thr_bandwidth_limit_kbps is not None:
            self.thr_bandwidth_limit_kbps = thr_bandwidth_limit_kbps
        if thr_until_time is not None:
            self.thr_until_time = thr_until_time

    @property
    def days(self):
        """Gets the days of this EditThrottle.  # noqa: E501

        Comma separated list of days of the week or 'all'.  # noqa: E501

        :return: The days of this EditThrottle.  # noqa: E501
        :rtype: str
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this EditThrottle.

        Comma separated list of days of the week or 'all'.  # noqa: E501

        :param days: The days of this EditThrottle.  # noqa: E501
        :type: str
        """

        self._days = days

    @property
    def description(self):
        """Gets the description of this EditThrottle.  # noqa: E501

        Description of the throttle.  # noqa: E501

        :return: The description of this EditThrottle.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EditThrottle.

        Description of the throttle.  # noqa: E501

        :param description: The description of this EditThrottle.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def thr_at_time(self):
        """Gets the thr_at_time of this EditThrottle.  # noqa: E501

        Start time for the throttle.  # noqa: E501

        :return: The thr_at_time of this EditThrottle.  # noqa: E501
        :rtype: int
        """
        return self._thr_at_time

    @thr_at_time.setter
    def thr_at_time(self, thr_at_time):
        """Sets the thr_at_time of this EditThrottle.

        Start time for the throttle.  # noqa: E501

        :param thr_at_time: The thr_at_time of this EditThrottle.  # noqa: E501
        :type: int
        """

        self._thr_at_time = thr_at_time

    @property
    def thr_bandwidth(self):
        """Gets the thr_bandwidth of this EditThrottle.  # noqa: E501

        Bandwidth for the throttle in megabits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This attribute is superseded by thr_bandwidth_limit_kbps. Use either thr_bandwidth or thr_bandwidth_kbps to set throttle bandwidth.  # noqa: E501

        :return: The thr_bandwidth of this EditThrottle.  # noqa: E501
        :rtype: int
        """
        return self._thr_bandwidth

    @thr_bandwidth.setter
    def thr_bandwidth(self, thr_bandwidth):
        """Sets the thr_bandwidth of this EditThrottle.

        Bandwidth for the throttle in megabits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This attribute is superseded by thr_bandwidth_limit_kbps. Use either thr_bandwidth or thr_bandwidth_kbps to set throttle bandwidth.  # noqa: E501

        :param thr_bandwidth: The thr_bandwidth of this EditThrottle.  # noqa: E501
        :type: int
        """

        self._thr_bandwidth = thr_bandwidth

    @property
    def thr_bandwidth_kbps(self):
        """Gets the thr_bandwidth_kbps of this EditThrottle.  # noqa: E501

        Bandwidth for the throttle in kilobits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This atttibute is superseded by thr_bandwidth_limit_kbps. Use either thr_bandwidth or thr_bandwidth_kbps to set throttle bandwidth.  # noqa: E501

        :return: The thr_bandwidth_kbps of this EditThrottle.  # noqa: E501
        :rtype: int
        """
        return self._thr_bandwidth_kbps

    @thr_bandwidth_kbps.setter
    def thr_bandwidth_kbps(self, thr_bandwidth_kbps):
        """Sets the thr_bandwidth_kbps of this EditThrottle.

        Bandwidth for the throttle in kilobits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This atttibute is superseded by thr_bandwidth_limit_kbps. Use either thr_bandwidth or thr_bandwidth_kbps to set throttle bandwidth.  # noqa: E501

        :param thr_bandwidth_kbps: The thr_bandwidth_kbps of this EditThrottle.  # noqa: E501
        :type: int
        """

        self._thr_bandwidth_kbps = thr_bandwidth_kbps

    @property
    def thr_bandwidth_limit_kbps(self):
        """Gets the thr_bandwidth_limit_kbps of this EditThrottle.  # noqa: E501

        Bandwidth for the throttle in kilobits per second or -1 to indicate that there is no limit.  # noqa: E501

        :return: The thr_bandwidth_limit_kbps of this EditThrottle.  # noqa: E501
        :rtype: int
        """
        return self._thr_bandwidth_limit_kbps

    @thr_bandwidth_limit_kbps.setter
    def thr_bandwidth_limit_kbps(self, thr_bandwidth_limit_kbps):
        """Sets the thr_bandwidth_limit_kbps of this EditThrottle.

        Bandwidth for the throttle in kilobits per second or -1 to indicate that there is no limit.  # noqa: E501

        :param thr_bandwidth_limit_kbps: The thr_bandwidth_limit_kbps of this EditThrottle.  # noqa: E501
        :type: int
        """

        self._thr_bandwidth_limit_kbps = thr_bandwidth_limit_kbps

    @property
    def thr_until_time(self):
        """Gets the thr_until_time of this EditThrottle.  # noqa: E501

        End time for the throttle.  # noqa: E501

        :return: The thr_until_time of this EditThrottle.  # noqa: E501
        :rtype: int
        """
        return self._thr_until_time

    @thr_until_time.setter
    def thr_until_time(self, thr_until_time):
        """Sets the thr_until_time of this EditThrottle.

        End time for the throttle.  # noqa: E501

        :param thr_until_time: The thr_until_time of this EditThrottle.  # noqa: E501
        :type: int
        """

        self._thr_until_time = thr_until_time

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
        if not isinstance(other, EditThrottle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
