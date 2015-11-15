from django.http import HttpResponse


def test(request):
    request.session['test'] = True
    return HttpResponse('test')