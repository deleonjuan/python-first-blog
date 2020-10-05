from django.urls import path
from . import views

urlpatterns = [
    path('', views.publicacion_lista, name='publicacion_lista'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/nueva', views.publicacion_nueva, name='publicacion_nueva'),
    path('post/<int:pk>/editar/', views.publicacion_editar, name='publicacion_editar'),
]