# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CompleteItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, item_name: str=None, price: float=None, warehouse_name: str=None, quantity: float=None, store_id: float=None, itemtype_id: float=None):  # noqa: E501
        """CompleteItem - a model defined in Swagger

        :param item_name: The item_name of this CompleteItem.  # noqa: E501
        :type item_name: str
        :param price: The price of this CompleteItem.  # noqa: E501
        :type price: float
        :param warehouse_name: The warehouse_name of this CompleteItem.  # noqa: E501
        :type warehouse_name: str
        :param quantity: The quantity of this CompleteItem.  # noqa: E501
        :type quantity: float
        :param store_id: The store_id of this CompleteItem.  # noqa: E501
        :type store_id: float
        :param itemtype_id: The itemtype_id of this CompleteItem.  # noqa: E501
        :type itemtype_id: float
        """
        self.swagger_types = {
            'item_name': str,
            'price': float,
            'warehouse_name': str,
            'quantity': float,
            'store_id': float,
            'itemtype_id': float
        }

        self.attribute_map = {
            'item_name': 'ItemName',
            'price': 'price',
            'warehouse_name': 'WarehouseName',
            'quantity': 'quantity',
            'store_id': 'storeID',
            'itemtype_id': 'itemtypeID'
        }
        self._item_name = item_name
        self._price = price
        self._warehouse_name = warehouse_name
        self._quantity = quantity
        self._store_id = store_id
        self._itemtype_id = itemtype_id

    @classmethod
    def from_dict(cls, dikt) -> 'CompleteItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CompleteItem of this CompleteItem.  # noqa: E501
        :rtype: CompleteItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def item_name(self) -> str:
        """Gets the item_name of this CompleteItem.


        :return: The item_name of this CompleteItem.
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name: str):
        """Sets the item_name of this CompleteItem.


        :param item_name: The item_name of this CompleteItem.
        :type item_name: str
        """

        self._item_name = item_name

    @property
    def price(self) -> float:
        """Gets the price of this CompleteItem.


        :return: The price of this CompleteItem.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price: float):
        """Sets the price of this CompleteItem.


        :param price: The price of this CompleteItem.
        :type price: float
        """

        self._price = price

    @property
    def warehouse_name(self) -> str:
        """Gets the warehouse_name of this CompleteItem.


        :return: The warehouse_name of this CompleteItem.
        :rtype: str
        """
        return self._warehouse_name

    @warehouse_name.setter
    def warehouse_name(self, warehouse_name: str):
        """Sets the warehouse_name of this CompleteItem.


        :param warehouse_name: The warehouse_name of this CompleteItem.
        :type warehouse_name: str
        """

        self._warehouse_name = warehouse_name

    @property
    def quantity(self) -> float:
        """Gets the quantity of this CompleteItem.


        :return: The quantity of this CompleteItem.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: float):
        """Sets the quantity of this CompleteItem.


        :param quantity: The quantity of this CompleteItem.
        :type quantity: float
        """

        self._quantity = quantity

    @property
    def store_id(self) -> float:
        """Gets the store_id of this CompleteItem.


        :return: The store_id of this CompleteItem.
        :rtype: float
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id: float):
        """Sets the store_id of this CompleteItem.


        :param store_id: The store_id of this CompleteItem.
        :type store_id: float
        """

        self._store_id = store_id

    @property
    def itemtype_id(self) -> float:
        """Gets the itemtype_id of this CompleteItem.


        :return: The itemtype_id of this CompleteItem.
        :rtype: float
        """
        return self._itemtype_id

    @itemtype_id.setter
    def itemtype_id(self, itemtype_id: float):
        """Sets the itemtype_id of this CompleteItem.


        :param itemtype_id: The itemtype_id of this CompleteItem.
        :type itemtype_id: float
        """

        self._itemtype_id = itemtype_id
