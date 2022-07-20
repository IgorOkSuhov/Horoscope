from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='horoscope-index'),
    path('<int:dinamic_zoo>/', views.get_info_about_zodiak_integer),
    path('<str:dinamic_zoo>/', views.get_info_about_zodiak, name='horoscope-name'),
]
