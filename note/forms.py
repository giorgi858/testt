from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import Todo
from django import forms

class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username")
        
class CustomerUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username")
        
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('task', 'describtion')
        labels = {
        'task': '',
        'describtion': '',
    }
        widgets = {
        'task': forms.TextInput(attrs={
            'class': 'todo-input',
            'placeholder': 'Enter task name...'
        }),
        'describtion': forms.Textarea(attrs={
            'class': 'todo-textarea',
            'rows': 3,
            'placeholder': 'Enter description name...',
        }),
        }    