
import boto3

# Connect to AWS using your local development profile
session = boto3.Session(
    profile_name="flight-dev",
    region_name="eu-north-1"
)

# Connect to DynamoDB
dynamodb = session.resource("dynamodb")
table = dynamodb.Table("FlightDestinations")

# Initial destination data
destinations = [
    {"City": "LONDON", "iataCode": "LON", "Price": 300},
]


def seed_destinations():
    try:
        with table.batch_writer() as batch:
            for destination in destinations:
                batch.put_item(Item=destination)
                print(
                    f"Uploaded: {destination['City']} "
                    f"({destination['iataCode']})"
                )

        print(
            f"\nSuccessfully uploaded "
            f"{len(destinations)} destinations."
        )

    except Exception as error:
        print(f"Failed to upload destinations: {error}")


if __name__ == "__main__":
    seed_destinations()