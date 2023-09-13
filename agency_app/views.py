from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    all_reservation = Reservation.objects.all()
    return render(request, 'admin/Reservationpage.html',
                  {'reservation': all_reservation})


def offre_fetch(request):
    all_offre = Offre.objects.all()
    return render(request, 'admin/Categorypage.html',
                  {'offre': all_offre})