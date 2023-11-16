"""
URL configuration for park project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.static import serve
from django.contrib import admin
from django.urls import path, include
from ppm.views import *
from user.views import *
from compte.views import *
from ppm.urls import *
from user.urls import *
from compte.urls import *

urlpatterns = [
    path('djangoadmin/', admin.site.urls),
    path('admin/', include(('ppm.urls', 'ppm'), namespace='ppm')),
    path('', include(('user.urls', 'user'), namespace='user')),
    path('auth', include(('compte.urls', 'compte'), namespace='compte')),
]
if settings.DEBUG:
    urlpatterns += [
        path(f'{settings.MEDIA_URL[1:]}<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    ]