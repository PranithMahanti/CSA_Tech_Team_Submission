from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class NewBookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = "__all__"

    def set_user(self, user):
        self.user = user
        self.save()


