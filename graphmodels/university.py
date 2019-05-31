from arango_orm.fields import String, Date, Integer, Boolean
from arango_orm import Collection, Relation, Graph, GraphConnection


class Student(Collection):

    __collection__ = 'students'

    _key = String(required=True)  # registration number
    name = String(required=True, allow_none=False)
    age = Integer()

    def __str__(self):
        return "<Student({})>".format(self.name)


class Teacher(Collection):

    __collection__ = 'teachers'

    _key = String(required=True)  # employee id
    name = String(required=True)

    def __str__(self):
        return "<Teacher({})>".format(self.name)


class Subject(Collection):

    __collection__ = 'subjects'

    _key = String(required=True)  # subject code
    name = String(required=True)
    credit_hours = Integer()
    has_labs = Boolean(missing=True)

    def __str__(self):
        return "<Subject({})>".format(self.name)


class Area(Collection):

    __collection__ = 'areas'

    _key = String(required=True)  # area name


class SpecializesIn(Relation):

    __collection__ = 'specializes_in'

    _key = String(required=True)
    expertise_level = String(required=True, options=["expert", "medium", "basic"])

    def __str__(self):
        return "<SpecializesIn(_key={}, expertise_level={}, _from={}, _to={})>".format(
            self._key, self.expertise_level, self._from, self._to)


class UniversityGraph(Graph):

    __graph__ = 'university_graph'

    graph_connections = [
        # Using general Relation class for relationship
        GraphConnection(Student, Relation("studies"), Subject),
        GraphConnection(Teacher, Relation("teaches"), Subject),

        # Using specific classes for vertex and edges
        GraphConnection(Teacher, SpecializesIn, Subject),
        GraphConnection([Teacher, Student], Relation("resides_in"), Area)
    ]