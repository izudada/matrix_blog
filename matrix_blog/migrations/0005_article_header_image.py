# Generated by Django 3.2.5 on 2021-07-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix_blog', '0004_alter_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='header_image',
            field=models.ImageField(default='dummy.png', upload_to='images'),
        ),
    ]