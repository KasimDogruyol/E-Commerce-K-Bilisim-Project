# Generated by Django 3.2.15 on 2022-11-10 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0053_sepet_fiyat'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sepet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='urunler.sepet'),
        ),
    ]
