from models_aDB import Department, Employee, Role
from arango import ArangoClient
from arango_orm import Database

import sys
# contains env variables
sys.path.append('/app/settings/arangodb')
import config


#Arango
client = ArangoClient(protocol='http', host=config.DATABASE_CONFIG['host'], port=config.DATABASE_CONFIG['port'])
dev_db = client.db(config.DATABASE_CONFIG['database'], username=config.DATABASE_CONFIG['username'],
                   password=config.DATABASE_CONFIG['password'], verify=config.DATABASE_CONFIG['verify'])
db = Database(dev_db)


def get_role(_key):
    return db.query(Role).by_key(_key)


def get_department(_key):
    return db.query(Department).by_key(_key)


def get_employee(_key):
    return db.query(Employee).by_key(_key)

# employees
def get_all_employee():
    r = db.query(Employee).all()
    return r


def get_count_of_all_employees():
    r = db.query(Employee).count()
    return r
