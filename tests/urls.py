from django.conf.urls import include, url, handler404
from django_url_decr import url_decr

def dummy_decr(func):
    def altered_func(*sub, **kw):
        return 'altered'
    return altered_func


urlpatterns = [
    url_decr(r'^decred/a/', include('tests.a.urls'), decr=dummy_decr),
    url_decr(r'^decred/b/', include('tests.b.urls'), decr=dummy_decr),
    url(r'^origin/a/', include('tests.a.urls')),
    url(r'^origin/b/', include('tests.b.urls'))
]
