from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from . import models

class IssueBookForm(forms.Form):
    isbn2 = forms.ModelChoiceField(queryset=models.Book.objects.all(), empty_label="Book Name [ISBN]", to_field_name="isbn", label="Book (Name and ISBN)")
    name2 = forms.ModelChoiceField(queryset=models.Student.objects.all(), empty_label="Name [Branch] [Class] [Roll No]", to_field_name="user", label="Student Details")
    
    isbn2.widget.attrs.update({'class': 'form-control'})
    name2.widget.attrs.update({'class':'form-control'})


class bookupdateform(ModelForm):
        class Meta:
            model = models.Book
            fields = ('name','author','isbn','category','price')



class returnupdateform(ModelForm):
        class Meta:
            model = models.IssuedBook
            fields = ('student_id','isbn','book_return')