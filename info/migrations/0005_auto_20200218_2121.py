# Generated by Django 3.0.3 on 2020-02-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20200218_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='col_id',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
    ]
