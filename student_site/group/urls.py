from django.urls import path

from .views import group_form, group_list, teacher_form, teacher_list, start

urlpatterns = [
    path("teacher", teacher_form, name="teacher_form"),
    path("teachers", teacher_list, name="teacher_list"),
    path("group", group_form, name="group_form"),
    path("groups", group_list, name="group_list"),
    path("", start, name="start"),
]
