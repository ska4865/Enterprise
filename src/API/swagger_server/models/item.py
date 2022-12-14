# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Item(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, quantity: float=None, store_id: float=None, itemtype_id: float=None):  # noqa: E501
        """Item - a model defined in Swagger

        :param quantity: The quantity of this Item.  # noqa: E501
        :type quantity: float
        :param store_id: The store_id of this Item.  # noqa: E501
        :type store_id: float
        :param itemtype_id: The itemtype_id of this Item.  # noqa: E501
        :type itemtype_id: float
        """
        self.swagger_types = {
            'quantity': float,
            'store_id': float,
            'itemtype_id': float
        }

        self.attribute_map = {
            'quantity': 'quantity',
            'store_id': 'storeID',
            'itemtype_id': 'itemtypeID'
        }
        self._quantity = quantity
        self._store_id = store_id
        self._itemtype_id = itemtype_id

    @classmethod
    def from_dict(cls, dikt) -> 'Item':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Item of this Item.  # noqa: E501
        :rtype: Item
        """
        return util.deserialize_model(dikt, cls)

    @property
    def quantity(self) -> float:
        """Gets the quantity of this Item.


        :return: The quantity of this Item.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: float):
        """Sets the quantity of this Item.


        :param quantity: The quantity of this Item.
        :type quantity: float
        """

        self._quantity = quantity

    @property
    def store_id(self) -> float:
        """Gets the store_id of this Item.


        :return: The store_id of this Item.
        :rtype: float
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id: float):
        """Sets the store_id of this Item.


        :param store_id: The store_id of this Item.
        :type store_id: float
        """

        self._store_id = store_id

    @property
    def itemtype_id(self) -> float:
        """Gets the itemtype_id of this Item.


        :return: The itemtype_id of this Item.
        :rtype: float
        """
        return self._itemtype_id

    @itemtype_id.setter
    def itemtype_id(self, itemtype_id: float):
        """Sets the itemtype_id of this Item.


        :param itemtype_id: The itemtype_id of this Item.
        :type itemtype_id: float
        """

        self._itemtype_id = itemtype_id
