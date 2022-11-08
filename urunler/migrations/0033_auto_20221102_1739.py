# Generated by Django 3.2.15 on 2022-11-02 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0032_auto_20221102_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategori',
            name='resim',
        ),
        migrations.RemoveField(
            model_name='kategori',
            name='resim2',
        ),
        migrations.CreateModel(
            name='KategoriFotograflari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.FileField(upload_to='images/kategoriler')),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urunler.kategori')),
            ],
        ),
    ]
