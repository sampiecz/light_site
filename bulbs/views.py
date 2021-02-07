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
    print("\n\n\n", "HSB {}".format(request.POST['color']), "\n\n\n")
    hsv = rgb_to_hsv(rgb[0], rgb[1], rgb[2])
    print("\n\n\n", "{}".format(hsv), "\n\n\n")
    print("{} {} {}".format(math.ceil((hsv[0]*100)*3.5),math.ceil(((hsv[1]*100)/255)*100),math.ceil(((hsv[2]*100)/255))))
    try:
        bc = BulbController("One","Two")
        bc.turn_color(hue=math.ceil((hsv[0]*100)*3.5),saturation=math.ceil(((hsv[1]*100)/255)*100),value=math.ceil(((hsv[2]*100)/255)))
        return render(request, 'bulbs/index.html', {'message': 'Success', 'color': 'green'})
    except Exception as e:
        return render(request, 'bulbs/index.html', {'message': 'Bulbs not responding', 'color': 'red'})

# color helpers
def hex_to_rgb(hex_val):
    h = hex_val.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hsv(r, g, b):
    r = float(r)
    g = float(g)
    b = float(b)
    high = max(r, g, b)
    low = min(r, g, b)
    h, s, v = high, high, high

    d = high - low
    s = 0 if high == 0 else d/high

    if high == low:
        h = 0.0
    else:
        h = {
            r: (g - b) / d + (6 if g < b else 0),
            g: (b - r) / d + 2,
            b: (r - g) / d + 4,
        }[high]
        h /= 6

    return h, s, v
