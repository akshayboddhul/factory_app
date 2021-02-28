from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('add/', views.addNew, name="addNew"),
    path('detail/', views.detailView, name="detail"),
]
