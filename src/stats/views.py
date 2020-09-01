from django.shortcuts import render, HttpResponse

import api

# Create your views here.
def dashboard(request, days_range=60, currencies="CAD"):

    days, rates = api.get_rates(curriences=currencies.split(","), days=days_range)
    page_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "Personnalisé")

    return render(request, "stats/index.html", context={"data": rates,
                                                        "days_labels": days,
                                                        "page_label": page_label})