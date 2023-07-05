# 1. Created a project
# 2. Created file requirements.txt
# 3. Write list of liabraries
# 4. Install all liabraries
# 5. pip freeze > requirements.txt
# 6. django-admin startproject config . # command for the creation of the project where config is a title of the project
# 7. django-admin startapp post - command for the creation of app
# 8. python3 manage.py makemigrations - command for schityvaniya dannyh
# 9. python3 manage.py migrate - for sending of tables to database
# 10. python3 manage.py runserver - for the launch of server
# 11. python3 manage.py createsuperuser - create of superuser

# python3 manage.py shell - open interactivnyi interpretator python. With the help of this can work with Django from command string.
# This helps for vypolneeniya zaprosov i testirovaniya fragmet of code

# c = Category.objects.get(pk=2)
# p = Post.objects.filter(title='vue').delete()
# c = Category.objects.filter(posts__title='backend')

import json

json_data = '{"category": "python", "title": "django", "body": "framework"}'
data = json.loads(json_data)
print(data)
print(type(data))

'------'
json_data = json.dumps(data)
print(json_data)
print(type(data))

