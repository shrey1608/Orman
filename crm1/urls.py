"""crm1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
# for get images as media files are not configured by default in django production servers
#For getting  static url
from django.conf.urls.static import static
# for getting media url from the setting
from django.conf import settings
#for password resetting
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    #to get the reset link of the password
    path('', include('django.contrib.auth.urls'))

]

# so when this media url is set find then files in this folder Media_root
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)