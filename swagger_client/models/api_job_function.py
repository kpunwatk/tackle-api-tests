# coding: utf-8

"""
    MTA 6.1 api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ApiJobFunction(object):
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
        'create_time': 'str',
        'create_user': 'str',
        'id': 'int',
        'name': 'str',
        'stakeholders': 'list[ApiRef]',
        'update_user': 'str'
    }

    attribute_map = {
        'create_time': 'createTime',
        'create_user': 'createUser',
        'id': 'id',
        'name': 'name',
        'stakeholders': 'stakeholders',
        'update_user': 'updateUser'
    }

    def __init__(self, create_time=None, create_user=None, id=None, name=None, stakeholders=None, update_user=None, _configuration=None):  # noqa: E501
        """ApiJobFunction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._create_user = None
        self._id = None
        self._name = None
        self._stakeholders = None
        self._update_user = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if id is not None:
            self.id = id
        self.name = name
        if stakeholders is not None:
            self.stakeholders = stakeholders
        if update_user is not None:
            self.update_user = update_user

    @property
    def create_time(self):
        """Gets the create_time of this ApiJobFunction.  # noqa: E501


        :return: The create_time of this ApiJobFunction.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiJobFunction.


        :param create_time: The create_time of this ApiJobFunction.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this ApiJobFunction.  # noqa: E501


        :return: The create_user of this ApiJobFunction.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ApiJobFunction.


        :param create_user: The create_user of this ApiJobFunction.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def id(self):
        """Gets the id of this ApiJobFunction.  # noqa: E501


        :return: The id of this ApiJobFunction.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiJobFunction.


        :param id: The id of this ApiJobFunction.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiJobFunction.  # noqa: E501


        :return: The name of this ApiJobFunction.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiJobFunction.


        :param name: The name of this ApiJobFunction.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def stakeholders(self):
        """Gets the stakeholders of this ApiJobFunction.  # noqa: E501


        :return: The stakeholders of this ApiJobFunction.  # noqa: E501
        :rtype: list[ApiRef]
        """
        return self._stakeholders

    @stakeholders.setter
    def stakeholders(self, stakeholders):
        """Sets the stakeholders of this ApiJobFunction.


        :param stakeholders: The stakeholders of this ApiJobFunction.  # noqa: E501
        :type: list[ApiRef]
        """

        self._stakeholders = stakeholders

    @property
    def update_user(self):
        """Gets the update_user of this ApiJobFunction.  # noqa: E501


        :return: The update_user of this ApiJobFunction.  # noqa: E501
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this ApiJobFunction.


        :param update_user: The update_user of this ApiJobFunction.  # noqa: E501
        :type: str
        """

        self._update_user = update_user

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
        if issubclass(ApiJobFunction, dict):
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
        if not isinstance(other, ApiJobFunction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiJobFunction):
            return True

        return self.to_dict() != other.to_dict()
