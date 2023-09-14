from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>This is home Page</h1>')   

def about(request):
    context = {
        'variable1':'this is Javed Sir',
        'variable2':'He is IT Teacher',
    }
    return render(request,'j1.html',context)