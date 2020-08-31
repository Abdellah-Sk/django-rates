from django.shortcuts import render, HttpResponse

import api

# Create your views here.
def dashboard(request, days_range=60, currencies="CAD"):

    days, rates = api.get_rates(curriences=currencies.split(","), days=days_range)

    return render(request, "stats/index.html", context={"data": rates,
                                                        "days_labels": days})