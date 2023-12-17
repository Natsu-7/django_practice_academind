from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january": "Focus on Crosshair Placement",
    "february": "Focus on 'Move,Aim and then Shoot Protocol'",
    "march": "Focus on K.I.S.S Protocol",
    "april": "Focus on Indvidual Plays",
    "may": "Focus on Minimap",
    "june": "Focus on Tracking",
    "july": "Improvise your mechanics",
    "august": "Win more cluthes",
    "septmeber": "Master Phoenix",
    "october": "Master Yoru",
    "november": "Keep Omen as Substitute",
    "december": "Reach Radiant in No Time"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def month_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponse("Invalid Month")
    forward_month = months[month - 1]
    redirect_path = reverse("monthly_challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def month_challenges(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "challenge": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported yet!</h1>")
