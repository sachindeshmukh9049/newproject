# Generated by Django 3.1.4 on 2020-12-12 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JsonToken', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='class_name',
        ),
    ]
