from django import forms
from portalapp.models import (Exam,Descriptive,MCQ,MultiCorrectMCQ,
IntegerType,Choice,MChoice,TrueFalse,FillBlanks,Course)
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxLengthValidator,MinLengthValidator
# class UserLoginForm(forms.ModelForm):
#     class META():
#         model=get_user_model
#         fields=['username','password']
# class SignupForm(forms.ModelForm):
#     password= forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = User
#         fields=('first_name','last_name','username','password1','password2','email')
class StudentSignupForm(UserCreationForm):
    courses=forms.ModelMultipleChoiceField(
    queryset=Course.objects.all(),
    widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model=User
        fields=('first_name','last_name','username','password1','password2','courses','email')
