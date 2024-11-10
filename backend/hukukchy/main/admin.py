from django.contrib import admin
from . import models

admin.site.register(models.ServiceCategory)
admin.site.register(models.BookUpload)
admin.site.register(models.NewsCategory)
admin.site.register(models.News)

