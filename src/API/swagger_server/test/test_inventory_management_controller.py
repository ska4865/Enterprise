# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.complete_item import CompleteItem  # noqa: E501
from swagger_server.models.id import Id  # noqa: E501
from swagger_server.models.item import Item  # noqa: E501
from swagger_server.models.item_id import ItemID  # noqa: E501
from swagger_server.models.item_sell_body import ItemSellBody  # noqa: E501
from swagger_server.models.item_stock_body import ItemStockBody  # noqa: E501
from swagger_server.models.item_type import ItemType  # noqa: E501
from swagger_server.models.item_type_id import ItemTypeID  # noqa: E501
from swagger_server.models.store import Store  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInventoryManagementController(BaseTestCase):
    """InventoryManagementController integration test stubs"""

    def test_api_inventory_itemtype_get(self):
        """Test case for api_inventory_itemtype_get

        Returns an itemtype specified by ID
        """
        query_string = [('id', Id())]
        response = self.client.open(
            '/inventory/itemtype',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_inventory_itemtype_post(self):
        """Test case for api_inventory_itemtype_post

        adds a new itemtype as specified
        """
        body = ItemType()
        response = self.client.open(
            '/inventory/itemtype',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_inventory_store_delete(self):
        """Test case for api_inventory_store_delete

        deletes a store
        """
        query_string = [('id', Id())]
        response = self.client.open(
            '/inventory/store',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_inventory_store_post(self):
        """Test case for api_inventory_store_post

        adds a new store as specified
        """
        body = Store()
        response = self.client.open(
            '/inventory/store',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_item_delete(self):
        """Test case for api_item_delete

        deletes an item
        """
        query_string = [('id', Id())]
        response = self.client.open(
            '/inventory/item',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_item_get(self):
        """Test case for api_item_get

        Returns an item specified by ID
        """
        query_string = [('id', Id())]
        response = self.client.open(
            '/inventory/item',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_item_post(self):
        """Test case for api_item_post

        adds a new item as specified
        """
        body = Item()
        response = self.client.open(
            '/inventory/item',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_item_put(self):
        """Test case for api_item_put

        updates an item
        """
        body = ItemID()
        response = self.client.open(
            '/inventory/item',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_item_sell(self):
        """Test case for api_item_sell

        sell an item from inventory stock
        """
        body = ItemSellBody()
        response = self.client.open(
            '/inventory/item/sell',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_item_stock(self):
        """Test case for api_item_stock

        stocks an item in inventory
        """
        body = ItemStockBody()
        response = self.client.open(
            '/inventory/item/stock',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_itemtype_delete(self):
        """Test case for api_itemtype_delete

        deletes a itemtype
        """
        query_string = [('id', Id())]
        response = self.client.open(
            '/inventory/itemtype',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_itemtype_put(self):
        """Test case for api_itemtype_put

        updates an itemtype
        """
        body = ItemTypeID()
        response = self.client.open(
            '/inventory/itemtype',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_list_item_get(self):
        """Test case for api_list_item_get

        lists all items
        """
        response = self.client.open(
            '/inventory/item/list',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_list_itemtype_get(self):
        """Test case for api_list_itemtype_get

        lists all itemtypes
        """
        response = self.client.open(
            '/inventory/itemtype/list',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_list_store_get(self):
        """Test case for api_list_store_get

        lists all stores
        """
        response = self.client.open(
            '/inventory/store/list',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_store_get(self):
        """Test case for api_store_get

        Returns a store specified by ID
        """
        query_string = [('id', Id())]
        response = self.client.open(
            '/inventory/store',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
