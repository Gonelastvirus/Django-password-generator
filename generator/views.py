from django.shortcuts import render
from django.http import HttpRequest
from django.contrib import messages
import time
import random
# Create your views here.
def Home(request):
    return render(request,'generator/Home.html')
def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    defult=list('BCDEF0345!&@#$')
    your_name=request.GET.get('your_name')
    your_day=request.GET.get('your_born_day')
    if(your_name or your_day)=='':
        return render(request,'generator/Home.html')
    else:
        concat=your_name+your_day
    if request.GET.get('uppercase'):
        characters.extend(list('AJKLMNOPQRST'))
        names=your_name.upper()
        reverse=names[:1]+concat[::-1]
    if request.GET.get('numbers'):
        characters.extend(list('12789'))
    if request.GET.get('special'):
        characters.extend(list('@#&'))
    names=your_name.upper()
    reverse=names[1:]+concat[::-1]+your_name[:1]
    thepassword=''
    thepassword+=random.choice('@!#$&+-?%/,.^')+reverse[4:]+random.choice(characters)+random.choice(defult)
    return render(request,'generator/password.html',{'password':thepassword})
