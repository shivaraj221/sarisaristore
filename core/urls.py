from django.urls import path
from .views import LoginView, RegisterView, FeedbackView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
]
