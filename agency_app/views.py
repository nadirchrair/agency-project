from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login


# Create your views here.
@login_required(login_url='login'
                )  # Replace 'login' with your actual login URL
def index(request):
    all_reservation = Reservation.objects.all()
    return render(request, 'admin/Reservationpage.html',
                  {'reservation': all_reservation})


#offfre fetch


@login_required(login_url='login'
                )  # Replace 'login' with your actual login URL
def offre_fetch(request):
    all_offre = Offre.objects.all()
    return render(request, 'admin/Offrepage.html', {'offre': all_offre})


# offfre details


@login_required(login_url='login'
                )  # Replace 'login' with your actual login URL
def offre_details(request, id):
    offre_details = Offre.objects.get(id=id)
    return render(request, 'admin/Offrepagedetails.html',
                  {'offre_details': offre_details})


#add offfre


@login_required(login_url='login'
                )  # Replace 'login' with your actual login URL
def add_ofrre(request):
    if request.method == 'POST':
        form = OffreForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.username = request.user
            form.save()
            # You may want to redirect to a different page after successful form submission.
            return redirect('offre')
    else:
        form = OffreForm()
    return render(request, 'admin/ajouteroffre.html', {'form': form})


#update offfre
@login_required(login_url='login'
                )  # Replace 'login' with your actual login URL
def updateoffre(request, id):
    offre_details = Offre.objects.get(id=id)
    if request.method == 'POST':
        form = OffreForm(request.POST, request.FILES, instance=offre_details)
        if form.is_valid():
            form.save()
            # You may want to redirect to a different page after successful form submission.
            return redirect('offre')
    else:
        form = OffreForm(instance=offre_details)
    return render(request, 'admin/updateoffre.html', {'form': form})


## delete ofrre
@login_required(login_url='login'
                )  # Replace 'login' with your actual login URL
def deleteoffre(request, id):
    offre = Offre.objects.get(id=id)
    offre.delete()
    return redirect('offre')


############ authentication (login signup logout)


def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            # Superuser login successful, perform login and redirect to a success page
            login(request, user)
            return redirect('home')
        else:
            # Authentication failed, show an error message
            return render(request, 'login.html',
                          {'error': 'Invalid credentials'})
    else:
        # Render the login form
        return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in the new user
            return redirect('login')  # Redirect to a success page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



