from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    courses=models.ManyToManyField('Course',related_name='students',through='Enrollment')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
class Enrollment(models.Model):
    course=models.ForeignKey('Course',related_name='enrolled',on_delete=models.CASCADE)
    student=models.ForeignKey('Student',related_name='enrolled',on_delete=models.CASCADE)
class Exam(models.Model):

    course=models.ManyToManyField('Course',related_name='exams')
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
