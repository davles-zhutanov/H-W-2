from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.list_item, name='list_item'),
    path('shop/<int:id>', views.detail_item, name='detail_item'),
    path('result/<int:id>', views.result, name='result'),
    path('vote/<int:id>', views.vote, name='vote'),
]