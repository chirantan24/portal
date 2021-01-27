from django.urls import path,re_path
from . import views
app_name='portalapp'

urlpatterns=[
path('login/',views.user_login,name='login'),
path('exams/create/',views.ExamCreateView.as_view(),name='exam_form'),
re_path('exams/update/(?P<pk>\d+)/',views.ExamUpdateView.as_view(),name='update')
]
