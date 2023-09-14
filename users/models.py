from django.db.models import *
from django.contrib.auth.models import User
from PIL import Image


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    image = ImageField(default='user_default.png', upload_to='profile_image/')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)
