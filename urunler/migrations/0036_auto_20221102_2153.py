# Generated by Django 3.2.15 on 2022-11-02 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0035_alter_kategori_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='adet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kategori',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='images/kategoriler'),
        ),
    ]