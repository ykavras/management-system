from django.contrib import admin

from .models import Business, Sector, StudentQualification,ScholarShip

admin.site.register(Business)
admin.site.register(Sector)
admin.site.register(StudentQualification)
admin.site.register(ScholarShip)