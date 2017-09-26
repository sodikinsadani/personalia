# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-25 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individu',
            fields=[
                ('id_individu', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=50)),
                ('tmpt_lahir', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_lahir', models.DateField(blank=True, null=True)),
                ('jk', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=1)),
                ('alamat', models.TextField(max_length=200)),
                ('alamat_desa', models.CharField(max_length=50)),
                ('alamat_kec', models.CharField(max_length=50)),
                ('alamat_kabkot', models.CharField(max_length=50)),
                ('alamat_prov', models.CharField(max_length=50)),
                ('lulusan', models.CharField(choices=[('1', 'SD'), ('2', 'SMP'), ('3', 'SMA'), ('4', 'D3'), ('5', 'S1'), ('6', 'S2'), ('7', 'S3')], max_length=3)),
                ('hp', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'ordering': ('jk', 'id_individu', 'nama'),
            },
        ),
        migrations.CreateModel(
            name='Pangkal',
            fields=[
                ('id_pk', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=50)),
                ('rt', models.CharField(choices=[('ahm', 'ahmad'), ('ksm', 'kusmawan'), ('mgd', 'migud'), ('sdk', 'sodikin'), ('sdr', 'sodirun')], max_length=5)),
            ],
            options={
                'ordering': ('rt', 'id_pk'),
            },
        ),
        migrations.CreateModel(
            name='Warga',
            fields=[
                ('id_warga', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('jenjang', models.CharField(blank=True, choices=[('0', 'WB'), ('1', 'Pra A1'), ('2', 'A1'), ('3', 'A2')], max_length=1, null=True)),
                ('tgl_daftar', models.DateField(blank=True, null=True)),
                ('status_aktif', models.CharField(choices=[('ak', 'AK'), ('pa', 'PA'), ('bk1', 'BK_1'), ('bk2', 'BK_2'), ('bk3', 'BK_3')], max_length=5)),
                ('segmentasi', models.CharField(choices=[('m', 'Mahasiswa'), ('p', 'Pelajar'), ('u', 'Umum')], max_length=1)),
                ('warga_media', models.BooleanField(default=False)),
                ('keterangan', models.TextField(blank=True, max_length=500, null=True)),
                ('tgl_input', models.DateTimeField(default=django.utils.timezone.now)),
                ('individu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personalia.Individu')),
                ('pangkal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PangkalDari', to='personalia.Pangkal')),
            ],
            options={
                'ordering': ('status_aktif', 'jenjang', 'id_warga'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='individu',
            unique_together=set([('nama', 'jk', 'lulusan')]),
        ),
    ]