from django.urls import path
from .views import LoginJWTView, UserDetailViels, UserViels


urlpatterns = [
    path("users/", UserViels.as_view()),
    path("users/login/", LoginJWTView.as_view()),
    path("users/<int:movie_id>/", UserDetailViels.as_view()),
]
