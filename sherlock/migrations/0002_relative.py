# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 15:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sherlock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('relationship', models.CharField(blank=True, max_length=30)),
                ('birth_year', models.IntegerField(null=True)),
                ('unique_id', models.CharField(blank=True, max_length=100)),
                ('location', models.TextField(blank=True)),
                ('family_surnames', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
