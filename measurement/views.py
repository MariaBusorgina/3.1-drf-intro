# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer2, SensorSerializer2


# 1. Создание датчика
class CreateSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# 2. Изменение датчика по id
class UpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# 3. Добавить измерение
class AddMeasurement(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer2


# 4. Получение списка датчиков
class SensorsList(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer2


# 5. Получить информацию по конкретному датчику.
class SensorDetail(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer



