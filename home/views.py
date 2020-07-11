from django.shortcuts import render
from .models import Student
from django.http import HttpResponse


def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {
        'students': students
    })