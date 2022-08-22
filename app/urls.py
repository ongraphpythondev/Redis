from django.urls import path
from app.views import Home, Add

app_name = "app"

urlpatterns = [
    path('add/', Add.as_view(), name="add" ),
    path('home/', Home.as_view(), name="home" ),
]