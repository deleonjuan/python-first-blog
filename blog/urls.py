from django.urls import path
from . import views

urlpatterns = [
    path('', views.publicacion_lista, name='publicacion_lista'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]