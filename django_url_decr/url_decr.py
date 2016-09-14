import functools
from django.conf.urls import url
try:
    from django.urls import RegexURLPattern, RegexURLResolver
except ImportError:
    from django.core.urlresolvers import RegexURLPattern, RegexURLResolver


def dummy_decr(func):
    @functools.wraps(func)
    def wrap(*sub, **kw):
        print("Calling %s" % func.__name__)
        ret = func(*sub, **kw)
        return ret
    return wrap


def iter_pattern(pattern):
    '''
    Iterate through patterns.
    '''
    stack = [(0, pattern)]
    while stack:
        level, curr = stack.pop()
        if type(curr) is RegexURLPattern:
            yield level, curr
        elif type(curr) is RegexURLResolver:
            for p in curr.url_patterns:
                stack.append((level + 1, p))
        else:
            raise Exception("Unknown url pattern type %s."\
                            % repr(type(curr)))


def url_decr(*sub, **kw):
    decr = kw.pop('decr', None)
    pattern = url(*sub, **kw)
    if decr:
        for __, p in iter_pattern(pattern):
            # For django<1.10.1
            if hasattr(p, '_callback') and callable(p._callback):
                p._callback = decr(p._callback)
            elif callable(p.callback):
                p.callback = decr(p.callback)
    return pattern
