from django.contrib import admin
from django.urls import path
from Mainc.views import MainView,ImageView,ReadTagView,TagAttributeView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(),name='home'),
    path('/Image', ImageView.as_view(),name='home'),
    path('/ReadByTag', ReadTagView.as_view(),name='ReadByTag'),
    path('/ReadByTagAttribute', TagAttributeView.as_view(),name='TagAttributeView'),
    url(r'^Mainview/$', MainView.as_view(), name='mainview'),
    url(r'^Image/$', ImageView.as_view(), name='Image'),
    url(r'^ReadByTag/$', ReadTagView.as_view(), name='ReadByTagView'),
    url(r'^ReadByTagAttribute/$', TagAttributeView.as_view(), name='TagAttributeView'),
]
