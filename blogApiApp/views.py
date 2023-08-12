from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def index(request):
    return Response({'success':'this setup was successful'})

@api_view(['GET'])
def GetALLPosts(request):
    get_posts = Post.objects.all()
    serializer = PostSerializer(get_posts, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def CreatePost(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Sucess':'this post was successfully created'},status=201)
    else:
        return Response(serializer.errors,status=400)