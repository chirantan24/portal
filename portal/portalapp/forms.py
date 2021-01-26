from django import forms
from portalapp.models import (Exam,Descriptive,MCQ,MultiCorrectMCQ,
IntegerType,Choice,MChoice,TrueFalse,FillBlanks)
from django.contrib.auth import User

class UserLoginForm(forms.ModelForm):
    class META():
        model=User
        fields=['username','password']
