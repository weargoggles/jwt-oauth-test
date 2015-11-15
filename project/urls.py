from django.conf.urls import url
import project.test.views as test_views

urlpatterns = [
    url(r'^test/', test_views.test),
]
