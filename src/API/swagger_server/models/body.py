# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, address: str=None, funds: float=None):  # noqa: E501
        """Body - a model defined in Swagger

        :param address: The address of this Body.  # noqa: E501
        :type address: str
        :param funds: The funds of this Body.  # noqa: E501
        :type funds: float
        """
        self.swagger_types = {
            'address': str,
            'funds': float
        }

        self.attribute_map = {
            'address': 'Address',
            'funds': 'Funds'
        }
        self._address = address
        self._funds = funds

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.  # noqa: E501
        :rtype: Body
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self) -> str:
        """Gets the address of this Body.


        :return: The address of this Body.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this Body.


        :param address: The address of this Body.
        :type address: str
        """

        self._address = address

    @property
    def funds(self) -> float:
        """Gets the funds of this Body.


        :return: The funds of this Body.
        :rtype: float
        """
        return self._funds

    @funds.setter
    def funds(self, funds: float):
        """Sets the funds of this Body.


        :param funds: The funds of this Body.
        :type funds: float
        """

        self._funds = funds