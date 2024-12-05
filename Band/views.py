from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event


# Create your views here.
def home(request):
    return render(request, 'Band/home.html')


def about(request):
    return render(request, 'Band/about.html')


@login_required
def events(request):
    events_list = Event.objects.all().order_by('date')
    return render(request, 'Band/events.html', {'events': events_list})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Band/register.html', {'form': form})
