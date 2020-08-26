# Generated by Django 2.2.15 on 2020-08-22 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('unit', models.CharField(max_length=20)),
            ],
            options={
                'unique_together': {('name', 'unit')},
            },
        ),
        migrations.CreateModel(
            name='LastUpdated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nappi_code', models.CharField(max_length=20)),
                ('regno', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('schedule', models.CharField(max_length=22, null=True)),
                ('dosage_form', models.CharField(max_length=20, null=True)),
                ('pack_size', models.FloatField()),
                ('num_packs', models.IntegerField()),
                ('sep', models.FloatField()),
                ('is_generic', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.CharField(max_length=20)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mpr.Ingredient')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_ingredients', to='mpr.Product')),
            ],
            options={
                'unique_together': {('product', 'ingredient', 'strength')},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(through='mpr.ProductIngredient', to='mpr.Ingredient'),
        ),
        migrations.CreateModel(
            name='FormularyProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('formulary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='mpr.Formulary')),
            ],
        ),
    ]