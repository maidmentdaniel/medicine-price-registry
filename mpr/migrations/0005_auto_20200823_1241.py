# Generated by Django 2.2.15 on 2020-08-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpr', '0004_auto_20200823_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulary',
            name='last_updated',
            field=models.DateField(),
        ),
    ]
