# Generated by Django 3.1.1 on 2020-09-14 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200914_2156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievements',
            old_name='todo',
            new_name='task',
        ),
    ]
