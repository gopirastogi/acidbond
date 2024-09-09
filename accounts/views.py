from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm

# Create your views here.

def login(request):
    return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your homepage URL
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})