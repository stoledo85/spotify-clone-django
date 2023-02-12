from django.urls import path
from . import views


app_name = "clientes"

# Local onde concentra todas rotas do App Cliente.

urlpatterns = [
    
    path("", views.index, name="index"),
]