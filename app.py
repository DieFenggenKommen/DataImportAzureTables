import os
import json
from dotenv import load_dotenv
from azure.data.tables import TableClient, TableEntity

# Load environment variables from .env file

load_dotenv()
account_name = os.environ.get('AZURE_STORAGE_ACCOUNT')
account_connection_string = os.environ.get(
    'AZURE_STORAGE_ACCOUNT_CONNECTION_STRING')

print(account_name)
print(account_connection_string)

exit()

# load local json data file into list

data = json.load(open('hexdata.json', encoding='utf-8'))
print(data[0])

exit()

# Create table client and create table


table_name = "interpretations"
table_client = TableClient.from_connection_string(
    conn_str=account_connection_string, table_name=table_name)

try:
    table_client.create_table()
    print(f"The table '{table_name}' has been created.")
except:
    print(f"The table '{table_name}' already exists.")

exit()

# Create entities

for hexagram in data:
    print(hexagram['name'])

    entity = TableEntity(PartitionKey='hexagram',
                         RowKey=hexagram["pattern"], Data=json.dumps(hexagram))
    table_client.create_entity(entity=entity)
