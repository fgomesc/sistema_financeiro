from django.urls import path
from .views import NaturezaList, NaturezaEdit, NaturezaDelete, NaturezaCreate

urlpatterns = [
    path('', NaturezaList.as_view(), name='list_natureza'),
    path('editar/<int:pk>/', NaturezaEdit.as_view(), name='edit_natureza'),
    path('delete/<int:pk>/', NaturezaDelete.as_view(), name='delete_natureza'),
    path('novo/', NaturezaCreate.as_view(), name='create_natureza'),


]