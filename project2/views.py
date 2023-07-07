from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from django.shortcuts import get_object_or_404
from .serializers import StudentSerializer
# Create your views here.

@api_view(['GET'])
def student_detail(request, id):
    detail = get_object_or_404(Student, id=id)
    serializer = StudentSerializer(detail)
    return Response(serializer.data)


@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)




@api_view(['POST'])
def create_post(request):
    print(request.data, 'REQUEST DATA')
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)



