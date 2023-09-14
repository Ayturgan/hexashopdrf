from django.db.models import *
from django.contrib.auth.models import User
from django.utils import timezone


class Product(Model):
    name = CharField(max_length=255, null=False)
    description = TextField()
    price = IntegerField()
    author = ForeignKey(User, on_delete=CASCADE)
    created_date = DateField(default=timezone.now)
    image = ImageField(default='default.png', upload_to="product_image/")

    def __str__(self):
        return self.name

