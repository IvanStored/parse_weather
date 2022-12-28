from django.db import models


class Forecast(models.Model):
    """
    Model for day instance
    """
    day = models.CharField(max_length=10)
    temperature = models.CharField(max_length=5)
    description = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Day: {self.day}(temperature: {self.temperature}), description: {self.description}"
