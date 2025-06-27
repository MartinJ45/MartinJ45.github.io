import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Website.settings")
django.setup()

from Website.core.models import Words

with open(r"data/valid-wordle-words.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    for line in data:
        try:
            Words.objects.create(word=line.rstrip())
        except django.db.utils.IntegrityError:
            print(f"{line.rstrip()} already in database!")

with open(r"data/wordle-answers.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    for line in data:
        if Words.objects.filter(word=line.rstrip()):
            w = Words.objects.get(word=line.rstrip())
            w.possible_answer = True
            w.save()
