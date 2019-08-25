from django.urls import path
from calculator.views import add, sub, div, mul, calculations_list, calculation_details

urlpatterns = [
    path("", calculations_list, name="calculations"),
    path("<int:id>", calculation_details),
    path("add/<int:x>/<int:y>", add),
    path("sub/<int:x>/<int:y>", sub),
    path("mul/<int:x>/<int:y>", mul),
    path("div/<int:x>/<int:y>", div),
]
