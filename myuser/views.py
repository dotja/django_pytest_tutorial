from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout


def home(request):
	return render(request, 'myuser/home.html')


def user_signup(request):
	if request.method == 'POST':
		email = request.POST['email']
		name = request.POST['name']
		password = request.POST['password']
		user_model = get_user_model()
		user_obj = user_model.objects.create_user(email=email, name=name)
		user_obj.set_password(password)
		user_obj.save()
		user_auth = authenticate(username=email, password=password)
		login(request, user_auth)
		return redirect('home')
	else:
		return render(request, 'myuser/signup.html')


def user_login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user_auth = authenticate(username=email, password=password)
		login(request, user_auth)
		return redirect('home')
	else:
		return render(request, 'myuser/login.html')


def user_logout(request):
	logout(request)
	return redirect('home')

