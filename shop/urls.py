from django.urls import path
from . import views

app_name='shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/buy', views.buy, name='buy'),
    # path('<int:article_id>/edit', views.edit, name='edit'),
]