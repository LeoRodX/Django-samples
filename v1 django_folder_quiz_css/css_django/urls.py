from django.contrib import admin
from css_app import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('css_app.urls')),
]
