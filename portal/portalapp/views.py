from django.shortcuts import render
from django.views.generic import TemplateView,View,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from portalapp.models import (Exam,Descriptive,MCQ,MultiCorrectMCQ,
IntegerType,Choice,MChoice,TrueFalse,FillBlanks)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    return render(request,'index.html')
def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else :
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else :
            return HttpResponse("Invalid Username or Password")
    else:
        return render(request,'login.html')

class ExamCreateView(LoginRequiredMixin,CreateView):
    def test_fun(self):
        return self.user.is_superuser()
    model=Exam
    login_url='login/'
    redirect_field_name=''
    fields=['course','name','totalmarks','totalquestions']

class ExamUpdateView(UserPassesTestMixin,UpdateView):
    def test_fun(self):
        return self.user.is_superuser()
    model=Exam
    fields=['name','totalmarks','totalfields']
