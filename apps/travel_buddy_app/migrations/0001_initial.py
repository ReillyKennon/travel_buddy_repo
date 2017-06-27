# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 16:54
from __future__ import unicode_literals

import apps.travel_buddy_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[apps.travel_buddy_app.models.validate_name])),
                ('last_name', models.CharField(max_length=30, validators=[apps.travel_buddy_app.models.validate_name])),
                ('email', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=1000, validators=[apps.travel_buddy_app.models.validate_password])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
