import boto3

class DestinationService:
    def __init__(self):
        session = boto3.session.Session(
            profile_name="flight-dev",
            region_name="eu-north-1"
        )

        dynamodb = session.resource("dynamodb")
        self.table = dynamodb.Table("FlightDestinations")

    def get_destinations(self):
        response = self.table.scan()
        return response["Items"]
