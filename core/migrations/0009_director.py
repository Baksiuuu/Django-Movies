# Generated by Django 3.1.1 on 2020-09-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200906_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
    ]
