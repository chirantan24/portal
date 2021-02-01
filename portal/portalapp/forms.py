from django import forms
from portalapp.models import (Exam,Descriptive,MCQ,MultiCorrectMCQ,
IntegerType,Choice,MChoice,TrueFalse,FillBlanks,Courses,studentCourses)
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxLengthValidator,MinLengthValidator
class UserCreateForm(UserCreationForm):
    class Meta:
        fields =('first_name','last_name','username','email','password1','password2')
        model = get_user_model()
