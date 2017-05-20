from django.shortcuts import render
from registerapp.forms import LoginForm
from registerapp.models import Login
from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.
def get_clients(request):
	return render(request, 'getclients.html')

def model_form(request):
	return render(request, 'modelform.html')

def login(request):
	# return render(request, 'Login.html')
    username = "not logged in"
    print username

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            print username
    else:
        MyLoginForm = LoginForm()
    if Login.objects.filter(username=username).exists():
        return render(request, 'modelform.html', {"username": username})
    else:
        return HttpResponseBadRequest("username or password is wrong")