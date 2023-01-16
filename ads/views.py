from django.http import JsonResponse
from ads.ad_metrics_helper import CalculateGoogleAdsMetrics
from ads.models import GoogleAds


def calculate_metrics(request):
    if request.method == "GET":
        google_ads_instance = GoogleAds.objects.all()
        for instance in google_ads_instance:
            instancess = CalculateGoogleAdsMetrics(instance)
            # instance.get_table_name()
            instancess.cpa_calculator()
            instancess.cpc_calculator()
            instancess.roas_calculator()
            instancess.upload_to_bigquery()
        return JsonResponse({"message": "success"}, status=200)
