from django.shortcuts import render, redirect
from .forms import NewUserForm, UserDetailsForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib.auth.forms import AuthenticationForm #add this
from django.http import HttpResponseRedirect
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def register_page(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, 'login/register_page.html', context={"register_form":form})

def login_page(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/home/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name='login/login_page.html', context={"login_form":form})

def logout_page(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/home/")

def profile_page(request, id):
    submitted = False
    if request.method == "POST":
        save_data_details(request, id, f'/account/profile/{request.user.id}')
    else:
        form = UserDetailsForm
        if Profile.objects.filter(user=id).exists():
            profile_details = Profile.objects.get(user=id)
            submitted = True
            form = UserDetailsForm(request.POST or None, instance=Profile.objects.get(user=id))
            return render(request, "Login/profile_page.html", {"form": form, "submitted": submitted, "profile_details": profile_details })
    return render(request, "Login/profile_page.html", {"form": form })

def update_details(request, id):
    profile_details = Profile.objects.get(user=request.user.id)
    form = UserDetailsForm(request.POST or None, instance=profile_details)
    if form.is_valid():
        form.save()
        messages.success(request, f"Your data has been updated")
        return HttpResponseRedirect(f'/account/profile/{request.user.id}')
    else:
        messages.error(request, f"Form is not valid. Check form and correct fields.")
    return render(request, 'Login/profile_page.html', {"form": form, "submitted": submitted})

def save_data_details(request, redirected_path):
    form = UserDetailsForm(request.POST)
    user = request.user
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    address = request.POST['address']
    city = request.POST['city']
    state = request.POST['state']
    zip_code = request.POST['zip_code']
    country = request.POST['country']
    user_details = Profile(user=user, first_name=first_name, last_name=last_name, address=address, city=city, state=state, zip_code=zip_code, country=country)
    if form.is_valid():
        user_details.save()
        messages.success(request, f"Your data has been saved")
        return HttpResponseRedirect(f'{redirected_path}')
    else:
        messages.error(request, f"Form is not valid. Check form and correct fields.")
    
    
