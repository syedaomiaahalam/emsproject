from django.forms import widgets
from django.forms.models import ModelFormMetaclass
from .models import *
from django import forms
from django.contrib.auth.models import Group, User

class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields =['cause_of_leave','start_date','end_date']

        widgets = {
            'cause_of_leave':forms.Textarea(attrs={'class':'bg-light form-control'}),
            'start_date':forms.DateInput(attrs={'type':'date', 'class':'bg-light form-control datepicker'}),
            'end_date':forms.DateInput(attrs={'type':'date', 'class':'bg-light form-control datepicker'})
        }





class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'
        exclude = ('user','pending_status','working_status','done_status')
        
        widgets = {
           
           'what_to_do':forms.TextInput(attrs = {'class':'form-group  bg-light col-md-5 p-3'}),
           'when_to_do':forms.DateInput(attrs = {'type':'date','class':'form-group  date-picker col-md-3 p-3'})

        }




class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class':'p-3 rounded border-0 form form-group bg-light col-md-3 mt-3','placeholder':"Enter password..."}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class':'p-3 rounded border-0 form form-group bg-light col-md-3 mt-3','placeholder':"Enter password again..."}))
    department = forms.ModelChoiceField(widget = forms.Select(attrs ={'class':'p-3 rounded border-0 form form-group bg-light col-md-5'} ) , queryset = Department.objects.all() )
    designation = forms.ModelChoiceField(widget = forms.Select(attrs ={'class':'p-3 rounded border-0 form form-group bg-light col-md-5'} ) , queryset = Group.objects.all() )
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password','confirm_password','department','designation']
        help_texts = {
            'username':None,
            'password':None,
            'email':None
            }


        widgets = {
            'first_name':forms.TextInput(attrs={'class':'mr-4 p-3 rounded border-0 form form-group  col-md-5','placeholder':"Enter First Name..."}),
            'last_name':forms.TextInput(attrs={'class':'p-3 border-0 form form-group col-md-5','placeholder':"Enter Last Name..."}),
            'email': forms.TextInput(attrs = {'class':'p-3 rounded border-0 form form-control bg-light col-md-12','placeholder':"Enter Email..."}),
            'username':forms.TextInput(attrs={'class':'p-3 rounded border-0 form form-group bg-light col-md-3 mt-3','placeholder':"Enter Username..."})
            
        }