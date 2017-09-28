# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.formsets import BaseFormSet, formset_factory
from personalia.models import Individu,Warga


class fIndividu(forms.ModelForm):
    class Meta:
        model = Individu
        fields = '__all__'
        widgets = {
            'alamat':forms.Textarea(attrs={'rows':2,}),
        }

    def __init__(self, *args, **kwargs):
        super(fIndividu, self).__init__(*args, **kwargs)
        # add common css classes to all widgets
        for field in iter(self.fields):
            #get current classes from Meta
            classes = self.fields[field].widget.attrs.get("class")
            if classes is not None:
                classes = classes
            else:
                classes = "form-control"
            self.fields[field].widget.attrs.update({
                'class': classes
            })

        dict_ph = {'tgl_lahir':'tanggal lahir','alamat_desa':'desa','alamat_kec':'kecamatan','alamat_kabkot':'kota/kabupaten',
            'alamat_prov':'provinsi','hp':'nomor handphone','tmpt_lahir':'tempat lahir'
        }

        for field in iter(self.fields):
            #get current classes from Meta
            placeholder = self.fields[field].widget.attrs.get("placeholder")
            if placeholder is not None:
                placeholder = placeholder
            elif dict_ph.has_key(field):
                placeholder = dict_ph[field]
            else:
                placeholder = field
            self.fields[field].widget.attrs.update({
                'placeholder': placeholder
            })

class fWarga(forms.ModelForm):
    class Meta:
        model = Warga
        exclude = ['individu','tgl_input','id_warga']
        widgets = {
            'keterangan':forms.Textarea(attrs={'rows':3,}),
        }

    def __init__(self, *args, **kwargs):
        super(fWarga, self).__init__(*args, **kwargs)
        # add common css classes to all widgets
        for field in iter(self.fields):
            #get current classes from Meta
            classes = self.fields[field].widget.attrs.get("class")
            if classes is not None:
                classes = classes
            else:
                classes = "form-control"
            self.fields[field].widget.attrs.update({
                'class': classes
            })

        dict_ph = {'tgl_daftar':'Tanggal Daftar',}

        for field in iter(self.fields):
            #get current classes from Meta
            placeholder = self.fields[field].widget.attrs.get("placeholder")
            if placeholder is not None:
                placeholder = placeholder
            elif dict_ph.has_key(field):
                placeholder = dict_ph[field]
            else:
                placeholder = field
            self.fields[field].widget.attrs.update({
                'placeholder': placeholder
            })
