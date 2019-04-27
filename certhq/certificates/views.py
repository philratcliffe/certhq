from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Certificate

app_name = 'certificates'


class CertificateList(LoginRequiredMixin, ListView):
    model = Certificate


class CertificateDetail(LoginRequiredMixin, DetailView):
    model = Certificate
