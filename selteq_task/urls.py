from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # Include 'users' app URLs under 'api/'
    path('api/', include('tasks.urls')),  # Include 'tasks' app URLs under 'api/'
]
