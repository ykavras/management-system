from django.contrib import admin

from .models import Term


class TermAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return not Term.objects.filter(archive=False).exists()


admin.site.register(Term, TermAdmin)
