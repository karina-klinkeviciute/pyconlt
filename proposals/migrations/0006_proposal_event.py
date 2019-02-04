# Generated by Django 2.1.5 on 2019-02-03 15:03

import conference.models.event
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0002_auto_20190127_1854'),
        ('proposals', '0005_auto_20180117_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='event',
            field=models.ForeignKey(blank=True, default=conference.models.event.get_current_event, help_text='Event to which this belongs. e.g. PyCon 2018.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='conference.Event'),
        ),
    ]