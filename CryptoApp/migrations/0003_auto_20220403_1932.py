# Generated by Django 3.1.6 on 2022-04-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CryptoApp', '0002_auto_20220403_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='quantity',
            field=models.FloatField(default=1),
        ),
    ]
