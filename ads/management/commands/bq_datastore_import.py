from django.core.management.base import BaseCommand
from django.conf import settings
from google.cloud import bigquery
from google.oauth2 import service_account
from ads.models import TableA

credentials = service_account.Credentials.from_service_account_file(
    settings.GOOGLE_APPLICATION_CREDENTIALS
)


class Command(BaseCommand):
    help = "Import data from BigQuery to PostgreSQL"

    def handle(self, *args, **options):

        # Set up BigQuery client
        client = bigquery.Client(credentials=credentials)

        # Define the query
        query = """
            SELECT * FROM `push-marketing-femi.Datastore.TableA`
        """

        # Execute the query and save the results to a variable
        query_results = client.query(query).result()

        # Iterate through the results and create MyModel objects
        for row in query_results:
            TableA.objects.create(name=row.name, phone=row.phone)

        # Print a message to the console
        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
