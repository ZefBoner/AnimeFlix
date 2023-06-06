from django.urls import path
from . import views

urlpatterns = [
    path('', views.webapp, name='webapp'),
    path('anime/<str:nombre_anime>/', views.anime_detail, name='anime_detail'),
    path('agregar_anime/', views.agregar_anime, name='agregar_anime'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/login/', views.login_view, name='login'),
    path('agregar_apisodio/', views.agregar_apisodio, name= 'agregar_apisodio')

]