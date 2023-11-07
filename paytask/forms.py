from django import forms
from django.contrib.auth.models import User
from paytask.models import Student, Teacher, Notice, Performance


#admin signup form
class AdminSignUp(forms.ModelForm):
  class Meta:
    model=User
    fields=['first_name', 'last_name','username', 'password']


#student form
class StudentForm(forms.ModelForm):
  class Meta:
    model=User
    fields=['first_name', 'last_name', 'username', 'password']
class StudentExtra(forms.ModelForm):
  class Meta:
    model = Student
    fields=['roll', 'cl', 'mobile', 'fee', 'status']


#teacher form
class Teacher(forms.ModelForm):
  class Meta:
    model=User
    fields=['first_name','last_name','username','password']
class TeacherExtra(forms.ModelForm):
  class Meta:
    model= Teacher
    fields=['salary','mobile','status']


#attendance form
presence_choices=(('Present','Present'))
class AttendanceForm(forms.Form):
  present_status= forms.ChoiceField(choices=presence_choices)
  date= forms.DateField()

class AskDateForm(forms.Form):
  date=forms.DateField()


#notice form
class NoticeForm(forms.ModelForm):
  class Meta:
    model= Notice
    fields='__all__'


#performance form
class PerformanceForm(forms.ModelForm):
  class Meta:
    model = Performance
    fields='__all__'


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))