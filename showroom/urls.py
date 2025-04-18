from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_mobil, name='list_mobil'),
    path('tambah/', views.tambah_mobil, name='tambah_mobil'),
    path('mobil/<int:pk>/', views.detail_mobil, name='detail_mobil'),
    path('mobil/<int:mobil_id>/tambah_service/', views.tambah_service, name='tambah_service'),
    path('mobil/<int:pk>/hapus/', views.hapus_mobil, name='hapus_mobil'),
]
