# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 16:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField(max_length=255)),
                ('birthdate', models.DateField()),
                ('city_of_birth', models.CharField(blank=True, max_length=255)),
                ('state_of_birth', models.CharField(blank=True, max_length=150)),
                ('country_of_birth', models.CharField(blank=True, max_length=255)),
                ('sex_at_birth', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('eye_color', models.CharField(choices=[('blk', 'BLACK'), ('blu', 'BLUE'), ('bro', 'BROWN'), ('gry', 'GRAY'), ('grn', 'GREEN'), ('hzl', 'HAZEL'), ('oth', 'OTHER')], max_length=3)),
                ('mother_first_name', models.CharField(blank=True, max_length=150)),
                ('mother_maiden_name', models.CharField(blank=True, max_length=150)),
                ('mother_last_name', models.CharField(blank=True, max_length=150)),
                ('father_first_name', models.CharField(blank=True, max_length=150)),
                ('father_last_name', models.CharField(blank=True, max_length=150)),
                ('birth_hospital', models.CharField(blank=True, max_length=150)),
                ('searching_for', models.CharField(choices=[('csn', 'COUSIN'), ('cld', 'CHILD'), ('prt', 'PARENT'), ('sbl', 'SIBLING')], max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(default='picture.png', upload_to='')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, max_length=25)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
