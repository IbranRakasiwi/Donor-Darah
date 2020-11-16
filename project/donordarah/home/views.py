from django.shortcuts import render
from django.contrib.auth import get_user_model
# from . import models

def index(req):
    group = req.user.groups.first()
    if group is not None and group.name == 'admin':
        return render(req, 'admin/index.html')
    else:
        return render(req, 'user/index.html')

def daftar(req):
    if req.POST:
        models.Pasien.objects.create(
        no_pasien=req.POST['no_pasien'],
        nama_pasien=req.POST['nama_pasien'],
        jenis_kelamin=req.POST['jenis_kelamin'],
        alamat_pasien=req.POST['alamat_pasien'],
        no_hp=req.POST['no_hp'],)
        return redirect('list-darah')
    task = models.Pasien.objects.all()
    return render(req, 'home/daftar.html')