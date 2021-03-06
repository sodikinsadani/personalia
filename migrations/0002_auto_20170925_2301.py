# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-25 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individu',
            name='alamat',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='individu',
            name='alamat_desa',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='individu',
            name='lulusan',
            field=models.CharField(blank=True, choices=[('1', 'SD'), ('2', 'SMP'), ('3', 'SMA'), ('4', 'D3'), ('5', 'S1'), ('6', 'S2'), ('7', 'S3')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='warga',
            name='segmentasi',
            field=models.CharField(blank=True, choices=[('m', 'Mahasiswa'), ('p', 'Pelajar'), ('u', 'Umum')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='warga',
            name='status_aktif',
            field=models.CharField(blank=True, choices=[('ak', 'AK'), ('pa', 'PA'), ('bk1', 'BK_1'), ('bk2', 'BK_2'), ('bk3', 'BK_3')], max_length=5, null=True),
        ),
    ]
