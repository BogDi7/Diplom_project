# Generated by Django 4.0.4 on 2022-05-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]