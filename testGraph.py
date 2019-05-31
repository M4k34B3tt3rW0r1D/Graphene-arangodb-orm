from arango import ArangoClient
from arango_orm.database import Database
from arango_orm import Collection, Relation, Graph, GraphConnection
from graphmodels.university import Area, SpecializesIn, Student, Subject, Teacher, UniversityGraph

import sys
# contains env variables
sys.path.append('/app/settings/arangodb')
import config


def initGraph():
    client = ArangoClient(protocol='http', host=config.DATABASE_CONFIG['host'], port=config.DATABASE_CONFIG['port'])
    dev_db = client.db(config.DATABASE_CONFIG['database'], username=config.DATABASE_CONFIG['username'], password=config.DATABASE_CONFIG['password'], verify=config.DATABASE_CONFIG['verify'])
    db = Database(dev_db)

    uni_graph = UniversityGraph(connection=db)
    db.create_graph(uni_graph)

    students_data = [
        Student(_key='S1001', name='John Wayne', age=30),
        Student(_key='S1002', name='Lilly Parker', age=22),
        Student(_key='S1003', name='Cassandra Nix', age=25),
        Student(_key='S1004', name='Peter Parker', age=20)
    ]

    teachers_data = [
        Teacher(_key='T001', name='Bruce Wayne'),
        Teacher(_key='T002', name='Barry Allen'),
        Teacher(_key='T003', name='Amanda Waller')
    ]

    subjects_data = [
        Subject(_key='ITP101', name='Introduction to Programming', credit_hours=4, has_labs=True),
        Subject(_key='CS102', name='Computer History', credit_hours=3, has_labs=False),
        Subject(_key='CSOOP02', name='Object Oriented Programming', credit_hours=3, has_labs=True),
    ]

    areas_data = [
        Area(_key="Gotham"),
        Area(_key="Metropolis"),
        Area(_key="StarCity")
    ]

    for s in students_data:
        db.add(s)

    for t in teachers_data:
        db.add(t)

    for s in subjects_data:
        db.add(s)

    for a in areas_data:
        db.add(a)

    db.add(SpecializesIn(_from="teachers/T001", _to="subjects/ITP101", expertise_level="medium"))

    gotham = db.query(Area).by_key("Gotham")
    metropolis = db.query(Area).by_key("Metropolis")
    star_city = db.query(Area).by_key("StarCity")

    john_wayne = db.query(Student).by_key("S1001")
    lilly_parker = db.query(Student).by_key("S1002")
    cassandra_nix = db.query(Student).by_key("S1003")
    peter_parker = db.query(Student).by_key("S1004")

    intro_to_prog = db.query(Subject).by_key("ITP101")
    comp_history = db.query(Subject).by_key("CS102")
    oop = db.query(Subject).by_key("CSOOP02")

    barry_allen = db.query(Teacher).by_key("T002")
    bruce_wayne = db.query(Teacher).by_key("T001")
    amanda_waller = db.query(Teacher).by_key("T003")

    db.add(uni_graph.relation(peter_parker, Relation("studies"), oop))
    db.add(uni_graph.relation(peter_parker, Relation("studies"), intro_to_prog))
    db.add(uni_graph.relation(john_wayne, Relation("studies"), oop))
    db.add(uni_graph.relation(john_wayne, Relation("studies"), comp_history))
    db.add(uni_graph.relation(lilly_parker, Relation("studies"), intro_to_prog))
    db.add(uni_graph.relation(lilly_parker, Relation("studies"), comp_history))
    db.add(uni_graph.relation(cassandra_nix, Relation("studies"), oop))
    db.add(uni_graph.relation(cassandra_nix, Relation("studies"), intro_to_prog))

    db.add(uni_graph.relation(barry_allen, SpecializesIn(expertise_level="expert"), oop))
    db.add(uni_graph.relation(barry_allen, SpecializesIn(expertise_level="expert"), intro_to_prog))
    db.add(uni_graph.relation(bruce_wayne, SpecializesIn(expertise_level="medium"), oop))
    db.add(uni_graph.relation(bruce_wayne, SpecializesIn(expertise_level="expert"), comp_history))
    db.add(uni_graph.relation(amanda_waller, SpecializesIn(expertise_level="basic"), intro_to_prog))
    db.add(uni_graph.relation(amanda_waller, SpecializesIn(expertise_level="medium"), comp_history))

    db.add(uni_graph.relation(bruce_wayne, Relation("teaches"), oop))
    db.add(uni_graph.relation(barry_allen, Relation("teaches"), intro_to_prog))
    db.add(uni_graph.relation(amanda_waller, Relation("teaches"), comp_history))

    db.add(uni_graph.relation(bruce_wayne, Relation("resides_in"), gotham))
    db.add(uni_graph.relation(barry_allen, Relation("resides_in"), star_city))
    db.add(uni_graph.relation(amanda_waller, Relation("resides_in"), metropolis))
    db.add(uni_graph.relation(john_wayne, Relation("resides_in"), gotham))
    db.add(uni_graph.relation(lilly_parker, Relation("resides_in"), metropolis))
    db.add(uni_graph.relation(cassandra_nix, Relation("resides_in"), star_city))
    db.add(uni_graph.relation(peter_parker, Relation("resides_in"), metropolis))