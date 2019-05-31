import sys
# contains env variables
sys.path.append('/app/settings/arangodb')
import config

from arango import ArangoClient
from arango_orm.database import Database

from arango_orm.fields import String, Integer, Int
from arango_orm import Collection, Relation, Graph, GraphConnection
from arango_orm.references import relationship, graph_relationship


class Person(Collection):

    __collection__ = 'persons'

    _index = [{'type': 'hash', 'unique': False, 'fields': ['name']}]
    _allow_extra_fields = False  # prevent extra properties from saving into DB

    _key = String(required=True)
    name = String(required=True, allow_none=False)

    cars = relationship(__name__ + ".Car", '_key', target_field='owner_key')

    def __str__(self):
        return "<Person(" + self.name + ")>"


class Car(Collection):

    __collection__ = 'cars'
    _allow_extra_fields = True

    make = String(required=True)
    model = String(required=True)
    year = Int(required=True)
    owner_key = String()

    owner = relationship(Person, 'owner_key', cache=False)

    def __str__(self):
        return "<Car({} - {} - {})>".format(self.make, self.model, self.year)


def initTest():
    client = ArangoClient(protocol='http', host=config.DATABASE_CONFIG['host'], port=config.DATABASE_CONFIG['port'])
    dev_db = client.db(config.DATABASE_CONFIG['database'], username=config.DATABASE_CONFIG['username'],
                       password=config.DATABASE_CONFIG['password'], verify=config.DATABASE_CONFIG['verify'])

    db = Database(dev_db)
    if db.has_collection(Person):
        db.drop_collection(Person)
        db.create_collection(Person)
    else:
        db.create_collection(Person)

    if db.has_collection(Car):
        db.drop_collection(Car)
        db.create_collection(Car)
    else:
        db.create_collection(Car)

    p = Person(_key='kashif', name='Kashif Iftikhar')
    db.add(p)
    p2 = Person(_key='azeen', name='Azeen Kashif')
    db.add(p2)

    c1 = Car(make='Honda', model='Civic', year=1984, owner_key='kashif')
    db.add(c1)

    c2 = Car(make='Mitsubishi', model='Lancer', year=2005, owner_key='kashif')
    db.add(c2)

    c3 = Car(make='Acme', model='Toy Racer', year=2016, owner_key='azeen')
    db.add(c3)

    print(c1.owner)
    print(c1.owner.name)
    print(c2.owner.name)
    print(c3.owner.name)

    print(p.cars)
    print(p.cars[0].make)
    print(p2.cars)