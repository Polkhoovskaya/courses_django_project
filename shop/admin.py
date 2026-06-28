from django.contrib import admin
from . import models

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Courses Admin Area"

admin.site.register(models.Category)
admin.site.register(models.Course)
