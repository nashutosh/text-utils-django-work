from django.contrib import admin
from django.urls import path
from .import veiws 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", veiws.index, name="index"),
    path("analyze/", veiws.analyze, name="analyze" )
]
