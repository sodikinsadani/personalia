from django.conf.urls import url
from . import views

app_name = 'personalia'
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^warga/$',views.warga, name='warga'),
    url(r'^tambahanggota/$',views.tambahWarga, name='tambahWarga'),
    url(r'^laporan/$',views.index, name='laporan'),
    url(r'^pengurus/$',views.index, name='pengurus'),
    url(r'^tambahAdmin/$',views.index, name='tambahAdmin'),
    url(r'^tambahdata/$',views.tambahdata, name='tambahdata',),
]
