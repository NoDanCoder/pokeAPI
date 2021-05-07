from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pokebase as pb
from .fetching import APIChainResource

import time

# Create your views here.
def chainView(resquest):

    # import pdb; pdb.set_trace()
    # t0 = time.time()

    data = APIChainResource('evolution-chain', 10)

    # t1 = time.time()

    # print((t1 - t0) * 100)

    return JsonResponse(data.data_fetch)