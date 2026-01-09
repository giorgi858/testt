from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .forms import CustomerUserCreationForm, TodoForm
from django.urls import reverse_lazy
from .models import Todo

def home(request):
    Todos = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        form = TodoForm()
    context = { 
                'form': form,
                'todos': Todos
               }
    return render(request, 'home.html', context)

class SignupPageView(generic.CreateView):
    form_class = CustomerUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    
# class FormlistView(generic.ListView):
#     model = Todo
#     template_engine = 'from.html'
    
def myform(request):
    Todos = Todo.objects.all()
    context = {
        'todos': Todos
    }
    return render(request, 'form.html', context)