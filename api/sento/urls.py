from django.urls import path
from .views import sento_list, sento_details, sento_visit_list

urlpatterns = [
    path('sentos/', sento_list, name='sento-list'),
    path('sentos/<int:pk>', sento_details, name='sento-detail'),
    path('sento/visits/', sento_visit_list, name='sento-visit-list'),
    # path('sento/visits/<int:pk>', sento_visit, name='sento-visit'),
]