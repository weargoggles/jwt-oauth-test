from urllib import urlencode

import requests
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from urlparse import urlunparse, urlparse

from django.utils.crypto import get_random_string

GITHUB_AUTH_URL = 'https://github.com/login/oauth/authorize'
GITHUB_AUTH_URL_PARTS = tuple(urlparse(GITHUB_AUTH_URL))[:4]
GITHUB_TOKEN_URL = 'https://github.com/login/oauth/access_token'


def get_github_auth_url_with_query_string(callback_url, state):
    query_string = urlencode({
        'client_id': settings.GITHUB_CLIENT_ID,
        'redirect_uri': callback_url,
        'scope': settings.GITHUB_SCOPES,
        'state': state,
    })
    return urlunparse(GITHUB_AUTH_URL_PARTS + (query_string, ''))


def get_callback_url(request):
    parts = request.scheme, request.get_host(), reverse('login-callback'), '', '', ''
    return urlunparse(parts)


def login(request):
    state = get_random_string(length=32)
    request.session['github'] = {}
    request.session['github']['oauth_state'] = state
    callback_url = get_callback_url(request)
    url = get_github_auth_url_with_query_string(callback_url, state)
    return redirect(url)


def login_callback(request):
    assert request.method == 'GET'
    code, state = request.GET['code'], request.GET['state']
    assert state == request.session['state']
    del request.session['state']
    token_response = requests.post(GITHUB_TOKEN_URL, data={
        'client_id': settings.GITHUB_CLIENT_ID,
        'client_secret': settings.GITHUB_CLIENT_SECRET,
        'code': code,
    }, headers={
        'Accept': 'application/json',
    })
    assert token_response.status_code == 200, token_response.content
    request.session['github'].update(token_response.json())
    return redirect('home')
