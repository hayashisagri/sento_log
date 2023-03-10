# Generated by Django 3.2.7 on 2023-01-22 05:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '市町村',
                'db_table': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Sento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='銭湯名')),
                ('description', models.TextField(verbose_name='紹介文')),
                ('address', models.CharField(max_length=255, verbose_name='住所')),
                ('time_open', models.CharField(blank=True, max_length=255, verbose_name='営業時間')),
                ('day_close', models.CharField(blank=True, max_length=255, verbose_name='定休日')),
                ('profile_image', models.ImageField(blank=True, upload_to='', verbose_name='画像')),
                ('station_distance', models.CharField(blank=True, max_length=255, verbose_name='アクセス')),
                ('homepage_url', models.CharField(blank=True, max_length=255, verbose_name='施設URL')),
                ('point', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326, verbose_name='所在地緯度経度')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='sento.area', verbose_name='市区町村')),
            ],
            options={
                'verbose_name': '銭湯',
                'db_table': 'sentos',
            },
        ),
    ]
