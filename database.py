#from mongoengine import connect

import sys
# contains env variables
sys.path.append('/app/settings/arangodb')
import config

from models_aDB import Department, Employee, Role
from arango import ArangoClient
from arango_orm import Database

# you can connect to a real mongo server instance by your own
#connect('graphene-mongo-example', host='mongomock://localhost', alias='default')

client = ArangoClient(protocol='http', host=config.DATABASE_CONFIG['host'], port=config.DATABASE_CONFIG['port'])
dev_db = client.db(config.DATABASE_CONFIG['database'], username=config.DATABASE_CONFIG['username'], password=config.DATABASE_CONFIG['password'], verify=config.DATABASE_CONFIG['verify'])
db = Database(dev_db)


def test():
    print(db.query(Employee).all())


def init_arangodb():

    if db.has_collection(Department):
        db.drop_collection(Department)
        db.create_collection(Department)
    else:
        db.create_collection(Department)

    if db.has_collection(Employee):
        db.drop_collection(Employee)
        db.create_collection(Employee)
    else:
        db.create_collection(Employee)

    if db.has_collection(Role):
        db.drop_collection(Role)
        db.create_collection(Role)
    else:
        db.create_collection(Role)

    # create the fixture
    engineering = Department(name='engineering')
    db.add(engineering)

    hr = Department(name='Human Resources')
    db.add(hr)

    manager = Role(name='manager')
    db.add(manager)

    engineer = Role(name='engineer')
    db.add(engineer)

    peter = Employee(name='Peter', role_key=engineer._key, department_key=engineering._key)
    db.add(peter)

    roy = Employee(name='Roy', role_key=engineer._key, department_key=engineering._key)
    db.add(roy)

    tracy = Employee(name='Tracy',role_key=manager._key, department_key=hr._key)
    db.add(tracy)

# def init_db():
#     # create the fixture
#     engineering = Department(name='Engineering')
#     engineering.save()
#
#     hr = Department(name='Human Resources')
#     hr.save()
#
#     manager = Role(name='manager')
#     manager.save()
#
#     engineer = Role(name='engineer')
#     engineer.save()
#
#     peter = Employee(name='Peter', department=engineering, role=engineer)
#     peter.save()
#
#     roy = Employee(name='Roy', department=engineering, role=engineer)
#     roy.save()
#
#     tracy = Employee(name='Tracy', department=hr, role=manager)
#     tracy.save()
