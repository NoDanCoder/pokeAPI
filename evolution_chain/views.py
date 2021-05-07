from django.shortcuts import render
from django.http import JsonResponse
from .fetching.loader import local_evolution_chain

import pokebase as pb

# Create your views here.
def chainView(resquest, id):
    
    data = local_evolution_chain(id)
    return JsonResponse(data.data_fetch)