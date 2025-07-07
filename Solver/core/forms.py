from django import forms
from django.core.exceptions import ValidationError
from Solver.core.models import Words

class GuessForm(forms.Form):
    guess = forms.CharField(max_length=5, required=False)

    def clean_guess(self):
        guess = self.cleaned_data.get('guess')
        if Words.objects.filter(word=guess.lower()).exists() or guess == "":
            return guess
        else:
            raise ValidationError("Not in word list")
    
    def split_guess(guess):
        return [char.upper() for char in guess]
