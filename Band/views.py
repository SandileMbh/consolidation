from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event


# Create your views here.
def home(request):
    """
    Render the home page for the band website.

    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'Band/home.html')


def about(request):
    """
    Render the about page, providing information about the band.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered about page."""
    return render(request, 'Band/about.html')


@login_required
def events(request):
    """
    Render the events page, displaying a list of all upcoming
    events for the band.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered events page, including a list of events
                        retrieved from the database.
    """
    events_list = Event.objects.all().order_by('date')
    return render(request, 'Band/events.html', {'events': events_list})


def register(request):
    """
    Handle user registration by displaying and
    processing the registration form.
    Renders a registration page where users can sign up for an account.
    If the form submission is valid, a new user is created,
    and the user is redirected to the login page.
    A success message is also displayed upon successful registration.

    Args:
        request (HttpRequest): The HTTP request object,
                                which can be either GET or POST.

    Returns:
        HttpResponse: The rendered registration page for GET requests.
        HttpResponseRedirect: A redirect to the login
                                for successful POST requests.

    Template:
        Band/register.html: Displays the registration form and
                            handles form validation errors.
    """
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
