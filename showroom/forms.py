from django import forms
from .models import Mobil, Service

class MobilForm(forms.ModelForm):
    class Meta:
        model = Mobil
        fields = '__all__'
    def clean_tahun(self):
        tahun = self.cleaned_data.get('tahun')
        if tahun < 1900 or tahun > 2100:
            raise forms.ValidationError("Tahun tidak valid.")
        return tahun

    def clean_harga_dasar(self):
        harga = self.cleaned_data.get('harga_dasar')
        if harga < 0:
            raise forms.ValidationError("Harga dasar tidak boleh negatif.")
        return harga
    

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
