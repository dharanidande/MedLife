# Generated by Django 3.1 on 2020-08-31 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0028_auto_20200831_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='slug',
            field=models.SlugField(default='aeFoi.hClad.olg', unique=True),
        ),
    ]
