from django.shortcuts import render
from . import models

def base(req):
    # task = models.Pasien.objects.all()
    return render(req, 'login/base.html')



