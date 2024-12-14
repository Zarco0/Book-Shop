from django.db import models

# Create your models here.

class tbl_Author(models.Model):
    name=models.CharField(max_length=50,null=True)

    def __str__(self):
        return '{}'.format(self.name)


class tbl_Book(models.Model):
    title=models.CharField(max_length=50,null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='book_media')
    quantity=models.IntegerField()

    author=models.ForeignKey(tbl_Author,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.title)