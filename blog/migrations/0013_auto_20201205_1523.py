# Generated by Django 3.1.3 on 2020-12-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(default='static/images/maxresdefault.jpg', null=True),
        ),
    ]