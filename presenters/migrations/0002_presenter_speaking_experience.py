# Generated by Django 2.1.5 on 2019-02-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presenters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presenter',
            name='speaking_experience',
            field=models.CharField(blank=True, help_text='Short description about your public speaking experience', max_length=1024, null=True, verbose_name='Public speaking experience'),
        ),
    ]
