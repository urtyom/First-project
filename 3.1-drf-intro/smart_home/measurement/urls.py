from django.urls import path


from .views import SensorList, SensorUpdate, MeasurementCreateView


urlpatterns = [
    path('sensors/', SensorList.as_view(), name='sensors'),
    path('sensors/<int:pk>/', SensorUpdate.as_view(), name='sensor'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurements'),
]