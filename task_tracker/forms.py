from django import forms

from task_tracker.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('content', 'tags', 'deadline')
        widgets = {'tags': forms.CheckboxSelectMultiple(),
                   'deadline': forms.DateInput(
                       attrs={'type': 'date',
                              'class': 'form-control',
                              'placeholder': 'Select a date'},
                   )}


class TagCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
