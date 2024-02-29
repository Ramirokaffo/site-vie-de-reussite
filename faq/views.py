from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from faq.models import FaqModel

def index(request: WSGIRequest):

    context = {}

    questions = FaqModel.objects.all()
    context["questions"] = questions
    return render(request, "appointment/add_success.html", context)
    return render(request, "faq/index.html", context)
