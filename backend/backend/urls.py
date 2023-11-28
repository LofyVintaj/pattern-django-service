from django.contrib import admin
from django.urls import path, include
# from backend.views import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('listening/', console_log_post_view, name='listening-log-post'),
]
