from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline

from tags.models import TaggedItem
from .models import Profile, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Custom user admin for our custom User model."""

    pass


class TagInline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ["tag"]
    extra = 0
