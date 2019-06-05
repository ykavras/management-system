from django.contrib import admin

from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'type')
    list_filter = ('type',)
    search_fields = ('user__first_name', 'user__first_name',)
