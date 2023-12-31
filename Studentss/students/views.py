from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Student
from .forms import StudentForm

def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return render(request, 'students/view.html', {
        'student': student
    })

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {
        'form': form
    })

def delete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return HttpResponseRedirect('/')