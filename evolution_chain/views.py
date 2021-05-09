from django.shortcuts import render
from django.http import JsonResponse
from .fetching.pokechain import get_poke_data

import pokebase as pb

# Create your views here.
def chainView(resquest, name):

    try:
        data = get_poke_data(name)
    except (ConnectionError, OSError):
        return JsonResponse({'error': 'Server error'}, status=500)
    else:
        if data.get('error', False):
            return JsonResponse(data, status=404)
        return JsonResponse(data, status=200)

    return JsonResponse(pokemon)