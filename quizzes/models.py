from django.db import models

# Create your models here.
DIFF_CHOICES = (
    ('Easy','Easy'),
    ('Medium','Medium'),
    ('Hard','Hard'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Duration of The Quiz in Munites")
    required_score_to_pass = models.IntegerField(help_text="Score in  %")
    Difficluty = models.CharField(max_length=6,choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"
    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions]
    
    class Meta:
        verbose_name_plural = 'Quizzes'
