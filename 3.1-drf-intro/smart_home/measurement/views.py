# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from .models import Measurement, Sensor
from .serializers import SensorSerializer, SensorDetailSerializer


from .serializers import MeasurementAddSerializer


class SensorList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.request.content_type == '' and 'id' in self.request.GET:
            return SensorDetailSerializer
        else:
            return SensorSerializer


    # serializer_class = SensorSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementAddSerializer
