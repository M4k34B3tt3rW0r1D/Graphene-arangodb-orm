from arango_orm.fields import String, Date
from arango_orm import Collection, Relation, Graph, GraphConnection
from arango_orm.references import relationship, graph_relationship
from datetime import datetime


class Department(Collection):
    __collection__ = 'department'
    _allow_extra_fields = True
    _index = [{'type': 'hash', 'unique': False, 'fields': ['name']}]
    _key = String(required=True)  # registration number
    name = String(required=True, allow_none=False)
    # dob = Date()


class Role(Collection):
    __collection__ = 'role'
    _allow_extra_fields = True
    _index = [{'type': 'hash', 'unique': False, 'fields': ['name']}]
    _key = String(required=True)  # registration number
    name = String(required=True, allow_none=False)
    # dob = Date()


class Employee(Collection):
    _allow_extra_fields = True
    __collection__ = 'employee'
    _index = [{'type': 'hash', 'unique': False, 'fields': ['name']}]
    _key = String(required=True)  # registration number
    name = String(required=True, allow_none=False)
    department_key = String(required=False)
    role_key = String(required=False)
    hired_on = Date(default=datetime.now)
    department = relationship(Department, field='department_key')
    role = relationship(Role, field='role_key')
