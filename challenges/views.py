from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

# def index(request):
#      return HttpResponse("Hi, This is the index")
#     #return render(request, 'home.html',{})

# def february(request):
#     return HttpResponse("<h1>Walk at least 20 minutes in a day....</h1>")

def udemy(request, month):
    challenge_text = None
    if month == "january":
          challenge_text = 'Read a book at least 20 minutes per day!'
    elif month == 'february':
          challenge_text = "<h1>Walk at least 20 minutes in a day....</h1>"
    elif month == 'march':
         challenge_text = "Learn Django for a 20 minutes daily."
    else:
         return HttpResponseNotFound("This month is not supported...")
     
    return HttpResponse(challenge_text)
