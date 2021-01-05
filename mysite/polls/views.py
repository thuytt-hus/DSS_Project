from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from django.contrib import messages


def emp(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except:
                pass
        else:
            return render(request, 'polls/create.html', {'form': form})
    else:
        form = StudentForm()
        return render(request, 'polls/create.html', {'form': form})


def index(request):
    user_list = Student.objects.all().order_by('name')
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'polls/index.html', {'students': students})


def edit(request, id):
    return render(request, 'polls/edit.html', {'student': Student.objects.get(id=id)})


def update(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            messages.error(request, "Error")
    else:
        form = StudentForm()
    return render(request, 'polls/edit.html', {'student': student})


def destroy(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/")


def search(request):
    query = request.GET.get('q')
    return render(request, 'polls/search.html', {'students': Student.objects.filter(Q(name__icontains=query))})
