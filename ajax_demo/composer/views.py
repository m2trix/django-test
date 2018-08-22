from django.shortcuts import render_to_response, get_object_or_404
import requests

# Create your views here.
def ajax_view(request):
    dictSet = request.GET.dict()
    print(dictSet)
    context = {'code':0}
    '''
    r = requests.get('http://httpbin.org/ip')
    context['code'] += r.status_code
    context['code'] = 0
    '''
    if len(dictSet) > 0:
        print('... 1', context)
        r = requests.get('http://httpbin.org/ip')
        context['code'] = r.status_code
        print('... 2', context, r.status_code)
    
    print('... 3', context)
    return render_to_response('ajax_submit.html', context)