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


@login_required(login_url='/accounts/login')
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            # print(f'image is {upload.image}')
            upload.save()
            return redirect('profile', username=request.user)
    else:
        form = ImageForm()
    
    return render(request, 'profile/upload_image.html', {'form':form})

@login_required(login_url='/accounts/login')
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile.html')
    else:
        form = ProfileForm()

    return render(request, 'profile/edit_profile.html', {'form':form})