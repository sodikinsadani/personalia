from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Individu(models.Model):
    PILIH_JK = [
        ('L','Laki-laki'),('P','Perempuan'),
    ]
    PILIH_LULUSAN = [
        ('1','SD'),('2','SMP'),('3','SMA'),('4','D3'),('5','S1'),('6','S2'),('7','S3'),
    ]

    id_individu = models.AutoField(primary_key=True)
    nama = models.CharField('nama lengkap',max_length=50)
    #nama = models.CharField(max_length=50,blank=True,null=True)
    tmpt_lahir = models.CharField(max_length=50,blank=True,null=True)
    tgl_lahir = models.DateField(blank=True,null=True)
    jk = models.CharField(max_length=1,choices=PILIH_JK)
    #jk = models.CharField(max_length=1,choices=PILIH_JK,blank=True,null=True)
    #alamat = models.TextField(max_length=200)
    alamat = models.TextField(max_length=200,blank=True,null=True)
    alamat_desa = models.CharField(max_length=50,blank=True,null=True)
    #alamat_desa = models.CharField(max_length=50)
    alamat_kec = models.CharField(max_length=50)
    alamat_kabkot = models.CharField(max_length=50)
    alamat_prov = models.CharField(max_length=50)
    #lulusan = models.CharField(max_length=3,choices=PILIH_LULUSAN)
    lulusan = models.CharField(max_length=3,choices=PILIH_LULUSAN,blank=True,null=True)
    hp = models.CharField(max_length=15,blank=True,null=True)

    class Meta:
        ordering = ('jk','id_individu','nama',)
        unique_together = ('nama','jk','lulusan')

    def __str__(self):
        return self.nama

class Pangkal(models.Model):
    PILIH_RT = [
        ('ahm','ahmad'),('ksm','kusmawan'),('mgd','migud'),
        ('sdk','sodikin'),('sdr','sodirun'),
    ]

    id_pk = models.CharField(max_length=5,primary_key=True,)
    nama = models.CharField(max_length=50)
    rt = models.CharField(max_length=5,choices=PILIH_RT)

    class Meta:
        ordering = ('rt','id_pk',)

    def __str__(self):
        return self.nama

class Warga(models.Model):
    PILIH_JEN = [
        ('0','WB'),('1','Pra A1'),('2','A1'),('3','A2')
    ]

    PILIH_SA = [
        ('ak','AK'),('pa','PA'),('bk1','BK_1'),('bk2','BK_2'),('bk3','BK_3')
    ]
    PILIH_SEG = [
        ('m','Mahasiswa'),('p','Pelajar'),('u','Umum')
    ]

    id_warga = models.CharField(max_length=10,primary_key=True)
    individu = models.OneToOneField(
        Individu,
        on_delete=models.CASCADE,
    )
    '''jenjang = models.CharField(max_length=1,
        choices=PILIH_JEN)'''
    jenjang = models.CharField(max_length=1,
        choices=PILIH_JEN,blank=True,null=True)
    tgl_daftar = models.DateField(blank=True,null=True)
    #status_aktif = models.CharField(max_length=5,choices=PILIH_SA)
    status_aktif = models.CharField(max_length=5,choices=PILIH_SA,blank=True,null=True)
    #segmentasi = models.CharField(max_length=1,choices=PILIH_SEG)
    segmentasi = models.CharField(max_length=1,choices=PILIH_SEG,blank=True,null=True)
    pangkal = models.ForeignKey(Pangkal, related_name='PangkalDari')
    #pangkal = models.ForeignKey(Pangkal, related_name='PangkalDari',blank=True,null=True)
    warga_media = models.BooleanField(default=False)
    keterangan = models.TextField(max_length=500,blank=True,null=True)
    #tgl_input = models.DateTimeField(default=timezone.now)
    tgl_input = models.DateTimeField(blank=True,null=True)

    class Meta:
        ordering = ('status_aktif','jenjang','id_warga',)

    def __str__(self): # __unicode__ on Python 2
        return '{}'.format(self.individu)
