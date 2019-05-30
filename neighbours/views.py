from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import  Profile
# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def profile(request):
    profile = User.objects.get(username=username)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    
    images = Images.get_profile_images(profile.id)
    title = f'@{profile.username} Hood Updates'

    return render(request, 'profile/profile.html',{'title':title, 'profile':profile,'profile_details':profile_details,'images':images})