from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin
    path('', include('trainer.urls')),  # Include the URLs for the trainer app
]
