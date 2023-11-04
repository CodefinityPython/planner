from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('note/<int:note_id>/delete/', views.delete, name='delete'),
]