from django.shortcuts import render
from django.utils import timezone
from .forms import Player_AttributesForm
from .models import Player_Attributes
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse

# Create your views here.
# @login_required
def player_signin(request):
    return render(request, 'player/player_signin.html', {})

# def player_signin(request):
#     return render(request, 'player/player_signin.html', {})

def player_map(request):
    players = Player_Attributes.objects.filter()
    # players = Player_Attributes.objects.all().values()
    # player_list = list(players) #converts QuerySet to list of objects
    # rendered_html = render(request, 'player/player_map.html', {'players': players})
    # return JsonResponse(player_list, safe=False, rendered_html)
    return render(request, 'player/player_map.html', {'players': players})


@login_required
def player_details(request, pk):
    player_object = get_object_or_404(Player_Attributes, pk=pk)
    players = Player_Attributes.objects.filter(pk=pk) #note to self, this pk=pk thing is the way to get individual items specific to the user popping up.
    return render(request, 'player/player_details.html', {'players': players})

@login_required
def player_attributes_new(request):
    if request.method == "POST":
        form = Player_AttributesForm(request.POST)
        if form.is_valid():
            player = form.save()
            player.save()
            return redirect(player_details, pk=player.pk)
    else:
        form = Player_AttributesForm()
    return render(request, 'player/player_attributes_edit.html', {'form': form})
