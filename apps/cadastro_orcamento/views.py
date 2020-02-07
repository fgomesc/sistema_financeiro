from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.cadastro_orcamento.models import CadastroOrcamento
from .forms import CadastroOrcamentoForm


class CadastroOrcamentoList(LoginRequiredMixin, ListView):
    model = CadastroOrcamento


class CadastroOrcamentoEdit(LoginRequiredMixin, UpdateView):
    model = CadastroOrcamento
    form_class = CadastroOrcamentoForm

    def get_form_kwargs(self):
        kwargs = super(CadastroOrcamentoEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class CadastroOrcamentoDelete(LoginRequiredMixin, DeleteView):
    model = CadastroOrcamento
    success_url = reverse_lazy('list_cadastro_orcamento')

class CadastroOrcamentoCreate(LoginRequiredMixin, CreateView):
    model = CadastroOrcamento
    form_class = CadastroOrcamentoForm

    def get_form_kwargs(self):
        kwargs = super(CadastroOrcamentoCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs