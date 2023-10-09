# Create your views here.
from django.shortcuts import render, redirect

from .forms import GroupForm

# Create your views here.
from .forms import TeacherForm
from .models import Group
from .models import Teacher


def start(reqeust):
    return render(reqeust, 'start.html')


def teacher_form(reqeust):
    if reqeust.method == "GET":
        form = TeacherForm()
        return render(reqeust, "teacher_form.html", {"form": form})
    form = TeacherForm(reqeust.POST)
    if form.is_valid():
        form.save()
        return redirect("teacher_list")
    return render(reqeust, "teacher_form.html", {"form": form})


def teacher_list(request):
    teacher = Teacher.objects.all()
    return render(request, "teacher_list.html", {"teacher": teacher})


def group_form(reqeust):
    if reqeust.method == "GET":
        form = GroupForm()
        return render(reqeust, "group_form.html", {"form": form})
    form = GroupForm(reqeust.POST)
    if form.is_valid():
        form.save()
        return redirect("group_list")
    return render(reqeust, "group_form.html", {"form": form})


def group_list(request):
    group = Group.objects.all()
    return render(request, "group_list.html", {"group": group})
