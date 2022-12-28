# Generated by Django 4.1.4 on 2022-12-26 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parser", "0005_alter_forecast_last_update"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="forecast",
            name="max_temperature",
        ),
        migrations.RemoveField(
            model_name="forecast",
            name="min_temperature",
        ),
        migrations.AddField(
            model_name="forecast",
            name="temperature",
            field=models.CharField(default="temp", max_length=5),
            preserve_default=False,
        ),
    ]
