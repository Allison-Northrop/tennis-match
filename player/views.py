from django.shortcuts import render
from django.utils import timezone
from .forms import Player_AttributesForm
from .models import Player_Attributes
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from .forms import Player_AttributesForm
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.
# @login_required
def player_signin(request): #the home page
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

def player_list(request):
    players = Player_Attributes.objects.filter()
    return render(request, 'player/player_list.html', {'players': players})

@login_required
def player_details(request, pk):
    # player_object = get_object_or_404(Player_Attributes, pk=request.session['player_id'])
    players = Player_Attributes.objects.filter(pk=pk) #note to self, this pk=pk thing is the way to get individual items specific to the user popping up.
    return render(request, 'player/player_details.html', {'players': players})

@login_required
def player_attributes_new(request):
    # player = get_object_or_404(Player_Attributes, pk=request.session['player_id'])
    if request.method == "POST":
        form = Player_AttributesForm(request.POST)
        if form.is_valid():
            player = form.save()
            request.session['player_id'] = player.pk
            # player.save()
            return redirect(player_details, pk=player.pk)
    else:
        form = Player_AttributesForm()
    return render(request, 'player/player_attributes_edit.html', {'form': form})

@login_required #edits existing profile
def player_attributes_edit(request, pk):
    player = get_object_or_404(Player_Attributes, pk=pk)
    if request.method == "POST":
        form = Player_AttributesForm(request.POST, instance=player) #this is the thing I need for the new one
        if form.is_valid():
            player = form.save(commit=False)
            player.save()
            return redirect('player_details', pk=player.pk)
    else:
        form = Player_AttributesForm(instance=player)
    return render(request, 'player/player_attributes_edit.html', {'form': form})

@login_required
def player_attributes_remove(request, pk): #removes existing profile
    player = get_object_or_404(Player_Attributes, pk=pk)
    player.delete()
    return render(request, 'player/player_signin.html', {})
