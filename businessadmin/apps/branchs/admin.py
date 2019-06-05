from django.contrib import admin

from .models import Branch, Department, Klass


admin.site.register(Branch)
admin.site.register(Department)
admin.site.register(Klass)