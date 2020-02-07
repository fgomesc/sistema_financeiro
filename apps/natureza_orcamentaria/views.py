from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import NaturezaOrcamentaria


class NaturezaList(LoginRequiredMixin, ListView):
    model = NaturezaOrcamentaria


class NaturezaEdit(LoginRequiredMixin, UpdateView):
    model = NaturezaOrcamentaria
    fields = ['numero_natureza', 'nome_natureza', 'natureza_orcamento']


class NaturezaDelete(LoginRequiredMixin, DeleteView):
    model = NaturezaOrcamentaria
    success_url = reverse_lazy('list_natureza')

class NaturezaCreate(LoginRequiredMixin, CreateView):
    model = NaturezaOrcamentaria
    fields = ['numero_natureza', 'nome_natureza', 'natureza_orcamento']