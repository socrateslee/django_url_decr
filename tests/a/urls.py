from django.conf.urls import url

urlpatterns = [url(r'^test$', lambda *sub, **kw: 'a.origin')]
