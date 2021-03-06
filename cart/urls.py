from django.urls import path
from . import views

app_name = "cart"
urlpatterns=[
    path('', views.index, name='index'),
    path('add/<int:product_id>/', views.addCart, name='add_cart'),
    path('plus/', views.plusCart, name='plus_cart'),
    path('minus/', views.minusCart, name='minus_cart'),
    path('delete/<int:product_id>/', views.deleteCart, name='delete_cart'),
    path('active/', views.activeItem, name='active_item'),
    path('disable/', views.disableItem, name='disable_item'),
]