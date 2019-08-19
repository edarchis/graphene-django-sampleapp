from rest_framework import serializers

from .models import Table, Foot


class FootSerializer(serializers.Serializer):
    class Meta:
        model = Foot

    number = serializers.IntegerField()
    style = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def get_attribute(self, instance):
        print("get_attr", self, instance)
        return []


class TableSerializer(serializers.Serializer):
    class Meta:
        model = Table

    name = serializers.CharField()
    height = serializers.IntegerField()
    foot_set = FootSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        feet = validated_data.pop('foot_set') if 'foot_set' in validated_data else []
        print("feet", type(feet), str(feet))
        table = Table.objects.create(name=validated_data['name'], height=validated_data['height'])
        for foot in feet:
            print("foot", type(foot), str(foot))
            Foot.objects.create(table=table, number=foot['number'], style=foot['style'])

        table.refresh_from_db()

        print("created table", table)
        return Table.objects.filter(id=table.id).prefetch_related("foot_set").first()

