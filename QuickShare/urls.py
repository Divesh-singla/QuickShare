"""
URL configuration for QuickShare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from routers.adminRoute.adminRouting import adminUrlPatterns
from routers.clientRoute.clientRounting import clientUrlPatterns
from django.conf import settings
from django.conf.urls.static import static
from controller.forbiddenController import forbiddenPage


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('opsLogin/', opsLoginPage , name="Operational login"),
    # path("forgotPassword/", getForgotPassword, name="forgot password"),
    # path("uploadDoc/", ImportDocx, name="Upload document"),
    path("admin/",include(adminUrlPatterns)),
    path("client/",include(clientUrlPatterns)),
    path("forbidden/",forbiddenPage),
    



]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


