# Generated by Django 5.1.4 on 2024-12-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_book',
            name='image',
            field=models.ImageField(upload_to='book_media'),
        ),
    ]
