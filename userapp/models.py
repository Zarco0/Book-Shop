from django.db import models
from myBook.models import tbl_Book
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(tbl_Book)

    def __str__(self):
        return '{}'.format(self.user)


class Cartitem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book=models.ForeignKey(tbl_Book,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.cart)