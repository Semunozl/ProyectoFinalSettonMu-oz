# Generated by Django 4.1 on 2022-08-31 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='name',
        ),
    ]
