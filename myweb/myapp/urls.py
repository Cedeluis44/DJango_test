from django.urls import path
from .views import client_list, client_update, client_delete
urlpatterns = [
    path('', client_list, name='client_list'),
    path('edit/<int:pk>/', client_update, name='client_update'),
    path('delete/<int:pk>/', client_delete, name='client_delete')
]
