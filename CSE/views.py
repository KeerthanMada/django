from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def products(request):
    return render(request,'products.html')

def service(request):
    return render(request,'service.html')

def AboutUs(request):
    return render(request,'AboutUs.html')

def contact(request):
    return render(request,'contact.html')

def contact(request):
    return render(request, 'student.html')



