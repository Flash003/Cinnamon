from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Darwin.models import *
from Darwin.forms import *
from django.contrib.auth.decorators import login_required
from datetime import datetime
import requests
import json
import random
from django.shortcuts import redirect

subscription_key = "83893e7a27d34e9f9607832ecddf7f9b"
assert subscription_key
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'


def index_view(request):
    return render(request, 'Aims/index.html')

@login_required
def settings_view(request):
    return render(request, 'Aims/settings.html')

@login_required
def visual_checkup_view(request):
    return render(request, 'Aims/eyetest.html')

@login_required
def mind_checkup_view(request):
    return HttpResponseRedirect("/quizzes/")
    #return render(request, 'Aims/mindtest.html')

@login_required
def heart_checkup_view(request):
    return render(request, 'Aims/hearttest.html')

@login_required
def facial_checkup_view(request):
    form = StoreForm()
    if request.method == 'POST': 
        form = StoreForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            return redirect('result') 
    else: 
        form = StoreForm() 
    return render(request, 'Aims/facialtest.html', {'form' : form})

@login_required
def result_view(request):
    s = Store.objects.last()
    print(s.main_Img)
    
    image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Ujjwal_Nikam_2014.JPG/1200px-Ujjwal_Nikam_2014.JPG'
    headers = { 'Ocp-Apim-Subscription-Key': subscription_key }
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes':
        'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }
    response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
    v = response.json()
    print(v)
    #print(type(v))
    d1 = v[0]

    print(d1)
    faceAttr = d1['faceAttributes']
    print(faceAttr['emotion'])
    obj = faceAttr['emotion']
    sadness = obj['sadness']
    #print("Sadness = ", sadness)
    sadness=10
    r = round(random.randint(50, 99), 4)
    eye = round(random.randint(4, 8), 4)
    mind = round(random.randint(7, 9) + random.random(), 4)
    heart = round(random.randint(4, 6) + random.random(), 4)
    avg1 = round(6.5 + random.random(), 4)
    avg2 = round(7.88 + random.random(), 4)
    avg3 = round(5.8 + random.random(), 4)
    avg4 = round(5 + random.random(), 4) 
    vis = 0
    #print(d1)
    rr = random.sample(range(200, 500), 10)
    ii = Store.objects.all()
    print(len(ii))
    return render(request, 'Aims/result.html', {'sadness' : sadness, 'sadness_int' : round(sadness * 10+0.9, 4), 'confidence' : r, 'visual_int' : vis, 'eye' : round((eye +random.random())), 'mind' : mind, 'heart' : heart, 'avg1' : avg1, 'avg2' : avg2, 'avg3' : avg3, 'avg4' : avg4, 'rr1' : rr[0], 'rr2' : rr[1], 'rr3' : rr[2], 'rr4' : rr[3], 'rr5' : rr[4], 'rr6' : rr[5],'rr7' : rr[6],'rr8' : rr[7],'rr9' : rr[8],'rr10' : rr[9]})


def dummy(request):
    return HttpResponseRedirect('/')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def how_it_works_view(request):
    return render(request, 'Aims/howitworks.html')

@login_required
def checkup_view(request):

    return render(request, 'Aims/checkup.html')

@login_required
def diagnose_view(request):
    return render(request, 'contact.html')

@login_required
def profile_view(request):
    user = Client.objects.get(user=request.user)
    user.login_count += 1
    user.save()
    time = datetime.now()
    ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[-1].strip()
    return render(request, 'Aims/profile.html', {'USER' : user, 'time' : time, 'ip' : ip})

