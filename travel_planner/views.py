from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Hebergement, Voyage, Reservation
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import logout as django_logout

@login_required
def liste_voyages(request):
    voyages = Voyage.objects.all()
    return render(request, 'voyage/liste_voyages.html', {'voyages': voyages})

@login_required
def search_voyage(request):
    query = request.GET.get('q')
    if query:
        voyages = Voyage.objects.filter(
            Q(titre__icontains=query) | 
            Q(ville_depart__icontains=query) |
            Q(ville_arrivee__icontains=query)
        )
    else:
        voyages = Voyage.objects.all()
    return render(request, 'voyage/liste_voyages.html', {'voyages': voyages})

@login_required
def detail_voyage(request, voyage_id):  
    voyage = Voyage.objects.get(id=voyage_id)
    return render(request, 'voyage/detail_voyage.html', {'voyage': voyage})

@login_required
def detail_reservation_voyage(request, voyage_id):
    voyage = Voyage.objects.get(id=voyage_id)
    return render(request, 'reservation/detail_reservation_voyage.html', {'voyage': voyage})

@login_required
def detail_reservation_hebergement(request, hebergement_id):
    hebergement = Hebergement.objects.get(id=hebergement_id)
    return render(request, 'reservation/detail_reservation_hebergement.html', {'hebergement': hebergement})

@login_required
def choix_reservation(request):
    reservations = Reservation.objects.filter(utilisateur=request.user)
    return render(request, 'reservation/choix_reservation.html', {'reservations': reservations})

@login_required
def mes_reservations_voyages(request):
    reservations = Reservation.objects.filter(utilisateur=request.user)
    return render(request, 'reservation/mes_reservations_voyages.html', {'reservations': reservations})

@login_required
def mes_reservations_hebergements(request):
    reservations = Reservation.objects.filter(utilisateur=request.user)
    return render(request, 'reservation/mes_reservations_hebergements.html', {'reservations': reservations})

@login_required
def supprimer_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.delete()
    return redirect('choix_reservation')

@login_required
def ajouter_reservation_voyage(request, voyage_id):
    if request.method == 'POST':
        voyage = get_object_or_404(Voyage, pk=voyage_id)
        Reservation.objects.create(voyage=voyage, utilisateur=request.user)
        return HttpResponseRedirect(reverse('mes_reservations_voyages'))

@login_required
def ajouter_reservation_hebergement(request, hebergement_id):
    if request.method == 'POST':
        hebergement = get_object_or_404(Hebergement, pk=hebergement_id)
        Reservation.objects.create(hebergement=hebergement, utilisateur=request.user)
        return HttpResponseRedirect(reverse('mes_reservations_hebergements'))
    
@login_required
def liste_hebergements(request):
    hebergements = Hebergement.objects.all()
    return render(request, 'hebergement/liste_hebergements.html', {'hebergements': hebergements})

@login_required
def search_hebergement(request):
    query = request.GET.get('q')
    if query:
        hebergements = Hebergement.objects.filter(Q(ville__icontains=query))
    else:
        hebergements = Hebergement.objects.all()
    return render(request, 'hebergement/liste_hebergements.html', {'hebergements': hebergements})

@login_required
def detail_hebergement(request, hebergement_id):
    hebergement = Hebergement.objects.get(id=hebergement_id)
    return render(request, 'hebergement/detail_hebergement.html', {'hebergement': hebergement})

@login_required
def destination(request):
    return render(request, 'destination/destination.html',)

@login_required
def search_destination(request):
    query = request.GET.get('q')
    voyages = Voyage.objects.filter(Q(ville_depart__icontains=query) | Q(ville_arrivee__icontains=query))
    hebergements = Hebergement.objects.filter(ville__icontains=query)

    return render(request, 'destination/destination.html', {'voyages': voyages, 'hebergements': hebergements, 'query': query}) 

@login_required
def index(request):
    username = request.user.username
    return render(request, 'index.html', {'username': username})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'authentification/login.html')
    elif request.method == 'GET':
        return render(request, 'authentification/login.html')

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'authentification/signup.html', {'form': form})

def redirect_login(request):
    return render(request, 'dashboard.html')

def my_logout(request):
    django_logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'dashboard.html')
