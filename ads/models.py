from django.db import models


class TableA(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class GoogleAds(models.Model):
    campaign_name = models.CharField(
        max_length=255, default=None, blank=True, null=True
    )
    impressions = models.IntegerField(default=0, blank=True, null=True)
    cost = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=True, null=True
    )
    clicks = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateField(default=None, blank=True, null=True)
    cpc = models.FloatField(default=0.00, blank=True, null=True)
    cpa = models.FloatField(default=0.00, blank=True, null=True)
    roas = models.FloatField(default=0.00, blank=True, null=True)
    is_uploaded_to_google = models.BooleanField(default=False)
