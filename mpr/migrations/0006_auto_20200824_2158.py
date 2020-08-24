# Generated by Django 2.2.15 on 2020-08-24 19:58

from django.db import migrations
from django.contrib.sites.models import Site

def install_site(apps, schema_editor):
    site = Site.objects.first()

    site.domain = "medicineprices.org.za"
    site.name = "Medicine Prices"
    site.save()

class Migration(migrations.Migration):

    dependencies = [
        ('mpr', '0005_auto_20200823_1241'),
    ]

    operations = [
        migrations.RunPython(install_site)
    ]
