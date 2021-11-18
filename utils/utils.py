"""
Utility functions used in the tomar project
"""

from django.core.files import File
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from PIL import Image, ImageOps


def get_unique_slug(Klass, base_word):
    """Generate a unique slug from the given base word i.e unique in the Klass."""
    unique_slug = slugify(base_word)
    is_slug_taken = Klass.objects.filter(slug=unique_slug).exists()

    while is_slug_taken:
        random_string = get_random_string(length=12)
        unique_slug += "-" + random_string
        is_slug_taken = Klass.objects.filter(slug=unique_slug).exists()

    return unique_slug


def get_post_image_path(instance, filename):
    """Assign a unique name for the post image and return its full path."""
    from datetime import date

    ext = filename.split(".")[-1]
    new_filename = f"{instance.slug}.{ext}"
    today_path = date.today().strftime("%Y/%m/%d")
    image_path = f"post-images/{today_path}/{new_filename}"
    return image_path


def get_avatar_image_path(instance, filename):
    """Assign a unique name for the profile image and return its full path."""
    from datetime import date

    ext = filename.split(".")[-1]
    new_filename = f"{instance.username}.{ext}"
    today_path = date.today().strftime("%Y/%m/%d")
    image_path = f"profile-pics/{today_path}/{new_filename}"
    return image_path


def get_compressed_image(original_img, size):
    """Compress an image file and save to a JPEG format to reduce disk size."""
    from io import BytesIO

    img = Image.open(original_img)
    img = img.convert("RGB")  # for saving the image in JPEG format
    img = ImageOps.exif_transpose(img)
    img = ImageOps.fit(img, size)  # resizing and croping the image
    output = BytesIO()
    img.save(output, format="JPEG", quality=90)
    compressed_img = File(output, name=original_img.name)
    return compressed_img
