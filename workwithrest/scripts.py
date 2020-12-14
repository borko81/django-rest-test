import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workwithrest.settings')
django.setup()

from articles.models import Article
from articles.serializers import ArticleSerializer

a = Article.objects.first()

data = {
    'title': 'Second Article',
    'content': 'Some content'
}

s = ArticleSerializer(data=data)