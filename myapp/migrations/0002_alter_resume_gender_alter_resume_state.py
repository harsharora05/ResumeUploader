# Generated by Django 4.1.4 on 2023-05-04 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='resume',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
