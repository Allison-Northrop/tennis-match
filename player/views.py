from django.shortcuts import render
from .forms import Player_AttributesForm

# Create your views here.
def player_signin(request):
    return render(request, 'player/player_signin.html', {})

def player_attributes_new(request):
    # if request.method == "POST":
    #     form = Player_AttributesForm(request.POST)
    # if form.is_valid():
    #   player = form.save(commit=False)
    #         # TODO come back here and fill out stuff that will automatically populate like the name
    #     player.save()
    #     return redirect('player_detail', pk=player.pk)
    # else:
    form = Player_AttributesForm()
    return render(request, 'player/player_attributes_edit.html', {'form': form})
