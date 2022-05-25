# Generated by Django 4.0.4 on 2022-05-23 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosticCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(default='default_center.jpg', upload_to='diagnostic_center_pics')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('contact_no', models.CharField(max_length=20)),
                ('website', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Diagnostic Centers',
            },
        ),
        migrations.CreateModel(
            name='DiagnosticStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=100, unique=True)),
                ('admin', models.BooleanField(default=False)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='center_staffs', to='diagnostic.diagnosticcenter')),
            ],
            options={
                'verbose_name_plural': 'Diagnostic Staffs',
            },
        ),
        migrations.CreateModel(
            name='DiagnosticAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=100, unique=True)),
                ('admin', models.BooleanField(default=True)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='center_admins', to='diagnostic.diagnosticcenter')),
                ('staff', models.ManyToManyField(to='diagnostic.diagnosticstaff')),
            ],
            options={
                'verbose_name_plural': 'Diagnostic Admins',
            },
        ),
    ]
