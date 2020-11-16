from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('darah/', include('darah.urls')),
    path('login/', include('login.urls')),
    path('data/', include('data.urls')),
    # path('admin/', include('admin.urls')),

]   
