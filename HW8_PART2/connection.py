import configparser
from mongoengine import connect


config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'USER')
mongo_pass  = config.get('DB', 'PASS')
db = config.get('DB', 'DB_NAME')
domain = config.get('DB', 'DOMAIN')


connect(host=f"""mongodb+srv://{mongo_user}:{mongo_pass}@{domain}/{db}?retryWrites=true&w=majority""", ssl=True)
