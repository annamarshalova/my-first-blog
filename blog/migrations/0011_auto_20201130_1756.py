# Generated by Django 3.1.3 on 2020-11-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_shorttext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='shorttext',
            field=models.TextField(default='', max_length=200),
        ),
    ]
