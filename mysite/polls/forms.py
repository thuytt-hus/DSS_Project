from django import forms
from .models import Student
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('studentid', 'name', 'major', 'faculty', 'university', 'location', 'image')
