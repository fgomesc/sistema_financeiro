from django.urls import path
from .views import UsuarioList, UsuarioEdit, UsuarioDelete, UsuarioCreate

urlpatterns = [
    path('', UsuarioList.as_view(), name='list_usuario'),
    path('editar/<int:pk>/', UsuarioEdit.as_view(), name='edit_usuario'),
    path('delete/<int:pk>/', UsuarioDelete.as_view(), name='delete_usuario'),
    path('novo/', UsuarioCreate.as_view(), name='create_usuario'),

]