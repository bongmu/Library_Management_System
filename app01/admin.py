from django.contrib import admin
from  app01 import models

# Register your models here.

# admin.site.register(models.User)
admin.site.register(models.Book)
admin.site.register(models.Publish)
admin.site.register(models.Author)
admin.site.register(models.AuthorDetail)

