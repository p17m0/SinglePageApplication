from django.urls import path

from . import views

app_name = 'tables'

urlpatterns = [
    path('index/', views.tables_view,)
]
