from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.hello_world),
    path('oddeven', views.even_odd),
    path('prime', views.prime),
    path('api-data/<id>', views.get_api_data),
    path('mahesh', views.json_lpu),
]