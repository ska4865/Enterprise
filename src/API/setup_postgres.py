import psycopg
import yaml

with open('../../docker-compose.yaml', 'r') as sql_setings:
	server_settings = yaml.unsafe_load(sql_setings)["services"]["db"]
	settings = {}
	for kv in server_settings["environment"]:
		splitkv = kv.split('=')
		settings[splitkv[0]] = splitkv[1]
	settings['PORT'] = server_settings["ports"][0].split(':')[0]
	
	conn_string = f"host=localhost port={settings['PORT']} user={settings['POSTGRES_USER']} password={settings['POSTGRES_PASSWORD']}"

with psycopg.connect(conn_string) as conn:
	with conn.cursor() as cur:
		# cur.execute("""
		# 	CREATE TABLE IF NOT EXISTS items (
		# 		ID          SERIAL PRIMARY KEY,
		# 		NAME        TEXT NOT NULL,
		# 		QUANTITY    INTEGER NOT NULL,
		# 		PRICE       NUMERIC NOT NULL)
		# 	""")
		with open('seed-data.yaml', 'r') as seed_data:
			seed_data = yaml.safe_load(seed_data)['seed']
			for account in seed_data["accounting"]["accounts"]:
				cur.execute("INSERT INTO accounting.accounts (NAME, BUDGET) VALUES (%s, %s)", (account["name"], account["budget"]))
			for store in seed_data["inventory"]["stores"]:
				cur.execute("INSERT INTO inventory.stores (NAME, MAXSTORE) VALUES (%s, %s)", (store["name"], store["maxstore"]))
			for itemtype in seed_data["inventory"]["itemtypes"]:
				cur.execute("INSERT INTO inventory.itemtypes (NAME, PRICE) VALUES (%s, %s)", (itemtype["name"], itemtype["price"]))
			for item in seed_data["inventory"]["items"]:
				cur.execute("INSERT INTO inventory.items (STOREID, ITEMTYPEID, QUANTITY) VALUES (%s, %s, %s)", (item["storeid"], item["itemtypeid"], item["quantity"]))
		cur.execute("SELECT * FROM inventory.items")
		for item in cur:
			print(item)