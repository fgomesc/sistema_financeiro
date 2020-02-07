from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Permissao


class PermissaoList(LoginRequiredMixin, ListView):
    model = Permissao

class PermissaoEdit(LoginRequiredMixin, UpdateView):
    model = Permissao
    fields = ['tipo_permissao']

class PermissaoDelete(LoginRequiredMixin, DeleteView):
    model = Permissao
    success_url = reverse_lazy('list_permissao')


class PermissaoCreate(LoginRequiredMixin, CreateView):
    model = Permissao
    fields = ['tipo_permissao']