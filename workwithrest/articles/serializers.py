from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def validate_title(self, value):
        articles = Article.objects.filter(title=value)

        if self.instance is not None:
            articles = articles.exclude(pk=self.instance.pk)

        if articles.exists():
            raise serializers.ValidationError('Duplicated')

        return value

    def create(self, validated_data):
        print('Created')
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print('Updated')
        return instance
