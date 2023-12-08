from django import forms 
from core.models import Story 

class StoryForm(forms.ModelForm):
    image = forms.FileField()
    class Meta:
        model = Story
        fields = ("image", )