from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/quizzes.html'

# def quizzes(request):
#     context = {}
#     return render(request, 'quizzes/quizzes.html', context)

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizzes/quizzes.html', {'obj':quiz})