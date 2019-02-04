# Generated by Django 2.1.5 on 2019-02-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0002_auto_20190204_1956'),
        ('presenters', '0009_auto_20180211_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='presenter',
            name='event',
            field=models.ManyToManyField(blank=True, help_text='Event to which this belongs. e.g. PyCon 2018.', null=True, to='conference.Event'),
        ),
    ]
