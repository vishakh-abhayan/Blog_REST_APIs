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
    
@api_view(['DELETE'])
def DeletePost(request):
    post_id = request.POST.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({'Success': 'This post was successfully deleted'}, status=200)
    except Post.DoesNotExist:
        return Response({'Error': 'The post does not exist'}, status=404)

@api_view(['GET'])
def GetPost(request):
    post_id = request.GET.get('post_id')
    print(post_id)
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({'Error': 'The post does not exist'}, status=404)