from django.urls import path
from .views import CentrodecustoList, CentrodecustoEdit, CentrodecustoDelete, CentrodecustoCreate

urlpatterns = [
    path('', CentrodecustoList.as_view(), name='list_centrodecusto'),
    path('editar/<int:pk>/', CentrodecustoEdit.as_view(), name='edit_centrodecusto'),
    path('delete/<int:pk>/', CentrodecustoDelete.as_view(), name='delete_centrodecusto'),
    path('novo/', CentrodecustoCreate.as_view(), name='create_centrodecusto'),

]