from django.core.management.base import BaseCommand
from ads.models import GoogleAds
import csv


class Command(BaseCommand):
    help = "Upload CSV file data to Google Ads Model"

    def handle(self, *args, **options):
        # Import CSV file data to Google Ads Model
        filename = "./ads_metrics.csv"

        data_list = []

        # Open the file for reading
        with open(filename, "r") as f:
            # Create a CSV reader
            reader = csv.DictReader(f)

            # Iterate through the rows
            for row in reader:

                # strip $ from cost
                row["cost"] = row["cost"].replace("$", "")

                # convert date format from DD-MM-YYYY to YYYY-MM-DD
                row["date"] = (
                    row["date"][6:] + "-" + row["date"][3:5] + "-" + row["date"][:2]
                )

                # Create a MyModel object for each row
                data_list.append(
                    GoogleAds(
                        campaign_name=row["campaign_name"],
                        impressions=int(row["impressions"]),
                        cost=float(row["cost"]),
                        clicks=int(row["clicks"]),
                        date=row["date"],
                    )
                )

        # Bulk insert the data into the database
        GoogleAds.objects.bulk_create(data_list)

        self.stdout.write(self.style.SUCCESS("Successfully uploaded CSV file data"))
