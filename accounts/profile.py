from accounts.models import UserProfile
from accounts.forms import UserProfileForm

def retrieve(request):
    """
    Note this requires an authenticated user before we try
    calling it.
    """
    try:
        #profile = request.user.profile
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()
    return profile

def set(request):
    profile = retrieve(request)
    profile_form = UserProfileForm(request.POST,instance=profile)
    profile_form.save()
        