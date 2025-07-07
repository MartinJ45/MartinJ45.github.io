from django import forms
from django.core.exceptions import ValidationError
from Website.core.models import Words, Guess

class GuessForm(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['guess'].required = False

    def clean_guess(self):
        guess = self.cleaned_data.get('guess')
        if Words.objects.filter(word=guess.lower()).exists() or guess == "":
            return guess
        else:
            raise ValidationError("Not in word list")
    
    def split_guess(guess):
        result = []
        for i in range(len(guess)):
            result.append(guess[i].upper())
        return result
    
    class Meta:
        model = Guess
        fields = ['guess']
