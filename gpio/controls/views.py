from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import control
import RPi.GPIO as GPIO
from django.urls import reverse
# Create your views here.
def controlpin(request, pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    state = GPIO.input(pin)
    if(state==True):
        GPIO.output(pin, GPIO.LOW)
    else:
        GPIO.output(pin, GPIO.HIGH)
    response = "You are controling pin: %s."
    return HttpResponseRedirect('/')

def index(request):
    control_list = control.objects.all()
    for c in control_list:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(c.pin, GPIO.OUT)
        c.state = GPIO.input(c.pin)
        c.save()
    context = {'control_list': control_list}
    return render(request, 'controls/index.html', context)
