import boto3
import json

class SecretsManager:
    def __init__(self, region_name="eu-north-1"):
        session = boto3.session.Session(
            profile_name="flight-dev"
        )

        self.client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

    def get_secret(self, secret_name="flight-search/production"):
        secret_response = self.client.get_secret_value(
            SecretId=secret_name
        )

        secret_data = json.loads(secret_response["SecretString"])
        return secret_data["FLIGHT_API_KEY"]

