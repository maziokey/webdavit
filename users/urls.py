from django.urls import path

from .views import SignupPageView, PasswordChangeView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
]