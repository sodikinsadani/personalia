from personalia.forms import fIndividu
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

def tambahdata(request):
    template_name = 'personalia/tambahdata.html'
    form = (fIndividu,)

    if request.method == 'POST':
        cekform = fIndividu(request.POST)
        if cekform.is_valid():
            individu = cekform.save()
            messages.add_message(request, messages.SUCCESS, 'Berhasil menambahkan {0} ke dalam data member'.format(individu.nama,))
            return HttpResponseRedirect(reverse('personalia:tambahdata'))
        else :
            form = (cekform,)
            individu = cekform.clean()
            messages.add_message(request, messages.WARNING, 'Gagal menambahkan {0} ke dalam data member'.format(individu['nama'],))

    return render(request,template_name,{'form':form,})
