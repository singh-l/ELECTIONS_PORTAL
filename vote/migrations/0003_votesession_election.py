# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 04:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0001_initial'),
        ('vote', '0002_auto_20160213_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='votesession',
            name='election',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vote_sessions', to='election.Election'),
        ),
    ]
