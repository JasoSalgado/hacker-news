"""apps/story/admin.py"""

# Django modules
from django.contrib import admin

# My modules
from .models import Story

admin.site.register(Story)