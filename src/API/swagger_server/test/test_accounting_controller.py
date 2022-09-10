# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.account import Account  # noqa: E501
from swagger_server.models.account_id import AccountID  # noqa: E501
from swagger_server.models.fund import Fund  # noqa: E501
from swagger_server.models.id import Id  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAccountingController(BaseTestCase):
    """AccountingController integration test stubs"""

    def test_api_account_delete(self):
        """Test case for api_account_delete

        deletes an Account
        """
        query_string = [('id', Id())]
        response = self.client.open(
            '/accounting/account',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_account_fund(self):
        """Test case for api_account_fund

        fund an Account
        """
        query_string = [('body', Fund())]
        response = self.client.open(
            '/accounting/account/fund',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_account_post(self):
        """Test case for api_account_post

        adds a new Account as specified
        """
        query_string = [('body', Account())]
        response = self.client.open(
            '/accounting/account',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_account_put(self):
        """Test case for api_account_put

        updates an Account
        """
        query_string = [('body', AccountID())]
        response = self.client.open(
            '/accounting/account',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_account_salary(self):
        """Test case for api_account_salary

        Pays out a salary to an employee
        """
        query_string = [('body', Transaction())]
        response = self.client.open(
            '/accounting/salary',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_account_withdraw_post(self):
        """Test case for api_account_withdraw_post

        withdraw from an Account
        """
        query_string = [('body', Object())]
        response = self.client.open(
            '/accounting/account/withdraw',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_accountingaccount_get(self):
        """Test case for api_accountingaccount_get

        get a particular account
        """
        query_string = [('id', Id())]
        response = self.client.open(
            '/accounting/account',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_list_account_get(self):
        """Test case for api_list_account_get

        list all accounts
        """
        response = self.client.open(
            '/accounting/account/list',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_list_transaction_get(self):
        """Test case for api_list_transaction_get

        get a particular transaction
        """
        response = self.client.open(
            '/accounting/transaction/list',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_transaction_get(self):
        """Test case for api_transaction_get

        get a particular transaction
        """
        query_string = [('id', Id())]
        response = self.client.open(
            '/accounting/transaction',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
