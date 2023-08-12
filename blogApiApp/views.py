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