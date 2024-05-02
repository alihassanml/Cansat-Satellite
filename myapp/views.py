from django.shortcuts import render,redirect
from .models import userreg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
import serial
from django.http import JsonResponse
from django.conf import settings

# Create your views here.

def main(request):
    return render(request,'main.html')

def sginup(request):
    if request.method =='POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            reg = userreg(username=username, email=email, password=password)
            if  userreg.objects.filter(username=username,email=email):
                 messages.success(request, 'You Already Have Account! Login Now')
                 return redirect('home')

            elif userreg.objects.filter(username=username):
                messages.success(request, 'Name is Already Taken!')
                return redirect('home')
            else:
                reg.save()
            return redirect('login')
    return render(request, 'sginup.html')



def login(request):
    if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if  not userreg.objects.filter(password=password ,username=username):
                messages.success(request,'Please Enter Correct!')
            
            else:
                fname =userreg.username
                return redirect( 'index')
    fname =request.POST.get('username')
    return render(request, 'login.html',{"fname":fname})



def index(request):
    # import serial
    # ser = serial.Serial('COM6', 9600)
    # data = ser.readline().decode().strip()
    # print(data)

    # components = data.split()

    # ltitude = components[1]
    # longuted = components[3]
    # ,{'ltitude':ltitude,'longuted':longuted}
    return render(request,'index.html')



def map(request):
    # import serial
    # ser = serial.Serial('COM6', 9600)
    # data = ser.readline().decode().strip()
    # print(data)

    # components = data.split()

    # ltitude = components[1]
    # longuted = components[3]
    # print(ltitude)
    # print(longuted)
    # ,{'ltitude':ltitude,'longuted':longuted}
    return render(request, 'map.html')

def groups(request):
     return render(request,'groups.html')

def profile(request):
     return render(request,'profile.html')

def rounder(request):
     return render(request,'rounder.html')


def contact(request):
     return render(request,'contact.html')


def feature(request):
     return render(request,'feature.html')

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

def values(request):
    data = 0
    try:
        ser = serial.Serial('COM7', 9600)
        while True:
            data = ser.readline().decode().strip()  
            components = data.split() 
            print(data)
            return JsonResponse(data)

            if len(components) == 4:
                pressure, temperature, location = components[:3]
                print("Pressure:", pressure)
                print("Temperature:", temperature)
                print("Location:", location)

    except KeyboardInterrupt:
        ser.close()
        print("Serial port closed.")
    except:
         pass
    return render(request,'values.html',{'data':data})



# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------


def testimnal(request):
     return render(request,'testimnal.html')


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------


def get_serial_data(request):
    try:
        try:
            ser = serial.Serial('COM6', 9600)
            data = ser.readline().decode().strip()
            components = data.split(',')

            temperature = components[0].split(':')[1].strip()
            pressure = components[1].split(':')[1].strip()
            altitude = components[2].split(':')[1].strip()

            print(pressure)
            print(temperature)
            print(altitude)
        
            return JsonResponse({'pressure': pressure, 'temperature': temperature,'altitude':altitude })
        
            # 2nd------------------------------------

        except:
            ser = serial.Serial('COM7', 9600)
            data = ser.readline().decode().strip()
            components = data.split(',')

            temperature = components[0].split(':')[1].strip()
            pressure = components[1].split(':')[1].strip()
            altitude = components[2].split(':')[1].strip()

            print(pressure)
            print(temperature)
            print(altitude)
        
            return JsonResponse({'pressure': pressure, 'temperature': temperature,'altitude':altitude })

    # 2nd------------------------------------
        

    except serial.SerialException:
        return JsonResponse({'error': 'Seria`l port not available'})
    return render(request,'get_serial_data.html')


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
import base64

def image(request):
    ser = serial.Serial('COM6', 9600)
    data = ser.readline().decode().strip()
    image_base64 = base64.b64encode(data).decode()

    html = f'<img src="data:image/jpeg;base64,{image_base64}">'
    image_path = "/path/to/your/image.jpg"
    context = {'image_path': image_path}
    html = f'<img src="data:image/jpeg;base64,{image_base64}">'
    return HttpResponse(html)


def dashboard(request):
     return render(request,'dashboard.html')