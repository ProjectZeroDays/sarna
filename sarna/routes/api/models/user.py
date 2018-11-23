# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from sarna.routes.api.models.base_model_ import Model
from sarna.routes.api.models.user_name import UserName  # noqa: F401,E501
from sarna.routes.api.models.user_type import UserType  # noqa: F401,E501
from sarna.routes.api import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, username: UserName=None, user_type: UserType=None):  # noqa: E501
        """User - a model defined in Swagger

        :param username: The username of this User.  # noqa: E501
        :type username: UserName
        :param user_type: The user_type of this User.  # noqa: E501
        :type user_type: UserType
        """
        self.swagger_types = {
            'username': UserName,
            'user_type': UserType
        }

        self.attribute_map = {
            'username': 'username',
            'user_type': 'user_type'
        }

        self._username = username
        self._user_type = user_type

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> UserName:
        """Gets the username of this User.


        :return: The username of this User.
        :rtype: UserName
        """
        return self._username

    @username.setter
    def username(self, username: UserName):
        """Sets the username of this User.


        :param username: The username of this User.
        :type username: UserName
        """

        self._username = username

    @property
    def user_type(self) -> UserType:
        """Gets the user_type of this User.


        :return: The user_type of this User.
        :rtype: UserType
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type: UserType):
        """Sets the user_type of this User.


        :param user_type: The user_type of this User.
        :type user_type: UserType
        """

        self._user_type = user_type
