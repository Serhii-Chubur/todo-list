from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_tracker.forms import TaskCreationForm, TagCreationForm
from task_tracker.models import Task, Tag


# Create your views here.
class IndexView(ListView):
    model = Task
    template_name = 'task_tracker/index.html'
    context_object_name = 'tasks'


class TagListView(ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = 'task_tracker/tag_list.html'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = 'task_tracker/task_form.html'

    def get_success_url(self):
        return reverse('task_tracker:index')


class TagCreateView(CreateView):
    model = Tag
    form_class = TagCreationForm
    template_name = 'task_tracker/tag_form.html'

    def get_success_url(self):
        return reverse('task_tracker:tag-list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskCreationForm
    template_name = 'task_tracker/task_form.html'

    def get_success_url(self):
        return reverse('task_tracker:index')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_tracker/index.html'

    def get_success_url(self):
        return reverse('task_tracker:index')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagCreationForm
    template_name = 'task_tracker/tag_form.html'

    def get_success_url(self):
        return reverse('task_tracker:tag-list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'task_tracker/tag_list.html'

    def get_success_url(self):
        return reverse('task_tracker:tag-list')


class TaskCompletedView(ListView):
    model = Task

    def get_object(self, queryset=None):
        return get_object_or_404(Task, pk=self.kwargs.get("pk"))

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.is_done = True
        task.save()
        return redirect("task_tracker:index")


class TaskUndoView(ListView):
    model = Task

    def get_object(self, queryset=None):
        return get_object_or_404(Task, pk=self.kwargs.get("pk"))

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.is_done = False
        task.save()
        return redirect("task_tracker:index")
