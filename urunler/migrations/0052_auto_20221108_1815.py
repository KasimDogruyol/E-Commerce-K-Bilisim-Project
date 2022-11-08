# Generated by Django 3.2.15 on 2022-11-08 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0051_alter_order_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sepet',
            name='adet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='sepet',
            name='urunler',
        ),
        migrations.AddField(
            model_name='sepet',
            name='urunler',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='urunler.urun'),
        ),
    ]
