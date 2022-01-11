 from django.shortcuts import render, redirect
 from .forms import SignupForm
 from django.contrib.auth import login, authenticate
 from django.contrib.auth.decorators import login_required
 from .models import NeighbourHood
 from .models import NeighbourHood, Profile
 from .forms import UpdateProfileForm
 from django.contrib.auth.models import User


 @login_required(login_url='login')
def index(request):
    return render(request, 'index.html')
 
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
   
def hoods(request):
    all_hoods = NeighbourHood.objects.all()
  
    params = {
        'all_hoods': all_hoods
    }
    return render(request, 'all_hoods.html', params)
   
def profile(request, username):
    return render(request, 'profile.html')


 def edit_profile(request, username):
     form = UpdateProfileForm()
     user = User.objects.get(username=username)
     if request.method == 'POST':
         form = UpdateProfileForm(request.POST)

     else:
         form = UpdateProfileForm()
     return render(request, 'editprofile.html', {'form': form})
