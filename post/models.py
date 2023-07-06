from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='posts', related_query_name='posts')
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.category:
            return f'{self.category.title} > {self.title} > {self.body}'
        else:
            return self.title



# CharField - для строковых значений (требуется указать max_length)
# TextField - для хранения текста
# DecimalField - для дробных/вещественных чисел (max_digits - количество цифр в целой части, decimal_places - количество цифр в дробной части)
# IntegerField - для чисел
# BooleanField - для логических значений
# DateField - для дат (в формате datetime.date в Python), auto_now - обновляется при обновлении записи, auto_now_add - устанавливается только при создании записи
# TimeField - для времени (может использоваться с auto_now и auto_now_add)
# DateTimeField - для даты и времени (может использоваться с auto_now и auto_now_add)
# DurationField - для временных периодов
# EmailField - для электронных адресов (проверка на валидность встроена)
# FileField - для загрузки файлов (upload_to - для указания директории, где будут храниться файлы, в базе данных хранится только путь к файлу)
# ImageField - для загрузки изображений (то же самое, что и FileField, но требуется библиотека Pillow)
# JSONField - для строк в формате JSON

# null - если True, то объект в базе данных может быть null, если данные не переданы
# blank (в основном для строковых полей) - если True, то поле может быть пустым, если данные не переданы
# choices - позволяет ограничить доступные варианты для поля (требуется передать список кортежей, где первый элемент сохраняется в базе данных, а второй элемент отображается)

# class MyModel(models.Model):
#     COLOR_CHOICES = (
#         ('R', 'RED'),
#         ('B', 'BLUE'),
#         ('G', 'GREEN')
#     )
#     color = models.CharField(max_length=255, choices=COLOR_CHOICES)


# default - value po umolchaniyu for the field, adds value if data is not peredana

# editable - if False, record cannot change

# unique - if True, to budet vyzyvat'sya oshibka pri attemps create record, that already in the table

# primary_key - if True, to eto field stanet pervichnym key in the table (po defaultu stoit u polya id)
# primary_key = null  = False unique = True

# validator- validators = [Валидация]
#
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DateField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator()])
#     code = models.CharField(max_length=10, validators=[RegexValidator(reges=r'[A-Z]{3}-d{3}$', message ='Code must be in the format AAA-666')
#     ])
#
# class Passport(models.Model):
#     info = models.CharField(max_length=255)
#
# class Person(models.Model):
#     passport = models.OneToOneField(Passport, on_delete=models.CASCADE)
#
# class Tag(models.Model):
#     title = models.CharField(max_length=255)
#
# class Post(models.Model):
#     tags = models.ManyToManyField(Tag)
#
#
#
# class Category(models.Model):
#     title = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title
#
# class Post(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

# on_delete=models.CASCADE - если удаляется главный объект, то удаляются все зависимые
# on_delete=models.PROTECT - предотвращает ошибку при попытке удаления основного объекта
# on_delete=models.SET_NULL - не удаляет зависимые объекты, а заменяет на null, если null=True
# on_delete=models.SET_DEFAULT - устанавливает значение по умолчанию, если было определено как default
# on_delete=models.DO_NOTHING - вообще ничего не делает (может возникнуть ошибка)

# related_name - используется для определения имени обратной связи с другой моделью.
# Устанавливает имя, по которому можно обращаться к связанным объектам.
# Обычно используется в поле ForeignKey.

# related_query_name - этот параметр используется для определения имени обратной связи, используемого в запросах.
# Он определяет, как связанные объекты могут быть запрошены с помощью метода filter() или exclude()
