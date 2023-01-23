from django.urls import path
from .views import sento_list, sento_details

urlpatterns = [
    path('sentos/', sento_list, name='sento-list'),
    path('sentos/<int:pk>', sento_details, name='sento-detail'),
]