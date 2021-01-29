from django.urls import path,re_path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
app_name='portalapp'

urlpatterns=[
path('login/',LoginView.as_view(template_name='login.html'),name='login'),
path('logout/',LogoutView.as_view(),name='logout'),
path('signup/',views.Signup.as_view(template_name='signup.html'),name='signup'),
path('login_success/',views.LoginSuccess.as_view(),name='login_success'),
path('logout_success/',views.LogoutSuccess.as_view(),name='logout_success'),
path('exams/create/',views.ExamCreateView.as_view(),name='exam_form'),
re_path('exams/update/(?P<pk>\d+)/',views.ExamUpdateView.as_view(),name='update'),
path('courses/',views.CourseListView.as_view(),name='course_list'),
re_path('courses/(?P<pk>\d+)/',views.CourseDetailView.as_view(),name='course_detail'),
]
