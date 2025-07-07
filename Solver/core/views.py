from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from django.http import JsonResponse, HttpResponse
import json

from Website.core.models import Words, Guess
from Website.core.forms import GuessForm

class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        form = GuessForm()
        guesses = request.session.get('guesses', [])
        colors = request.session.get('colors', [])
        all_guesses = []
        split_guesses = []
        for i in range(len(guesses)):
            split_guesses.insert(0, GuessForm.split_guess(guesses[i]))
            all_guesses.insert(0, zip(GuessForm.split_guess(guesses[i]), colors[i]))
        all_suggestions = []

        zipped = zip(split_guesses, all_guesses)

        print("GUESS", guesses)
        print("COLORS", colors)

        return render(request, self.template_name, context={
            'form' : form,
            'guesses' : zipped,
            'suggestions' : all_suggestions,
        })
    
    def post(self, request):
        form = GuessForm(request.POST)
        action = request.POST.get('action')
        try:
            if not request.body:
                data = {}
            else:
                data = json.loads(request.body)
        
        except json.JSONDecodeError:
            data = {}

        if action == 'clear':
            if 'guesses' in request.session:
                del request.session['guesses']
            if 'colors' in request.session:
                del request.session['colors']
        else:
            if data and data['action'] == 'update':
                if 'colors' in request.session:
                    del request.session['colors']
                
                print("DATA", data)

                colors = request.session.get('colors', [])
                for d in data['words']:
                    color = d[1]
                    colors.insert(0, color)
                
                request.session['colors'] = colors
                request.session.modified = True

                ###############

                guesses = request.session.get('guesses', [])
                colors = request.session.get('colors', [])

                print("GUESS", guesses)
                print("COLORS", colors)

                return JsonResponse({'status': 'success'})
            
            if form.is_valid():
                cleaned_guess = form.cleaned_data['guess']
                guesses = request.session.get('guesses', [])
                guesses.append(cleaned_guess)
                request.session['guesses'] = guesses

                colors = request.session.get('colors', [])
                colors.append(['none', 'none', 'none', 'none', 'none'])
                request.session['colors'] = colors

                request.session.modified = True

                return redirect('home')
        
        guesses = request.session.get('guesses', [])
        colors = request.session.get('colors', [])
        all_guesses = []
        split_guesses = []
        for i in range(len(guesses)):
            split_guesses.insert(0, GuessForm.split_guess(guesses[i]))
            all_guesses.insert(0, zip(GuessForm.split_guess(guesses[i]), colors[i]))
        all_suggestions = []

        zipped = zip(split_guesses, all_guesses)

        print("GUESS", guesses)
        print("COLORS", colors)
        
        return render(request, self.template_name, context={
            'form' : form,
            'guesses' : zipped,
            'suggestions' : all_suggestions,
        })
