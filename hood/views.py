from django.shortcuts import render
 from django.shortcuts import render, redirect
 from .forms import SignupForm
 from django.contrib.auth import login, authenticate


 def index(request):
     return render(request, 'index.html')


 def signup(request):
     return render(request, 'registration/signup.html')
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