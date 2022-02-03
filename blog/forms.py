from django import forms

from blog.models.task import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'description', 'status',)