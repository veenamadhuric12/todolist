from django.urls import path
from . import views

urlpatterns = [
    path('1',views.index),
    path('2',views.todo),
    path('3',views.history),
]