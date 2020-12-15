from rest_framework import serializers

from .models import *


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choices
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'


"""
[
    {
        "id": 1,
        "choices": [],
        "question": "Some Question",
        "pub_date": "2020-12-14T19:40:13.998270Z",
        "created_by": 1
    },
    {
        "id": 2,
        "choices": [
            {
                "id": 1,
                "votes": [
                    {
                        "id": 1,
                        "choice": 1,
                        "poll": 2,
                        "voted_by": 1
                    }
                ],
                "choice_text": "Yes",
                "poll": 2
            },
            {
                "id": 2,
                "votes": [],
                "choice_text": "No",
                "poll": 2
            }
        ],
        "question": "Question One",
        "pub_date": "2020-12-14T19:40:21.523668Z",
        "created_by": 1
    }
]"""