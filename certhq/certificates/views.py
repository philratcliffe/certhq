from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Certificate

app_name = 'certificates'


class CertificateList(ListView):
    model = Certificate
