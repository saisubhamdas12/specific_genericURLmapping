from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'firstg.html')

def second(request):
    return render(request,'secondG.html')