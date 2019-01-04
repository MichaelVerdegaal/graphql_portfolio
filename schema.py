import graphene
from graphene.relay import Connection, Node
from graphene_sqlalchemy import SQLAlchemyObjectType, FilterableConnectionField

from models.user import UserModel


class UserNode(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (Node,)


class UserConnection(Connection):
    class Meta:
        node = UserNode


class Query(graphene.ObjectType):
    users = FilterableConnectionField(UserConnection)


# noinspection PyTypeChecker
schema = graphene.Schema(query=Query)
