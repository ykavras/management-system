from django.contrib import admin

from .models import Business, Sector, StudentQualification

admin.site.register(Business)
admin.site.register(Sector)
admin.site.register(StudentQualification)