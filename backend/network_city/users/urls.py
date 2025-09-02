from django.urls import path
from .views import UsersList

app_name = "users"

urlpatterns = [
    path("", UsersList.as_view(), name="users_list")
]