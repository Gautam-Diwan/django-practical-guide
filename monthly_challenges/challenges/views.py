from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "Run for an hour daily",
    "february": "Try a new recipe each week",
    "march": "Learn a new language for 15 minutes every day",
    "april": "Do 30 minutes of yoga each morning",
    "may": "Read a book for at least 30 minutes every day",
    "june": "Write a short story or poem every week",
    "july": "Practice a musical instrument for 30 minutes daily",
    "august": "Learn a new skill through online courses",
    "september": "Take a photo every day and create a photo journal",
    "october": "Complete a daily drawing challenge",
    "november": "Write down three things you're grateful for each day",
    # "december": "Do a daily act of kindness for others",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month < 0 and month >= len(months):
        return HttpResponseNotFound("Invalid Month Number")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()
