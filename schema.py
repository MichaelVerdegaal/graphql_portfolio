import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models.user import UserModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        query = User.get_query(info)  # SQLAlchemy query
        return query.all()


# noinspection PyTypeChecker
schema = graphene.Schema(query=Query)
