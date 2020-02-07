from django.urls import path
from .views import PermissaoList, PermissaoEdit, PermissaoDelete, PermissaoCreate

urlpatterns = [
    path('', PermissaoList.as_view(), name='list_permissao'),
    path('editar/<int:pk>/', PermissaoEdit.as_view(), name='edit_permissao'),
    path('delete/<int:pk>/', PermissaoDelete.as_view(), name='delete_permissao'),
    path('novo/', PermissaoCreate.as_view(), name='create_permissao'),
]