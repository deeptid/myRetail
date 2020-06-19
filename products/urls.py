from django.urls import path
from products import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('<int:productId>/', views.detail, name='detail'),
    path('<int:productId>/raw_data/', views.rawData, name='rawData'),
    path('<int:productId>/edit/', views.edit, name='edit'),
    path('<int:productId>/delete/', views.delete, name='delete'),
]