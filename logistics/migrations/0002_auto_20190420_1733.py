# Generated by Django 2.2 on 2019-04-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='condition',
            field=models.CharField(choices=[('WORKING', 'working'), ('MAINTENANCEUS', 'maintenanceus')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehical_type',
            field=models.CharField(choices=[('TRUCK', 'truck'), ('BUS', 'bus'), ('AIRPLANE', 'airplane')], max_length=100),
        ),
    ]
