from django.urls import path
from .views import FlightFeatureCollectionView

urlpatterns = [
    path('flights/', FlightFeatureCollectionView.as_view(), name="flight-feature-collection"), 
]
