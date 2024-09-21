from django.contrib import admin

# Register your models here.
from apps.models import *
admin.site.register(Dept)
admin.site.register(Emp)
admin.site.register(SalGrade)