import requests
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    repos_response = requests.get('https://api.github.com/v3/user/repos', headers={
        'Authorization': 'token %s' % request.session['github']['access_token'],
        'Accept': 'application/json',
    })
    if repos_response.status_code == 200:
        repos = repos_response.json()
        error = ''
    else:
        repos = []
        error = repos_response.content
    return render_to_response("home.html", {
        'repos': repos,
        'error': error,
    }, RequestContext(request))
