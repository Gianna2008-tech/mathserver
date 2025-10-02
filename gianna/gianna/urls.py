from django.contrib import admin
from django.urls import path
from mathapp import views  # Ensure 'mathapp' is your app name

urlpatterns = [
    path('admin/', admin.site.urls),

    # Route for power calculator
    path('', views.power_calculator, name='power_calculator'),
]
