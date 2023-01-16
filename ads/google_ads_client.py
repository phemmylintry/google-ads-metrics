from django.conf import settings
from google.cloud import bigquery
from google.oauth2 import service_account
from google.ads.googleads.client import GoogleAdsClient


credentials = service_account.Credentials.from_service_account_file(
    settings.GOOGLE_APPLICATION_CREDENTIALS
)
google_ads_client = GoogleAdsClient(credentials=credentials, developer_token=settings.GOOGLE_ADS_DEVELOPER_TOKEN)

def check_google_ads():
    # Connect to BigQuery
    bigquery_client = bigquery.Client(credentials=credentials)

    # Retrieve data from BigQuery
    query = """
        SELECT * FROM `push-marketing-femi.Datastore.GoogleAds ` LIMIT 1
    """
    query_job = bigquery_client.query(query)
    results = query_job.result()

    # Convert data to CSV format
    csv_data = results.to_dataframe().to_csv()

    # print(csv_data)

    # # Use the Google Ads API client to upload the data
    # upload_service = google_ads_client.get_service("ConversionUploadService")
    # upload_response = upload_service.upload_click_conversions()

    campaign_service = google_ads_client.get_service("CampaignService")
    print(campaign_service.get_campaign("1234567890"))