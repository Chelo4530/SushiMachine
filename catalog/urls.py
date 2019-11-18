from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pedido/<int:pk>/', views.pedido_detail, name='pedido_detail'),
    path('pedido/new', views.pedido_new, name='pedido_new'),
    path('pedido/<int:pk>/edit/', views.pedido_edit, name='pedido_edit'),
]