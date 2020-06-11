from django.urls import path

from . import views

urlpatterns = [
    path('<str:lat>/<str:lon>/', views.HotelList.as_view(), name='hotel-list'),
]
