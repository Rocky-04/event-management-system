from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/login/', ObtainAuthToken.as_view(), name='auth-login'),
    path('api-token-auth/', include('rest_framework.urls')),
    path('events/', include('events.urls')),
]
