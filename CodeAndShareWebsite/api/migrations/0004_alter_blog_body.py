# Generated by Django 4.1.7 on 2023-03-21 22:32

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_photo_project_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
