# coding: utf-8

"""
    tackle2.0 api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ApiTTL(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created': 'int',
        'failed': 'int',
        'pending': 'int',
        'postponed': 'int',
        'running': 'int',
        'succeeded': 'int'
    }

    attribute_map = {
        'created': 'created',
        'failed': 'failed',
        'pending': 'pending',
        'postponed': 'postponed',
        'running': 'running',
        'succeeded': 'succeeded'
    }

    def __init__(self, created=None, failed=None, pending=None, postponed=None, running=None, succeeded=None, _configuration=None):  # noqa: E501
        """ApiTTL - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._failed = None
        self._pending = None
        self._postponed = None
        self._running = None
        self._succeeded = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if failed is not None:
            self.failed = failed
        if pending is not None:
            self.pending = pending
        if postponed is not None:
            self.postponed = postponed
        if running is not None:
            self.running = running
        if succeeded is not None:
            self.succeeded = succeeded

    @property
    def created(self):
        """Gets the created of this ApiTTL.  # noqa: E501


        :return: The created of this ApiTTL.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ApiTTL.


        :param created: The created of this ApiTTL.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def failed(self):
        """Gets the failed of this ApiTTL.  # noqa: E501


        :return: The failed of this ApiTTL.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this ApiTTL.


        :param failed: The failed of this ApiTTL.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def pending(self):
        """Gets the pending of this ApiTTL.  # noqa: E501


        :return: The pending of this ApiTTL.  # noqa: E501
        :rtype: int
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this ApiTTL.


        :param pending: The pending of this ApiTTL.  # noqa: E501
        :type: int
        """

        self._pending = pending

    @property
    def postponed(self):
        """Gets the postponed of this ApiTTL.  # noqa: E501


        :return: The postponed of this ApiTTL.  # noqa: E501
        :rtype: int
        """
        return self._postponed

    @postponed.setter
    def postponed(self, postponed):
        """Sets the postponed of this ApiTTL.


        :param postponed: The postponed of this ApiTTL.  # noqa: E501
        :type: int
        """

        self._postponed = postponed

    @property
    def running(self):
        """Gets the running of this ApiTTL.  # noqa: E501


        :return: The running of this ApiTTL.  # noqa: E501
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this ApiTTL.


        :param running: The running of this ApiTTL.  # noqa: E501
        :type: int
        """

        self._running = running

    @property
    def succeeded(self):
        """Gets the succeeded of this ApiTTL.  # noqa: E501


        :return: The succeeded of this ApiTTL.  # noqa: E501
        :rtype: int
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this ApiTTL.


        :param succeeded: The succeeded of this ApiTTL.  # noqa: E501
        :type: int
        """

        self._succeeded = succeeded

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ApiTTL, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiTTL):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiTTL):
            return True

        return self.to_dict() != other.to_dict()