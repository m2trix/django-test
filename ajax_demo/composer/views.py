from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import UrlBody
import requests
import json

# Create your views here.
def ajax_view(request):
    context = {}
    print(request)
    print(request.GET.get('body_pk', '1'))

    if request.is_ajax():
        body_pk = request.GET.get('body_pk', '1')
        url_body = get_object_or_404(UrlBody, pk=body_pk)

        # r = requests.get('http://httpbin.org/ip')
        full_url = ""
        if "\'\'" != url_body.url_params:
            full_url = 'http://httpbin.org' + url_body.url_path + "?" + url_body.url_params
        else:
            full_url = 'http://httpbin.org' + url_body.url_path
        print(full_url)

        r = requests.get('full_url: ' + full_url)
        context['code'] = r.status_code
        return JsonResponse(context)

    context['code'] = 0
    context['api_list'] = UrlBody.objects.all()
    return render(request, 'base.html', context)