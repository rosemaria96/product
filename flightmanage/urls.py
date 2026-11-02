from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add/', views.add_flight, name = 'add'),
    path('flight_list/', views.flight_list, name = 'flight_list'),
     path('detail/<int:id>/', views.flight_detail, name='detail'),
    path('edit/<int:id>/', views.edit_flight, name = 'edit'),
    path('delete/<int:id>/', views.delete_flight, name = 'delete'),
    path('search/', views.search_flight, name = 'search'),
]