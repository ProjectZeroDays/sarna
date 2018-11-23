# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from sarna.routes.api.models.base_model_ import Model
from sarna.routes.api import util


class OWASPMobileTop10Category(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    M1 = "M1"

    def __init__(self):  # noqa: E501
        """OWASPMobileTop10Category - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'OWASPMobileTop10Category':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OWASPMobileTop10Category of this OWASPMobileTop10Category.  # noqa: E501
        :rtype: OWASPMobileTop10Category
        """
        return util.deserialize_model(dikt, cls)
