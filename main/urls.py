from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.contrib.auth.models import User

def view_admin_users(request):
    users = User.objects.filter(is_staff=True).values(
        "id", "username", "email", "is_superuser", "is_staff"
    )
    return JsonResponse(list(users), safe=False)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),

    # 🔴 ADD THIS LINE
    path("view-admin-users/", view_admin_users),

    # Frontend pages
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("login/", TemplateView.as_view(template_name="login.html"), name="login"),
    path("register/", TemplateView.as_view(template_name="register.html"), name="register"),
    path("store/", TemplateView.as_view(template_name="store.html"), name="store"),
]
