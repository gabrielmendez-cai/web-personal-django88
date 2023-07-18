"""
URL configuration for webpersonal12 project.

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from core import views as core_views
from portfolio import views as portfolio_views

urlpatterns = [
    path ('', core_views.home, name="home"),
    path ('about-me/', core_views.about, name="about"),
    path ('portfolio/', portfolio_views.portfolio, name="portfolio"),
    path ('contacto/', core_views.contacto, name="contacto"),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)