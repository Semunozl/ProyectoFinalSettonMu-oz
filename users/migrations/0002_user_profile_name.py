# Generated by Django 4.1 on 2022-08-29 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
