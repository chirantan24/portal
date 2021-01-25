from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Exam(models.Model):

    totalquestions=models.PositiveIntegerField()
    totalmarks=models.PositiveIntegerField()
    name=models.CharField()
    duration=models.TimeField()
    starttime=models.DateTimeField()

class Descriptive(models.Model):

    number=models.PositiveIntegerField()
    exam=models.ForeignKey('Exam',related_name='Descriptive',on_delete=models.CASCADE)
    question=models.CharField(max_length=300)
    maxmarks=models.PositiveIntegerField()
    marks=models.PositiveIntegerField()
    answer=models.CharField(max_length=1000,blank=true)
    upload=models.FileField(upload_to='uploads/')

class IntegerType(models.Model):

    exam=models.ForeignKey('Exam',related_name='Integer',on_delete=models.CASCADE)
    question=models.CharField(max_length=300)
    maxmarks=models.PositiveIntegerField()
    marks=models.PositiveIntegerField()
    answer=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(9),MinValueValidator(0)])

class MCQ(models.Model):

    exam=models.ForeignKey('Exam',related_name='MCQ',on_delete=models.CASCADE)
    question=models.CharField(max_length=300)
    maxmarks=models.PositiveIntegerField()
    marks=models.PositiveIntegerField()

class Choice(models.Model):

    question=models.ForeignKey('MCQ',related_name='choices',on_delete=models.CASCADE)
    iscorrect=models.BoolField()
    text=models.CharField()
    position=models.PositiveIntegerField()

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
    ispartial=models.BoolField()

class MChoice(models.Model):

    question=models.ForeignKey('MultiCorrectMCQ',related_name='choices',on_delete=models.CASCADE)
    iscorrect=models.BoolField()
    text=models.CharField()
    position=models.PositiveIntegerField()

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
    iscorrect=models.BoolField()

class FillBlanks(models.Model):

    exam=models.ForeignKey('Exam',related_name='FillBlanks',on_delete=models.CASCADE)
    question=models.CharField(max_length=300)
    answer=models.CharField(max_length=30)
    maxmarks=models.PositiveIntegerField()
    marks=models.PositiveIntegerField()
