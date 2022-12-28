from django_q.models import Schedule
from django_q.tasks import async_task, fetch
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from parser.models import Forecast
from parser.serializers import (
    WeatherSerializer,
    ScheduleDetailSerializer,
    TaskSerializer,
)


class WeatherViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    serializer_class = WeatherSerializer
    queryset = Forecast.objects.all()

    @action(methods=["GET"], detail=False, url_path="update-weather")
    def update_weather(self, request) -> Response:
        """
        Manual run task for update weather information
        :param request:

        """
        task = fetch(async_task("parser.parse.parse_weather", sync=True))
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ScheduleViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ScheduleDetailSerializer
    queryset = Schedule.objects.all()
