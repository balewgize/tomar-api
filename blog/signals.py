from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Post


@receiver(post_delete, sender=Post)
def post_delete_image_handler(sender, **kwargs):
    """Deletes the image associated with the post after the post has been deleted."""
    import os

    if kwargs["instance"].image and kwargs["instance"].image.url:
        try:
            os.remove(kwargs["instance"].image.path)
        except OSError:
            pass
