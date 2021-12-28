from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('delete-comment/<str:pk>', views.delete_comment, name='delete-comment'),
]