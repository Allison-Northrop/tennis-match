from django.shortcuts import render

# Create your views here.
def player_signin(request):
    return render(request, 'player/player_signin.html', {})
