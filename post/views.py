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
    try:
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response('This object does not exist')








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