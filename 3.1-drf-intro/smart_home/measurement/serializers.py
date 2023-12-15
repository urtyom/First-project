from rest_framework import serializers

from .models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('temperature', 'date_time')


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description')


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description', 'measurements')


class MeasurementAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ('sensor', 'temperature')
