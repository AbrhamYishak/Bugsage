from django.contrib import admin
from .models import ErrorCase, ErrorType
admin.site.register(ErrorType)
admin.site.register(ErrorCase)
# Register your models here.
