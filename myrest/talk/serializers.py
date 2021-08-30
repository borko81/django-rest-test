from rest_framework import serializers
from .models import Post


class PostSerialzier(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'
