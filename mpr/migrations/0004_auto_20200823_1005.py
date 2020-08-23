# Generated by Django 2.2.15 on 2020-08-23 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mpr', '0003_formulary_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularyproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formularyproducts', to='mpr.Product'),
        ),
        migrations.AlterUniqueTogether(
            name='formularyproduct',
            unique_together={('formulary', 'product')},
        ),
    ]
