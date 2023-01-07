from django import forms
from django.forms import ModelForm
from .models import Recommendation
from django.contrib.auth.models import User
# Create opinion form



class RecommendationForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "class": "form-control"}))
    rating = forms.ChoiceField(choices=Recommendation.RatingChoices.choices, widget=forms.Select(attrs={"class": "form-select"}))
    
    class Meta:
        model = Recommendation
        fields = ('title', 'content', 'rating')
    
    
class UserDetailsForm(ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'