from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('api/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
