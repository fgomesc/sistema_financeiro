from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.cadastro_orcamento.models import CadastroOrcamento
from .forms import CadastroOrcamentoForm


class CadastroOrcamentoList(LoginRequiredMixin, ListView):
    model = CadastroOrcamento
    fields = ['cc_cadastro_orcamento', 'no_cadastro_orcamento', 'valor_cadastro_orcamento', 'data_cadastro_orcamento', 'obs_cadastro_orcamento']


class CadastroOrcamentoEdit(LoginRequiredMixin, UpdateView):
    model = CadastroOrcamento


class CadastroOrcamentoDelete(LoginRequiredMixin, DeleteView):
    model = CadastroOrcamento
    success_url = reverse_lazy('list_cadastro_orcamento')

class CadastroOrcamentoCreate(LoginRequiredMixin, CreateView):
    model = CadastroOrcamento
    fields = ['cc_cadastro_orcamento', 'no_cadastro_orcamento', 'valor_cadastro_orcamento', 'data_cadastro_orcamento', 'obs_cadastro_orcamento']

