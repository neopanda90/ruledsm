# Generated by Django 3.1.4 on 2021-01-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qradardb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logsource', models.TextField()),
                ('sigma_name', models.TextField(blank=True)),
                ('dec', models.TextField(blank=True)),
                ('name', models.TextField(blank=True)),
                ('sigma_condition', models.TextField(blank=True)),
                ('qradar_condition', models.TextField(blank=True)),
                ('tactics', models.TextField(blank=True)),
                ('techinque', models.TextField(blank=True)),
            ],
        ),
    ]
