# Generated by Django 2.1.2 on 2018-10-06 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0003_auto_20181005_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='foosball_points',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='tt_points',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
