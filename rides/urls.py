from django.urls import path
from . import views

urlpatterns = [
    path('rides/', views.signup, name='ride'),
    path('rider/', views.riderregistercheck, name='rider_register_check'),
    path('riderregister/', views.riderregister, name='rider_register'),
    path('requestride/',views.request_ride)
]