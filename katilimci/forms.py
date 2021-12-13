from django import forms
from .models import Toplanti_Konusu

class ToplantiForm(forms.ModelForm):

    class Meta:
        model=Toplanti_Konusu
        fields=('t_konu','t_tarih','t_bassaat','t_bitsaat','t_katilimcilar')
        labels={
            't_konu':'Toplantı Konusu',
            't_tarih':'Tarih',
            't_bassaat':'Başlangıç Saati',
            't_bitsaat':'Bitiş Saati',
            't_katilimcilar':'Katılımcılar'
            }