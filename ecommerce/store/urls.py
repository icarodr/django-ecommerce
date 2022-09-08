from django.urls import path
from . import views
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.login, name='login'),
    url(r'^musics/$', views.MusicList.as_view(), name='music-list'),
]
