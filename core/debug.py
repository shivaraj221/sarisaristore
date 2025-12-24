from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def view_admin_users(request):
    # List superusers and staff users
    users = User.objects.filter(is_staff=True).values(
        "id", "username", "email", "is_superuser", "is_staff"
    )
    return JsonResponse(list(users), safe=False)
