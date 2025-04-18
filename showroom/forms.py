from django import forms
from .models import Mobil, Service
from django.forms.widgets import DateInput

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
        widgets = {
            'tanggal': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),
            'biaya': forms.NumberInput(attrs={'class': 'form-control'}),
            'mobil': forms.Select(attrs={'class': 'form-control'}),
        }
