import datetime
from django import forms
from django.db import models

# Create your models here.

class Department(models.Model):
    code = models.CharField(max_length=4, default='DEPT')   #CMPT
    name = models.CharField(max_length=200, default='Department Name') #Computing Science
    def __str__(self):
        return self.code + ": "+self.name

class Course(models.Model):
    subject = models.CharField(max_length=4, default='SUBJ') #CMPT
    number  = models.IntegerField(range(100, 999), default=999) #470 
    title = models.CharField(max_length=50) #Web-based Information Systems
    meta_score = models.DecimalField(max_digits=2, decimal_places=1, default=0)    #will be generated on the fly
    def __str__(self):
        return self.subject + " " + str(self.number) + ": " + self.title

class Professor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department)
    meta_score = models.DecimalField(max_digits=2, decimal_places=1)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Review(models.Model):
    professor = models.ForeignKey(Professor)
    comments = models.CharField(max_length=350)
    interest_in_course = models.DecimalField(max_digits=2, decimal_places=1)
    course_subject = models.CharField(max_length=4, default='SUBJ') #CMPT
    course_number = models.IntegerField(range(100, 999), default=999) #470  
    #date_published = models.DateTimeField('date published', default=datetime.date.today())
    date_published = models.DateTimeField(("Date published"), auto_now_add = True)
    final_score = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return "["+self.course_subject+" "+str(self.course_number)+"] anonymous review for "+str(self.professor)+":  " + self.comments + ""

class WordCloud(models.Model):
    professor = models.ForeignKey(Professor)
    phrase_one = models.CharField(max_length=20, default='')
    phrase_two = models.CharField(max_length=20, default='')
    phrase_three = models.CharField(max_length=20, default='')

    def __str__(self):
        return "Word cloud entry for "+ str(self.professor)


