from django.urls import path
from core.views import MainView , WinView , ShopListView ,ContactView,AboutView

app_name = 'core'


urlpatterns = [
    path('',MainView.as_view(),name ='main'),
    path('vin/',WinView.as_view() ,name ='win'),
    path('list/',ShopListView.as_view(),name ='list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),

]