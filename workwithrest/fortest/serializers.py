from rest_framework import serializers

from . import models


class FriendSerialzier(serializers.ModelSerializer):
    class Meta:
        model = models.Friend
        fields = 'id name'.split()


class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Belonging
        fields = 'id name'.split()


class BorowedSerialzier(serializers.ModelSerializer):
    class Meta:
        model = models.Borrowed
        fields = 'id what to_who when returned'.split()


