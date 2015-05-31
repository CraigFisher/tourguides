from django import forms
from django.forms import ModelForm
from profiles.models import GuideProfile
from profiles.models import MemberProfile
from django.contrib.auth.models import User


class MemberProfileForm(ModelForm):

    class Meta:
        model = MemberProfile
        fields = ['country', 'gender', 'dob']


class GuideProfileForm(ModelForm):

    class Meta:
        model = GuideProfile
        fields = ['licensed', 'description', 'country', 'gender', 'dob']


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
