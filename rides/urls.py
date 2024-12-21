from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='ride'),
    path('login',views.login),
    path('ridercheck/', views.riderregistercheck, name='rider_register_check'),
    path('riderregister/', views.riderregister, name='rider_register'),
    path('rideractivate/', views.activateRider),
    path('requestride/',views.request_ride),
    path('reqRider/',views.req_rider),
    path('riderRideReq', views.rider_ride_req),
    path('riderAcceptRide',views.rider_accept_ride),
    path('rideTerminate', views.ride_terminate),
]