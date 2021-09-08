from rest_framework import serializers

from .models import Poll, Choices, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoicesSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choices
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoicesSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'
