from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Perfil


class PerfilList(LoginRequiredMixin, ListView):
    model = Perfil


class PerfilEdit(LoginRequiredMixin, UpdateView):
    model = Perfil
    fields = ['tipo_perfil']


class PerfilDelete(LoginRequiredMixin, DeleteView):
    model = Perfil
    success_url = reverse_lazy('list_perfil')


class PerfilCreate(LoginRequiredMixin, CreateView):
    model = Perfil
    fields = ['tipo_perfil']