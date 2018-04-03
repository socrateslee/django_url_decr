from django.conf import settings
from django.urls import resolve
from .urls import urlpatterns

settings.configure()
settings.ROOT_URLCONF = urlpatterns


def test_a_decred():
    assert(resolve('/decred/a/test').func() == 'altered')

def test_a_origin():
    assert(resolve('/origin/a/test').func() == 'a.origin')


def test_b_decred():
    assert(resolve('/decred/b/test').func() == 'altered')

def test_b_origin():
    assert(resolve('/origin/b/test').func() == 'b.origin')
