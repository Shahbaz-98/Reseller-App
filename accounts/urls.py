from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    url(r'imagefit/', include('imagefit.urls')),
    path('create_order//', views.createOrder, name="create_order"),
]