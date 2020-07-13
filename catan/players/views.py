from django.http import JsonResponse
from .models import User

# Create your views here.
def players(request):
    qs = User.objects.all()
    usernames = [u.username for u in qs]

    return JsonResponse(
        {'usernames': usernames}
    )
