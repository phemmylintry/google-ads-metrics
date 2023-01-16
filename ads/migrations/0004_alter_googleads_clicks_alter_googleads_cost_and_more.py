# Generated by Django 4.1.5 on 2023-01-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_googleads_is_uploaded_to_google"),
    ]

    operations = [
        migrations.AlterField(
            model_name="googleads",
            name="clicks",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="googleads",
            name="cost",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="googleads",
            name="cpa",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="googleads",
            name="cpc",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="googleads",
            name="impressions",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="googleads",
            name="roas",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
