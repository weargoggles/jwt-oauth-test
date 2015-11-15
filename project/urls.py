from django.conf.urls import url
import project.test.views as test_views
import project.home.views as home
import project.login.views as login
import project.hooks.views as hooks

urlpatterns = [
    url(r'^test/$', test_views.test),
    url(r'^$', home.home, name='home'),
    url(r'^login/$', login.login, name='login'),
    url(r'^login/callback/$', login.login_callback, name='login-callback'),
    url(r'^hook/$', hooks.receive_hook, name='receive-hook'),
]
