from django.contrib import admin
from django.db import models
from .models import Poll, Responde
# Register your models here.


class RespondeAdmin(admin.TabularInline):
    model = Responde


class PollAdmin(admin.ModelAdmin):
    inlines = [
        RespondeAdmin,
    ]


admin.site.register(Poll, PollAdmin)
