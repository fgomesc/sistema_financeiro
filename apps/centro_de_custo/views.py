from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import CentroDeCusto


class CentrodecustoList(LoginRequiredMixin, ListView):
    model = CentroDeCusto


class CentrodecustoEdit(LoginRequiredMixin, UpdateView):
    model = CentroDeCusto
    fields = ['numero_centro', 'nome_centro', 'centro_de_custo','user_respon', 'vinculo_natureza']

class CentrodecustoCreate(LoginRequiredMixin, CreateView):
    model = CentroDeCusto
    fields = ['numero_centro', 'nome_centro', 'centro_de_custo', 'user_respon', 'vinculo_natureza']

class CentrodecustoDelete(LoginRequiredMixin, DeleteView):
    model = CentroDeCusto
    success_url = reverse_lazy('list_centrodecusto')



