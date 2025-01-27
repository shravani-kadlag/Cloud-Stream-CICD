from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),  # Use todos app for all functionality
]

urlpatterns += staticfiles_urlpatterns()
