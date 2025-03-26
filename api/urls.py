from .views import CreateTripDetails,GetTrip
from django.urls import path,include

urlpatterns = [
    path('trips/',CreateTripDetails.as_view(),name='api'),
    path('trips/<int:pk>',GetTrip.as_view(),name='get-trip')
]