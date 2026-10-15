import pprint
import datetime
from dateutil.relativedelta import relativedelta
from flight_details import FlightDetails
from destination_service import DestinationService

destinations = DestinationService()
client = FlightDetails()

def get_date_after_two_months():
    today = datetime.date.today()
    future = today + relativedelta(months=2)
    return future.strftime("%Y-%m-%d")

for data in destinations.get_destinations():
    origin = "LOS"
    destination = data["iataCode"]
    departure_date = get_date_after_two_months()

    response = client.search_flights(
        origin=origin,
        destination=destination,
        departure_date=departure_date
    )
    pprint.pprint(response["itineraries"][0]["price"])

    if data["Price"] > response["itineraries"][0]["price"]["amount"]:
        new_price = response["itineraries"][0]["price"]["amount"]

        print("✈️ Flight Price Alert!")
        print(
            f"Your flight price for {data['City']} has dropped "
            f"from ${data['Price']} to ${new_price}."
        )
