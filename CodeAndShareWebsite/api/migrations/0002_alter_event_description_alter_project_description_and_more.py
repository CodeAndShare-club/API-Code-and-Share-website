# Generated by Django 4.1.7 on 2023-03-19 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
