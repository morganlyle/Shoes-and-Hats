from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import signup
from receipts.views import AccountsCreateView

# from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", AccountsCreateView.as_view(), name="accounts"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", signup, name="signup"),
]
