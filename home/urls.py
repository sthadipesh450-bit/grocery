from django.urls import path
from django.views.generic import RedirectView
from .views import login_view, Signup_view, dashboard_view, logout_view

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="login", permanent=False)),
    path("login/", login_view, name="login"),
    path("signup/", Signup_view, name="signup"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("logout/", logout_view, name="logout"),
]
