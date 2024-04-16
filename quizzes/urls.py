from django.urls import path
from . import views

urlpatterns = [
    path('quiz_view/', views.quiz_view, name='quiz_view'),
]
