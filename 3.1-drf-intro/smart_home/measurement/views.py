# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from .models import Measurement, Sensor
from .serializers import SensorSerializer, MeasurementSerializer


class SensorList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     measurement = Measurement.objects.create(
    #         sensor=serializer.validated_data['sensor'],
    #         temperature=serializer.validated_data['temperature'],
    #         date_time=timezone.now()
    #     )
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # from django.utils import timezone
    #
    # measurement = Measurement(
    #     sensor=1,
    #     temperature=22.3,
    #     date_time=timezone.now()
    # )
    # measurement.save()
