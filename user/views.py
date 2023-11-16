from django.shortcuts import render, get_object_or_404, redirect
from ppm.models import Activite, Contact, Reservation
from ppm.forms import ReservationForm
#
# from django.shortcuts import render, redirect
# from ppm.models import Activite
# from ppm.forms import ReservationForm

def index(request):
    activites = Activite.objects.all()
    reservations = Reservation.objects.all()  # Récupérer toutes les réservations
    form = ReservationForm()  # Créer une instance de formulaire de réservation vide
    return render(request, 'user/index.html', {'activites': activites, 'reservations': reservations, 'form': form})

def search(request):
    query = request.GET.get('q')
    activites = Activite.objects.filter(nom__icontains=query)
    return render(request, 'user/index.html', {'activites': activites})

def detail(request, activite_id):
    activite = get_object_or_404(Activite, pk=activite_id)
    return render(request, 'user/detail.html', {'activite': activite})

def reservation(request, activite_id):
    activite = get_object_or_404(Activite, pk=activite_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.activite = activite
            reservation.save()
            return redirect('user:index')
    else:
        form = ReservationForm()
    return render(request, 'user/reservation.html', {'activite': activite, 'form': form})


def tri(request):
    sort_by = request.GET.get('sort_by', 'default')

    if sort_by == 'price':
        activites = Activite.objects.all().order_by('prix')
    elif sort_by == 'popularity':
        activites = Activite.objects.all().order_by('-capacite_max')  # You might need a different popularity metric
    else:
        activites = Activite.objects.all()

    return render(request, 'user/tri.html', {'activites': activites, 'sort_by': sort_by})


def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'user/contact.html', {'contacts': contacts})
