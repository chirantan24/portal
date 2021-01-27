from django.shortcuts import render
from django.views.generic import TemplateView,View,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from portalapp.models import (Exam,Descriptive,MCQ,MultiCorrectMCQ,
IntegerType,Choice,MChoice,TrueFalse,FillBlanks,Student)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from . import forms
from portalapp.forms import SignupForm,StudentSignupForm
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
def signup(request):

    registered=False
    if request.method == "POST" :
        user_form=SignupForm(data=request.POST)
        student_form=StudentSignupForm(data=request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            student=student_form.save(commit=False)
            student.user=user
            student.save()
            registered=True
        else :
            print(user_form.errors,student_form.errors)
    else :
        user_form = SignupForm()
        student_form = StudentSignupForm()
    return render(request,'signup.html',context={'registered':registered,'user_form':user_form,'student_form':student_form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser

class ExamCreateView(AdminStaffRequiredMixin,CreateView):

    model=Exam
    login_url='login/'
    redirect_field_name=''
    fields=['course','name','totalmarks','totalquestions','starttime','duration']

class ExamUpdateView(AdminStaffRequiredMixin,UpdateView):
    model=Exam
    fields=['name','totalmarks','totalquestions','starttime','duration']

class ExamListView(ListView):
    model=Exam

    def get_queryset(self):
        return Post.objects.filter(starttime__lte=timezone.now()).order_by('-starttime')
