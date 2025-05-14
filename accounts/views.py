from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from .forms import SignupForm, SigninForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    signup_form = SignupForm() 

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  

    signin_form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  



    context = {'form': signup_form, 'signin':signin_form}

    return render(request, 'auth.html', context)


def signout(request):
    logout(request)
    return redirect('signup')

def consultation(request):
    return render(request, 'consultation.html')