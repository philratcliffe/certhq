from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Certificate

app_name = 'certificates'


class CertificateList(ListView):
    model = Certificate


class CertificateDetail(DetailView):
    model = Certificate
