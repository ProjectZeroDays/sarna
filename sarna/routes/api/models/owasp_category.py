# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from sarna.routes.api.models.base_model_ import Model
from sarna.routes.api import util


class OWASPCategory(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _001 = "OTG-INFO-001"

    def __init__(self):  # noqa: E501
        """OWASPCategory - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'OWASPCategory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OWASPCategory of this OWASPCategory.  # noqa: E501
        :rtype: OWASPCategory
        """
        return util.deserialize_model(dikt, cls)
