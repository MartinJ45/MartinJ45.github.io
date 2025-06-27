from django.db import models

class Words(models.Model):
    word = models.CharField(max_length=5, unique=True)
    possible_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.word
