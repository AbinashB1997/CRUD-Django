from django.shortcuts import render
from django.template.response import TemplateResponse

from .models import Person


def car_detail(request, pk):

    owner_obj = Person.objects.get(pk = pk)
    print('owner_obj = ', owner_obj)

    context = {
        "drivers": owner_obj,
    }

    return render(request, "car_detail.html", context=context)
    # return TemplateResponse(request, "car_detail.html", context=context).render()