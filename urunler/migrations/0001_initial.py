# Generated by Django 3.2.15 on 2022-10-30 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SeriNo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urun_adi', models.CharField(blank=True, max_length=100, null=True)),
                ('urun_aciklama', models.CharField(blank=True, max_length=100, null=True)),
                ('urun_fiyat', models.IntegerField(blank=True, null=True)),
                ('urun_ekipman', models.CharField(blank=True, max_length=100, null=True)),
                ('urun_marka', models.CharField(blank=True, max_length=100, null=True)),
                ('resim', models.FileField(blank=True, null=True, upload_to='urunler/')),
                ('urun_firma', models.CharField(blank=True, max_length=100, null=True)),
                ('kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='urunler.kategori')),
                ('no', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='urunler.serino')),
                ('subcategories', models.ManyToManyField(null=True, to='urunler.Subcategory')),
            ],
        ),
    ]