from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class UserDetailsForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'address', 'city', 'state', 'zip_code', 'country')
    