from urllib.parse import parse_qs, urlparse
import connexion
import six
from urllib.parse import urlparse
from urllib.parse import parse_qs
import psycopg
import yaml
from swagger_server.models.complete_item import CompleteItem  # noqa: E501
from swagger_server.models.id import Id  # noqa: E501
from swagger_server.models.item import Item  # noqa: E501
from swagger_server.models.item_id import ItemID  # noqa: E501
from swagger_server.models.item_sell_body import ItemSellBody  # noqa: E501
from swagger_server.models.item_stock_body import ItemStockBody  # noqa: E501
from swagger_server.models.item_type import ItemType  # noqa: E501
from swagger_server.models.item_type_id import ItemTypeID  # noqa: E501
from swagger_server.models.store import Store  # noqa: E501
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

def itemToObject(item):
    return {
    "id":item[0],
    "store_id":item[1],
    "item_type_id":item[2],
    "quantity":item[3],
    }

def api_inventory_itemtype_get(id):  # noqa: E501
    """Returns an itemtype specified by ID

     # noqa: E501

    :rtype: Item
    """
    if connexion.request.is_json:
        id = Id.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
    


def api_inventory_itemtype_post(body):  # noqa: E501
    """adds a new itemtype as specified

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        id = Id.from_dict(connexion.request.get_json())  # noqa: E501
    with psycopg.connect(conn_string) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT ITEMTYPEID FROM inventory.items WHERE id = %s", (id,))
            record = cur.fetchone()
            cur.execute("SELECT * FROM inventory.itemtypes WHERE id = %s", (record))
            record = cur.fetchone()
    return itemToObject(record)



def api_inventory_store_post(body):  # noqa: E501

    if connexion.request.is_json:
        body = ItemID.from_dict(connexion.request.get_json())  # noqa: E501
        with psycopg.connect(conn_string) as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE inventory.items SET STOREID=%s, ITEMTYPEID=%s, QUANTITY=%s WHERE Id=%s",
                (body.storeid, body.quantity, body.id))
                body = cur.fetchone()
    return body
def api_inventory_store_delete(id):  # noqa: E501

    if connexion.request.is_json:
        body = ItemID.from_dict(connexion.request.get_json())  # noqa: E501
        #with psycopg.connect(conn_string) as conn:
        #    with conn.cursor() as cur:
                #cur.execute("UPDATE inventory.items SET STOREID=%s, ITEMTYPEID=%s, QUANTITY=%s WHERE Id=%s",
                #(body.storeid, body.quantity, body.id))
                #body = cur.fetchone()
    return "magic" #body


def api_item_get(id):  # noqa: E501
    """Returns an item specified by ID

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: CompleteItem
    """
    def returnItem(item):
        return {
            "quantity": item[0],
            "storeid": item[1],
            "itemtypeid": item[2],
            "name": item[3],
            "price": item[4],
        }
    if id is None:
        parsedURL = urlparse(connexion.request.url)
        kvQuery = parse_qs(parsedURL.query)
        id = kvQuery["id"][0]

    if connexion.request.is_json:
        id = Id.from_dict(connexion.request.get_json())  # noqa: E501
    with psycopg.connect(conn_string) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM inventory.items WHERE id = %s", (id,))
            record = cur.fetchone()

    return itemToObject(record)


def api_item_post(body):  # noqa: E501
    """adds a new item as specified

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Item.from_dict(connexion.request.get_json())  # noqa: E501
    with psycopg.connect(conn_string) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO inventory.items (NAME, QUANTITY, PRICE, ) VALUES (%s, %s, %s) RETURNING id", 
            (body.name, body.quantity, body.price))
            id = cur.fetchone()
    return id


def api_item_put(body):  # noqa: E501
    """updates an item

    :rtype: None
    """
    if connexion.request.is_json:
        body = ItemID.from_dict(connexion.request.get_json())  # noqa: E501
        with psycopg.connect(conn_string) as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE inventory.items SET NAME=%s, QUANTITY=%s, PRICE=%s WHERE Id=%s",
                (body.name, body.quantity, body.price, body.id))
                id = cur.fetchone()
    return 'quantity'

def api_item_delete(body):  # noqa: E501
    return "magic"

def api_item_sell(body):  # noqa: E501
    return "magic"
def api_item_stock(body):  # noqa: E501
    """stocks an item in inventory

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ItemID.from_dict(connexion.request.get_json())  # noqa: E501
        """with psycopg.connect(conn_string) as conn:
                with conn.cursor() as cur:
                    cur.execute("UPDATE inventory.items SET NAME=%s, QUANTITY=%s, PRICE=%s WHERE Id=%s",
                    (body.name, body.quantity, body.price, body.id))
                    id = cur.fetchone()"""
    return 'quantity'


def api_itemtype_delete(id=None):  # noqa: E501
    """deletes a itemtype

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: ItemType
    """
    if connexion.request.is_json:
        id = Id.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_itemtype_put(body):  # noqa: E501
    """updates an itemtype

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ItemTypeID.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_list_item_get():  # noqa: E501
    """lists all items

     # noqa: E501


    :rtype: List[CompleteItem]
    """
    def returnItem(item):
        return {
            "quantity": item[0],
            "storeid": item[1],
            "itemtypeid": item[2],
            "name": item[3],
            "price": item[4],
            "store": item[5]
        }
    sql = """
        SELECT 	items.QUANTITY AS AMOUNT, 
				items.STOREID,
				items.ITEMTYPEID,
                itemtypes.NAME AS NAME,
                itemtypes.PRICE AS PRICE,
                stores.NAME AS STORE
        FROM inventory.items
        INNER JOIN inventory.itemtypes ON items.ITEMTYPEID=itemtypes.ID
        INNER JOIN inventory.stores ON items.STOREID=stores.ID
        """
    items = list()
    with psycopg.connect(conn_string) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            for item in cur:
                items.append(returnItem(item))
                #items.append(item)
    return items


def api_list_itemtype_get():  # noqa: E501
    """lists all itemtypes

     # noqa: E501


    :rtype: List[ItemType]
    """


    def returnItem(item):
        return {
            "id": item[0],
            "name": item[1],
            "price": item[2],
        }

    sql = """
    SELECT * FROM inventory.itemtypes
    """
    items = list()
    with psycopg.connect(conn_string) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            for item in cur:
                items.append(returnItem(item))
                #items.append(item)
    return items
    return 'do some magic!'


def api_list_store_get():  # noqa: E501
    """lists all stores

     # noqa: E501


    :rtype: List[Store]
    """

    def returnItem(item):
        return {
            "id": item[0],
            "name": item[1],
            "maxstore": item[2],
        }
    sql = """
    SELECT * FROM inventory.stores
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


def api_store_get(id):  # noqa: E501
    """Returns a store specified by ID

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: Store
    """
    if connexion.request.is_json:
        id = Id.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
