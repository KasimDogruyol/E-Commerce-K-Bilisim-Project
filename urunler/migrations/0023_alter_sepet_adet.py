# Generated by Django 3.2.15 on 2022-11-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0022_auto_20221101_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sepet',
            name='adet',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
