from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Flight
from .forms import FlightForm

def home(request):
    return render(request, 'home.html')

def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'add.html', {'form': form})

def flight_list(request):
    flightmanage = Flight.objects.all()
    return render(request, 'list.html', {'flightmanage':flightmanage})

def flight_detail(request):
    flight = Flight.objects.all()

    return render(request, 'list.html',
                  {'flight': flight})

def edit_flight(request, id):
    flight = get_object_or_404(Flight, product_id = id)
    if  request.method == 'POST':
        form = FlightForm(request.POST,instance = flight)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm(instance = flight)
    return render(request, 'edit.html', {'form': form})

def delete_flight(request, id):
    flight = get_object_or_404(Flight, product_id = id)
    if request.method == 'POST':
        flight.delete()
        return redirect('flight_list')
    return render(request, 'delete.html', {'flight':flight})

def search_flight(request):
    query = request.GET.get('q')

    flightmanage = Flight.objects.all()
    if query:
        flightmanage = flightmanage.filter(product_name__icontains = query) | flightmanage.filter(supplier_name__icontains = query)
    return render(request, 'search.html', {'flightmanage': flightmanage, 'query': query})