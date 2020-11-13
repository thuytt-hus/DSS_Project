from django.http import HttpResponse
from django.shortcuts import render
from .models import Student


def index(request):
    return render(request, 'polls/index.html', {'students': Student.objects.all()})
