"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from post.views import posts_list, posts_list_api_view, post_detail, create_post, delete, update_post, \
    PostListAPIView, CategoryListAPIView, PostDetailsAPIViews, PostCreateAPIView, PostDeleteAPIView, PostUpdateAPIView
from project2.views import student_detail, create_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_list/', posts_list),
    # path('api/listing/', posts_list_api_view),
    # path('api/details/<int:id>/', post_detail),
    # path('api/create/', create_post),
    # path('api/delete/<int:id>/', delete),
    # path('api/update/<int:id>/', update_post),
    # path('api/detail/<int:id>/', student_detail),
    # path('api/create_student/', create_student)
    #APIView urls
    path('api/listing/', PostListAPIView.as_view()),
    path('api/listing-category/', CategoryListAPIView.as_view()),
    path('api/detail/<int:id>/', PostDetailsAPIViews.as_view()),
    path('api/create/', PostCreateAPIView.as_view()),
    path('api/delete/<int:id>/', PostDeleteAPIView.as_view()),
    path('api/update/<int:id>/', PostUpdateAPIView.as_view())
]
# localhost:8000/api/details/1/