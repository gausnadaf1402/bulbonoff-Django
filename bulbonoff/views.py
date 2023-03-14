from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        return render(request, "bulbon.html")
    else:
        return render(request, "bulboff.html")