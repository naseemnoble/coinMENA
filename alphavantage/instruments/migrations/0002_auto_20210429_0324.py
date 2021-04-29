# Generated by Django 2.2.20 on 2021-04-29 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricerequest',
            name='interval_min',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='pricerequest',
            name='from_currency',
            field=models.CharField(default='BTC', max_length=200),
        ),
        migrations.AlterField(
            model_name='pricerequest',
            name='is_requested',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pricerequest',
            name='to_currency',
            field=models.CharField(default='USD', max_length=200),
        ),
    ]
