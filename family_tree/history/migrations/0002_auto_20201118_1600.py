# Generated by Django 3.1.3 on 2020-11-18 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedigree',
            old_name='tag',
            new_name='slug',
        ),
    ]