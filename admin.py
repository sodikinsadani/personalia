from django.contrib import admin
from personalia.models import Pangkal, Individu, Warga

class PangkalAdmin(admin.ModelAdmin):
    list_display = ('id_pk','nama','rt',)

class IndividuAdmin(admin.ModelAdmin):
    list_display = ('id_individu','nama','tgl_lahir','tmpt_lahir','jk','alamat',
        'alamat_desa','alamat_kec','alamat_kabkot','alamat_prov','lulusan','hp',)

class WargaAdmin(admin.ModelAdmin):
    list_display = ('id_warga','individu','jenjang','tgl_daftar','status_aktif',
        'segmentasi','pangkal','warga_media','keterangan','tgl_input')

admin.site.register(Pangkal,PangkalAdmin)
admin.site.register(Individu,IndividuAdmin)
admin.site.register(Warga,WargaAdmin)
