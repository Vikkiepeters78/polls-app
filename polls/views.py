from django.shortcuts import render
from .models import Question, Choice, Student

# Create your views here.





def index(request):
    questions = Question.objects.all()
    choices = Choice.objects.all()
    data = Student.objects.all()


    context = {
        'questions': questions,
        'choices': choices,
        'data': data,


    }

    return render(request, "index.html", context)


def contact(request):
    return render(request, "contact.html")


def about(request):
    context = {
        'address': "Area E, Nyanya road.Abuja",
        'contact': "08146124879"
    }

    return render(request, "about.html", context)
