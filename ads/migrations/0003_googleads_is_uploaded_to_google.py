# Generated by Django 4.1.5 on 2023-01-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_googleads"),
    ]

    operations = [
        migrations.AddField(
            model_name="googleads",
            name="is_uploaded_to_google",
            field=models.BooleanField(default=False),
        ),
    ]
