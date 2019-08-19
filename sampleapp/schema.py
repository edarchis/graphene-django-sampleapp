import json

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
        name = graphene.String()
        height = graphene.Int()

    table = graphene.Field(TableNode)

    @classmethod
    def mutate(cls, root, info, input):
        print(json.dumps(input))
        table = Table.objects.create(name=input['name'], height=input['height'])
        print(str(table))
        return CreateTableMutation(table=table)


class Mutation(graphene.ObjectType):
    create_table = CreateTableMutation.Field()


schema = Schema(query=Query, mutation=Mutation)
