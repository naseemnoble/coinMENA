# Generated by Django 2.2.20 on 2021-04-29 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=200)),
                ('from_currency', models.CharField(max_length=200)),
                ('to_currency', models.CharField(max_length=200)),
                ('is_requested', models.BooleanField()),
            ],
        ),
    ]
