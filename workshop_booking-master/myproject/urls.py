
from django.contrib import admin
from django.urls import path, include
from workshop_app import views  # import your home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # make sure this is here
    path('workshop_app/', include('workshop_app.urls')),
]
