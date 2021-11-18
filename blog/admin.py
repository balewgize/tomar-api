from django.contrib import admin
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Custom admin for the Post model."""

    autocomplete_fields = ["category"]
    list_display = ["title", "category", "user", "date_posted"]
    list_filter = ["date_posted"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Custom admin for the Category model."""

    list_display = ["title", "posts_count"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ["title"]}

    @admin.display(ordering="posts_count")
    def posts_count(self, category):
        url = (
            reverse("admin:blog_post_changelist")
            + "?category__id__exact="
            + str(category.id)
        )
        return format_html('<a href="{}">{}</a>', url, category.posts_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(posts_count=Count("post"))
