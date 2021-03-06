# Generated by Django 3.1.1 on 2020-09-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='director',
            unique_together={('first_name', 'last_name')},
        ),
    ]
