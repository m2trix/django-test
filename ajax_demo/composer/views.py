from django.shortcuts import render_to_response, get_object_or_404
from django.http import JsonResponse
import requests
import json

# Create your views here.
def ajax_view(request):
    dictSet = request.GET.dict()
    print(dictSet)
    context = {'code':0}

    if request.is_ajax():
        r = requests.get('http://httpbin.org/ip')
        context['code'] = r.status_code
        return JsonResponse(context)

    return render_to_response('ajax_submit.html', context)