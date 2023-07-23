from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'number': 'Номер студента', 
            'name': 'Имя студента',
            'last_name': 'Фамилия студента',
            'email': 'EMAIL',
            'study': 'изучает',
            'gpa': 'Средний балл'
        }
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}), 
            'name': forms.TextInput(attrs={'class': 'form-control'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'study': forms.TextInput(attrs={'class': 'form-control'}), 
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}), 
        }