# Generated by Django 4.1.6 on 2023-02-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('own_forms', '0005_models_changess'),
    ]

    operations = [
        migrations.AddField(
            model_name='filledforms',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='filledforms',
            name='fullname',
            field=models.CharField(max_length=250, null=True),
        ),
    ]