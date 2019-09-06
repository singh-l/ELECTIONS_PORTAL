# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 06:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(blank=True, choices=[(1, 'Yes'), (-1, 'No')], null=True)),
                ('casted_at', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='post.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='VoteSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='vote',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.VoteSession'),
        ),
    ]