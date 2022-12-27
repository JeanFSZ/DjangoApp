from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import  Room,Alert
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def home(request):
    try:
        rooms = Room.objects.all().filter(user_reservation = request.user.id)
        alerts = Alert.objects.all()
        return render(request, 'room/home.html', {'rooms': rooms, 'alerts': alerts})
    except:
        return render(request, 'room/home.html')
 
def booking(request):
    return render(request, 'room/booking.html',{'rooms': Room.objects.all})    

def register(request):
    return render(request, 'registration/signup.html') 

##
## class RoomListView (TemplateView):
##     template = 'room/list.html'