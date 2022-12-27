from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from vac.models import Room, Alert


# Create your views here.
@login_required
def home(request):
    try:
        rooms = Room.objects.all().filter(user_reservation=request.user.id)
        alerts = Alert.objects.all()
        return render(request, 'room/home.html', {'rooms': rooms, 'alerts': alerts})
    except:
        return render(request, 'room/home.html')


def booking(request):
    return render(request, 'room/booking.html', {'rooms': Room.objects.all})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {'form': form }

    return render(request, 'registration/signup.html', context)