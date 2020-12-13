from .models import Problem, Employee, Type
from rest_framework import serializers


# class SerializerType(serializers.Serializer):
#     name = serializers.CharField(max_length=50)
#
#     def created(self, validated_data):
#         return Type.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance

class SerializerType(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'