from django.urls import path
from measurement.views import SensorDetail, CreateSensor, UpdateSensor, AddMeasurement, SensorsList

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('create/', CreateSensor.as_view()),
    path('update/<pk>/', UpdateSensor.as_view()),
    path('measurements/', AddMeasurement.as_view()),
    path('sensors_list/', SensorsList.as_view()),
    path('sensor_detail/<pk>/', SensorDetail.as_view()),



]
