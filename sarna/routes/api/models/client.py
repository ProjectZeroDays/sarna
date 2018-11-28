# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from sarna.routes.api.models.base_model_ import Model
from sarna.routes.api.models.user import User  # noqa: F401,E501
from sarna.routes.api import util


class Client(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, short_name: str=None, long_name: str=None, creator: User=None, managers: List[User]=None):  # noqa: E501
        """Client - a model defined in Swagger

        :param short_name: The short_name of this Client.  # noqa: E501
        :type short_name: str
        :param long_name: The long_name of this Client.  # noqa: E501
        :type long_name: str
        :param creator: The creator of this Client.  # noqa: E501
        :type creator: User
        :param managers: The managers of this Client.  # noqa: E501
        :type managers: List[User]
        """
        self.swagger_types = {
            'short_name': str,
            'long_name': str,
            'creator': User,
            'managers': List[User]
        }

        self.attribute_map = {
            'short_name': 'short_name',
            'long_name': 'long_name',
            'creator': 'creator',
            'managers': 'managers'
        }

        self._short_name = short_name
        self._long_name = long_name
        self._creator = creator
        self._managers = managers

    @classmethod
    def from_dict(cls, dikt) -> 'Client':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Client of this Client.  # noqa: E501
        :rtype: Client
        """
        return util.deserialize_model(dikt, cls)

    @property
    def short_name(self) -> str:
        """Gets the short_name of this Client.


        :return: The short_name of this Client.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name: str):
        """Sets the short_name of this Client.


        :param short_name: The short_name of this Client.
        :type short_name: str
        """
        if short_name is None:
            raise ValueError("Invalid value for `short_name`, must not be `None`")  # noqa: E501
        if short_name is not None and len(short_name) > 64:
            raise ValueError("Invalid value for `short_name`, length must be less than or equal to `64`")  # noqa: E501

        self._short_name = short_name

    @property
    def long_name(self) -> str:
        """Gets the long_name of this Client.


        :return: The long_name of this Client.
        :rtype: str
        """
        return self._long_name

    @long_name.setter
    def long_name(self, long_name: str):
        """Sets the long_name of this Client.


        :param long_name: The long_name of this Client.
        :type long_name: str
        """
        if long_name is None:
            raise ValueError("Invalid value for `long_name`, must not be `None`")  # noqa: E501
        if long_name is not None and len(long_name) > 128:
            raise ValueError("Invalid value for `long_name`, length must be less than or equal to `128`")  # noqa: E501

        self._long_name = long_name

    @property
    def creator(self) -> User:
        """Gets the creator of this Client.


        :return: The creator of this Client.
        :rtype: User
        """
        return self._creator

    @creator.setter
    def creator(self, creator: User):
        """Sets the creator of this Client.


        :param creator: The creator of this Client.
        :type creator: User
        """

        self._creator = creator

    @property
    def managers(self) -> List[User]:
        """Gets the managers of this Client.


        :return: The managers of this Client.
        :rtype: List[User]
        """
        return self._managers

    @managers.setter
    def managers(self, managers: List[User]):
        """Sets the managers of this Client.


        :param managers: The managers of this Client.
        :type managers: List[User]
        """

        self._managers = managers
