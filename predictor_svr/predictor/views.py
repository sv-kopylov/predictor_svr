from django.http import HttpResponse
from django.shortcuts import render

from .modelkeeper import ModelKeeper
from .preprocessor import str2input
from .postprocessor import prepareOutput
import json

# Create your views here.
globals()['modelkeeper']=ModelKeeper()


def predict(request):
    print(request.GET)
    result = request.GET['query']
    result = str2input(result)
    result = globals()['modelkeeper'].predict(result)
    result = prepareOutput(result)
    return HttpResponse(json.dump(result))
