from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.tasks.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
    #path('about/', include('apps.about.urls')),
    #path('users/', include('apps.users.urls')),
]