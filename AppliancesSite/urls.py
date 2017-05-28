from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^AppliancesApp/', include('AppliancesApp.urls')),
    url(r'^admin/', admin.site.urls),
]

