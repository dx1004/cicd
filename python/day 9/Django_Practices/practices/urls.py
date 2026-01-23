from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('about/', about),
    path('service/', services),
    path('render/', render_temp),
    path('name/', name),
    path('number/', number),
    path('lang/', lang),
    path('form/', form)
]
