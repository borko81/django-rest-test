from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .serializers import PostSerialzier
from .forms import PostForm
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return render(request, 'talk/js_index.html')

def home(request):
    form = PostForm(request.POST or None)
    tmp_var = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'talk/index.html', tmp_var)


@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerialzier(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_concrete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerialzier(post)
        return Response(serializer.data)


