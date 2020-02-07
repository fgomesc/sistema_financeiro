from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Usuario




class UsuarioList(LoginRequiredMixin, ListView):
    model = Usuario

class UsuarioEdit(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['primeiro_nome', 'ultimo_nome', 'email', 'centrodecusto_usuario', 'perfil_usuario', 'permissao_usuario']

class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('list_usuario')

class UsuarioCreate(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ['primeiro_nome', 'ultimo_nome', 'email', 'centrodecusto_usuario', 'perfil_usuario','permissao_usuario']


    def form_valid(self, form):
        usuario = form.save(commit=False)
        username = usuario.primeiro_nome.lower() + usuario.ultimo_nome.lower()
        usuario.user = User.objects.create(username=username)
        usuario.save()
        return super(UsuarioCreate, self).form_valid(form)