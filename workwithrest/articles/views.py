from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import  Article
from .serializers import ArticleSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(instance=articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
