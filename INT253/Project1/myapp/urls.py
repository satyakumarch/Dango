from django.urls import path
from myapp import views
from django.urls import re_path

urlpatterns = [
    # path('', views.hello_world),
    # path('oddeven', views.even_odd),
    # path('prime', views.prime),
    # path('api-data/<id>', views.get_api_data),
    # path('mahesh', views.json_lpu),
    # path('greet/<str:name>/', views.greet, name='greet_user'),
    # re_path(r'^report/(?P<date>\d{4}-\d{2}-\d{2})/$', views.report)
    path('abcd', views.abcd),

]   