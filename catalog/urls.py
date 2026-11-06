from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_details, name='book_details'),
]