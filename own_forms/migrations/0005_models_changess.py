# Generated by Django 4.1.6 on 2023-02-17 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('own_forms', '0004_models_changesss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filledforms',
            name='email',
        ),
        migrations.RemoveField(
            model_name='filledforms',
            name='fullname',
        ),
    ]