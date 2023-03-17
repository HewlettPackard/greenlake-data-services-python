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


class NimbleHandoverVolumeCollectionsInput(object):
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
        'invoke_on_upstream_partner': 'bool',
        'no_reverse': 'bool',
        'override_upstream_down': 'bool',
        'replication_partner_id': 'str'
    }

    attribute_map = {
        'invoke_on_upstream_partner': 'invoke_on_upstream_partner',
        'no_reverse': 'no_reverse',
        'override_upstream_down': 'override_upstream_down',
        'replication_partner_id': 'replication_partner_id'
    }

    def __init__(self, invoke_on_upstream_partner=None, no_reverse=None, override_upstream_down=None, replication_partner_id=None):  # noqa: E501
        """NimbleHandoverVolumeCollectionsInput - a model defined in OpenAPI"""  # noqa: E501

        self._invoke_on_upstream_partner = None
        self._no_reverse = None
        self._override_upstream_down = None
        self._replication_partner_id = None
        self.discriminator = None

        if invoke_on_upstream_partner is not None:
            self.invoke_on_upstream_partner = invoke_on_upstream_partner
        if no_reverse is not None:
            self.no_reverse = no_reverse
        if override_upstream_down is not None:
            self.override_upstream_down = override_upstream_down
        self.replication_partner_id = replication_partner_id

    @property
    def invoke_on_upstream_partner(self):
        """Gets the invoke_on_upstream_partner of this NimbleHandoverVolumeCollectionsInput.  # noqa: E501

        Invoke handover request on upstream partner. Default: 'false'. This operation is not supported for synchronous replication volume vollections. Possible values: 'true', 'false'.  # noqa: E501

        :return: The invoke_on_upstream_partner of this NimbleHandoverVolumeCollectionsInput.  # noqa: E501
        :rtype: bool
        """
        return self._invoke_on_upstream_partner

    @invoke_on_upstream_partner.setter
    def invoke_on_upstream_partner(self, invoke_on_upstream_partner):
        """Sets the invoke_on_upstream_partner of this NimbleHandoverVolumeCollectionsInput.

        Invoke handover request on upstream partner. Default: 'false'. This operation is not supported for synchronous replication volume vollections. Possible values: 'true', 'false'.  # noqa: E501

        :param invoke_on_upstream_partner: The invoke_on_upstream_partner of this NimbleHandoverVolumeCollectionsInput.  # noqa: E501
        :type: bool
        """

        self._invoke_on_upstream_partner = invoke_on_upstream_partner

    @property
    def no_reverse(self):
        """Gets the no_reverse of this NimbleHandoverVolumeCollectionsInput.  # noqa: E501

        Do not automatically reverse direction of replication. Using this argument will prevent the new owner from automatically replicating the volume collection to this node when the handover completes. The default behavior is to enable replication back to this node. Default: 'false'. Possible values: 'true', 'false'.  # noqa: E501

        :return: The no_reverse of this NimbleHandoverVolumeCollectionsInput.  # noqa: E501
        :rtype: bool
        """
        return self._no_reverse

    @no_reverse.setter
    def no_reverse(self, no_reverse):
        """Sets the no_reverse of this NimbleHandoverVolumeCollectionsInput.

        Do not automatically reverse direction of replication. Using this argument will prevent the new owner from automatically replicating the volume collection to this node when the handover completes. The default behavior is to enable replication back to this node. Default: 'false'. Possible values: 'true', 'false'.  # noqa: E501

        :param no_reverse: The no_reverse of this NimbleHandoverVolumeCollectionsInput.  # noqa: E501
        :type: bool
        """

        self._no_reverse = no_reverse

    @property
    def override_upstream_down(self):
        """Gets the override_upstream_down of this NimbleHandoverVolumeCollectionsInput.  # noqa: E501

        Allow the handover request to proceed even if upstream array is down. The default behavior is to return an error when upstream is down. This option is applicable for synchronous replication only. Default: 'false'. Possible values: 'true', 'false'.  # noqa: E501

        :return: The override_upstream_down of this NimbleHandoverVolumeCollectionsInput.  # noqa: E501
        :rtype: bool
        """
        return self._override_upstream_down

    @override_upstream_down.setter
    def override_upstream_down(self, override_upstream_down):
        """Sets the override_upstream_down of this NimbleHandoverVolumeCollectionsInput.

        Allow the handover request to proceed even if upstream array is down. The default behavior is to return an error when upstream is down. This option is applicable for synchronous replication only. Default: 'false'. Possible values: 'true', 'false'.  # noqa: E501

        :param override_upstream_down: The override_upstream_down of this NimbleHandoverVolumeCollectionsInput.  # noqa: E501
        :type: bool
        """

        self._override_upstream_down = override_upstream_down

    @property
    def replication_partner_id(self):
        """Gets the replication_partner_id of this NimbleHandoverVolumeCollectionsInput.  # noqa: E501

        Replication partner ID of the new owner. A 42 digit hexadecimal number.  # noqa: E501

        :return: The replication_partner_id of this NimbleHandoverVolumeCollectionsInput.  # noqa: E501
        :rtype: str
        """
        return self._replication_partner_id

    @replication_partner_id.setter
    def replication_partner_id(self, replication_partner_id):
        """Sets the replication_partner_id of this NimbleHandoverVolumeCollectionsInput.

        Replication partner ID of the new owner. A 42 digit hexadecimal number.  # noqa: E501

        :param replication_partner_id: The replication_partner_id of this NimbleHandoverVolumeCollectionsInput.  # noqa: E501
        :type: str
        """
        if replication_partner_id is None:
            raise ValueError("Invalid value for `replication_partner_id`, must not be `None`")  # noqa: E501

        self._replication_partner_id = replication_partner_id

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
        if not isinstance(other, NimbleHandoverVolumeCollectionsInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other