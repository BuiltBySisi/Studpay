from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Teacher(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  joindate = models.DateField(auto_now_add=True)
  phone = models.CharField(max_length=40)
  salary = models.PositiveIntegerField(null=False)
  status = models.BooleanField(default=False)
  def __str__(self):
    return self.user.first_name

  @property
  def get_id(self):
    return self.user.id 

  @property
  def get_name(self):
    return self.user.first_name+" "+self.user.last_name


classes = [
  ('Grade one','one'),
  ('Grade two','two'),
  ('Grade three','three'),
  ('Grade four','four'),
  ('Grade five','five'),
  ('Grade six','six'),
  ('Grade seven','seven'),
  ('Grade eight','eight'),
  ('Grade nine','nine'),
  ('Grade ten','ten'),
]

class Student(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  phone = models.CharField(max_length=10)
  fee = models.PositiveIntegerField(null=True)
  cl = models.CharField(max_length=10, choices=classes, default='Grade one')
  status = models.BooleanField(default=False)
  roll = models.CharField(max_length=10)
  @property
  def get_name(self):
    return self.user.first_name+" "+self.user.last_name

  @property
  def get_id(self):
    return self.user.id
  
  def __str__(self):
    return self.user.first_name


  
class Attendance(models.Model):
  roll= models.CharField(max_length=10, null=True)
  date= models.DateField()
  cl = models.CharField(max_length=10)
  present_status = models.CharField(max_length=10)


class Notice(models.Model):
  date= models.DateField(auto_now=True)
  by = models.CharField(max_length=20, null=True, default='School Management')
  message = models.CharField(max_length=500)


grades=[
  ('A', 'Excellent'),
  ('B', 'Very Good'),
  ('C', 'Credit'),
  ('D', 'Pass'),
  ('F', 'Fail'),
]
class Performance(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  subject = models.CharField(max_length=20, null=True)
  grade = models.CharField(max_length=10, choices=grades, default='null')
  teacherComment = models.CharField(max_length=100)
  
  @property
  def get_grade(self):
    return self.subject + " " + self.grade
  
  @property
  def get_performer(self):
    return self.user + " " + self.teacherComment