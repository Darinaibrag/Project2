from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    queryset = Post.objects.all()
    print(queryset)
    return render(request, 'listing.html', {'posts': queryset})

# REST

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def posts_list_api_view(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_detail(request, id):
    # post = Post.objects.get(id=id)
    # serializer = PostSerializer(post)
    # print(serializer.data)
    # return Response(serializer.data)

    # try:
    #     post = Post.objects.get(id=id)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     return Response('This object does not exist')

    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
    print(request.data, 'REQUEST DATA')
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)

@api_view(['DELETE'])
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return Response(status=204)

# @api_view(['PUT'])
# def update_post(request, id):
#     post = get_object_or_404(Post, id=id)
#     serializer = PostSerializer(post, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=201)
#
# @api_view(['PATCH'])
# def update_post(request, id):
#     post = get_object_or_404(Post, id=id)
#     serializer = PostSerializer(post, data=request.data, partial=True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=201)


@api_view(['PUT', 'PATCH'])
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    partial = True if request.method == 'PATCH' else False
    serializer = PostSerializer(post, request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)



# QuerySet - lets us read data from database
# filter and change order

# objects - is a Manager that lets us work with database.
# They give us access through methonds to Django ORM(that v svoyu ochered otpravlyaet zaprosy to database)
# Interface that lets work with database through models

# Model.objects.all()
# Method all() vozvrashaet QuerySet all objects in database
# SELECT * from table_name;

# filter(**kwargs)
# Vozvrashaet new QuerySet, contains objects, that sootvetstvuyut zadannym parametres of search
# Post.objects.filter(create_at__year=2022)
# Post.objects.filter(category=1)
# Post.object.all().filter(category=1)

# exclude(**kwargs)
# Vozvrashaet new QuerySet, soderjashii objects, that ne sootvetst ukazanym parametres
# Post.objects.exclude(category=1)

# Vozvrashet new QuerySet, contains object according to condition
# Post.objects.get(id=1)

# Post.objects.order_by('price')
# Post.objects.order_by('-price')

# Post.objects.all()[:5]