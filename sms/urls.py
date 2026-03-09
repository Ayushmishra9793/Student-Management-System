
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("student/", include("student.urls")),
]


# jaise hi student/ likha ho url me vo student(app) ke urls se fetch kare 