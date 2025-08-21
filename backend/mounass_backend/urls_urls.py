from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/users/', include('users.urls')),
    path('api/meet/', include('meet.urls')),
    path('api/texts/', include('texts.urls')),
    path('api/marketplace/', include('marketplace.urls')),
    path('api/realestate/', include('realestate.urls')),
]
