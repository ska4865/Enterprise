# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body1(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, account_id: float=None, funds: float=None):  # noqa: E501
        """Body1 - a model defined in Swagger

        :param account_id: The account_id of this Body1.  # noqa: E501
        :type account_id: float
        :param funds: The funds of this Body1.  # noqa: E501
        :type funds: float
        """
        self.swagger_types = {
            'account_id': float,
            'funds': float
        }

        self.attribute_map = {
            'account_id': 'AccountID',
            'funds': 'Funds'
        }
        self._account_id = account_id
        self._funds = funds

    @classmethod
    def from_dict(cls, dikt) -> 'Body1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_1 of this Body1.  # noqa: E501
        :rtype: Body1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_id(self) -> float:
        """Gets the account_id of this Body1.


        :return: The account_id of this Body1.
        :rtype: float
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: float):
        """Sets the account_id of this Body1.


        :param account_id: The account_id of this Body1.
        :type account_id: float
        """

        self._account_id = account_id

    @property
    def funds(self) -> float:
        """Gets the funds of this Body1.


        :return: The funds of this Body1.
        :rtype: float
        """
        return self._funds

    @funds.setter
    def funds(self, funds: float):
        """Sets the funds of this Body1.


        :param funds: The funds of this Body1.
        :type funds: float
        """

        self._funds = funds
