from django.db import models

class Words(models.Model):
    word = models.CharField(max_length=5, unique=True)
    possible_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.word

class Guess(models.Model):
    guess = models.CharField(max_length=5)
    colors = models.JSONField(default=list)

    def __str__(self):
        return self.guess
    
    def split_guess(self):
        result = []
        for i in range(len(self.guess)):
            result.append(self.guess[i])
        return result
    
    def get_colors(self):
        return self.colors

class Suggestion(models.Model):
    suggestion = models.CharField(max_length=5)

    def __str__(self):
        return self.suggestion

    def update_suggestion(word, letter, color):
        pass
