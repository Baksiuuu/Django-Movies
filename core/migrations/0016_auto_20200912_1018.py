# Generated by Django 3.1.1 on 2020-09-12 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200906_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='age_limit',
        ),
        migrations.AddField(
            model_name='genre',
            name='age_category',
            field=models.IntegerField(blank=True, choices=[(0, 'kids'), (1, 'teens'), (2, 'adults')], null=True),
        ),
    ]
