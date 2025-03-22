import time
import random
import threading
from django.core.management.base import BaseCommand
from django.core.management import call_command
from flight_tracker_app.models import Flight

class Command(BaseCommand):
    help = 'Updates the location of all flights'

    def handle(self, *args, **kwargs):
        def update_location():
            while True:
                flights = Flight.objects.all()
                for flight in flights:
                    new_latitude = flight.latitude + random.uniform(0, 0.01)
                    new_longitude = flight.longitude + random.uniform(0, 0.01)

                    flight.latitude = new_latitude
                    flight.longitude = new_longitude
                    flight.save()

                    self.stdout.write(self.style.SUCCESS(
                        f"Updated flight {flight.id} to ({new_latitude}, {new_longitude})"
                    ))

                time.sleep(0.5)

        thread = threading.Thread(target=update_location)
        thread.daemon = True  # Allow the thread to exit when the main program exits
        thread.start()

        # Keep the main thread alive so that the background thread keeps running
        while True:
            time.sleep(1)
