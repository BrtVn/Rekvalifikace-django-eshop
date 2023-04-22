from . import views
from django.urls import path

urlpatterns = [
    path("profile/", views.UpdateUserProfileView.as_view(), name="profile_detail"),
]
