# from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import login as login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import UserProfile
from .forms import SignUpForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'sampleapp/login.html')

# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'sampleapp/signup.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')  # Redirect to login page after signup
        else:
            messages.error(request, "There was an error with your signup.")
    else:
        form = SignUpForm()
    return render(request, 'sampleapp/signup.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'sampleapp/dashboard.html')



def signup(request):
    if request.method == 'POST':
        print("Form submitted!")  # Debugging line
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, email=email, password=password1)
                print(f"User {username} created!")  # Debugging line
                login(request, user)
                return redirect('dashboard')
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'signup.html')
