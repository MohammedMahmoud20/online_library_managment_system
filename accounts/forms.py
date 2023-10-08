from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Admins,Student

class studentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_students = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student.save()
        return user

class adminSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        admins = Admins.objects.create(user=user)
        admins.phone_number=self.cleaned_data.get('phone_number')
        admins.save()
        return user


# class signupform(UserCreationForm):
#

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if self.cleaned_data['image']:
#             profile = Profile.objects.get_or_create(user=user)[0]
#             profile.image = self.cleaned_data['image']
#             profile.save()
#         if commit:
#             user.save()
#         return user


# class userform(forms.ModelForm):
#     class Meta:
#         model=User
#         fields= ['username', 'email']

# class profileform(forms.ModelForm):
#     class Meta:
#         model=Profile
#         fields=['image']