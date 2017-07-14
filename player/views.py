from django.shortcuts import render
from django.utils import timezone
from .forms import Player_AttributesForm
from .models import Player_Attributes
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
def player_signin(request):
    return render(request, 'player/player_signin.html', {})

def player_map(request):
    return render(request, 'player/player_map.html', {})

def player_details(request, pk):
    #do i need to find here?
    player_object = get_object_or_404(Player_Attributes, pk=pk)
    players = Player_Attributes.objects.filter(pk=pk) #note to self, this pk=pk thing is the way to get individual items specific to the user popping up.
    return render(request, 'player/player_details.html', {'players': players})

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
