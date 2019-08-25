from django.shortcuts import render
from calculator.models import Calculation

# Create your views here.

def add(request, x, y):
    Calculation.objects.create(x=x, y=y, operation="ADD")
    return render(
        request=request,
        template_name="calculator/calculator.html",
        context={'result': x + y}
    )


def sub(request, x, y):
    Calculation.objects.create(x=x, y=y, operation="SUB")
    return render(
        request=request,
        template_name="calculator/calculator.html",
        context={'result': x - y}
    )


def mul(request, x, y):
    Calculation.objects.create(x=x, y=y, operation="MUL")
    return render(
        request=request,
        template_name="calculator/calculator.html",
        context={'result': x * y}
    )


def div(request, x, y):
    Calculation.objects.create(x=x, y=y, operation="DIV")
    if y == 0:
        result = "Nie dziel przez zero"
    else:
        result = x / y
    return render(
        request=request,
        template_name="calculator/calculator.html",
        context={'result': result}
    )


def calculations_list(request):
    if 'x' in request.GET:
        x = request.GET['x']
        operations = Calculation.objects.filter(x=x)
    else:
        operations = Calculation.objects.all()
    return render(
        request=request,
        template_name="calculator/calculator.html",
        context={'operations': operations}
    )

def calculation_details(request, id):
    op = Calculation.objects.get(pk=id)
    return render(
        request=request,
        template_name="calculator/details.html",
        context={'operation': op}
    )
