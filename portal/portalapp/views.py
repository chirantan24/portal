from django.shortcuts import render
from django.views.generic import TemplateView,View,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from portalapp.models import (Exam,Descriptive,MCQ,MultiCorrectMCQ,
IntegerType,Choice,MChoice,TrueFalse,FillBlanks,Courses,studentCourses)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from . import forms
from django.forms import DateInput
# Create your views here.
from django.contrib.auth import get_user_model
class Home(TemplateView):
    template_name='base.html'

class Category(LoginRequiredMixin,CreateView):
    template_name='portalapp/cat.html'
    model=Courses
    fields=('title',)
    login_url=reverse_lazy('portalapp:login')
    success_url=reverse_lazy('portalapp:login_success')
    def form_valid(self,form):
        form.instance.faculty=self.request.user
        return super(Category,self).form_valid(form)
class Signup(CreateView):
    form_class = forms.UserCreateForm
    template_name='signup.html'
    success_url=reverse_lazy('portalapp:login')
class Examlist(LoginRequiredMixin,ListView):
    template_name='portalapp/exam_list.html'
    context_object_name='exam_list'
    model=Exam
    def get_queryset(self):
        qs=super(Examlist,self).get_queryset()
        return qs.filter(course__exact=self.kwargs['id'])

@login_required
def examlist(request,id):
    qs=Exam.objects.filter(course_id=id)
    return render(request,'portalapp/exam_list.html',{'exam_list':qs,'pk':id})
class Exam(LoginRequiredMixin,CreateView):
    template_name='portalapp/create_exam.html'
    fields=('title','total_marks','start_time','end_time')

    login_url=reverse_lazy('portalapp:login')
    success_url=reverse_lazy('portalapp:login_success')
    model=Exam
    def form_valid(self,form):
        form.instance.course_id=self.kwargs['pk']
        return super(Exam,self).form_valid(form)
class Catlist(LoginRequiredMixin,ListView):
    context_object_name='catlist'
    template_name='portalapp/cat_list.html'
    model=Courses
    login_url=reverse_lazy('portalapp:login')
    success_url=reverse_lazy('portalapp:login_success')
    def get_queryset(self):
        qs=super(Catlist,self).get_queryset()
        return qs.filter(faculty__exact=self.request.user)

# @login_required
# def question(request,pk):
#     try:
#         tf=models.TF.objects.filter(exam_id=pk)
#     except:pass
#     try:
#         dis=models.discriptive.objects.filter(exam_id=pk)
#     except:pass
#     try:
#         fill=models.fillnblanks.objects.filter(exam_id=pk)
#     except:pass
#     return render(request,'eapp/q_list.html',{'tf':tf,'pk':pk,'dis':dis,'fill':fill})
#
# class TFV(LoginRequiredMixin,CreateView):
#     model=models.TF
#     template_name='eapp/tf.html'
#     login_url=reverse_lazy('portalapp:login')
#     success_url=reverse_lazy('portalapp:login_success')
#     fields=('question','ans','marks')
#     def form_valid(self,form):
#         form.instance.exam_id=self.kwargs['pk']
#         return super(TFV,self).form_valid(form)
# class DisV(LoginRequiredMixin,CreateView):
#     model=models.discriptive
#     template_name='eapp/tf.html'
#     success_url=reverse_lazy('home')
#     login_url=reverse_lazy('login')
#     fields=('question','marks')
#     def form_valid(self,form):
#         form.instance.exam_id=self.kwargs['pk']
#         return super(DisV,self).form_valid(form)
# class fillV(LoginRequiredMixin,CreateView):
#     model=models.fillnblanks
#     template_name='eapp/tf.html'
#     success_url=reverse_lazy('home')
#     login_url=reverse_lazy('login')
#     fields=('question','marks')
#     def form_valid(self,form):
#         form.instance.exam_id=self.kwargs['pk']
#         return super(fillV,self).form_valid(form)
class CourseEnroll(LoginRequiredMixin,CreateView):
    model=studentCourses
    template_name='portalapp/cour.html'
    login_url=reverse_lazy('portalapp:login')
    success_url=reverse_lazy('portalapp:login_success')
    fields=('courses',)
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(CourseEnroll,self).form_valid(form)
class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    login_url=reverse_lazy('login')
    success_url=reverse_lazy('home')
    def test_func(self):
        return self.request.user.is_superuser
class Requests(AdminStaffRequiredMixin,ListView):
    model=studentCourses
    template_name='portalapp/request.html'
    context_object_name='list'
    def get_queryset(self):
        qs=super(Requests,self).get_queryset()
        return qs.filter(status__exact='False')
class Detail(AdminStaffRequiredMixin,UpdateView):
    model=studentCourses
    template_name='portalapp/details.html'
    fields=('status',)
    success_url=reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        req=studentCourses.objects.get(id=self.kwargs['pk'])

        context["usname"] = req
        context["pk"]=self.kwargs['pk']
        return context
class ReqDelete(AdminStaffRequiredMixin,DeleteView):
    model=studentCourses
    success_url='/'
class LoginSuccess(TemplateView):
    template_name='login_success.html'
class LogoutSuccess(TemplateView):
    template_name='logout_success.html'
