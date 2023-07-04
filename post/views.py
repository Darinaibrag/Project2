from django.shortcuts import render
from post.models import Post
from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    queryset = Post.objects.all()
    print(queryset)
    return render(request, 'listing.html', {'posts':queryset})



# QuerySet - lets read data from database
# filter and change order

# objects - is a Manager that lets us work with database.
# They gives us access through methonds to Django ORM(that v svoyu ochered otpravlyaet zaprosy to database)
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