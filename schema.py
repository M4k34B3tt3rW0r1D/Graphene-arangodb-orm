import graphene
from graphene.relay import Node, ConnectionField, Connection

from resolvers.resolvers import get_role, get_department, get_employee, get_all_employee, get_count_of_all_employees


class Department(graphene.ObjectType):
    '''A Department'''

    class Meta:
        # model = DepartmentModel
        interfaces = (Node,)

    name = graphene.String(description='The Department')
    _key = graphene.String()  # registration number

    @classmethod
    def get_node(cls, info, id):
        return get_department(id)


class Role(graphene.ObjectType):
    '''a Role'''

    class Meta:
        # model = RoleModel
        interfaces = (Node,)

    name = graphene.String(description='The Role')
    _key = graphene.String()  # registration number

    @classmethod
    def get_node(cls, info, id):
        return get_role(id)


class RoleConnection(Connection):
    class Meta:
        node = Role


class Employee(graphene.ObjectType, ):
    '''An Employee'''

    class Meta:
        # model = EmployeeModel
        interfaces = (Node,)

    name = graphene.String(description='The Employee')
    _key = graphene.String()  # registration number
    department_key = graphene.String()
    role_key = graphene.String()
    role = graphene.Field(Role)
    department = graphene.Field(Department)

    @classmethod
    def get_node(cls, info, id):
        return get_employee(id)


class EmployeeConnection(Connection):
    total_count = graphene.Int()

    class Meta:
        node = Employee

    @staticmethod
    def resolve_total_count(self, info):
        return get_count_of_all_employees()


class Query(graphene.ObjectType):
    node = Node.Field()
    all_employees = ConnectionField(EmployeeConnection)
    all_role = ConnectionField(RoleConnection)


    @staticmethod
    def resolve_all_employees(_, info, **args):
        return get_all_employee()


schema = graphene.Schema(query=Query)

#
# class Department(MongoengineObjectType):
#     '''A Department'''
#     class Meta:
#         model = DepartmentModel
#         interfaces = (Node,)
#
#
# class Role(MongoengineObjectType):
#
#     class Meta:
#         model = RoleModel
#         interfaces = (Node,)
#
#
# class Employee(MongoengineObjectType):
#
#     class Meta:
#         model = EmployeeModel
#         interfaces = (Node, )
#
#
# class Query(graphene.ObjectType):
#     node = Node.Field()
#     all_employees = MongoengineConnectionField(Employee)
#     all_role = MongoengineConnectionField(Role)
#     role = graphene.Field(Role)
#
#
# schema = graphene.Schema(query=Query, types=[Department, Employee, Role])
