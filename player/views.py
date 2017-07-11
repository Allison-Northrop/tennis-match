from django.shortcuts import render
from .forms import Player_AttributesForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
def player_signin(request):
    return render(request, 'player/player_signin.html', {})

def player_details(request, pk):
    # player_object = get_object_or_404(Player, pk=pk)
    return render(request, 'player/player_details.html', {})

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
