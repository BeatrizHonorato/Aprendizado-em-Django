from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_usuarios/', views.cadastrar_usuario, name="cadastrar_usuarios"),
    path('login/', views.login, name="login")
]
