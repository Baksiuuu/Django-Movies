# Generated by Django 3.1.1 on 2020-09-12 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20200912_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='age_category',
            field=models.IntegerField(blank=True, choices=[(0, 'kids'), (1, 'teens'), (2, 'adults')], null=True),
        ),
    ]