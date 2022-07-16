from django.contrib import admin
from django.urls import path
from Mainc.views import MainView,ImageView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(),name='home'),
    path('/Image', ImageView.as_view(),name='home'),
    url(r'^Mainview/$', MainView.as_view(), name='mainview'),
    url(r'^Image/$', ImageView.as_view(), name='mainview'),
]
