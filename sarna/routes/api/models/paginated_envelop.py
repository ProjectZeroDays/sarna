# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from sarna.routes.api.models.base_model_ import Model
from sarna.routes.api.models.error import Error  # noqa: F401,E501
from sarna.routes.api import util


class PaginatedEnvelop(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, total: int=None, page_size: int=None, page: int=None, error: Error=None, data: List[object]=None):  # noqa: E501
        """PaginatedEnvelop - a model defined in Swagger

        :param total: The total of this PaginatedEnvelop.  # noqa: E501
        :type total: int
        :param page_size: The page_size of this PaginatedEnvelop.  # noqa: E501
        :type page_size: int
        :param page: The page of this PaginatedEnvelop.  # noqa: E501
        :type page: int
        :param error: The error of this PaginatedEnvelop.  # noqa: E501
        :type error: Error
        :param data: The data of this PaginatedEnvelop.  # noqa: E501
        :type data: List[object]
        """
        self.swagger_types = {
            'total': int,
            'page_size': int,
            'page': int,
            'error': Error,
            'data': List[object]
        }

        self.attribute_map = {
            'total': 'total',
            'page_size': 'page_size',
            'page': 'page',
            'error': 'error',
            'data': 'data'
        }

        self._total = total
        self._page_size = page_size
        self._page = page
        self._error = error
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'PaginatedEnvelop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PaginatedEnvelop of this PaginatedEnvelop.  # noqa: E501
        :rtype: PaginatedEnvelop
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total(self) -> int:
        """Gets the total of this PaginatedEnvelop.

        Number of items  # noqa: E501

        :return: The total of this PaginatedEnvelop.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int):
        """Sets the total of this PaginatedEnvelop.

        Number of items  # noqa: E501

        :param total: The total of this PaginatedEnvelop.
        :type total: int
        """

        self._total = total

    @property
    def page_size(self) -> int:
        """Gets the page_size of this PaginatedEnvelop.

        number of items per page  # noqa: E501

        :return: The page_size of this PaginatedEnvelop.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: int):
        """Sets the page_size of this PaginatedEnvelop.

        number of items per page  # noqa: E501

        :param page_size: The page_size of this PaginatedEnvelop.
        :type page_size: int
        """

        self._page_size = page_size

    @property
    def page(self) -> int:
        """Gets the page of this PaginatedEnvelop.

        Current page number  # noqa: E501

        :return: The page of this PaginatedEnvelop.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page: int):
        """Sets the page of this PaginatedEnvelop.

        Current page number  # noqa: E501

        :param page: The page of this PaginatedEnvelop.
        :type page: int
        """

        self._page = page

    @property
    def error(self) -> Error:
        """Gets the error of this PaginatedEnvelop.


        :return: The error of this PaginatedEnvelop.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error: Error):
        """Sets the error of this PaginatedEnvelop.


        :param error: The error of this PaginatedEnvelop.
        :type error: Error
        """

        self._error = error

    @property
    def data(self) -> List[object]:
        """Gets the data of this PaginatedEnvelop.


        :return: The data of this PaginatedEnvelop.
        :rtype: List[object]
        """
        return self._data

    @data.setter
    def data(self, data: List[object]):
        """Sets the data of this PaginatedEnvelop.


        :param data: The data of this PaginatedEnvelop.
        :type data: List[object]
        """

        self._data = data
