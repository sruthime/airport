from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('registr/',views.registr),
    path('login/',views.login),
    path('success/',views.success)
]