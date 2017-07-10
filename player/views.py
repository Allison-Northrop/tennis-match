from django.shortcuts import render

# Create your views here.
def player_signup(request):
    return render(request, 'player/player_signup.html', {})
