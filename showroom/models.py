from django.db import models
from decimal import Decimal 

class Mobil(models.Model):
    merk = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    tahun = models.IntegerField()
    harga_dasar = models.DecimalField(max_digits=15, decimal_places=2)
    pinjaman_bank = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    suku_bunga = models.FloatField(null=True, blank=True)

    def total_biaya_service(self):
        return sum(service.biaya for service in self.service_set.all())

    def cicilan_bulanan(self, durasi_tahun=5):
        if self.pinjaman_bank and self.suku_bunga:
            total_pinjaman = self.pinjaman_bank + (self.pinjaman_bank * Decimal(str(self.suku_bunga)) / Decimal('100'))
            return round(total_pinjaman / (durasi_tahun * 12), 2)
        return 0

    def hpp(self):
        if self.pinjaman_bank and self.suku_bunga:
            try:
                bunga = Decimal(str(self.suku_bunga))
                produksi = self.harga_dasar / (self.pinjaman_bank + bunga)
            except (ZeroDivisionError, InvalidOperation):
                produksi = 0
        else:
            produksi = self.harga_dasar
        return round(produksi + self.total_biaya_service(), 2)

    def __str__(self):
        return f"{self.merk} {self.model} ({self.tahun})"

class Service(models.Model):
    mobil = models.ForeignKey(Mobil, on_delete=models.CASCADE)
    tanggal = models.DateField()
    deskripsi = models.TextField()
    biaya = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.mobil} - {self.tanggal}"
