# Generated by Django 3.1.1 on 2020-09-14 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievements',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='todo',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
