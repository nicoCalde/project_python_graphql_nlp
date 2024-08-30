# Generated by Django 4.2 on 2024-08-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('engine_fuel_type', models.CharField(blank=True, max_length=100, null=True)),
                ('engine_hp', models.FloatField(blank=True, null=True)),
                ('engine_cylinders', models.FloatField(blank=True, null=True)),
                ('transmission_type', models.CharField(blank=True, max_length=100, null=True)),
                ('driven_wheels', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_doors', models.FloatField(blank=True, null=True)),
                ('market_category', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_size', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_style', models.CharField(blank=True, max_length=100, null=True)),
                ('highway_mpg', models.IntegerField(blank=True, null=True)),
                ('city_mpg', models.IntegerField(blank=True, null=True)),
                ('popularity', models.IntegerField(blank=True, null=True)),
                ('msrp', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
