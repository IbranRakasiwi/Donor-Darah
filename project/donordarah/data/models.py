from django.db import models

class Data(models.Model):
    no_pasien = models.CharField(max_length =10, null=True,blank=False)
    nama_pasien = models.CharField(max_length=240, null=True,blank=False)
    jenis_kelamin = models.CharField(max_length=6, null=True,blank=False)
    alamat_pasien = models.CharField(max_length=100, null=True,blank=False)
    no_hp = models.IntegerField(null=True,blank=False)

    def __str__(self):
        return self.jenis_kelamin