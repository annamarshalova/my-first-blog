# Generated by Django 3.1.3 on 2020-11-30 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201130_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_file',
        ),
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.URLField(null=True),
        ),
    ]