from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('authenticate/', include('django.contrib.auth.urls')),
    path('authenticate/', include('authenticate.urls')),
]
admin.site.site_header = "My Club Administration Page"
admin.site.site_title = "Browser Title"
admin.site.index_title = "Welcome To Admin Area ..."
