from django.contrib import admin
from .models import Problem, Info , Contact

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('name', 'firstname', 'problem_type', 'incident_date')
    list_filter = ('problem_type', 'incident_date')
    search_fields = ('name', 'firstname', 'description')


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject')
    search_fields = ('name', 'email', 'subject')