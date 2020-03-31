from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:pk>/remove/', views.post_remove, name='post_remove'),
]