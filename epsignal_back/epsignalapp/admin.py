from django.contrib import admin
from .models import Problem, Info , Contact , Newsletter

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('problem_type',)


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'surname', 'subject')
    search_fields = ('name', 'email', 'subject')