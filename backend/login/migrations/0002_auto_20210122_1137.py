# Generated by Django 3.1.5 on 2021-01-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
