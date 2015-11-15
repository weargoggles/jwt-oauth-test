from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def test(request):
    request.session['test'] = True
    if request.method == "POST":
        request.session['posted'] = request.POST['posted']
    return render_to_response('test.html', RequestContext(request))
