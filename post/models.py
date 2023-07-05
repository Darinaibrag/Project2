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




# CharField - for string values (required to write max_length)
# TextField - for storage of text
# DecimalField - for drobnyh/float numbers (max_digits quantity of numbers of celoi chasti, decimal places - quantity of numbers drobnoi chasti)
# IntengerField - for numbers
# BooleanField - for bool values
# DateField - for dates (in puython datetime.date) auto_now - obnovlyaetsya each time pri obnovllenii of record auto_now_add
# TimeField - for the time (takje can prinipat' auto_now and auto_now_add)
# DateTimeField - for dates and time (takje can prinipat' auto_now and auto_now_add)
# DurationField - for time periods
# EmailField for email (has build-in checking, yavlyaetsya deistvitel'nym adres of email)
# FileField - for zagruzki files (upload_to - for ukazanii direktorii, where budut hranit'sya faily, v database budet hranitsya lish put' do faila)
# ImageField - dlya zagruzki foto (toje samoe, chto i FileField, no trebuetsya biblioteka Pillow)
# JSONField - for strings in JSON format

# null = if True, budet stavit in BD object null, if data ne peredany
# blank (bolshe idet dlya string fields) if True, budet stavit' pustuyu string if data ne peredany)
# choises - lets constraint variants in this field for this nujno peredat spisok s kortejami, gde pervyi element hranitsya v BD, vtoroi , chto budet otobrajat'sya

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
#
# class Category(models.Model):
#     title = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title
#
# class Post(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    # on_delete=models.CASCADE - (если удаляется главный объект, то удаляются все зависимые)
    # on_delete=models.PROTECT - recalls mistake pri attemp of deleting of main object
    # on_delete=models.SET_NULL - (does not delete dependent objects, a replace with null if null=True)
    # models.SET_DEFAULT - stavit default if was determined as default
    # models.DO_NOTHING - voobshe nichego ne delaet (mojet vozniknut' oshibka)



# related_name - used for opredelenniya of name obratnoi svyazi with another model.
# Ustanavlivaet imya, po kotoromu mojno obrashtsya to svyzannym objects.
# Usually used in the field ForeignKey.

# related_query_name - this option is used for opredeleniya imya obratnoi svyazi, used in requests.
# Ona opred, kak svyazannye objects can be zaprosheny s pomosheyu method fileter() exclude()

