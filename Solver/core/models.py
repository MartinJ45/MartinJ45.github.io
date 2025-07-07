from django.db import models

class Words(models.Model):
    word = models.CharField(max_length=5, unique=True)
    possible_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.word

class Suggestion(models.Model):
    suggestion = models.CharField(max_length=5)

    def __str__(self):
        return self.suggestion

    def update_suggestion(word, letter, color):
        pass
