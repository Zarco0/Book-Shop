# Generated by Django 5.1.4 on 2024-12-12 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='type',
        ),
    ]
