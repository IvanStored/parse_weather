import datetime

from django_q.models import Schedule, Task
from rest_framework import serializers

from parser.models import Forecast


class WeatherSerializer(serializers.ModelSerializer):
    """
    Serializer for Day instance
    """

    class Meta:
        model = Forecast
        fields = "__all__"


class ScheduleDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for Schedule instance
    """

    class Meta:
        model = Schedule
        fields = "__all__"
        read_only_fields = (
            "id",
            "name",
            "func",
            "hook",
            "args",
            "kwargs",
            "schedule_type",
            "minutes",
            "repeats",
            "cron",
            "task",
            "cluster",
        )

    def to_representation(self, instance):
        schedule = super(ScheduleDetailSerializer, self).to_representation(
            instance
        )

        if instance.next_run.strftime(
            "%Y-%m-%dT%H:%M:%S%z"
        ) < datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z"):
            schedule["status"] = "Done"
        elif instance.next_run.strftime(
            "%Y-%m-%dT%H:%M:%S%z"
        ) > datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z"):
            schedule["status"] = "Scheduled"
        else:
            schedule["status"] = "In Progress"
        return schedule


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task instance
    """

    class Meta:
        model = Task
        fields = "__all__"
