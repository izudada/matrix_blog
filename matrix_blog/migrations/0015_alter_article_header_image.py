# Generated by Django 3.2.5 on 2021-07-29 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix_blog', '0014_alter_article_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='header_image',
            field=models.ImageField(default='images/dummy.png', upload_to=''),
        ),
    ]
