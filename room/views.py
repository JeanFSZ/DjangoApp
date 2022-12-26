from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User, Room

# Create your views here.
@login_required
def home(request):
    room = Room.objects.get(user_reservation = request.user.id)
    return render(request, 'room/home.html', {'room': room})

def register(request):
    return render(request, 'registration/signup.html')
