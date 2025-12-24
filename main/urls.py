from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def debug_admin(request):
    users = User.objects.all()
    result = []
    result.append("<h2>📊 Database Users:</h2>")
    
    if users.exists():
        for user in users:
            result.append(f"{user.id}: {user.username} - Superuser: {user.is_superuser} - Staff: {user.is_staff} - Email: {user.email}")
    else:
        result.append("No users found in database!")
    
    result.append("<h2>🔑 Authentication Tests:</h2>")
    
    # Test with the correct password
    auth_user = authenticate(username='shiva', password='Shiva@2025!')
    if auth_user:
        result.append(f"✅ Authentication SUCCESS for 'shiva' with 'Shiva@2025!'")
    else:
        result.append(f"❌ Authentication FAILED for 'shiva' with 'Shiva@2025!'")
    
    return HttpResponse("<br>".join(result))

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),
    path("debug-admin/", debug_admin),
    
    # ✅ FRONTEND PAGES
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("login/", TemplateView.as_view(template_name="login.html"), name="login"),
    path("register/", TemplateView.as_view(template_name="register.html"), name="register"),
    path("store/", TemplateView.as_view(template_name="store.html"), name="store"),
]
