# Generated by Django 2.2.20 on 2021-04-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0003_exchangerate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricerequest',
            name='interval_min',
            field=models.IntegerField(default=60),
        ),
    ]