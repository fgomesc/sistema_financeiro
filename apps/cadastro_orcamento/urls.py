from django.urls import path
from .views import CadastroOrcamentoList, CadastroOrcamentoEdit, CadastroOrcamentoDelete, CadastroOrcamentoCreate

urlpatterns = [
    path('', CadastroOrcamentoList.as_view(), name='list_cadastro_orcamento'),
    path('editar/<int:pk>/', CadastroOrcamentoEdit.as_view(), name='edit_cadastro_orcamento'),
    path('delete/<int:pk>/', CadastroOrcamentoDelete.as_view(), name='delete_cadastro_orcamento'),
    path('novo/', CadastroOrcamentoCreate.as_view(), name='create_cadastro_orcamento'),
]