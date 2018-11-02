
from django.contrib import admin
from django.urls import path
from .views import (
    home,
    count,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",home, name="home" ),
    path("home/count/",count, name="count" ),
]
