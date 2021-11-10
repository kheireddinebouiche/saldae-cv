from django.shortcuts import render





def index(request):
    return render(request, 'front/index.html')

def MonProfile(request):
    return render(request,'front/mon-profile.html')

def cv_1(request):
    return render(request, 'front/cv/srt-resume.html')
