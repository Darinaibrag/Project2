from django.db import models


# # Получение общего количества объектов модели
# total_count = MyModel.objects.count()
#
# # Получение суммы значения поля 'field_name' для всех объектов
# total_sum = MyModel.objects.aggregate(Sum('field_name'))
#
# # Получение среднего значения поля 'field_name' для всех объектов
# average_value = MyModel.objects.aggregate(Avg('field_name'))


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Syllabus(models.Model):
    syllabus = models.CharField(max_length=50)

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name='cs', related_query_name='cs')
    syllabus = models.OneToOneField(Syllabus, on_delete=models.CASCADE, blank=True, null=True, related_name='course', related_query_name='course')

    def __str__(self):
        return self.name


# # Получение студентов старше 20 лет
# students_above_20 = Student.objects.filter(age__gt=20)
#
# # Получение курсов с названием, содержащим слово "Math"
# math_courses = Course.objects.filter(name__contains='Math')
#  st = Student.objects.exclude(age__gt = 30)



# from myapp.models import MyModel
# from django.db.models import Count, Sum, Avg
#
# # Получение общего количества объектов модели
# total_count = MyModel.objects.count()
#
# # Получение суммы значения поля 'field_name' для всех объектов
# total_sum = MyModel.objects.aggregate(Sum('field_name'))
#
# # Получение среднего значения поля 'field_name' для всех объектов
# average_value = MyModel.objects.aggregate(Avg('field_name'))

# stud = Student.objects.get(id=3).delete()

