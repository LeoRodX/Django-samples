from django.http import HttpResponse
from django.shortcuts import render


QUESTIONS = [
    {'question': 'Столица Польши?', 'options': ['Берлин', 'Мадрид', 'Варшава', 'Рим'], 'answer': 'Варшава'},
    {'question': 'Столица Австрии?', 'options': ['Вена', 'Астана', 'Лондон', 'Каракас'], 'answer':
        'Вена'},
    {'question': 'Столица Испании?', 'options': ['Доха', 'Дели', 'Мадрид', 'Тунис'], 'answer':
        'Мадрид'},
]


# Create your views here.
def index(request):
    return render(request, 'css_app/index.html')


def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")


def about(request):
    return render(request, 'css_app/about.html')


# def quiz(request):
#    return render(request, 'css_app/quiz.html')


def result(request):
    return render(request, 'css_app/result.html')


def quiz(request):
    if request.method == 'POST':
         selected_answers = [request.POST.get(f'question_{i + 1}') for i in range(len(QUESTIONS))]
         correct_answers = [q['answer'] for q in QUESTIONS]
         score = sum(1 for i in range(len(selected_answers)) if selected_answers[i] ==
                correct_answers[i])
         return render(request, 'css_app/result.html', {'score': score, 'total': len(QUESTIONS)})
    return render(request, 'css_app/quiz.html', {'questions': QUESTIONS})