from django.db import models
from quizzes.models import Quiz

# Create your models here.
class Questions(models.Model):
    text = models.CharField(max_length=200)
    quiz= models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)
    def get_answers(self):
        return self.answer_set.all()

class Answer (models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=True)
    Question = models.ForeignKey(Questions, on_delete=models.CASCADE,)

    def __str__(self):
        return f'question:{self.text},answer:{self.text},correct{self.correct}'