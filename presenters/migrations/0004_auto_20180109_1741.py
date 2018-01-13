# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-09 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presenters', '0003_presenter_expertise'),
    ]

    operations = [
        migrations.AddField(
            model_name='presenter',
            name='github_handle',
            field=models.CharField(blank=True, help_text="Presenter's github handle", max_length=39, null=True),
        ),
        migrations.AddField(
            model_name='presenter',
            name='linkedin_handle',
            field=models.CharField(blank=True, help_text="Presenter's linkedin handle", max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='presenter',
            name='twitter_handle',
            field=models.CharField(blank=True, help_text="Presenter's twitter handle", max_length=15, null=True),
        ),
    ]