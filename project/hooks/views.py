import binascii
from cryptography.hazmat.primitives import hmac
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.constant_time import bytes_eq
import cryptography.hazmat.backends
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

crypto_backend = cryptography.hazmat.backends.default_backend()


def verify_signature(request, request_body):
    hmac_hmac = hmac.HMAC(settings.GITHUB_WEBHOOK_SECRET, SHA1, crypto_backend)
    hmac_hmac.update(request_body)
    signature = b'sha1=' + binascii.hexlify(hmac_hmac.finalize())
    return bytes_eq(signature, request.META['HTTP_X_HUB_SIGNATURE'])


@csrf_exempt
def receive_hook(request):
    verify_signature(request, request.body)
    send_mail('Hook from github', request.body, settings.SERVER_EMAIL,
              map(lambda t: t[-1], settings.ADMINS))
    return HttpResponse(status=200)


