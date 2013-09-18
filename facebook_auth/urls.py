import codecs
import json
import urllib
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls import url
from django.core.urlresolvers import reverse


class Next():
    def encode(self, data):
        data = codecs.getencoder('rot13')(json.dumps(data))[0]
        return urllib.urlencode({'next': data})

    def decode(self, data):
        return json.loads(codecs.getdecoder('rot13')(data)[0])


def redirect_uri(next, close):
    return urljoin(
        settings.FACEBOOK_CANVAS_URL,
        reverse('facebook-auth-handler') + "?" +
        Next().encode({'next': next, 'close': close})
    )

urlpatterns = patterns('facebook_auth.views',
    url(r'^handler$', 'handler', name='facebook-auth-handler'),
)
