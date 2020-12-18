from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('addtest/',views.add_todo)
]