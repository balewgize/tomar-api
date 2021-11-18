from django.conf import settings
from django.db import models

from utils import utils


class Category(models.Model):
    """Categories used to organize posts."""

    title = models.CharField(max_length=40)
    slug = models.SlugField(unique=True)  # auto generate

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        # assing a unique slug from the title of a category
        self.slug = utils.get_unique_slug(self.__class__, self.title)
        return super().save(*args, **kwargs)


class Post(models.Model):
    """Posts written by admin or users of the platform."""

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(
        upload_to=utils.get_post_image_path,
        help_text="Select an appropriate image for your post."
        "Good images increase the chance of being read.",
    )
    slug = models.SlugField(max_length=212, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="category"
    )
    date_posted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_posted", "title"]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.image = utils.get_compressed_image(self.image, size=(1200, 630))
        self.slug = utils.get_unique_slug(self.__class__, self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """User's comment on posts."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(verbose_name="")
    date_posted = models.DateTimeField(auto_now=True)


class Reply(models.Model):
    """Replies to a comment."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="replies"
    )
    content = models.TextField(verbose_name="")
    date_posted = models.DateTimeField(auto_now=True)
