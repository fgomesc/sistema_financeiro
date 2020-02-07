from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

class ClienteEdit(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nome_cliente', 'centro_de_custo_cliente', 'user_cliente']

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('list_cliente')

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nome_cliente', 'centro_de_custo_cliente', 'user_cliente']