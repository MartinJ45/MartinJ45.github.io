from django.shortcuts import render
from django.views import View

from Website.core.models import Words

class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        w = request.GET.get("w", "crane")

        if Words.objects.filter(word=w).exists():
            word = w.capitalize()
        else:
            word = "This word is not in Wordle"

        return render(request, self.template_name, context={
            "word" : word,
        })
