# Generated by Django 4.1 on 2022-08-17 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0035_alter_etender_organization_established_year_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etender',
            name='Organization_size',
        ),
    ]
