# Generated by Django 3.2.5 on 2021-07-29 14:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix_blog', '0007_alter_article_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='dislikes',
            field=models.ManyToManyField(related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
