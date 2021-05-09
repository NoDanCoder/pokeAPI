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
    except KeyError:
        return JsonResponse({'error': 'Only lookup for pokemon name (not id) and not type of it'}, status=404)
    else:
        return JsonResponse(data, status=200)

    return JsonResponse(pokemon)