# Generated by Django 3.2.15 on 2022-10-31 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0006_alter_sepet_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sepet',
            old_name='urun',
            new_name='makaleler',
        ),
    ]