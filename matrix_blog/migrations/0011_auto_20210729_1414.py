# Generated by Django 3.2.5 on 2021-07-29 14:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix_blog', '0010_auto_20210729_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='dislikes',
        ),
        migrations.AddField(
            model_name='article',
            name='dislikes',
            field=models.ManyToManyField(null=True, related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='article',
            name='likes',
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
