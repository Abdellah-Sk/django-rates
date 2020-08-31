from django.shortcuts import render, HttpResponse

import api

# Create your views here.
def dashboard(request):
    days, rates = api.get_rates(curriences=["USD"], days=30)

    return render(request, "stats/index.html", context={"data": rates["USD"],
                                                        "days_labels": days})