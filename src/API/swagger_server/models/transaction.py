# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Transaction(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, accountid: float=None, amount: float=None):  # noqa: E501
        """Transaction - a model defined in Swagger

        :param accountid: The accountid of this Transaction.  # noqa: E501
        :type accountid: float
        :param amount: The amount of this Transaction.  # noqa: E501
        :type amount: float
        """
        self.swagger_types = {
            'accountid': float,
            'amount': float
        }

        self.attribute_map = {
            'accountid': 'accountid',
            'amount': 'amount'
        }
        self._accountid = accountid
        self._amount = amount

    @classmethod
    def from_dict(cls, dikt) -> 'Transaction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Transaction of this Transaction.  # noqa: E501
        :rtype: Transaction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accountid(self) -> float:
        """Gets the accountid of this Transaction.


        :return: The accountid of this Transaction.
        :rtype: float
        """
        return self._accountid

    @accountid.setter
    def accountid(self, accountid: float):
        """Sets the accountid of this Transaction.


        :param accountid: The accountid of this Transaction.
        :type accountid: float
        """

        self._accountid = accountid

    @property
    def amount(self) -> float:
        """Gets the amount of this Transaction.


        :return: The amount of this Transaction.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this Transaction.


        :param amount: The amount of this Transaction.
        :type amount: float
        """

        self._amount = amount
