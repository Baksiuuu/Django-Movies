# Generated by Django 3.1.1 on 2020-09-12 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200912_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='age_category',
            field=models.IntegerField(blank=True, choices=[('kids', 'kids'), ('teens', 'teens'), ('adults', 'adults')], null=True),
        ),
    ]
