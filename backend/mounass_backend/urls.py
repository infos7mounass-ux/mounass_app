from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/meet/', include('meet.urls')),
    path('api/texts/', include('texts.urls')),
    path('api/shop/', include('marketplace.urls')),
    path('api/realestate/', include('realestate.urls')),
    path('api/payments/', include('payments.urls')),
]
from django.urls import path, include

urlpatterns = [
    path('api/users/', include('users.urls')),
    path('api/meet/', include('meet.urls')),
    path('api/texts/', include('texts.urls')),
    path('api/marketplace/', include('marketplace.urls')),
    path('api/realestate/', include('realestate.urls')),
]
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'users',
    'meet',
    'texts',
    'marketplace',
    'realestate',
]
