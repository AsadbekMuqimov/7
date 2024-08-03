from django.urls import path, include
from Goods import views



urlpatterns = [
    path('', views.main, name='index'),
    path('info/', include('Goods.back-office.info.urls')),
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
    path('user/', include('Goods.user.urls')), 
]