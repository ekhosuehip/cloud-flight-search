import json
import requests
from secrets_manager import SecretsManager

class FlightDetails:
    def __init__(self):
        self.api_key = SecretsManager().get_secret()
        self.url =  "https://ignav.com/api/fares/one-way"

    def search_flights(self, origin, destination, departure_date):
        headers = {
            "X-Api-Key": self.api_key
        }
        payload = {
            "origin": origin,
            "destination": destination,
            "departure_date": departure_date
        }

        response = requests.post(url=self.url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
