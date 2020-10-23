from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return redirect('profile/')

def viewProfile(request):
    context = {
        'intro_message' : 'Hello Lacey'
    }
    return render(request, 'myProfile/index.html', context)
