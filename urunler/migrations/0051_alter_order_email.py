# Generated by Django 3.2.15 on 2022-11-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0050_order_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
