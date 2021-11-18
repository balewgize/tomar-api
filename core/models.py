from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from utils import utils


class User(AbstractUser):
    """Custom user model with unique email."""

    email = models.EmailField(unique=True)


class Profile(models.Model):
    """User's profile."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    title = models.CharField(max_length=50)
    bio = models.TextField()
    avatar = models.ImageField(
        default="default-avatar.jpg", upload_to=utils.get_avatar_image_path
    )

    def save(self, *args, **kwargs):
        self.avatar = utils.get_compressed_image(self.avatar, size=(300, 300))
        return super().save(*args, **kwargs)
