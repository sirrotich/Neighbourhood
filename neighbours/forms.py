from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image, Profile, Comments
from pyuploadcare.dj.forms import FileWidget
from pyuploadcare.dj.models import ImageField


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'post_date', 'profile']