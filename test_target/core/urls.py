from django.urls import path
from core.views import show_balance


urlpatterns = [
    path("objects/<int:pk>", show_balance),
]

# curl -v -H "Content-Type: application/json" -X POST -d '{"name":"your name","phonenumber":"111-111"}' http://www.example.com/details