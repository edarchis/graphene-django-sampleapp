import json

import graphene
from graphene import Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from furniture.models import Table, Foot
from graphene_django.rest_framework.mutation import SerializerMutation

from furniture.serializers import TableSerializer


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


class CreateTableMutation(SerializerMutation):
    class Meta:
        serializer_class = TableSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


class Mutation(graphene.ObjectType):
    create_table = CreateTableMutation.Field()


schema = Schema(query=Query, mutation=Mutation)
