import graphene
from graphene.relay import Connection, Node
from graphene_sqlalchemy import SQLAlchemyObjectType, FilterableConnectionField

from models.coding_skills import CodingSkillsModel
from models.misc_skills import MiscSkillsModel
from models.my_work import MyWorkModel
from models.soft_skills import SoftSkillsModel


class SoftSkillsNode(SQLAlchemyObjectType):
    class Meta:
        model = SoftSkillsModel
        interfaces = (Node,)


class SoftSkillsConnection(Connection):
    class Meta:
        node = SoftSkillsNode


class CodingSkillsNode(SQLAlchemyObjectType):
    class Meta:
        model = CodingSkillsModel
        interfaces = (Node,)


class CodingSkillsConnection(Connection):
    class Meta:
        node = CodingSkillsNode


class MiscSkillsNode(SQLAlchemyObjectType):
    class Meta:
        model = MiscSkillsModel
        interfaces = (Node,)


class MiscSkillsConnection(Connection):
    class Meta:
        node = MiscSkillsNode


class MyWorkNode(SQLAlchemyObjectType):
    class Meta:
        model = MyWorkModel
        interfaces = (Node,)


class MyWorkConnection(Connection):
    class Meta:
        node = MyWorkNode


class Query(graphene.ObjectType):
    soft_skills = FilterableConnectionField(SoftSkillsConnection)
    coding_skills = FilterableConnectionField(CodingSkillsConnection)
    misc_skills = FilterableConnectionField(MiscSkillsConnection)
    my_work = FilterableConnectionField(MyWorkConnection)


# noinspection PyTypeChecker
schema = graphene.Schema(query=Query)
