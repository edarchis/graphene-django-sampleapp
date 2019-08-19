import graphene
from graphene import Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from furniture.models import Table, Foot


class TableNode(DjangoObjectType):
    class Meta:
        model = Table
        filter_fields = "__all__"
        interfaces = (graphene.relay.Node,)


class FootNode(DjangoObjectType):
    class Meta:
        model = Foot
        filter_fields = "__all__"
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    tables = DjangoFilterConnectionField(TableNode)


class CreateTableMutation(graphene.ClientIDMutation):
    class Input:
        height = graphene.Int()

    table = graphene.Field(TableNode)

    @classmethod
    def mutate(cls, root, info, input):
        return super().mutate(root, info, input)


class Mutation(graphene.ObjectType):
    create_table = CreateTableMutation.Field()


schema = Schema(query=Query)
