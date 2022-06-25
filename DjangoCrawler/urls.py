from django.contrib import admin
from django.urls import path
from Mainc.views import MainView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(),name='home'),
]
