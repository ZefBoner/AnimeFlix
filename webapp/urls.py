from django.urls import path

from . import views

urlpatterns = [
    path('', views.webapp),
    # Ruta para mostrar el detalle de un anime específico
    path('anime/<int:anime_id>/', views.anime_detail, name='anime_detail'),
    path('agregar_anime/', views.agregar_anime, name='agregar_anime'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register')
]
