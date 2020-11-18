# Generated by Django 3.1.3 on 2020-11-18 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedigree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Есімі')),
                ('level', models.IntegerField(verbose_name='Деңгей')),
                ('tag', models.CharField(blank=True, max_length=150, unique=True, verbose_name='Идентификатор')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Child', to='history.pedigree', verbose_name='Әкесі')),
            ],
        ),
    ]
