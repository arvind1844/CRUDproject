from socket import fromshare
from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Enter your Name','class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder':'Enter you Email','class':'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Enter your Password','class':'form-control'})
        }
