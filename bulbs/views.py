from django.shortcuts import render
from bulbs.BulbController import BulbController
import math

# Create your views here.
def controls(request):
    return render(request, 'bulbs/index.html')

def off(request):
    try:
        bc = BulbController("One","Two")
        bc.bulb_off()
        return render(request, 'bulbs/index.html', {'message': 'Success', 'color': 'green'})
    except Exception as e:
        return render(request, 'bulbs/index.html', {'message': 'Bulbs not responding', 'color': 'red'})

def on(request):
    try:
        bc = BulbController("One","Two")
        bc.bulb_on()
        return render(request, 'bulbs/index.html', {'message': 'Success', 'color': 'green'})
    except Exception as e:
        return render(request, 'bulbs/index.html', {'message': 'Bulbs not responding', 'color': 'red'})

def red(request):
    try:
        bc = BulbController("One","Two")
        bc.turn_red()
        return render(request, 'bulbs/index.html', {'message': 'Success', 'color': 'green'})
    except Exception as e:
        return render(request, 'bulbs/index.html', {'message': 'Bulbs not responding', 'color': 'red'})

def blue(request):
    try:
        bc = BulbController("One","Two")
        bc.turn_blue()
        return render(request, 'bulbs/index.html', {'message': 'Success', 'color': 'green'})
    except Exception as e:
        return render(request, 'bulbs/index.html', {'message': 'Bulbs not responding', 'color': 'red'})

def color(request):
    rgb = hex_to_rgb(request.POST['color'])
    print("\n", "HEX {}".format(request.POST['color']))
    print("\n", "RGB {}".format(rgb))
    hsv = rgb_to_hsv(rgb[0], rgb[1], rgb[2])
    print("\n", "HSV {}".format(hsv))
    print("{} {} {}".format(math.floor((hsv[0]*100)*3.5),math.floor(((hsv[1]*100)/255)*100),math.floor(((hsv[2]*100)/255))))
    try:
        bc = BulbController("One","Two")
        bc.turn_color(hue=math.floor(hsv[0]),saturation=math.floor(hsv[1]),value=math.floor(hsv[2]))
        return render(request, 'bulbs/index.html', {'message': 'Success', 'color': 'green'})
    except Exception as e:
        return render(request, 'bulbs/index.html', {'message': 'Bulbs not responding', 'color': 'red'})

# color helpers
def hex_to_rgb(hex_val):
    h = hex_val.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hsv(r, g, b):
    R_dash = r / 255
    G_dash = g / 255
    B_dash = b / 255
    Cmax = max(R_dash, G_dash, B_dash)
    Cmin = min(R_dash, G_dash, B_dash)
    delta = Cmax - Cmin
    if (delta == 0):
        H = 0
    elif (Cmax == R_dash):
        H = (60 * (((G_dash  - B_dash) / delta) % 6))
    elif (Cmax == G_dash):
        H = (60 * (((B_dash  - R_dash) / delta) + 2))
    elif (Cmax == B_dash):
        H = (60 * (((R_dash  - G_dash) / delta) + 4))

    if (Cmax == 0):
        S = 0
    else:
        S = delta / Cmax
    V = Cmax
    return (H, S*100, V*100)
