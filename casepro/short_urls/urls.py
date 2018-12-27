from django.conf.urls import url

from .views import ShortUrlsView

urlpatterns = [
    url(r"^sh/(?P<short>[a-zA-Z0-9]+)/$", ShortUrlsView.as_view(), name="short_urls.redirect"),
]
