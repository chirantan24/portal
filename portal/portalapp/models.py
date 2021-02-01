from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User,PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class User(User,PermissionsMixin):
    def __str__(self):
        return self.username
status_choice=(
('True','True'),
('False','False'),
)
class Courses(models.Model):
    title=models.CharField(max_length=256)
    faculty=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class studentCourses(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    courses=models.ForeignKey(Courses,on_delete=models.CASCADE)
    status=models.CharField(choices=status_choice,default='False',max_length=20)
    def __str__(self):
        return self.user.username
class Exam(models.Model):
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    title=models.CharField(default='exam',max_length=256)
    total_marks=models.PositiveIntegerField()
    start_time=models.DateTimeField(blank=True,null=True)
    end_time=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title
status_choice=(
('True','True'),
('False','False'),
)
class Descriptive(models.Model):

    exam=models.ForeignKey('Exam',related_name='Descriptive',on_delete=models.CASCADE)
    question=models.CharField(max_length=300)
    maxmarks=models.PositiveIntegerField()
    marks=models.PositiveIntegerField()
    answer=models.CharField(max_length=1000,blank=True)
    upload=models.FileField(upload_to='uploads/')

    def __str__(self):
        return 'Que'

class IntegerType(models.Model):

    exam=models.ForeignKey('Exam',related_name='Integer',on_delete=models.CASCADE)
    question=models.CharField(max_length=300)
    maxmarks=models.PositiveIntegerField()
    marks=models.PositiveIntegerField()
    answer=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(9),MinValueValidator(0)])
    def __str__(self):
        return 'Que'
class MCQ(models.Model):

    exam=models.ForeignKey('Exam',related_name='MCQ',on_delete=models.CASCADE)
    question=models.CharField(max_length=300)
    maxmarks=models.PositiveIntegerField()
    marks=models.PositiveIntegerField()
    def __str__(self):
        return 'Que'

class Choice(models.Model):

    question=models.ForeignKey('MCQ',related_name='choices',on_delete=models.CASCADE)
    iscorrect=models.BooleanField()
    text=models.CharField(max_length=50)
    position=models.PositiveIntegerField()

    def __str__(self):
        return 'Que'

    class META:
        unique_together=[
        ("question","text"),
        ("question","position")
        ]
        ordering = ("position",)

class MultiCorrectMCQ(models.Model):

    exam=models.ForeignKey('Exam',related_name='MultiCorrectMCQ',on_delete=models.CASCADE)
    question=models.CharField(max_length=300)
    maxmarks=models.PositiveIntegerField()
    marks=models.PositiveIntegerField()
    correct=models.PositiveIntegerField()
    incorrect=models.PositiveIntegerField()
    ispartial=models.BooleanField()
    def __str__(self):
        return 'Que'

class MChoice(models.Model):

    question=models.ForeignKey('MultiCorrectMCQ',related_name='choices',on_delete=models.CASCADE)
    iscorrect=models.BooleanField()
    text=models.CharField(max_length=50)
    position=models.PositiveIntegerField()
    def __str__(self):
        return 'Que'

    class META:
        unique_together=[
        ("question","text"),
        ("question","position")
        ]
        ordering = ("position",)

class TrueFalse(models.Model):

    exam=models.ForeignKey('Exam',related_name='TrueFalse',on_delete=models.CASCADE)
    question=models.CharField(max_length=300)
    maxmarks=models.PositiveIntegerField()
    marks=models.PositiveIntegerField()
    iscorrect=models.BooleanField()
    def __str__(self):
        return 'Que'

class FillBlanks(models.Model):

    exam=models.ForeignKey('Exam',related_name='FillBlanks',on_delete=models.CASCADE)
    question=models.CharField(max_length=300)
    answer=models.CharField(max_length=30)
    maxmarks=models.PositiveIntegerField()
    marks=models.PositiveIntegerField()
    def __str__(self):
        return 'Que'
