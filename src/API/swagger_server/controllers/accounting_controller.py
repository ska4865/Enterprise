import connexion
import six

import psycopg
import yaml
from swagger_server.models.account import Account  # noqa: E501
from swagger_server.models.account_id import AccountID  # noqa: E501
from swagger_server.models.fund import Fund  # noqa: E501
from swagger_server.models.id import Id  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server import util

conn_string = ""
with open('/docker-compose.yaml', 'r') as sql_setings:
    server_settings = yaml.unsafe_load(sql_setings)["services"]["db"]
    settings = {}
    for kv in server_settings["environment"]:
        splitkv = kv.split('=')
        settings[splitkv[0]] = splitkv[1]
    settings['PORT'] = server_settings["ports"][0].split(':')[0]
    
    conn_string = f"host=db port={settings['PORT']} user={settings['POSTGRES_USER']} password={settings['POSTGRES_PASSWORD']}"

def api_account_delete(id=None):  # noqa: E501
    """deletes an Account

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: Account
    """
    if connexion.request.is_json:
        id = Id.from_dict(connexion.request.get_json())  # noqa: E501
        """with psycopg.connect(conn_string) as conn:
            with conn.cursor() as cur:
            cur.execute("DELETE * FROM accounting.accounts WHERE id = %s", (id,))"""
    return 'deleted'


def api_account_fund(body=None):  # noqa: E501
    """fund an Account

     # noqa: E501

    :param body: JSON document
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())  # noqa: E501
        """with psycopg.connect(conn_string) as conn:
                with conn.cursor() as cur:
                    cur.execute("UPDATE accounting.account SET NAME=%s, BUDGET=%s WHERE Id=%s",
                    (body.name, body.budget, body.id))
                    id = cur.fetchone()"""
    return 'quantity'


def api_account_post(body=None):  # noqa: E501
    """adds a new Account as specified

     # noqa: E501

    :param body: JSON document
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Account.from_dict(connexion.request.get_json())  # noqa: E501
    """with psycopg.connect(conn_string) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO inventory.items (NAME, QUANTITY, PRICE) VALUES (%s, %s, %s) RETURNING id",
            (body.name, body.quantity, body.price))
            id = cur.fetchone()"""
    return 'account'


def api_account_put(body=None):  # noqa: E501
    """updates an Account

     # noqa: E501

    :param body: JSON document
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AccountID.from_dict(connexion.request.get_json())  # noqa: E501
        """with psycopg.connect(conn_string) as conn:
                with conn.cursor() as cur:
                    cur.execute("UPDATE accounting.account SET NAME=%s, BUDGET=%s WHERE Id=%s",
                    (body.name, body.budget, body.id))
                    id = cur.fetchone()"""
    return 'account'


def api_account_salary(body=None):  # noqa: E501
    """Pays out a salary to an employee

     # noqa: E501

    :param body: JSON document
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Transaction.from_dict(connexion.request.get_json())  # noqa: E501
        """with psycopg.connect(conn_string) as conn:
                with conn.cursor() as cur:
                    cur.execute("UPDATE accounting.account SET NAME=%s, BUDGET=%s WHERE Id=%s",
                    (body.name, body.budget, body.id))
                    id = cur.fetchone()"""
    return 'Pay day!'


def api_account_withdraw_post(body=None):  # noqa: E501
    """withdraw from an Account

     # noqa: E501

    :param body: JSON document
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    
        """with psycopg.connect(conn_string) as conn:
                with conn.cursor() as cur:
                    cur.execute("UPDATE accounting.account SET NAME=%s, BUDGET=%s WHERE Id=%s",
                    (body.name, body.budget, body.id))
                    id = cur.fetchone()"""
    return 'budget'


def api_accountingaccount_get(id):  # noqa: E501
    """get a particular account

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: Account
    """
    if connexion.request.is_json:
        id = Id.from_dict(connexion.request.get_json())  # noqa: E501
        """with psycopg.connect(conn_string) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM accounting.account WHERE id = %s", (id,))
                    record = cur.fetchone()"""
    return 'account'


def api_list_account_get():  # noqa: E501
    """list all accounts

     # noqa: E501


    :rtype: List[Account]
    """
    def returnItem(item):
        return {
            "id": item[0],
            "name": item[1],
            "budget": item[2],
        }
    accounts = list()
    with psycopg.connect(conn_string) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM accounting.accounts")
            for account in cur:
                accounts.append(returnItem(account))
    return accounts


def api_list_transaction_get():  # noqa: E501
    """get a particular transaction

     # noqa: E501


    :rtype: Transaction
    """
    
    sql = """
    SELECT * FROM accounting.transactions
    """
    items = list()
    with psycopg.connect(conn_string) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            for item in cur:
                items.append(item)
                #items.append(item)
    return items
    return 'do some magic!'


def api_transaction_get(id):  # noqa: E501
    """get a particular transaction

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: Transaction
    """
    if connexion.request.is_json:
        id = Id.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
