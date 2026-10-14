import pprint
from flight_details import FlightDetails
from destination_service import DestinationService

destinations = DestinationService()
client = FlightDetails()

for data in destinations.get_destinations():
    origin = "LOS"
    destination = data["iataCode"]
    departure_date = "2026-11-12"

    response = client.search_flights(
        origin=origin,
        destination=destination,
        departure_date=departure_date
    )
    pprint.pprint(response["itineraries"][0]["price"])

