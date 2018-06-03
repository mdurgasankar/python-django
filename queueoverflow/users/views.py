from django.shortcuts import render,redirect
from django.views.generic import (TemplateView)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from . import models
# Create your views here.


class IndexView(TemplateView):
    template_name='registration/login.html'


class HomeView(TemplateView):
    template_name = 'home.html'
    #context_object_name  = 'question_list'
    model  = models.Question

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password= password)
            login(request, user)
            return redirect('/home')
    else:
        form = UserCreationForm(request.POST)

    return render(request, 'registration/login.html', {'form':form})
