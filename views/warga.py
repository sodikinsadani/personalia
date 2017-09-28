from __future__ import unicode_literals

from django.shortcuts import render
from personalia.forms import fIndividu,fWarga
from django.db import transaction,IntegrityError
from django.http import HttpResponseRedirect

def tambahWarga(request):
    template_name = 'personalia/tambahWarga.html'
    form = (fIndividu,fWarga)
    msg = None#'Silahkan input data warga'

    if request.method == 'POST':
        cekform1 = fIndividu(request.POST)
        err_list = []
        if not cekform1.is_valid():
            errList = cekform1.errors.as_data().values()
            for e in errList :
                err_list.append(str(e[0]))

        cekform2 = fWarga(request.POST)
        if not cekform2.is_valid():
            errList = cekform1.errors.as_data().values()
            for e in errList :
                err_list.append(str(e[0]))

        if cekform1.is_valid() and cekform2.is_valid():
            with transaction.atomic():
                individu = cekform1.save()
                id_warga = str(individu.id_individu)
                id_warga = id_warga.zfill(10)
                warga = cekform2.save(commit=False)
                warga.individu = individu
                warga.id_warga = id_warga
                warga.save()
                #msg = 'Berhasil menambah data warga. Silahkan input kembali'
                return HttpResponseRedirect("/personalia/tambahWarga/")
        else :
            #raise Exception, cekform1.errors.as_data()['__all__'][0]
            #raise Exception, cekform1.errors.as_json()
            #raise Exception, str(cekform1.errors.as_data().values()[0][0])
            #raise Exception, cekform1.errors.as_data().values()
            form = (cekform1,cekform2)
            msg = '''Ada kesalahan dalam pengisian form. {0}'''.format(err_list)
            #raise Exception, 'form invalid'

    return render(request,template_name,{'form':form,'msg':msg})
