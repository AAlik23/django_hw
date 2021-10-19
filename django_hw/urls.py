from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('home/',views.home,name='django_hw_home'),
    path('admin/', admin.site.urls),
    path('human/',views.human , name='django_hw_human')
]