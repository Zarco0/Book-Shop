# Generated by Django 5.1.4 on 2024-12-13 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBook', '0003_tbl_book_quandity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_book',
            old_name='quandity',
            new_name='quantity',
        ),
    ]