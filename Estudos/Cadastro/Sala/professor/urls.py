from django.urls import path
from . import views

urlpatterns = [
    path('criar_professor/', views.criar_professor, name="criar_professor"), 
    path('visualizar_professor/', views.visualizar_professor, name="visualizar_professor"),
    path('deletar_professor/<int:id>', views.deletar_professor, name="deletar_professor")
]
