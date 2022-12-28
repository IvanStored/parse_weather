from django.urls import path, include
from rest_framework import routers

from parser import views


router = routers.DefaultRouter()
router.register("weather", views.WeatherViewSet, basename="weather")
router.register("schedule", views.ScheduleViewSet, basename="schedule")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "parser"
