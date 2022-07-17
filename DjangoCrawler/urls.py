from django.contrib import admin
from django.urls import path
from Mainc.views import MainView,ImageView,ReadTagView,TagAttributeView,AhrefView,HeadingView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(),name='home'),
    path('/Image', ImageView.as_view(),name='home'),
    path('/Ahref', AhrefView.as_view(),name='Ahref'),
    path('/Heading', HeadingView.as_view(),name='Ahref'),
    path('/ReadByTag', ReadTagView.as_view(),name='ReadByTag'),
    path('/ReadByTagAttribute', TagAttributeView.as_view(),name='TagAttributeView'),
    url(r'^Mainview/$', MainView.as_view(), name='mainview'),
    url(r'^Image/$', ImageView.as_view(), name='Image'),
    url(r'^Ahref/$', AhrefView.as_view(), name='Ahref'),
    url(r'^ReadByTag/$', ReadTagView.as_view(), name='ReadByTagView'),
    url(r'^ReadByTagAttribute/$', TagAttributeView.as_view(), name='TagAttributeView'),
    url(r'^Heading/$', HeadingView.as_view(), name='Heading'),

]
