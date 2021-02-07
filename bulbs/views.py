from django.shortcuts import render
from bulbs.BulbController import BulbController

# Create your views here.
def controls(request):
    return render(request, 'bulbs/index.html')

def off(request):
    bc = BulbController("Uno","Dos")
    bc.bulb_off()
    return render(request, 'bulbs/index.html')

def on(request):
    bc = BulbController("Uno","Dos")
    bc.bulb_on()
    return render(request, 'bulbs/index.html')

def red(request):
    bc = BulbController("Uno","Dos")
    bc.turn_red()
    return render(request, 'bulbs/index.html')

def blue(request):
    bc = BulbController("Uno","Dos")
    bc.turn_blue()
    return render(request, 'bulbs/index.html')

def color(request):
    bc = BulbController("Uno","Dos")
    bc.turn_color(hue=255,saturation=100,value=100)
    return render(request, 'bulbs/index.html')
