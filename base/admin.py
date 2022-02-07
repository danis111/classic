from django.contrib import admin

from .models import Project, Skill, Tag

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tag)
