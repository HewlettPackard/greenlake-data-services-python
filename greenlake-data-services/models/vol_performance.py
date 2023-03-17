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


class VolPerformance(object):
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
        'iops': 'NimbleKpiMetrics',
        'latency': 'NimbleKpiMetrics',
        'request_uri': 'str',
        'resource_uri': 'str',
        'throughput': 'NimbleKpiMetrics'
    }

    attribute_map = {
        'iops': 'iops',
        'latency': 'latency',
        'request_uri': 'requestURI',
        'resource_uri': 'resourceUri',
        'throughput': 'throughput'
    }

    def __init__(self, iops=None, latency=None, request_uri=None, resource_uri=None, throughput=None):  # noqa: E501
        """VolPerformance - a model defined in OpenAPI"""  # noqa: E501

        self._iops = None
        self._latency = None
        self._request_uri = None
        self._resource_uri = None
        self._throughput = None
        self.discriminator = None

        if iops is not None:
            self.iops = iops
        if latency is not None:
            self.latency = latency
        if request_uri is not None:
            self.request_uri = request_uri
        if resource_uri is not None:
            self.resource_uri = resource_uri
        if throughput is not None:
            self.throughput = throughput

    @property
    def iops(self):
        """Gets the iops of this VolPerformance.  # noqa: E501


        :return: The iops of this VolPerformance.  # noqa: E501
        :rtype: NimbleKpiMetrics
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this VolPerformance.


        :param iops: The iops of this VolPerformance.  # noqa: E501
        :type: NimbleKpiMetrics
        """

        self._iops = iops

    @property
    def latency(self):
        """Gets the latency of this VolPerformance.  # noqa: E501


        :return: The latency of this VolPerformance.  # noqa: E501
        :rtype: NimbleKpiMetrics
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this VolPerformance.


        :param latency: The latency of this VolPerformance.  # noqa: E501
        :type: NimbleKpiMetrics
        """

        self._latency = latency

    @property
    def request_uri(self):
        """Gets the request_uri of this VolPerformance.  # noqa: E501

        requestUri for detailed volume object  # noqa: E501

        :return: The request_uri of this VolPerformance.  # noqa: E501
        :rtype: str
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri):
        """Sets the request_uri of this VolPerformance.

        requestUri for detailed volume object  # noqa: E501

        :param request_uri: The request_uri of this VolPerformance.  # noqa: E501
        :type: str
        """

        self._request_uri = request_uri

    @property
    def resource_uri(self):
        """Gets the resource_uri of this VolPerformance.  # noqa: E501

        resourceUri for detailed volume object  # noqa: E501

        :return: The resource_uri of this VolPerformance.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this VolPerformance.

        resourceUri for detailed volume object  # noqa: E501

        :param resource_uri: The resource_uri of this VolPerformance.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

    @property
    def throughput(self):
        """Gets the throughput of this VolPerformance.  # noqa: E501


        :return: The throughput of this VolPerformance.  # noqa: E501
        :rtype: NimbleKpiMetrics
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """Sets the throughput of this VolPerformance.


        :param throughput: The throughput of this VolPerformance.  # noqa: E501
        :type: NimbleKpiMetrics
        """

        self._throughput = throughput

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
        if not isinstance(other, VolPerformance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
