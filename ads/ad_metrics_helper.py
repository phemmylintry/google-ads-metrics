from django.conf import settings
from google.cloud import bigquery
from google.oauth2 import service_account

from ads.models import GoogleAds

credentials = service_account.Credentials.from_service_account_file(
    settings.GOOGLE_APPLICATION_CREDENTIALS
)


class CalculateGoogleAdsMetrics:
    def __init__(self, google_ads_instance) -> None:
        self.client = bigquery.Client(
            credentials=credentials, project=settings.GOOGLE_BQ_PROJECT_ID
        )
        self.dataset_id = settings.GOOGLE_BQ_DATASET_ID
        self.table_id = settings.GOOGLE_BQ_TABLE_ID
        self.google_ads_instance = google_ads_instance

    def upload_to_bigquery(self):
        instance = self.google_ads_instance

        # serialize date field
        instance.date = instance.date.strftime("%Y-%m-%d")

        query = f"""
            INSERT INTO `push-marketing-femi.Datastore.GoogleAds ` (id, campaign_name, impressions, cost, clicks, cpc, cpa, roas)
            VALUES (
                {instance.id},
                "{instance.campaign_name}",
                {instance.impressions},
                {instance.cost},
                {instance.clicks},
                {instance.cpc},
                {instance.cpa},
                {instance.roas}
            )
            """

        query_job = self.client.query(query).result()
        print(query_job)

    def cpa_calculator(self) -> int:
        cpa = int(self.google_ads_instance.cost) / int(self.google_ads_instance.clicks)
        self.google_ads_instance.cpa = cpa
        self.google_ads_instance.save()

    def cpc_calculator(self) -> int:
        cpc = int(self.google_ads_instance.cost) / int(self.google_ads_instance.clicks)
        self.google_ads_instance.cpc = cpc
        self.google_ads_instance.save()

    def roas_calculator(self) -> int:
        roas = int(self.google_ads_instance.cost) / int(
            self.google_ads_instance.impressions
        )
        self.google_ads_instance.roas = roas
        self.google_ads_instance.save()
