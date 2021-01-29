from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User,PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class User(User,PermissionsMixin):

    def __str__(self):
        return self.username

class Course(models.Model):
    name=models.CharField(max_length=50)
    students=models.ManyToManyField('User',through='Enrollment')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('course_detail',kwargs={'pk':self.pk})
class Enrollment(models.Model):
    course=models.ForeignKey('Course',related_name='enrolled_students',on_delete=models.CASCADE)
    student=models.ForeignKey('User',related_name='enrolled_courses',on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username
    class Meta:
        unique_together=('course','student')

class Exam(models.Model):
    course=models.ForeignKey('Course',related_name='exams',on_delete=models.CASCADE)
    totalquestions=models.PositiveIntegerField()
    totalmarks=models.PositiveIntegerField()
    name=models.CharField(max_length=50)
    duration=models.TimeField()
    starttime=models.DateTimeField()
    obtainedmarks=models.PositiveIntegerField()
    def __str__(self):
        return self.name

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
