from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Flight
from .serializers import FlightSerializer

class FlightFeatureCollectionView(APIView):
    def get(self, request, *args, **kwargs):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)

        geojson_response = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "id": flight['id'],
                    "geometry": {
                        "type": "Point",
                        "coordinates": [flight['longitude'], flight['latitude']]
                    },
                    "properties": {
                        "name": flight['name'],
                        "model": flight['model']
                    }
                }
                for flight in serializer.data
            ]
        }

        return Response(geojson_response)
