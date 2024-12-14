from django.contrib import admin
from .models import tbl_Author,tbl_Book
# Register your models here.
admin.site.register(tbl_Book)
admin.site.register(tbl_Author)