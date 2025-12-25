from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),
    
    # Your App API
    path("api/", include("core.urls")),
    
    # Frontend Pages
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("login/", TemplateView.as_view(template_name="login.html"), name="login"),
    path("register/", TemplateView.as_view(template_name="register.html"), name="register"),
    path("store/", TemplateView.as_view(template_name="store.html"), name="store"),
]

# ✅ NO AUTO-CREATION IN URLS.PY - Security risk!
