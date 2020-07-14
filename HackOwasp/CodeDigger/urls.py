"""CodeDigger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Hookups import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #auth
    path('signup/',views.signupuser,name="signupuser"),
    path('logout/',views.logoutuser,name="logoutuser"),
    path('login/',views.loginuser,name="loginuser"),
    #hookups
    path('',views.home,name="home"),
    path('create/',views.createprojects,name="createprojects"),
    path('myprojects/',views.myprojects,name="myprojects"),
    path('<int:Hookup_pk>/',views.viewprojects,name="viewprojects"),
    path('myprojects/<int:hookup_pk>/',views.userviewproject,name="userviewproject"),
    path('myprojects/completed/',views.mycompletedprojects,name="mycompletedprojects"),
    path('resources/',views.resources,name="resources"),
    #category
    path('webdevelopment/',views.webdevelopment,name="webdevelopment"),
    path('androiddevelopment/',views.androiddevelopment,name="androiddevelopment"),
    path('blockchain/',views.blockchain,name="blockchain"),
    path('iot/',views.iot,name="iot"),
    path('machinelearning/',views.machinelearning,name="machinelearning"),
    path('iosdevelopment/',views.iosdevelopment,name="iosdevelopment"),
    path('datascience/',views.datascience,name="datascience"),
    path('others/',views.others,name="others"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)