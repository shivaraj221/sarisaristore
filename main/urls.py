from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def debug_admin(request):
    users = User.objects.all()
    result = []
    result.append(f"<h2>🔍 DEBUGGING: {request.get_host()}</h2>")
    
    if users.exists():
        for user in users:
            result.append(f"{user.id}: {user.username} - Superuser: {user.is_superuser} - Staff: {user.is_staff}")
    else:
        result.append("❌ NO USERS IN THIS DATABASE!")
    
    # Test authentication
    result.append("<h3>🔑 Authentication Tests:</h3>")
    
    test_cases = [
        ('shiva', 'Shiva@2025!'),
        ('admin', 'Admin123!!'),
        ('admin', 'AdminSecure123!'),
    ]
    
    for username, password in test_cases:
        auth_user = authenticate(username=username, password=password)
        if auth_user:
            result.append(f"✅ Authentication SUCCESS: {username} / {password}")
        else:
            result.append(f"❌ Authentication FAILED: {username} / {password}")
    
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
