from django.urls import path
from . import views

app_name='shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('create', views.create, name='create'),
]