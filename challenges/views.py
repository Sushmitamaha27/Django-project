from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound,HttpResponseRedirect


Monthly_challenges={
    "january":"Eat no meat for entire month",
    "febuary":"walk atleat for 20 min every day!",
    "march":"learn django atleat for 20 min every day!",
    "April":"learn django atleat for 20 min every day!",
    "may":"learn django atleat for 20 min every day!",
}

# Create your views here.
def Monthly_challenges_by_number(request,month):
    months=list(Monthly_challenges.keys())

    if month >len(months):
        return HttpResponseNotFound("Invalid month")



    redirect_month=months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenges(request,month):
    try:
        challenge_text=monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
   